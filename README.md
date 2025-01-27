# lazy.nvimAutomaticPluginInstaller

Terminal UI for seleting input for nvim options. 

User inputs options

Program outputs config (lua) files.


Design Notes:

I want to be able to give this to my friends so they can set up neovim without having to basically learn lua and what each different thing in the lua files do

Right now it's hard to tell what's going on
Bc rhe code for a lot of the plug-ins is very messy

Basically just so that if u want u can go to the yaml files and input stuff directly (but still less complicated then looking at a jumble of code)

And then another python script will take that yaml and combine it with the template and output the correct configuration files

What the python is going to do is get user input and then write it to a yaml

But thats just to test the templates

And then it writes them directly to the jinja template

I just made the data on the python script

But rn there's no input

So just click the button that says "set your tab width" and put 4, then ur tab width is 4

Bc it's really confusing to try and change the settings urself

And then it spits out the config files with those settings

Rhat let's you select and input what options you want

Basically the plan is to make a terminal ui
