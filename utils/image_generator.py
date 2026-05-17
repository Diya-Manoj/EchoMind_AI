from PIL import Image, ImageDraw
import os
import random


def generate_image(prompt):

    prompt = prompt.lower()

    os.makedirs("generated_images", exist_ok=True)

    width = 900
    height = 500

    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    # -----------------------------------
    # CYBERPUNK / FUTURISTIC CITY
    # -----------------------------------

    if "city" in prompt or "cyberpunk" in prompt or "futuristic" in prompt:

        # Neon background
        for y in range(height):

            color = (
                20,
                int(20 + y * 0.2),
                int(60 + y * 0.3)
            )

            draw.line((0, y, width, y), fill=color)

        # Buildings
        for x in range(50, 850, 80):

            building_height = random.randint(150, 350)

            draw.rectangle(
                [(x, height - building_height), (x + 50, height)],
                fill=(30, 30, 40)
            )

            # Neon windows
            for wy in range(height - building_height + 20, height - 20, 30):

                draw.rectangle(
                    [(x + 10, wy), (x + 20, wy + 10)],
                    fill=(0, 255, 255)
                )

        draw.text(
            (30, 30),
            "Cyberpunk AI City",
            fill=(255, 255, 255)
        )

    # -----------------------------------
    # GALAXY / SPACE
    # -----------------------------------

    elif "space" in prompt or "galaxy" in prompt or "planet" in prompt:

        img.paste((5, 5, 30), [0, 0, width, height])

        # Stars
        for _ in range(200):

            x = random.randint(0, width)
            y = random.randint(0, height)

            draw.ellipse(
                [(x, y), (x + 3, y + 3)],
                fill=(255, 255, 255)
            )

        # Planet
        draw.ellipse(
            [(300, 120), (600, 420)],
            fill=(120, 80, 255)
        )

        draw.text(
            (30, 30),
            "Galaxy Scene",
            fill=(255, 255, 255)
        )

    # -----------------------------------
    # FOREST
    # -----------------------------------

    elif "forest" in prompt or "nature" in prompt:

        img.paste((100, 180, 255), [0, 0, width, height])

        draw.rectangle(
            [(0, 350), (900, 500)],
            fill=(40, 120, 40)
        )

        # Trees
        for x in range(50, 850, 100):

            draw.rectangle(
                [(x, 250), (x + 20, 400)],
                fill=(90, 50, 20)
            )

            draw.ellipse(
                [(x - 30, 180), (x + 50, 280)],
                fill=(30, 140, 30)
            )

        draw.text(
            (30, 30),
            "Nature Landscape",
            fill=(255, 255, 255)
        )

    # -----------------------------------
    # DEFAULT SUNSET
    # -----------------------------------

    else:

        pixels = img.load()

        for y in range(height):

            r = int(255 * (y / height))
            g = int(120 * (y / height))
            b = int(180 * (1 - y / height))

            for x in range(width):
                pixels[x, y] = (r, g, b)

        draw.ellipse(
            (350, 120, 550, 320),
            fill=(255, 220, 100)
        )

        draw.rectangle(
            [(0, 420), (900, 500)],
            fill=(20, 20, 35)
        )

        draw.text(
            (30, 30),
            "Sunset Artwork",
            fill=(255, 255, 255)
        )

    filepath = os.path.join(
        "generated_images",
        "generated_image.png"
    )

    img.save(filepath)

    return filepath