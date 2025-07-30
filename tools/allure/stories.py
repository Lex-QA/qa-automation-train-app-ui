from enum import Enum


class AllureStory(str, Enum):
    # Elements section
    TEXT_BOX = "Text Box"
    CHECK_BOX = "Check Box"
    RADIO_BUTTON = "Radio Button"
    WEB_TABLES = "Web Tables"
    BUTTONS = "Buttons"
    LINKS = "Links"
    BROKEN_LINKS = "Broken Links - Images"
    UPLOAD_DOWNLOAD = "Upload and Download"
    DYNAMIC_PROPERTIES = "Dynamic Properties"

    # Forms section
    PRACTICE_FORM = "Practice Form"

    # Alerts section
    BROWSER_WINDOWS = "Browser Windows"
    ALERTS = "Alerts"
    FRAMES = "Frames"
    NESTED_FRAMES = "Nested Frames"
    MODAL_DIALOGS = "Modal Dialogs"

    # Widgets section
    ACCORDIAN = "Accordian"
    AUTO_COMPLETE = "Auto Complete"
    DATE_PICKER = "Date Picker"
    SLIDER = "Slider"
    PROGRESS_BAR = "Progress Bar"
    TABS = "Tabs"
    TOOL_TIPS = "Tool Tips"
    MENU = "Menu"
    SELECT_MENU = "Select Menu"

    # Interactions section
    SORTABLE = "Sortable"
    SELECTABLE = "Selectable"
    RESIZABLE = "Resizable"
    DROPPABLE = "Droppable"
    DRAGABBLE = "Dragabble"

    # Game Store section
    LINK_PAGE = "Link Page"
