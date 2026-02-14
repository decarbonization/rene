import os
from typing import override

from gi.repository import Gio, Gtk, WebKit

import rene.config


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title("Rene")
        self.set_size_request(400, 300)
        self.maximize()

        self.web_view = WebKit.WebView()

        web_view_settings = self.web_view.get_settings()
        web_view_settings.set_enable_back_forward_navigation_gestures(True)
        web_view_settings.set_enable_developer_extras(True)
        web_view_settings.set_enable_media(True)
        web_view_settings.set_media_playback_requires_user_gesture(False)
        web_view_settings.set_enable_encrypted_media(True)

        self.web_view.connect("close", lambda _web_view, _frame: self.close())
        self.web_view.connect("load-changed", self._on_load_changed)
        self.web_view.connect(
            "notify::title",
            lambda _web_view, _frame: self.set_title(
                f"Rene - {self.web_view.get_title()}"
            ),
        )

        self.set_child(self.web_view)

        navigation_bar = Gtk.HeaderBar(
            name=self.get_title() or "",
        )
        self.connect(
            "notify::title",
            lambda window, _pspec: navigation_bar.set_name(window.get_title()),
        )

        back_button = Gtk.Button(label="Back", icon_name="go-previous-symbolic")
        back_button.connect("clicked", lambda _button: self.web_view.go_back())
        self.web_view.connect(
            "notify::can-go-back",
            lambda web_view, _frame: back_button.set_sensitive(web_view.can_go_back()),
        )
        navigation_bar.pack_start(back_button)

        forward_button = Gtk.Button(label="Forward", icon_name="go-next-symbolic")
        forward_button.connect("clicked", lambda _button: self.web_view.go_forward())
        self.web_view.connect(
            "notify::can-go-forward",
            lambda web_view, _frame: forward_button.set_sensitive(
                web_view.can_go_forward()
            ),
        )
        navigation_bar.pack_start(forward_button)

        self._stop_reload_button = Gtk.Button(
            label="Reload", icon_name="view-refresh-symbolic"
        )
        self._stop_reload_button.connect("clicked", self._stop_reload)
        navigation_bar.pack_start(self._stop_reload_button)

        reboot_action = Gio.SimpleAction(name="reboot")
        reboot_action.connect("activate", self._reboot)
        self.add_action(reboot_action)

        poweroff_action = Gio.SimpleAction(name="poweroff")
        poweroff_action.connect("activate", self._poweroff)
        self.add_action(poweroff_action)

        menu_button = Gtk.MenuButton(
            label="Menu",
            icon_name="open-menu-symbolic",
        )
        menu_model = Gio.Menu()
        menu_model.append("Reboot", "win.reboot")
        menu_model.append("Shut Down", "win.poweroff")
        menu_button.set_menu_model(menu_model)
        navigation_bar.pack_end(menu_button)

        self.set_titlebar(navigation_bar)

    @override
    def present(self) -> None:
        if not self.web_view.get_uri():
            self.web_view.load_uri(rene.config.SERVER)

        return super().present()

    def _stop_reload(self, _button: Gtk.Button):
        if self.web_view.is_loading():
            self.web_view.stop_loading()
        else:
            self.web_view.reload()

    def _reboot(self, _action: Gio.Action, _):
        os.system("systemctl reboot")

    def _poweroff(self, _action: Gio.Action, _):
        os.system("systemctl poweroff")

    def _on_load_changed(self, web_view: WebKit.WebView, load_event: WebKit.LoadEvent):
        if load_event == WebKit.LoadEvent.STARTED:
            self._stop_reload_button.set_label("Stop")
            self._stop_reload_button.set_icon_name("process-stop-symbolic")
        elif load_event == WebKit.LoadEvent.FINISHED:
            self._stop_reload_button.set_label("Reload")
            self._stop_reload_button.set_icon_name("view-refresh-symbolic")
