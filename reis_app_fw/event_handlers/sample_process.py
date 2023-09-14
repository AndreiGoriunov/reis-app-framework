from threading import Thread
from time import sleep

import PySimpleGUI as sg

from reis_app_fw.window_config import HOME_BTN_SELECT_FOLDER_KEY

def sample_process_handler(window: sg.Window, values: dict):
    # get values from the window
    folder_path = values.get(HOME_BTN_SELECT_FOLDER_KEY)
    thread = Thread(target=sample_process)
    window["-FEEDBACK-"].update(f"5 sec, using: {folder_path if folder_path != '' else 'empty'}")
    window.refresh()
    thread.start()
    while True:
        event, values = window.read(timeout=100)  # type: ignore ; checks every 100 ms
        if event == sg.WINDOW_CLOSED:
            window.close()
            return
        if not thread.is_alive():  # if the thread has finished its job
            window["-FEEDBACK-"].update("Finished.")  # type: ignore
            break


def sample_process():
    sleep(5)