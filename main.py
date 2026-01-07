import numpy as np 
from PIL import Image
def rgbimagetoarray(picture, size, min = 0, max = 225):
  preimage = Image.open(picture)
  image = np.asarray(preimage)
  pixelsize = (int(image.shape[0] / size[0]), int(image.shape[1] / size[1]))
  pixel = 0
  finished = np.zeros(size)
  for i in range(size[1]):
    for j in range(size[0]):
      pixel = 0
      for e in range(i * pixelsize[0], (i + 1) * pixelsize[0]):
        for f in range(j * pixelsize[1], (j + 1) * pixelsize[1]):
          pixel += np.average(image[e][f])
      average = 255 - int(pixel / (pixelsize[0] * pixelsize[1]))
      finished[i][j] = average * int(average < max) * int(average > min) + 255 * int(average >= max) + int(average <= min)
  return finished
a = rgbimagetoarray('9,0.jpg', (28, 28), min = 170, max = 230)
for i in a:
  for e in i:
    if e < 170:
      print('  ', end = '')
    else: print('██', end = '')
  print()