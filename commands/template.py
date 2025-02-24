def template(arg):
    template = None
    # Valid templates
    if arg == "javascript":
        template = "JavaScript"
    elif arg == "react":
        template = "React"
    elif arg == "svelte":
        template = "Svelte"
    elif arg == "astro":
        template = "Astro"

    # Confirm message
    if template is not None:
        print(f'✅ The template "{template}" has been chosen.')
    else:
        print("❌ This template is not valid, please choose a valid template.")
    return template
