import os
import markdown


def convert_markdown_to_html(markdown_text):
    """Convert Markdown text into HTML."""
    return markdown.markdown(
        markdown_text,
        extensions=[
            "fenced_code",
            "tables"
        ]
    )


def create_html_document(html_body, title="Markdown Document"):
    """Create a complete HTML document."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>

{html_body}

</body>
</html>
"""


def main():
    path = input("Enter Markdown file path: ").strip()

    if not path:
        print("Error: Path cannot be empty.")
        return

    if not os.path.isfile(path):
        print("Error: File not found.")
        return

    if not path.lower().endswith(".md"):
        print("Error: Please provide a Markdown (.md) file.")
        return

    try:
        with open(path, "r", encoding="utf-8") as file:
            markdown_text = file.read()

    except PermissionError:
        print("Error: Permission denied.")
        return

    except OSError as error:
        print(f"Error reading file: {error}")
        return

    if not markdown_text.strip():
        print("Error: Markdown file is empty.")
        return

    print("\nConverting...")

    html_body = convert_markdown_to_html(markdown_text)

    title = os.path.splitext(os.path.basename(path))[0]

    html_document = create_html_document(
        html_body,
        title=title
    )

    output_path = os.path.splitext(path)[0] + ".html"

    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(html_document)

    except PermissionError:
        print("Error: Permission denied while creating HTML file.")
        return

    except OSError as error:
        print(f"Error writing file: {error}")
        return

    print("\n✓ Conversion successful!")
    print(f"HTML saved to: {output_path}")


if __name__ == "__main__":
    main()