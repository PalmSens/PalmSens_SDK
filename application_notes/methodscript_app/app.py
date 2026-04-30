# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pypalmsens>=1.9",
#     "pandas>=2.3",
#     "plotly>=6.6",
#     "streamlit>=1.55",
# ]
# ///

from __future__ import annotations

import plotly.express as px
import streamlit as st
from pydantic import BaseModel

import pypalmsens as ps
from pypalmsens.data import CallbackData

st.set_page_config(
    page_title='Measurement dashboard',
    page_icon=':microscope:',
    menu_items={
        'Get Help': 'https://palmsens.com/contact',
        'Report a bug': 'https://github.com/palmsens/palmsens_sdk/issues',
    },
)

TEMPLATE = """\
e
wait {wait_time}m
if 1 < 2
    send_string "Hello {name}"
endif

"""

connect_to_device = st.cache_resource(ps.connect)


class MyVariables(BaseModel):
    wait_time: int
    """Time to wait."""

    name: str = 'World'
    """Who to greet."""


def main():
    st.title('Cyclic Voltammetry')

    with st.form('parameters_form'):
        equilibration_time = st.number_input(
            'Equilibration time', value=0.0, help='Equilibration time in s.'
        )
        begin_potential = st.number_input(
            'Begin potential',
            value=-0.5,
            help='Potential where the scan starts and stops at in V.',
        )
        vertex1_potential = st.number_input(
            'Vertex 1 potential',
            value=0.5,
            help='First potential where direction reverses in V.',
        )
        vertex2_potential = st.number_input(
            'Vertex 2 potential',
            value=-0.5,
            help='Second potential where direction reverses. V.',
        )
        step_potential = st.number_input(
            'Step potential', value=0.1, help='Potential step size in V.'
        )
        scanrate = st.number_input('Scanrate', value=1.0, help='Scan rate in V/s.')

        submitted = st.form_submit_button('Start measurement')
        if not submitted:
            st.stop()

    method = ps.CyclicVoltammetry(
        equilibration_time=equilibration_time,
        begin_potential=begin_potential,
        vertex1_potential=vertex1_potential,
        vertex2_potential=vertex2_potential,
        step_potential=step_potential,
        scanrate=scanrate,
    )

    manager: ps.InstrumentManager = connect_to_device()
    assert manager.is_connected()

    chart = st.empty()

    def update(data: CallbackData):
        fig = px.line(
            x=data.x_array,
            y=data.y_array,
            title='CV',
        )
        fig.update_layout(
            xaxis={'title': {'text': 'Current / mA'}},
            yaxis={'title': {'text': 'Potential / V'}},
        )
        chart.plotly_chart(fig)

    manager.measure(method, callback=update)

    st.write('Done')


if __name__ == '__main__':
    main()
