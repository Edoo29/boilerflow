# Builtin modules
import cmd

# My modules
# Utils
from utils.clear_screen import clear_screen
from utils.intro_text import intro_text

# Commands
from commands.help import help
from commands.name import name
from commands.template import template
from commands.status import status
from commands.use import use
from commands.create.create_javascript import create_javascript


# Main class
class App(cmd.Cmd):
    # Clear the screen for better readability
    clear_screen()

    version = "0.0.1"
    prompt = "\n🚀 Boilerflow> "
    intro = intro_text

    # Status variables
    name = None
    template = None
    use_tailwind = None

    # Status command
    def do_status(self, arg):
        status(self.name, self.template, self.use_tailwind)

    # Name command
    def do_name(self, arg):
        self.name = name(arg)

    # Template command
    def do_template(self, arg):
        self.template = template(arg)

    def do_go(self, arg):
        if self.name is not None and self.template is not None:
            if self.template == "JavaScript":
                create_javascript(self.name)
        else:
            return print(
                "❌ You must choose a name and a template before creating the project."
            )

    # TailwindCSS command
    def do_use(self, arg):
        self.use_tailwind = use(arg)

    # Help command
    def do_help(self, arg):
        help(arg)

    do_h = do_help

    # Version command
    def do_version(self, arg):
        print(self.version)

    # Exit command
    def do_exit(self, arg):
        clear_screen()
        return True


if __name__ == "__main__":
    App().cmdloop()
