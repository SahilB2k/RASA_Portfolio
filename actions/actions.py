# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ExtractFoodEntity(Action):

    def name(self) -> Text:
        return "action_extract_food_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            food_entity= next(tracker.get_latest_entity_values('food'),None)   

            if food_entity:
                dispatcher.utter_message(text=f"You have selected {food_entity} as your food choice")
            else:
                dispatcher.utter_message(text="I am sorry , i could not detect your food choice")     

            
            return []

