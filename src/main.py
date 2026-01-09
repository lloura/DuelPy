# main.py
#
# Copyright 2025 Lucas Loura
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys, gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw
from .window import DuelpyWindow

class DuelpyApplication(Adw.Application):
    from . import _

    """The main application singleton class."""
    def __init__(self):
        super().__init__(application_id='io.github.lloura.DuelPy',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
                         resource_base_path='/io/github/lloura/DuelPy')

        # Define application-wide actions
        self.create_action('quit', lambda *_: self.quit(), ['<control>q'])
        self.create_action('about', self.on_about_action)

    def do_activate(self):
        """
        Called when the application is activated.
        We raise the application's main window, creating it if necessary.
        """
        win = self.props.active_window
        if not win:
            win = DuelpyWindow(application=self)
        win.present()

    def on_about_action(self, *args):
        """Callback for the app.about action."""
        resource_path = "/io/github/lloura/DuelPy/io.github.lloura.DuelPy.metainfo.xml"
        about = Adw.AboutDialog.new_from_appdata(resource_path, "0.3.2")

        about.set_copyright("© 2025-2026 Lucas Loura")
        about.set_license_type(Gtk.License.GPL_3_0)

        about.set_developers([
            ("Lucas Loura https://github.com/lloura")
        ])
        about.set_designers([
            ("Lucas Loura https://github.com/lloura")
        ])
        about.set_translator_credits(_("translator-credits"))

        about.add_acknowledgement_section(_("Game Variant Creators"), [
            "Sam Kass & Karen Bryla https://www.samkass.com/theories/RPSSL.html",
            "David C. Lovelace https://umop.com/rps.htm"
        ])
        about.add_acknowledgement_section(_("Original Inspiration"), [
            "ByteSeb's Duel https://github.com/byteseb/Duel",
            "ByteSeb's Tutorial Video https://www.youtube.com/watch?v=WtvObZHhdf0"
        ])

        about.present(self.props.active_window)

    def create_action(self, name, callback, shortcuts=None):
        """
        Helper to add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)

def main(version):
    """The application's entry point."""
    app = DuelpyApplication()
    return app.run(sys.argv)

