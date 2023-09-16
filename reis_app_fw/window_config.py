import PySimpleGUI as sg

# Settings ====================================================================
TITLE = "Rei's GUI Template"
TITLE_FONT = ("Any", 13, "bold")
BUTTON_FONT = ("Any", 13)
MIN_WIDTH = 50
ICON = "icon.ico"

# Pages =======================================================================
# Home
HOME = "Home"
HOME_BTN_PROCESS_TEXT = "Process Start"
HOME_BTN_PROCESS_TEXT_KEY = "-SAMPLE_PROCESS-"
HOME_BTN_SELECT_FOLDER_KEY = "-HOME_BTN_SELECT_FOLDER_KEY-"
# Sample Page
SAMPLE_PAGE = "Sample Page"
# General


# Layouts =====================================================================
def home_layout():
    return [
        [sg.Text(HOME, font=TITLE_FONT)],
        [sg.Text("", size=(MIN_WIDTH, 0))],
        [
            sg.Text("Select folder", size=(13, 1)),
            sg.InputText(key=HOME_BTN_SELECT_FOLDER_KEY),
            sg.FolderBrowse(),
        ],
        [
            sg.Button(HOME_BTN_PROCESS_TEXT, key=HOME_BTN_PROCESS_TEXT_KEY),
            sg.Text("Feedback Text", size=(20, 0), key="-FEEDBACK-"),
        ],
        [sg.Button(SAMPLE_PAGE, key=SAMPLE_PAGE)],
    ]


def sample_page_layout():
    return [
        [sg.Text(SAMPLE_PAGE, font=TITLE_FONT)],
        [sg.Text("", size=(MIN_WIDTH, 0))],
        [sg.Text("A Demo second page")],
        home_button(),
    ]


def home_button() -> list:
    return [sg.Button(HOME, key=HOME)]


# Layout Config ===============================================================
LAYOUT_CONFIG = {
    HOME: {"title": TITLE, "layout": home_layout},
    SAMPLE_PAGE: {"title": TITLE, "layout": sample_page_layout},
}
