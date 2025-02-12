import os

from jinja2 import Environment, FileSystemLoader

# Need to encapsulate in a function to be able to call from other file/script
def main(work_dir):

        # we need to configure th path to templates dynamically
        path_to_templates = os.path.join(work_dir, 'templates')
        env = Environment(loader=FileSystemLoader(path_to_templates))
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

if __name__ == '__main__':
        main()