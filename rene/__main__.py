import sys

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("WebKit", "6.0")

if __name__ == "__main__":
    from rene.application import ReneApplication

    app = ReneApplication()
    app.run(sys.argv)
