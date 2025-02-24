html_boilerplate = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>Javascript template</title>
</head>
<body>
    
</body>
</html>
"""

html_with_tailwind_boilerplate = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <script src="https://unpkg.com/@tailwindcss/browser@4"></script>
    <title>Javascript with TailwindCSS template</title>
</head>
<body>
    
</body>
</html>
"""

css_boilerplate = """
html,
body {
    background-color: #121212;
    color: #ffffff;
}
"""

js_boilerplate = """
// Your code goes here
console.log("Hello from Boilerflow!")
"""

javascript = {
    "index.html": html_boilerplate,
    "index.html_tailwind": html_with_tailwind_boilerplate,
    "style.css": css_boilerplate,
    "index.js": js_boilerplate,
}
