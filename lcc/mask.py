import cv2

import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

import numpy as np

image = cv2.imread('./LCC5.jpeg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

print(hsv_image.shape)

plt.imshow(image)
plt.show()

# masking range in hsv
lower_bound = (20, 60, 35)
upper_bound = (100, 255, 255)

# show image from masking range
lower_square = np.full((10, 10, 3), lower_bound, dtype=np.uint8) / 255.0
upper_square = np.full((10, 10, 3), upper_bound, dtype=np.uint8) / 255.0

plt.imshow(hsv_to_rgb(lower_square))
plt.show()

plt.imshow(hsv_to_rgb(upper_square))
plt.show()

mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
result = cv2.bitwise_and(image, image, mask=mask)

plt.imshow(result)
plt.show()