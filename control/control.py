from PostalCodeToLocation.postal_code_to_location import convert_postal_code_to_location
from LocationToPostalCode.location_to_postal_code import convert_location_to_postal_code
from typing import Any
import aiohttp
import asyncio
from modules import convert_postal_code_to_location, judgment_of_postal_code

async def control(requested_values: list[dict[str, str]], **kwargs) -> list[dict[str, Any]]:
    
    async with aiohttp.ClientSession() as session:
        tasks: list = []

        for requested_value in requested_values:
            if "postal_code" in requested_value:
                value: str = requested_value.get('postal_code')
                tasks.append(convert_postal_code_to_location(session, value, POSTCODE_JP_API_KEY = kwargs.get('POSTCODE_JP_API_KEY', '')))
                #await asyncio.sleep(2)
            
            elif "address" in requested_value:
                value: str = requested_value.get('address')
                tasks.append(convert_location_to_postal_code(session, "address", value, GOOGLE_MAPS_API_KEY = kwargs.get('GOOGLE_MAPS_API_KEY', '')))
            """
            elif "landmark" in requested_value:
                value: str = requested_value.get('landmark')
                tasks.append(convert_location_to_postal_code(session, "landmark", value, GOOGLE_MAPS_API_KEY = kwargs.get('GOOGLE_MAPS_API_KEY', '')))
            """
        results = await asyncio.gather(*tasks)
    
    return results
#asyncio.run(control([{ "postal_code" : "1008111" }], POSTCODE_JP_API_KEY = userdata.get('POSTCODE_JP_API_KEY')))
