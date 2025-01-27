from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('initLuaTemplate.j2')

config_data = {
        'expandtab': 'expandtab',
        'tabstop': '4',
        'softtabstop': '4',
        'shiftwidth': '4',
        'relativenumber': 'true'
}

config_output = template.render(config_data)

with open('init.lua', 'w') as config_file:
    config_file.write(config_output)


print("Complete!")
