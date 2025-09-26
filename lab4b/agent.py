# Lab 4b: Output Schema Validation Demo
# This lab demonstrates structured output using Pydantic schemas
# Based on official ADK weather data example

from google.adk import Agent
from .schema import WeatherData

# Weather agent with structured output
root_agent = Agent(
    model="gemini-2.0-flash",
    name="weather_agent",
    description="Weather information service with structured output",

    instruction="""
    You are a Weather Information Agent. Answer user's questions based on the data you have.

    If you don't have the data, you can just say you don't know.

    Here are the data you have for San Jose:
    * temperature: 26 C
    * humidity: 20%
    * wind_speed: 29 mph

    Here are the data you have for Cupertino:
    * temperature: 16 C
    * humidity: 10%
    * wind_speed: 13 mph

    Here are the data you have for Mountain View:
    * temperature: 22 C
    * humidity: 15%
    * wind_speed: 18 mph

    Always respond with structured weather data in JSON format.
    """,

    # Output validation - ensures structured response format
    output_schema=WeatherData,
    output_key='weather_data'
)