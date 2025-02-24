def status(name, template, tailwind):
    if name is not None:
        print(f"✅ Name: {name}")
    else:
        print("❌ Name: not set")
    if template is not None:
        print(f"✅ Template: {template}")
    else:
        print("❌ Template: not set")
    if tailwind is not None:
        print(f"✅ You are using TailwindCSS")
    else:
        print("❌ You aren't using TailwindCSS")
