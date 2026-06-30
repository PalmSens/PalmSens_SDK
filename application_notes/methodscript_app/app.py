# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pypalmsens>=1.9",
#     "streamlit>=1.55",
# ]
# ///

from __future__ import annotations

import asyncio

import streamlit as st

import pypalmsens as ps

st.set_page_config(
    page_title='Battery Cycling',
    page_icon=':material/battery_android_frame_bolt:',
    menu_items={
        'Get Help': 'https://palmsens.com/contact',
        'Report a bug': 'https://github.com/palmsens/palmsens_sdk/issues',
    },
    layout='wide',
    initial_sidebar_state='expanded',
)


@st.cache_resource
def connect_to_device():
    return asyncio.run(ps.connect_async())


def main():
    st.title('Battery Cycling')

    c1, c2 = st.columns(2)

    with st.sidebar:
        potential_max = st.number_input(
            'Potential Max (mV)',
            value=4300,
            help='Maximum potential to charge to (units: mV).',
        )

        current_min = st.number_input(
            'Current Min (μA)',
            value=5,
            help='Minimum current to stop the CV charge step (units: μA).',
        )

        potential_min = st.number_input(
            'Potential Min (mV)',
            value=2500,
            help='Minimum potential to discharge to (units: mV).',
        )

        current_charge = st.number_input(
            'Current Charge (μA)',
            value=100,
            help='Constant current to charge with (units: μA).',
        )

        current_discharge = st.number_input(
            'Current Discharge (μA)',
            value=-100,
            help='Constant current to discharge with (units: μA).',
        )

        cycles = st.number_input(
            'Cycles', value=1, help='Number of charge and discharge cycles.'
        )

        interval = st.number_input(
            'Interval (s)',
            value=10,
            help='Interval time of each measurement point (units: s).',
        )

        max_time = st.number_input(
            'Max Time (s)',
            value=3,
            help='Maximum duration of each step (if the cut-off is not met) (units: s).',
        )

        delta_v = st.number_input(
            'Delta V (μV)',
            value=100,
            min_value=0,
            help='Minimum potential variation required for plotting data in CC steps (units: μV).',
        )

        delta_i = st.number_input(
            'Delta I (nA)',
            value=500,
            min_value=0,
            help='Minimum current variation reuqired for plotting data in the CV step (units: nA).',
        )

        delta_t = st.number_input(
            'Delta T (ms)',
            value=100,
            help='Maximum time without plotting data (units: ms).',
        )

    method = ps.energy.experimental_BatteryCycling(
        potential_max=potential_max,
        current_min=current_min,
        potential_min=potential_min,
        current_charge=current_charge,
        current_discharge=current_discharge,
        cycles=cycles,
        interval=interval,
        max_time=max_time,
        delta_v=delta_v,
        delta_i=delta_i,
        delta_t=delta_t,
    )

    ms = method.to_methodscript()

    with st.expander('Click to show generated MethodSCRIPT'):
        st.code(ms.script, line_numbers=True, height=600)

    c1, c2 = st.columns(2)
    with c1:
        st.download_button(
            'Save as script (.mscr)',
            data=ms.script,
            file_name='battery_cycler.mscr',
            mime='text/plain',
            icon=':material/download:',
            width='stretch',
        )
    with c2:
        _ = st.download_button(
            'Save as method file (.psmethod)',
            data=ms._serialize(),
            file_name='battery_cycler.psmethod',
            mime='text/plain',
            icon=':material/download:',
            width='stretch',
        )

    manager: ps.InstrumentManagerAsync = connect_to_device()
    assert manager.is_connected()

    async def async_measure(manager, method):
        def update_status_message(message: str):
            status.update(label=message)

        manager.register_receive_message_callback(update_status_message)

        measurement = await manager.measure(method)

        manager.unregister_receive_message_callback()
        return measurement

    with st.status('Starting measurement') as status:
        status.write('Collecting data...')

        asyncio.run(async_measure(manager, method))
        status.update(label='Measurement finished!', state='complete')


if __name__ == '__main__':
    main()
