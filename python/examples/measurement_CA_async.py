import asyncio

import pypalmsens as ps


def new_data_callback(data):
    print(data.last_datapoint())


def status_callback(args):
    status = args.GetStatus()

    potential = status.PotentialReading
    current = status.CurrentReading

    print(potential.Value, current.Value, status.ToString())
    print('pretreatment phase:', status.PretreatmentPhase)
    print('device state', args.DeviceState)


def ca_callback(args):
    status = args.GetStatus()
    potential = status.PotentialReading
    current = status.CurrentReading

    print(potential.Value, current.Value, status.ToString())
    print('pretreatment phase:', status.PretreatmentPhase)
    print('device state', args.DeviceState)


async def main():
    instruments = await ps.discover_async()
    print(instruments)

    async with await ps.connect_async(instruments[0]) as manager:
        serial = await manager.get_instrument_serial()
        print(serial)

        manager.subscribe_status_async(callback=ca_callback)

        await asyncio.sleep(10)

        # Chronoamperometry measurement using helper class
        method = ps.ChronoAmperometry(
            pretreatment=ps.settings.Pretreatment(
                conditioning_time=10,
                deposition_time=10,
            ),
            interval_time=0.02,
            potential=1.0,
            run_time=2.0,
        )

        measurement = await manager.measure(method, callback=new_data_callback)

        manager.unsubscribe_status_async()

    print(measurement)


asyncio.run(main())
