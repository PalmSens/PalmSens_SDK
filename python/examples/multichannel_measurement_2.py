import asyncio

import pypalmsens
import csv

from pypalmsens._instruments.instrument_manager_async import InstrumentManagerAsync
from pypalmsens._methods.techniques import MethodSettings


def new_data_callback(new_data):
    for point in new_data:
        print(point)


def stream_to_csv_callback(csv_writer):
    def stream_to_csv_callback_channel(new_data):
        for point in new_data:
            csv_writer.writerow([point['index'], point['x'], point['y']])

    return stream_to_csv_callback_channel


async def main():
    method = pypalmsens.ChronoAmperometry(
        interval_time=0.004,
        potential=1.0,
        run_time=5.0,
    )

    instruments = await pypalmsens.discover_async(ftdi=True)

    # run multichannel experiment
    async with pypalmsens.InstrumentPoolAsync(instruments) as pool:
        tasks = await pool.measure(method)
        results = await asyncio.gather(*tasks)

    print(results)

    # run multichannel experiment with callback
    async with pypalmsens.InstrumentPoolAsync(
        instruments,
        callback=new_data_callback,
    ) as pool:
        tasks = await pool.measure(method)
        results = await asyncio.gather(*tasks)

    # run multichannel experiment with custom task
    async def my_task(manager: InstrumentManagerAsync, method: MethodSettings):
        serial = await manager.get_instrument_serial()
        csv_file = open(f'{serial}.csv', 'w', newline='')
        csv_writer = csv.writer(csv_file, delimiter=' ')
        manager.callback = stream_to_csv_callback(csv_writer)
        measurement = await manager.measure(method)
        csv_file.close()
        return measurement

    # run multichannel experiment with csv writer
    async with pypalmsens.InstrumentPoolAsync(instruments) as pool:
        tasks = await pool.submit(my_task, method=method)
        results = await asyncio.gather(*tasks)

    print(results)

    # run multichannel experiment with csv writer
    async with pypalmsens.InstrumentPoolAsync(instruments) as pool:
        tasks = await pool.measure_hw_sync(method, main_channel=0)
        results = await asyncio.gather(*tasks)

    print(results)

    # callback
    # hardware sync
    # custom loop


asyncio.run(main())
