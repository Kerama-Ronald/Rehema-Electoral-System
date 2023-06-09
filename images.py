from PIL import Image
from art import *
import os

def display_image():
    image_path = "Snapchat-482846735.jpg"  # Replace with the actual image file name

    # Load the image
    image = Image.open(image_path)

    # Resize the image to fit the terminal width
    terminal_width = os.get_terminal_size().columns - 2  # Subtract 2 to account for padding
    aspect_ratio = terminal_width / float(image.size[0])
    height = int(aspect_ratio * image.size[1] * 0.55)  # Adjust the aspect ratio and height to fit the terminal better
    image = image.resize((terminal_width, height), Image.ANTIALIAS)

    # Convert the image to ASCII art
    ascii_art = text2art("REHEMA", "block")

    # Print the ASCII art
    print(ascii_art)
    print()

    # Display the image
    print(image)

if __name__ == "__main__":
    display_image()
