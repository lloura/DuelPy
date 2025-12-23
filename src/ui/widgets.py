# ui/widgets.py
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

from gi.repository import Gtk, Adw
import gettext

_ = gettext.gettext

def create_shortcuts(title, moves):
    dialog = Adw.ShortcutsDialog(title=title)

    gameplay_section = Adw.ShortcutsSection(title=_("Gameplay"))
    for label, accel, action in moves:
        item = Adw.ShortcutsItem(title=label, accelerator=accel, action_name=action)
        gameplay_section.add(item)

    gameplay_section.add(Adw.ShortcutsItem(
        title=_("Try Again"),
        accelerator="<Ctrl>R",
        action_name="win.retry"
    ))
    dialog.add(gameplay_section)

    mode_section = Adw.ShortcutsSection(title=_("Game Mode"))

    mode_section.add(Adw.ShortcutsItem(
        title=_("Switch to RPSLS Mode"),
        accelerator="<Ctrl><Shift>R",
        action_name="win.change-mode('rpsls')"
    ))

    mode_section.add(Adw.ShortcutsItem(
        title=_("Switch to Classic Mode"),
        accelerator="<Ctrl><Shift>C",
        action_name="win.change-mode('classic')"
    ))

    dialog.add(mode_section)
    return dialog

@Gtk.Template(resource_path='/io/github/lloura/DuelPy/ui/rpsls_view.ui')
class RpslsView(Gtk.Box):
    __gtype_name__ = 'RpslsView'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shortcuts_dialog = create_shortcuts(
            _("RPSLS Mode"),
            [
                (_("Rock"), "1", "win.rock"),
                (_("Paper"), "2", "win.paper"),
                (_("Scissors"), "3", "win.scissors"),
                (_("Lizard"), "4", "win.lizard"),
                (_("Spock"), "5", "win.spock"),
            ]
        )

@Gtk.Template(resource_path='/io/github/lloura/DuelPy/ui/classic_view.ui')
class ClassicView(Gtk.Box):
    __gtype_name__ = 'ClassicView'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shortcuts_dialog = create_shortcuts(
            _("Classic Mode"),
            [
                (_("Rock"), "1", "win.rock"),
                (_("Paper"), "2", "win.paper"),
                (_("Scissors"), "3", "win.scissors"),
            ]
        )
