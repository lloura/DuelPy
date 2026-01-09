# __init__.py
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

import gettext, locale, os

# localization setup

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
gettext.bindtextdomain('io.github.lloura.DuelPy', localedir)
gettext.textdomain('io.github.lloura.DuelPy')

_ = gettext.gettext
