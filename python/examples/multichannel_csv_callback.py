import asyncio
import pypalmsens as ps
import csv
import functools


def stream_to_csv_callback(new_data, csv_writer):
    for point in new_data:
        csv_writer.writerow([point['index'], point['x'], point['y']])


async def stream_to_csv(manager, *, method):
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
    method = ps.ChronoAmperometry(
        interval_time=0.004,
        potential=1.0,
        run_time=5.0,
    )

    instruments = await ps.discover_async(ftdi=True)

    print(instruments)

    # run multichannel experiment with csv writer
    async with ps.InstrumentPoolAsync(instruments) as pool:
        results = await pool.submit(stream_to_csv, method=method)

    print(results)


asyncio.run(main())
