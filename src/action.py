import requests
import os
import filetype
from dotenv import load_dotenv

load_dotenv()


PATH = "https://api.imgbb.com/1/upload"
API_KEY = os.getenv("IMGBB_API_KEY")
ALLOWED_MIMES = {
    "image/jpeg",
    "image/png",
    "image/bmp",
    "image/gif",
    "image/tiff",
    "image/webp",
    "image/heic",
    "image/avif",
    "application/pdf",
}


# print(API_KEY)


def uploadFile(path, expiration):

    if not os.path.isfile(path):
        raise FileNotFoundError(f"File Not found {path}")

    file_kind = filetype.guess(path)
    # JPG PNG BMP GIF TIF WEBP HEIC AVIF PDF
    if file_kind is None:
        raise ValueError("Unable to determine file type")

    mime = file_kind.mime.lower()

    if mime not in ALLOWED_MIMES:
        raise ValueError(f"Unsupported File type {mime}")

    params = {
        "key": API_KEY,
    }

    if expiration:
        if 60 <= int(expiration) <= 15552000:
            params["e"] = int(expiration)
        else:
            raise ValueError("Expliration value out of range")

    with open(path, "rb") as image_file:
        files = {"image": (os.path.basename(path), image_file, mime)}

        response = requests.post(
            PATH,
            files=files,
            params=params,
        )

        if response.status_code != 200:
            raise RuntimeError(f"Failed to upload file {response.text}")

        data = response.json()
        return data["data"]["url"]
