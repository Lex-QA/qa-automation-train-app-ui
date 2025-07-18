from enum import Enum


class AllureTag(str, Enum):
    ELEMENTS = "ELEMENTS"
    FORMS = "FORMS"
    ALERTS = "ALERTS"
    FRAME = "FRAME"
    WINDOWS = "WINDOWS"
    WIDGETS = "WIDGETS"
    INTERACTIONS = "INTERACTIONS"
