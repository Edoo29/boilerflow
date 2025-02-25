import os
from boilerplates.javascript import javascript

html = javascript["index.html"]
html_with_tailwind = javascript["index.html_tailwind"]
css = javascript["style.css"]
js = javascript["index.js"]


def create_javascript(name, use_tailwind):
    print("✨ Project creation started...")
    print()

    # Create folders
    os.mkdir(name)
    os.mkdir(f"{name}/src")
    if not use_tailwind:
        os.mkdir(f"{name}/css")

    # Initialize NPM
    os.system(f"cd {name} && npm init -y")

    # Create files
    # HTML
    with open(f"{name}/index.html", "w") as f:
        if not use_tailwind:
            f.write(html)
        else:
            f.write(html_with_tailwind)
    # CSS
    if not use_tailwind:
        with open(f"{name}/css/style.css", "w") as f:
            f.write(css)
    # JavaScript
    with open(f"{name}/src/index.js", "w") as f:
        f.write(js)

    print("✅ Project created successfully!")
    if use_tailwind:
        print(
            "⚠️ NOTE: This boilerplate use the Play CDN of TailwindCSS to use it only in development. Make sure to actually install TailwindCSS."
        )
    print(f'✨ Now type cd "{name}" and run "npm install" to install the dependencies.')
    print()
    exit()
