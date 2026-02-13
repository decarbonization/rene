from gi.repository import GLib, Gtk

from rene.main_window import MainWindow


class ReneApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.swampmonkeyco.ReneApplication")
        GLib.set_application_name("Rene")

    def do_activate(self):
        main_window = MainWindow(application=self)
        main_window.present()
