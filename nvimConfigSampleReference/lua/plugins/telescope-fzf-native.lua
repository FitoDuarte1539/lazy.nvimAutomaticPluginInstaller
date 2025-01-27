return { 
    'nvim-telescope/telescope-fzf-native.nvim',
    build = 'make',
    config = function()
        require('telescope').setup {
            extensions = {
                fzf = {
                fuzzy = true,                    -- false will only do exact
                override_generic_sorter = true,  -- override the generic sorter
                override_file_sorter = true,     -- override the file sorter
                case_mode = "smart_case",        -- or "ignore_case" or "respe
                }
            }
        }
        -- To get fzf loaded and working with telescope, you need to call
        -- load_extension, somewhere after setup function:
        require('telescope').load_extension('fzf')
    end,
}
