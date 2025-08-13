from pypalmsens import instruments
from pypalmsens.methods import ChronoAmperometryParameters
import asyncio

method = ChronoAmperometryParameters(
    interval_time=0.01,
    potential=1.0,
    run_time=10.0,
)


async def main():
    async with instruments.connect_async() as manager:
        measurement = await manager.measure(method)


asyncio.run(main())
