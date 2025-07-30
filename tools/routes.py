from enum import Enum


class AppRoute(str, Enum):
    MAIN = ""
    TEXT_BOX = "./text-box"
    CHECKBOX = "./checkbox"
    RADIO_BUTTON = "./radio-button"
    WEBTABLES = "./webtables"
    BUTTONS = "./buttons"
    LINKS = "./links"
    BROKEN_LINKS = "./broken"
    UPLOAD_DOWNLOAD = "./upload-download"
    DYNAMIC_PROPERTIES = "./dynamic-properties"
    PRACTICE_FORM = "./automation-practice-form"
    BROWSER_WINDOWS = "./browser-windows"
    ALERTS = "./alerts"
    FRAMES = "./frames"
    NESTED_FRAMES = "./nestedframes"
    MODAL_DIALOGS = "./modal-dialogs"
    ACCORDIAN = "./accordian"
    DATE_PICKER = "./date-picker"
    SLIDER = "./slider"
    PROGRESS_BAR = "./progress-bar"
    TABS = "./tabs"
    TOOL_TIPS = "./tool-tips"
    MENU = "./menu"
    SELECT_MENU = "./select-menu"
    SORTABLE = "./sortable"
    SELECTABLE = "./selectable"
    RESIZABLE = "./resizable"
    DROPPABLE = "./droppable"
    DRAGABBLE = "./dragabble"


class SidebarSection(str, Enum):
    ELEMENTS = "1"
    FORMS = "Forms"
    ALERTS_FRAMES_WINDOWS = "Alerts, Frame & Windows"
    WIDGETS = "Widgets"
    INTERACTIONS = "Interactions"
    GAME_STORE = "Game Store Application"


class SidebarItem(str, Enum):
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
