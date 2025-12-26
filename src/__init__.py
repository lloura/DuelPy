import gettext, os

# localization setup
localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
gettext.bindtextdomain('io.github.lloura.DuelPy', localedir)
gettext.textdomain('io.github.lloura.DuelPy')

_ = gettext.gettext
