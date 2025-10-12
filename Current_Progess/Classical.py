import numpy as np
import matplotlib.pyplot as plt
def classical_Edge_detection(image,threshold):
  fig, axs = plt.subplots(1, 4, figsize=(16, 40))
  axs[0].imshow(image)
  axs[0].set_title("Original image")
  b=np.zeros_like(image)
  b[:-1]=np.abs(image[:-1]-image[1:])>threshold
  axs[1].imshow(b)
  axs[1].set_title("Horizontal Scan")
  c=np.zeros_like(image)
  c[:,:-1]=np.abs(image[:,:-1]-image[:,1:])>threshold
  axs[2].imshow(c)
  axs[2].set_title("VerticL Scan")
  d=b|c
  axs[3].set_title("Edge Detected Image")
  axs[3].imshow(d)