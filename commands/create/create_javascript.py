import os
from boilerplates.javascript import javascript

html = javascript["index.html"]
css = javascript["style.css"]
js = javascript["index.js"]


def create_javascript(name):
    print("✨ Project creation started...")
    print()

    # Create folders
    os.mkdir(name)
    os.mkdir(f"{name}/src")
    os.mkdir(f"{name}/css")

    # Initialize NPM
    os.system(f"cd {name} && npm init -y")

    # Create files
    # HTML
    with open(f"{name}/index.html", "w") as f:
        f.write(html)
    # CSS
    with open(f"{name}/css/style.css", "w") as f:
        f.write(css)
    # JavaScript
    with open(f"{name}/src/index.js", "w") as f:
        f.write(js)

    print("✅ Project created successfully!")
    print(f'✨ Now type cd "{name}" and run "npm install" to install the dependencies.')
    print()
    exit()
