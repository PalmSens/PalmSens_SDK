import asyncio

import pypalmsens
from pypalmsens.methods import ChronoAmperometry


def new_data_callback(new_data):
    for point in new_data:
        print(point)


async def main():
    available_instruments = await pypalmsens.discover_async()
    print('connecting to ' + available_instruments[0].name)

    async with pypalmsens.connect_async(available_instruments[0]) as manager:
        print('connection established')
        manager.callback = new_data_callback

        serial = await manager.get_instrument_serial()
        print(serial)

        # Chronoamperometry measurement using helper class
        method = ChronoAmperometry(
            interval_time=0.02,
            potential=1.0,
            run_time=2.0,
        )

        measurement = await manager.measure(method)

        if measurement is not None:
            print('measurement finished')
        else:
            print('failed to start measurement')


asyncio.run(main())
