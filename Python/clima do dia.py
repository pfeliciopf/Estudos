import asyncio
import python_weather


async def main():
    cidade = input("Cidade: ")

    async with python_weather.Client(unit=python_weather.METRIC) as client:
        clima = await client.get(cidade)
        hoje = clima.daily_forecasts[0]

        print(f"{clima.location} - {clima.region} - {clima.country}")
        print(f"min --- {hoje.lowest_temperature}")
        print(f"max === {hoje.highest_temperature}")


asyncio.run(main())