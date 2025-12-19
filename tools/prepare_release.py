from pathlib import Path

ROOT = Path(__file__).parents[1]


def announce(tag: str):
    releases_path = Path(
        ROOT, "docs", "start", "modules", "ROOT", "pages", "releases.adoc"
    )
    assert releases_path.exists()
    lines = releases_path.read_text().splitlines()

    index = lines.index("// latest")

    if tag in lines[index + 1]:
        print("Tag already exists, skipping")
    else:
        new_line = (
            f"- https://github.com/palmsens/palmsens_sdk/releases/tag/maui-{tag}[{tag}]"
        )
        lines.insert(index + 1, new_line)
        releases_path.write_text("\n".join(lines) + "\n", encoding="UTF-8")
        print(f"Tag added to {releases_path.name}")


if __name__ == "__main__":
    announce("python-1.5.0")
