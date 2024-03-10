# face-blur-detection

Detect

BLUR DETECTION TECHNIQUES

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
   
3.  Laplacian Operator (LAP)
This method is implemented to discover edges in a
picture. It is additionally a derivative operator but
the basic contrast between different operators like
Sobel, Kirsch and Laplacian operator is that all other
derivatives are first order derivative mask. Laplacian
operator is further separated into two classification
which are the positive Laplacian operator and
negative Laplacian operator. 

Combine FFT and HWT to detect face blur to make accuracy higher.




Python3
opencv-python
PyWavelets
gradio
insightface

$ pip install -r requirements.txt
