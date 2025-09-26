# Lab 4b: Output Schema for Structured Weather Data
# Based on official ADK example

from pydantic import BaseModel

class WeatherData(BaseModel):
    temperature: str
    humidity: str
    wind_speed: str