import typing as t
import io
import requests

import constants


def send_images_and_predict(images: t.List) -> str:
    files = []
    for i, image in enumerate(images):
        buf = io.BytesIO()
        image.save(buf, format="jpeg")
        buf.seek(0)
        files.append(("files", buf))

    r = requests.post(constants.SERVER_URL, files=files)
    try:
        return r.json()["class"]
    except KeyError:
        print("KeyError")
        print(r.json())
        return "trash"
