import asyncio
import pypalmsens


async def main():
    method = pypalmsens.ChronoAmperometry(
        interval_time=0.004,
        potential=1.0,
        run_time=5.0,
    )

    instruments = await pypalmsens.discover_async(ftdi=True)

    print(instruments)

    async with pypalmsens.InstrumentPoolAsync(instruments) as pool:
        tasks = await pool.measure_hw_sync(method, main_manager=pool.managers[0])

        ## You can also use the serial number to select the main channel:
        # tasks = await pool.measure_hw_sync(method, main_serial='ES4HR20B0008')

        ## If you have a multi-channel instrument, you can use the channel number:
        # tasks = await pool.measure_hw_sync(method, main_channel=0)

        results = await asyncio.gather(*tasks)

    print(results)


asyncio.run(main())
