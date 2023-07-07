# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class AgeRegistration(Action):

    EDAD_RIESGO = 0

    def name(self) -> Text:
        return "age_registration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if tracker.latest_message['entities'][0]['value'] < 18:
            self.EDAD_RIESGO = 1
        dispatcher.utter_message(
            text="A continuación, tienes 3 opciones, por favor elige una opción." +
            "1.- ¿Quieres conocer qué es la trata y cómo te puede afectar?" +
            "2.- ¿Quieres que hablemos de si en tu caso existe algún riesgo de trata?" +
            "3.- ¿Quieres pedir ayuda porque crees que te encuentras en peligro?" +
            "Ahora, presiona 1, 2 o 3.")

        return []
