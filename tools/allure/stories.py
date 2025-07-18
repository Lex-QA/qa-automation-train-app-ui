from enum import Enum


class AllureStory(str, Enum):
    ELEMENTS = "Elements"
    FORMS = "Forms"
    ALERTS = "Alerts"
    FRAME = "Frame"
    WINDOWS = "Windows"
    WIDGETS = "Widgets"
    INTERACTIONS = "Interactions"
