# ui/shortcuts.py
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

from gi.repository import Adw

class ShortcutManager:
    from . import _

    def __init__(self, title, moves):
        self.title = title
        self.moves = moves

    def get_dialog(self):

        dialog = Adw.ShortcutsDialog(title=self.title)

        # Gameplay Section
        gameplay_section = Adw.ShortcutsSection(title=_("Gameplay"))

        for label, accel, action in self.moves:
            item = Adw.ShortcutsItem(title=label, accelerator=accel, action_name=action)
            gameplay_section.add(item)

        gameplay_section.add(Adw.ShortcutsItem(
            title=_("Try Again"),
            accelerator="<Ctrl>R",
            action_name="win.retry"
        ))
        dialog.add(gameplay_section)

        # Game Modes Section
        mode_section = Adw.ShortcutsSection(title=_("Game Mode"))
        modes = [
            (_("Switch to RPSLS Mode"), "<Ctrl><Shift>R", "rpsls"),
            (_("Switch to Classic Mode"), "<Ctrl><Shift>C", "classic"),
            (_("Switch to RPS-7 Mode"), "<Ctrl><Shift>S", "rps7"),
        ]

        for label, accel, mode_id in modes:
            mode_section.add(Adw.ShortcutsItem(
                title=label,
                accelerator=accel,
                action_name=f"win.change-mode('{mode_id}')"
            ))

        dialog.add(mode_section)
        return dialog
