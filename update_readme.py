import random
import re

# List of available themes for GitHub stats
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

# List of colors for Komarev visit counter badge
komarev_colors = [
    "brightgreen", "green", "yellow", "yellowgreen", "orange", "red", "blue", "grey", 
    "lightgrey", "blueviolet", "ff69b4",  # Requested colors
    "00b7eb",  # Cyan
    "ff4500",  # OrangeRed
    "8a2be2",  # Purple
    "00ff7f",  # SpringGreen
    "ff1493",  # DeepPink
    "00ced1",  # DarkTurquoise
    "ff8c00",  # DarkOrange
    "9932cc",  # DarkOrchid
    "00ff00",  # Lime
    "ff00ff"   # Magenta
    # Soft & Elegant Colors
    "FFB6C1",  # Light Pink
    "ADD8E6",  # Light Blue
    "98FB98",  # Pale Green
    "FFFF99",  # Canary Yellow
    "DDA0DD",  # Plum
    "FFDAB9",  # Peach Puff
    "87CEFA",  # Light Sky Blue
    "FFA07A",  # Light Salmon
    "20B2AA",  # Light Sea Green
    "F08080",  # Light Coral
    "B0E0E6",  # Powder Blue
    "FFDEAD",  # Navajo White
    "E6E6FA",  # Lavender
    "98FF98",  # Mint Green
    "AFEEEE",  # Pale Turquoise

    # Additional Classy Colors
    "708090",  # Slate Gray
    "4682B4",  # Steel Blue
    "BC8F8F",  # Rosy Brown
    "F5DEB3",  # Wheat
    "DEB887",  # Burly Wood
    "B0C4DE",  # Light Steel Blue
    "C0C0C0",  # Silver
    "A9A9A9",  # Dark Gray
    "5F9EA0",  # Cadet Blue
    "8FBC8F",  # Dark Sea Green
    "DAA520",  # Goldenrod
    "D2B48C",  # Tan
    "CD853F",  # Peru
    "FFE4C4",  # Bisque
    "BDB76B",  # Dark Khaki
    "EEE8AA",  # Pale Goldenrod
]

# Select a random theme and color
random_theme = random.choice(themes)
random_komarev_color = random.choice(komarev_colors)

# Read the README file
with open("README.md", "r") as file:
    content = file.read()

# Update GitHub stats URLs with the new theme
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

# Function to update the color in the Komarev badge URL
def update_komarev_color(match):
    image_link = match.group(0)
    # Replace the color parameter within the URL
    updated_image_link = re.sub(r'color=[^&)]+', f'color={random_komarev_color}', image_link)
    return updated_image_link

# Update the entire image link for the Komarev badge
updated_content = re.sub(
    r'!\[.*?\]\(https://komarev\.com/ghpvc/\?[^)]*\)',
    update_komarev_color,
    updated_content
)

# Write the updated content back
with open("README.md", "w") as file:
    file.write(updated_content)

#print(f"Updated GitHub stats theme to: {random_theme}")
#print(f"Updated Komarev badge color to: {random_komarev_color}")
