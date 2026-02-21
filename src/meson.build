pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()

moduledir = pkgdatadir / 'duelpy'
logicdir = moduledir / 'game_logic'
uidir = moduledir / 'ui'
game_modes_dir = moduledir / 'game_modes'

gnome = import('gnome')

blueprints = custom_target('blueprints',
  input: files(
    'window.blp',
    'ui/how_to_play.blp',
    'game_modes/rpsls_view.blp',
    'game_modes/classic_view.blp',
    'game_modes/rps7_view.blp',
    'game_modes/rps9_view.blp',
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)

metainfo_dir = meson.project_build_root() / 'data'

gnome.compile_resources('duelpy',
  'duelpy.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
  source_dir: [
    '.',
    metainfo_dir,
    meson.current_source_dir(),
  ],
  dependencies: blueprints,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', get_option('prefix') / get_option('localedir'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'duelpy.in',
  output: 'duelpy',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'rwxr-xr-x'
)

duelpy_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]

logic_sources = [
  'game_logic/__init__.py',
  'game_logic/rules.py',
  'game_logic/modes.py',
]

ui_sources = [
  'ui/__init__.py',
  'ui/how_to_play.py',
  'ui/shortcuts.py',
]

game_modes_sources = [
  'game_modes/__init__.py',
  'game_modes/rpsls_view.py',
  'game_modes/classic_view.py',
  'game_modes/rps7_view.py',
  'game_modes/rps9_view.py',
]

install_data(duelpy_sources, install_dir: moduledir)
install_data(logic_sources, install_dir: logicdir)
install_data(ui_sources, install_dir: uidir)
install_data(game_modes_sources, install_dir: game_modes_dir)