import random
import re

# List of available themes
themes = [
    "default", "default_repocard", "transparent", "shadow_red", "shadow_green", "shadow_blue",
    "dark", "radical", "merko", "gruvbox", "gruvbox_light", "tokyonight", "onedark", "cobalt",
    "synthwave", "highcontrast", "dracula", "prussian", "monokai", "vue", "vue-dark",
    "shades-of-purple", "nightowl", "buefy", "blue-green", "algolia", "great-gatsby",
    "darcula", "bear", "solarized-dark", "solarized-light", "chartreuse-dark", "nord",
    "gotham", "material-palenight", "graywhite", "vision-friendly-dark", "ayu-mirage",
    "midnight-purple", "calm", "flag-india", "omni", "react", "jolly", "maroongold",
    "yeblu", "blueberry", "slateorange", "kacho_ga", "outrun", "ocean_dark", "city_lights",
    "github_dark", "github_dark_dimmed", "discord_old_blurple", "aura_dark", "panda",
    "noctis_minimus", "cobalt2", "swift", "aura", "apprentice", "moltack", "codeSTACKr",
    "rose_pine", "catppuccin_latte", "catppuccin_mocha", "date_night", "one_dark_pro",
    "rose", "holi", "neon", "blue_navy", "calm_pink", "ambient_gradient"
]

# Select a random theme
random_theme = random.choice(themes)

# Read the README file
with open("README.md", "r") as file:
    content = file.read()

# Update all three URLs with the new theme
updated_content = re.sub(
    r'(https://github-readme-stats\.vercel\.app/api\?username=mtptisid&theme=)[^&]+',
    rf'\1{random_theme}',
    content
)

updated_content = re.sub(
    r'(https://github-readme-streak-stats\.herokuapp\.com/\?user=mtptisid&theme=)[^&]+',
    rf'\1{random_theme}',
    updated_content
)

updated_content = re.sub(
    r'(https://github-readme-stats\.vercel\.app/api/top-langs/\?username=mtptisid&theme=)[^&]+',
    rf'\1{random_theme}',
    updated_content
)

# Write the updated content back
with open("README.md", "w") as file:
    file.write(updated_content)

print(f"Updated theme to: {random_theme}")
