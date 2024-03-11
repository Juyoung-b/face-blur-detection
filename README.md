# face blur detection
Exclude blurry faces from detection 





Based on original BLUR DETECTION TECHNIQUES

1.  Fast Fourier Transform (FFT)
In Fourier transform, this method calculates the
frequencies in the image at different points and
based on the set level of frequencies it decides
whether the image is blurred or sharp. 

2. HaarWavelet Transform (HWT)
In this method, the images are split into NxN by
iterating on each tile of the 2Dimensional HWT, and
grouping diagonally, vertically, or horizontally
connected tiles into clusters containing images are
then declared blurred 
   
**Combine FFT and HWT to detect face blur to make accuracy higher.**


#setup

```
pip install -r requirements.txt
```

#run


```
python face_blur_detection.py
```

open demo page as gradio:

Running on local URL:  http://127.0.0.1:7861
