# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from geopy.geocoders import Nominatim
from pymongo import MongoClient

def initialize_db(collection_name):
    client = MongoClient('mongodb+srv://caseyh9438:opensavannah@mapdata-j3m49.mongodb.net/test?retryWrites=true&w=majority')
    collection = client.get_database(collection_name)
    db = collection.savannah_floods
    return db


class PlottingFloodData(Action):

    def name(self):
        return 'floodaction'

    def run(self, dispatcher, tracker, domain):
        print('Starting Action')
        address = tracker.get_slot('addres')
        print('Address: {}'.format(address))

        #use address geolocation
        geolocator = Nominatim(user_agent="savannah_floods")
        location = geolocator.geocode(address)
        lat = location.latitude
        print('Lat: {}'.format(lat))
        lon = location.longitude
        print('Lon: {}'.format(lon))
        db = initialize_db('flood_db')
        new_flood = {
            'lat': lat,
            'lon': lon
        }
        db.insert_one(new_flood)

        if address is not None:
            dispatcher.utter_message("Thank you for letting us know! We've added your flood report to the Savannah Floods community map")
        else:
            dispatcher.utter_message("The address you provide wasn't recognised. Make sure that the full correct address is entered.")

        return []
