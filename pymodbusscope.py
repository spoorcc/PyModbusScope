"""
Script for autmating ModbusScope
"""

from pywinauto.application import Application
from pywinauto.findwindows import ElementNotFoundError
from pywinauto.keyboard import send_keys

class ModbusScope:
    ''' API class for ModbusScope '''

    def __init__(self, path='ModbusScope.exe'):
        ''' Create an API object that can control a single instance of ModbusScope '''
        try:
            self.app = Application(backend="uia").connect(title=u'ModbusScope')
        except ElementNotFoundError:
            try:
                self.app = Application(backend="uia").start(path)
            except ElementNotFoundError:
                raise RuntimeError("ModbusScope is not running or in PATH")

        self.app['ModbusScope.*'].set_focus()
        #self.app['ModbusScope.*'].print_control_identifiers()

    def load_project(self, path):
        ''' Load a project (.mbs) file from the given absolute or relative path '''
        self.app['ModbusScope.*'].set_focus()
        self.app['ModbusScope.*'].toolBar.LoadProjectFile.click_input()
        self.app['ModbusScope.*'].SelectMbsFile.BestandsNaamEdit.type_keys(path, with_spaces=True)
        send_keys("{ENTER}")

    def start_logging(self):
        ''' Start logging - Some registers must be added '''
        self.app['ModbusScope.*'].set_focus()
        self.app['ModbusScope.*'].toolBar.StartLogging.click()

    def stop_logging(self):
        ''' Stop the current logging '''
        self.app['ModbusScope.*'].set_focus()
        self.app['ModbusScope.*'].toolBar.StopLogging.click()

    def add_register(self, address):
        ''' Add a register at the given address '''
        self.app['ModbusScope.*'].toolBar.RegisterSettings.click_input()
        self.app['ModbusScope.*'].RegisterSettings.AddNewRegister.click_input()
        self.app['ModbusScope.*'].RegisterSettings.print_control_identifiers()

    def clear_data(self):
        ''' Clear the data '''
        self.app['ModbusScope.*'].Menu2.View.print_control_identifiers()

    def about(self):
        ''' Open the About menu '''
        self.app['ModbusScope.*'].Menu2.menu_select("? -> About")
