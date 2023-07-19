from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import Restarted
from telegram import Bot


# class ActionFallback(Action):
#     def name(self) -> Text:
#         return "action_fallback"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(
#             template="utter_fallback")

#         return []


class ValidateSentimientoForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_sentimiento_form"

    def validate_como_te_sientes(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `como_te_sientes` value."""
        if tracker.get_intent_of_latest_message() == "positive_response_sentimiento":
            dispatcher.utter_message(
                text=f"Entiendo que estás más o menos bien.")
            return {"como_te_sientes": "positivo",
                    "que_hace_sentirte_asi": False}
        elif tracker.get_intent_of_latest_message() == "negative_response_sentimiento":
            dispatcher.utter_message(text=f"Entiendo que estás mal.")
            return {"como_te_sientes": "negativo"}
        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "si estás bien o mal?")
            return {"como_te_sientes": None}

    def validate_que_hace_sentirte_asi(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `que_hace_sentirte_asi` value."""
        if tracker.get_slot("que_hace_sentirte_asi") == False:
            return {"que_hace_sentirte_asi": False}
        return {"que_hace_sentirte_asi": True}


class ValidateOfrecimientoForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_ofrecimiento_form"

    def validate_ofreciendo_algo(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `ofreciendo_algo` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            dispatcher.utter_message(
                text=f"Entiendo que si.")
            return {"ofreciendo_algo": "affirm"}
        elif tracker.get_intent_of_latest_message() == "deny":
            dispatcher.utter_message(text=f"Entiendo que no.")
            return {"ofreciendo_algo": "deny", "que_ofrece": True}
        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "si o no?")
            return {"ofreciendo_algo": None}

    def validate_que_ofrece(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `que_ofrece` value."""
        dispatcher.utter_message(text=f"Entiendo")
        return {"que_ofrece": True}


class ValidateMenorForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_menor_form"

    def validate_pregunta_menor(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `pregunta_menor` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"pregunta_menor": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"pregunta_menor": False}
        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"pregunta_menor": None}


class ValidateViajeForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_viaje_form"

    def validate_vas_a_viajar(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `vas_a_viajar` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"vas_a_viajar": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"vas_a_viajar": False,
                    "pagar_para_viajar": True,
                    "pagar_tu_billete": True,
                    "pagar_alojamiento": True,
                    "preocupacion_dinero": False,
                    "ganar_dinero": False,
                    "fotos_intimas": False,
                    "pregunta_pasaporte": False,
                    "pasaporte_falso": False,
                    "espera_alguien": False,
                    "espera_conocida": True,
                    "fiabilidad_espera": True}
        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"vas_a_viajar": None}

    def validate_pagar_para_viajar(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `pagar_para_viajar` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"pagar_para_viajar": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"pagar_para_viajar": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"pagar_para_viajar": None}

    def validate_pagar_tu_billete(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `pagar_tu_billete` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"pagar_tu_billete": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"pagar_tu_billete": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"pagar_tu_billete": None}

    def validate_pagar_alojamiento(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `pagar_alojamiento` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"pagar_alojamiento": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"pagar_alojamiento": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"pagar_alojamiento": None}

    def validate_preocupacion_dinero(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `preocupacion_dinero` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"preocupacion_dinero": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"preocupacion_dinero": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"preocupacion_dinero": None}

    def validate_ganar_dinero(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `ganar_dinero` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"ganar_dinero": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"ganar_dinero": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"ganar_dinero": None}

    def validate_fotos_intimas(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `fotos_intimas` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"fotos_intimas": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"fotos_intimas": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"fotos_intimas": None}

    def validate_pregunta_pasaporte(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `pregunta_pasaporte` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"pregunta_pasaporte": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"pregunta_pasaporte": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"pregunta_pasaporte": None}

    def validate_pasaporte_falso(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `pasaporte_falso` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"pasaporte_falso": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"pasaporte_falso": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"pasaporte_falso": None}

    def validate_espera_alguien(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `espera_alguien` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"espera_alguien": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"espera_alguien": False,
                    "espera_conocida": True,
                    "fiabilidad_espera": True}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"espera_alguien": None}

    def validate_espera_conocida(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `espera_conocida` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"espera_conocida": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"espera_conocida": False,
                    "fiabilidad_espera": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"espera_conocida": None}

    def validate_fiabilidad_espera(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `fiabilidad_espera` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"fiabilidad_espera": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"fiabilidad_espera": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"fiabilidad_espera": None}


# class ValidateTrabajoForm(FormValidationAction):

#     def name(self) -> Text:
#         return "validate_contrato_form"


    def validate_ofrecido_trabajo(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `ofrecido_trabajo` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"ofrecido_trabajo": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"ofrecido_trabajo": False,
                    "ofrecido_contrato": True,
                    "visto_contrato": True,
                    "demasiado_buena": False,
                    "confias": True,
                    "libertad_romper_contrato": True,
                    "avance_dinero": False,
                    "contenido_intimo": False,
                    "contenido_desnudo": False,
                    "datos_personales": False}
        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"vas_a_viajar": None}

    def validate_ofrecido_contrato(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `ofrecido_contrato` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"ofrecido_contrato": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            print("Entra")
            return {"ofrecido_contrato": False,
                    "visto_contrato": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"ofrecido_contrato": None}

    def validate_visto_contrato(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `visto_contrato` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"visto_contrato": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"visto_contrato": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"visto_contrato": None}

    def validate_demasiado_buena(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `demasiado_buena` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"demasiado_buena": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"demasiado_buena": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"demasiado_buena": None}

    def validate_confias(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `confias` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"confias": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"confias": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"confias": None}

    def validate_libertad_romper_contrato(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `libertad_romper_contrato` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"libertad_romper_contrato": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"libertad_romper_contrato": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"libertad_romper_contrato": None}

    def validate_avance_dinero(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `avance_dinero` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"avance_dinero": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"avance_dinero": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"avance_dinero": None}

    def validate_contenido_intimo(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `contenido_intimo` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"contenido_intimo": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"contenido_intimo": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"contenido_intimo": None}

    def validate_contenido_desnudo(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `contenido_desnudo` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"contenido_desnudo": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"contenido_desnudo": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"contenido_desnudo": None}

    def validate_datos_personales(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate `datos_personales` value."""
        if tracker.get_intent_of_latest_message() == "affirm":
            return {"datos_personales": True}
        elif tracker.get_intent_of_latest_message() == "deny":
            return {"datos_personales": False}

        else:
            dispatcher.utter_message(text=f"Perdona, no te he entendido, ¿podrías decirme " +
                                     "con si o no para entenderte mejor?")
            return {"datos_personales": None}


class RestartAction(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Union[Dict[Text, Any], Text]]]:

        # Reinicia los slots
        return [Restarted()]


class ActionDeleteAllMessages(Action):

    def name(self) -> Text:
        return "action_delete_all_messages"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Obtén el token de acceso de Telegram desde el archivo credentials.yml
        token = domain['telegram']['access_token']

        # Crea una instancia del bot de Telegram
        bot = Bot(token=token)

        # Obtiene el chat_id del remitente
        chat_id = tracker.sender_id

        try:
            messages = bot.get_chat(chat_id).get("messages")
            if messages:
                for message_id in messages:
                    bot.delete_message(chat_id, message_id)
                dispatcher.utter_message(
                    text="Se han borrado todos los mensajes del chat.")
            else:
                dispatcher.utter_message(
                    text="No hay mensajes para borrar en el chat.")
        except Exception as e:
            dispatcher.utter_message(
                text=f"Error al borrar mensajes del chat: {e}")

        return []
