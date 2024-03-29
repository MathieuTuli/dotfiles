config = get_config()

config.TerminalIPythonApp.display_banner = False
config.TerminalInteractiveShell.confirm_exit = False
config.TerminalInteractiveShell.editing_mode = 'vi'
config.TerminalInteractiveShell.highlighting_style = 'monokai'  # or emacs
config.TerminalInteractiveShell.true_color = True
config.TerminalInteractiveShell.emacs_bindings_in_vi_insert_mode = False

# --nosep
config.InteractiveShell.separate_in = ''
config.InteractiveShell.separate_out = ''
config.InteractiveShell.separate_out2 = ''
