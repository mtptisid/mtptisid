import random

# List of themes you want to cycle through
themes = ["flag-india", "neon", "dark", "gruvbox", "tokyonight", "radical"]

# Read the README.md file
with open("README.md", "r") as file:
    lines = file.readlines()

# Replace theme in streak stats URLs
updated_lines = []
for line in lines:
    if "github-readme-streak-stats" in line:
        new_theme = random.choice(themes)
        line = line.replace(
            line.split("&theme=")[1].split("&")[0], new_theme
        )  # Replace theme
    updated_lines.append(line)

# Write the updated content back to README.md
with open("README.md", "w") as file:
    file.writelines(updated_lines)
