
import gradio as gr
import numpy as np
from insightface.app import FaceAnalysis 
from blur_func import blur_fft, blur_hwt
from PIL import Image

import cv2

def get_sharp_face(image):
    face_coordinates=[]
    image = Image.fromarray(image)
    image = image.convert("RGB")
    faceapp = FaceAnalysis(name='buffalo_l')  # noqa
    faceapp.prepare(ctx_id=0, det_size=(640, 640))
    image = np.array(image)
    faces = faceapp.get(image)

    for face in faces:
        bbox_lst = face["bbox"].tolist()
        face_coordinates.append(bbox_lst)
    print(face_coordinates)

    indices = [
        index
        for index, element in enumerate(face_coordinates)
        if (
                        blur_hwt(image[int(element[1]):int(element[3]), int(element[0]):int(element[2])], 30) > 0.73
                        and blur_fft(
                    image[int(element[1]):int(element[3]), int(element[0]):int(element[2])]) > 10
                )
        
    ]

    faces = [faces[index] for index in range(len(faces)) if index not in indices]

    for i in range(len(faces)):
        face = faces[i]
        box = face.bbox.astype(int)
        color = (0, 0, 255)
        cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), color, 2)
        cv2.putText(
            image,
            "%d" % (i),
            (box[0] - 1, box[1] - 4),
            cv2.FONT_HERSHEY_COMPLEX,
            0.7,
            (0, 255, 0),
            1,
        )

    return image


css = ".output-image, .input-image, .image-preview {height: 600px !important} "
with gr.Blocks(css=css) as demo:
    gr.Markdown(
        """
    # FACE blur detection demo page 🐣
    """
    )
    inp = gr.Image()
    out = gr.Image()
    inp.change(get_sharp_face, inp, out)
    
demo.launch(share=True)
