import os
import base64

from PIL import Image
from io import BytesIO

def image_to_base64_str(image_path):
    ext = os.path.splitext(image_path)[1].lower()
    if ext == ".svg":
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    else:
        img = Image.open(image_path)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()