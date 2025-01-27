vim.cmd("set expandtab")
vim.cmd("set tabstop=4")
vim.cmd("set softtabstop=4")
vim.cmd("set shiftwidth=4")
vim.o.relativenumber = true

require("config.lazy")

vim.keymap.set('n', '<leader>p', ':Lazy<CR>', { desc = 'Open Lazy.nvim' })
