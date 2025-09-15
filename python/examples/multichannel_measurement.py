import asyncio
import pypalmsens
import csv
import functools

from pypalmsens._instruments.instrument_manager_async import InstrumentManagerAsync
from pypalmsens._methods.techniques import MethodSettings


def stream_to_csv_callback(new_data, csv_writer):
    for point in new_data:
        csv_writer.writerow([point['index'], point['x'], point['y']])


async def stream_to_csv(manager: InstrumentManagerAsync, *, method: MethodSettings):
    """Measure with a custom csv writer callback."""
    serial = await manager.get_instrument_serial()

    with open(f'{serial}.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=' ')

        callback = functools.partial(stream_to_csv_callback, csv_writer=csv_writer)
        manager.callback = callback

        measurement = await manager.measure(method)

    print(f'Wrote data to {csv_file.name}')

    return measurement


async def main():
    method = pypalmsens.ChronoAmperometry(
        interval_time=0.004,
        potential=1.0,
        run_time=5.0,
    )

    instruments = await pypalmsens.discover_async(ftdi=True)

    print(instruments)

    # run multichannel experiment with csv writer
    async with pypalmsens.InstrumentPoolAsync(instruments) as pool:
        tasks = await pool.submit(stream_to_csv, method=method)
        results = await asyncio.gather(*tasks)

    print(results)


asyncio.run(main())
