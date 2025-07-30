from enum import Enum


class AllureStory(str, Enum):
    TEXT_BOX = "TextBox"
    FORMS = "Forms"
    ALERTS = "Alerts"
    FRAME = "Frame"
    WINDOWS = "Windows"
    WIDGETS = "Widgets"
    INTERACTIONS = "Interactions"
