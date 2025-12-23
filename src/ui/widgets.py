from gi.repository import Gtk, Adw
import gettext

_ = gettext.gettext

def create_shortcuts(title, moves):
    dialog = Adw.ShortcutsDialog(title=title)
    section = Adw.ShortcutsSection(title=_("Gameplay"))

    for label, accel, action in moves:
        item = Adw.ShortcutsItem(title=label, accelerator=accel, action_name=action)
        section.add(item)

    retry_item = Adw.ShortcutsItem(title=_("Try Again"), accelerator="<Ctrl>R", action_name="win.retry")
    section.add(retry_item)
    dialog.add(section)
    return dialog

@Gtk.Template(resource_path='/io/github/lloura/DuelPy/ui/rpsls_view.ui')
class RpslsView(Gtk.Box): # Voltamos para Gtk.Box aqui
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
