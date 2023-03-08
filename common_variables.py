from enum import Enum


class common_variables:
    top_left_text = "EventReader - Caretronic, Oddelek za integracije"

    gui_label_width = 200
    gui_label_heigth = 30

    gui_textbox_width = 200
    gui_button_width = 200
    gui_bottom_button_heigth = 60

    es_sender = 'Sender'
    es_receiver = 'Receiver'
    es_password = 'Password'

class EvtLevel(Enum):
    LOG_ALWAYS = 0
    CRITICAL = 1
    ERROR = 2
    WARNING = 3
    INFORMATIONAL = 4
    VERBOSE = 5
    SIEG_HEIL=88

    @classmethod
    def _missing_(cls, value):
        return cls.SIEG_HEIL


