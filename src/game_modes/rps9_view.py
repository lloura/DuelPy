# ui/game_modes/Rps9View.py
#
# Copyright 2025-2026 Lucas Loura
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
from ..ui.shortcuts import ShortcutManager

@Gtk.Template(resource_path='/io/github/lloura/DuelPy/game_modes/rps9_view.ui')
class Rps9View(Gtk.Box):
    __gtype_name__ = 'Rps9View'

    from . import _

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shortcuts_dialog = ShortcutManager(
            title=_("RPS-9 Mode"),
            moves=[
                (_("Rock"), "1", "win.rock"),
                (_("Paper"), "5", "win.paper"),
                (_("Scissors"), "3", "win.scissors"),
                (_("Sponge"), "4", "win.sponge"),
                (_("Fire"), "5", "win.fire"),
                (_("Water"), "6", "win.water"),
                (_("Air"), "7", "win.air"),
                (_("Human"), "8", "win.human"),
                (_("Gun"), "9", "win.gun"),
            ]
        )
