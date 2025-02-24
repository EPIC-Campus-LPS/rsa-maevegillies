import cv2
from blake3 import blake3

def random_num(upper, lower):

    diff = upper - lower

    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    cv2.imwrite("captured_image.jpg", frame)
    camera.release()

    for i in range(100):
        result, image = camera.read()


    with open("captured_image.jpg", "rb") as file:
        image_bytes = file.read()



    image_hash = blake3(image_bytes).hexdigest()
    i = int(image_hash, 16)
    i = i % diff
    i = i + lower
    return(i)
    



