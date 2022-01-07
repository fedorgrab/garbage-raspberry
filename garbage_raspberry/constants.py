SERVER_URL = "http://34.121.25.48/predict"
IMG_SIZE = (320, 320)
TRASH = 0
RECYCLE = 1
COMPOST = 2

CLASS_TO_BIN_MAP = {
    "trash": TRASH,
    "glass": RECYCLE,
    "cardboard": RECYCLE,
    "paper": RECYCLE,
    "metal": RECYCLE,
    "plastic": RECYCLE,
    "compost": COMPOST,
}


CLASSES = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]
NUMBER_OF_IMAGES_TO_PROCESS = 2
