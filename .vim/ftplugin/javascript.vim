set ts=2
set sts=2
set sw=2
" Vim filetype plugin file
" Language:     JavaScript
" Maintainer:   vim-javascript community
" URL:          https://github.com/pangloss/vim-javascript

setlocal iskeyword+=$ suffixesadd+=.js

if exists('b:undo_ftplugin')
  let b:undo_ftplugin .= ' | setlocal iskeyword< suffixesadd<'
else
  let b:undo_ftplugin = 'setlocal iskeyword< suffixesadd<'
endif
set ts=2
set sts=2
set sw=2
