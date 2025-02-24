import re


def name(arg):
    if arg == "":
        print("❌ Project name cannot be empty.")
    else:
        if re.match("^[a-zA-Z0-9_\-]*$", arg):
            print(f'✅ The name "{arg}" has been chosen.')
            return arg
        else:
            print("❌ Project name is not valid.")
            print(
                "You can only use letters (a-z), numbers (0-9), underscores (_), and hyphens (-)."
            )
            return None
