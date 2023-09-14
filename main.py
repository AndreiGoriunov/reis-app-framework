import config
from reis_app_fw.gui import GUI
from reis_app_fw.window_config import HOME_BTN_PROCESS_TEXT_KEY

def gui_setup() -> GUI:
    import reis_app_fw.window_config as wc
    from reis_app_fw.event_handlers import sample_process

    app = GUI(wc.HOME)
    app.add_event_handler(HOME_BTN_PROCESS_TEXT_KEY, sample_process.sample_process_handler)
    return app


if __name__ == "__main__":
    config.init()
    print(f"SCRIPT_DIR = {config.SCRIPT_DIR}")
    print(f"PROPERTIES = {config.PROPERTIES}")
    app = gui_setup()
    app.start()