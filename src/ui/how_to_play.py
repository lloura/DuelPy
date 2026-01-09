# ui/how_to_play.py
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

from gi.repository import Gtk, Adw, Gio

@Gtk.Template(resource_path='/io/github/lloura/DuelPy/ui/how_to_play.ui')
class HowToPlayDialog(Adw.Dialog):
    __gtype_name__ = 'HowToPlayDialog'

    from . import _

    rules_group = Gtk.Template.Child()
    img_diagram = Gtk.Template.Child()

    def __init__(self, mode, **kwargs):
        super().__init__(**kwargs)

        # defines diagram image based on current mode
        if mode.diagram:
            self.img_diagram.set_from_icon_name(mode.diagram)

        for action, victims in mode.wins_map.items():
            # creating expander row for main move
            expander = Adw.ExpanderRow()
            expander.set_title(_(action.capitalize()))
            expander.set_accessible_role(Gtk.AccessibleRole.BUTTON)

            # main move icon (prefix)
            img = Gtk.Image.new_from_icon_name(f"{action}-symbolic")
            img.set_accessible_role(Gtk.AccessibleRole.PRESENTATION)
            expander.add_prefix(img)

            # adding a nested row for each win for this move
            for victim in victims:
                explanation = mode.get_explanation(action, victim)

                nested_row = Adw.ActionRow()
                nested_row.set_title(_(explanation))
                nested_row.set_accessible_role(Gtk.AccessibleRole.LIST_ITEM)

                victim_img = Gtk.Image.new_from_icon_name(f"{victim}-symbolic")
                victim_img.set_accessible_role(Gtk.AccessibleRole.PRESENTATION)
                nested_row.add_prefix(victim_img)

                expander.add_row(nested_row)

            self.rules_group.add(expander)

