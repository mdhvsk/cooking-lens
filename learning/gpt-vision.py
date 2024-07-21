from openai import OpenAI
from PIL import Image
import base64

client = OpenAI()


def clean_img(image):
    with Image.open(image) as img:
        # Convert the image to RGB mode if it's not already, as JPEG doesn't support RGBA
        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGB')
        # Save the image as JPEG
        img.save(img, 'JPEG')
    pass


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image



def generate_image_to_text(image):
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "I will provide an image of a food item. Return back only the name of the ingredient in json format."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image}"
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return response


image_path = "path_to_your_image.jpg"

# Getting the base64 string

img = '/Users/madhavasok/Documents/projects/cooking-lens/images/carrot.jpeg'

base64_image = encode_image(img)

print(generate_image_to_text(base64_image))
