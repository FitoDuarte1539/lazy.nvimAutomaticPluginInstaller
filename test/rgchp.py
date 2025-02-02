from rich.console import Console
from rich.text import Text
from rich.live import Live
from rich.panel import Panel
from rich.align import Align


def print_menu(console: Console, current_index, menu_items):

    text_width = max(len(item) for item in menu_items)
    menu = []

    for index, choice in enumerate(menu_items):
        if index == current_index:
            choice = Text(choice, style="bold yellow")
        else:
            choice = Text(choice)

        choicelen = len(choice)
        pad_len = text_width - choicelen
        leftpad = pad_len // 2

        rightpad = pad_len - leftpad

        leftpadtxt = Text(" " * leftpad)
        rightpadtxt = Text(" " * rightpad)

        menu.append(leftpadtxt + choice + rightpadtxt)

        result = Text()
        for i, item in enumerate(menu):
            if i == len(menu) - 1:
                result += item + "\n"
            else:
                result += item + "\n\n"

    return result


def generate_panel(choices, console, selected_index):
    choices = ["Install Plugins", "Configure Plugins", "Settings", "Help"]
    selected_index = 0
    menu_text = print_menu(console, selected_index, choices)

    terminal_width, terminal_height = console.size

    panel = Align.center(Panel(Align(menu_text, align="center"),
                               title="NVIM PLUGIN INSTALLER",
                               border_style="blue",
                               padding=2,
                               width=terminal_width//2))

    return panel


def gui():
    console = Console()
    console.clear()
    choices = ["Install Plugins", "Configure Plugins", "Settings", "Help"]
    selected_index = 0

    with Live(generate_panel(choices, console, selected_index), console=console, refresh_per_second=20) as live:
        key = console.input()

        if key == 'up':
            selected_index = (selected_index - 1) % len(choices)

        elif key == 'down':
            selected_index = (selected_index + 1) % len(choices)

        live.update(generate_panel(choices, console, selected_index))


if __name__ == "__main__":
    gui()
