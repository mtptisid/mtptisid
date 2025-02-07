import random

# List of themes extracted from your HTML
themes = [
    "default", "default_repocard", "transparent", "shadow_red", "shadow_green", "shadow_blue", "dark", "radical", 
    "merko", "gruvbox", "gruvbox_light", "tokyonight", "onedark", "cobalt", "synthwave", "highcontrast", "dracula", 
    "prussian", "monokai", "vue", "vue-dark", "shades-of-purple", "nightowl", "buefy", "blue-green", "algolia", 
    "great-gatsby", "darcula", "bear", "solarized-dark", "solarized-light", "chartreuse-dark", "nord", "gotham", 
    "material-palenight", "graywhite", "vision-friendly-dark", "ayu-mirage", "midnight-purple", "calm", "flag-india", 
    "omni", "react", "jolly", "maroongold", "yeblu", "blueberry", "slateorange", "kacho_ga", "outrun", "ocean_dark", 
    "city_lights", "github_dark", "github_dark_dimmed", "discord_old_blurple", "aura_dark", "panda", "noctis_minimus", 
    "cobalt2", "swift", "aura", "apprentice", "moltack", "codeSTACKr", "rose_pine", "catppuccin_latte", 
    "catppuccin_mocha", "date_night", "one_dark_pro", "rose", "holi", "neon", "blue_navy", "calm_pink", "ambient_gradient"
]

# Select a random theme
new_theme = random.choice(themes)

# Read README.md
with open("README.md", "r") as file:
    readme_content = file.read()

# Replace existing theme in the line containing "github-readme-streak-stats"
updated_content = []
for line in readme_content.split("\n"):
    if "github-readme-streak-stats" in line:
        line = line.replace("theme=", f"theme={new_theme}")  # Update the theme
    updated_content.append(line)

# Write back the updated content
with open("README.md", "w") as file:
    file.write("\n".join(updated_content))
