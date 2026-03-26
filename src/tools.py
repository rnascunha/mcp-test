from instance import mcp
from datetime import datetime
from zoneinfo import ZoneInfo
import json
from typing import Optional
from enum import Enum
import requests
from fastmcp.exceptions import ToolError


class PlaceType(Enum):
    city = "city"
    location = "location"


@mcp.tool()
def get_weather(
    place: str,
    type: PlaceType = PlaceType.city,
) -> object:
    """
    Get weather information from place provided

    Args:
        place: Location place where you want weather information
        type: "Place type from where to get weather"
    """

    try:
        place = place.replace(" ", "+")
        if type == PlaceType.location:
            place = "~" + place

        url = f"https://wttr.in/{place}?format=j1"
        response = requests.get(url)
        response = response.json()

        # return json.dumps(response)
        return response
    except Exception as e:
        raise ToolError("Error getting weather")


# Define a tool using the @mcp.tool decorator
@mcp.tool()
def get_current_datetime(timezone: Optional[str] = None) -> str:
    """
    Get current date and time. Format output: DD/mm/YYYY HH:MM:SS

    Args:
        timezone: "Timezone from date time that will be queried. Local timezone if not provided"
    """
    try:
        current_datetime = None
        if timezone:
            current_datetime = datetime.now(ZoneInfo(timezone))
        else:
            current_datetime = datetime.now()
        return json.dumps(
            {
                "datetime": current_datetime.strftime("%d/%m/%Y %H:%M:%S"),
                "timezone": timezone if timezone else "local",
            }
        )
    except:
        raise ToolError("Error getting current time")
