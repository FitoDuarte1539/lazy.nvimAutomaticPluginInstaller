# Neovim Auto Installer

A Python-based tool to automate the setup and configuration of Neovim. Currently, the project features a work-in-progress terminal UI (TUI) for selecting plugins and configuration options.

### Current Features (WIP)

Terminal UI: A simple CLI-based interface to interact with the installer. This allows you to select Neovim plugins and configuration options. The UI is still in early stages.

### Planned Features

- Automated Dependency Installation: The installer will handle dependencies for Neovim and plugins.
- Plugin Management: Integration with lazy.nvim for managing plugins.
- Configuration Generation: Using Jinja templates to generate Lua configuration files for Neovim based on user input.
- YAML Configuration: User selections will be stored in YAML files for future customizations.
- Containerized Setup: Option to run the installer in a Docker container for easy distribution.

#### Requirements

Python 3.x
Neovim
pip (for Python dependencies)
git (for cloning plugin repositories)

### Installation (Python Virtual Environment Recommended)

Step 1: Set up a Python virtual environment
It's highly recommended to use a virtual environment to manage dependencies for this project. To set up a virtual environment, run the following commands:

```# Create a virtual environment (optional: replace 'venv' with your preferred name)
python -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```
Step 2: Clone the repository
```git clone https://github.com/yourusername/neovim-auto-installer.git
cd neovim-auto-installer
```
Step 3: Install Python dependencies
 FIXME: create dependancies.txt
 
Step 4: Run the program

```python gui.py
# This will launch the TUI where you can select plugins and configuration options. Note that the TUI is still a work-in-progress, so some functionality may not be complete.
python main.py
# This will make a simple config for vim settings based on templates
```
### Current Status

The project is in the early stages, with the TUI being the main feature available so far.
The planned features are yet to be fully implemented.
