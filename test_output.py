import asyncio

from p1_monitor import P1Monitor, SmartMeter, Settings, Phases

async def main():
    async with P1Monitor(
        host="HOST",
    ) as p1mon:
        smartmeter: SmartMeter = await p1mon.smartmeter()
        settings: Settings = await p1mon.settings()
        phases: Phases = await p1mon.phases()
        print(f"P1 Monitor - SmartMeter: {smartmeter}")
        print()
        print(f"P1 Monitor - Settings: {settings}")
        print()
        print(f"P1 Monitor - Phase: {phases}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())