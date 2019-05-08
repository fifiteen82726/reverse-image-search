# import numpy as np
# import pandas as pd
# import cv2
# import matplotlib.pyplot as plt
# import os

# dataset_path = '../app/assets/images/paris/louvre/paris_louvre_000004.jpg'
# # img_building = cv2.imread(os.path.join(dataset_path, 'paris_louvre_000013.jpg'))
# img_building = cv2.imread(dataset_path)
# print '123'

# # print (os.path.join(dataset_path, 'paris_louvre_000013.jpg'))

# # Convert from cv's BRG default color order to RGB
# img_building = cv2.cvtColor(img_building, cv2.COLOR_BGR2RGB)
# orb = cv2.ORB_create()  # OpenCV 3 backward incompatibility: Do not create a detector with `cv2.ORB()`.
# key_points, description = orb.detectAndCompute(img_building, None)



# print sum(k.class_id == -1 for k in key_points)


# img_building_keypoints = cv2.drawKeypoints(img_building,
#                                            [key_points[0]],
#                                            img_building,
#                                            flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) # Draw circles.
# # plt.figure(figsize=(16, 16))
# plt.title('ORB Interest Points')
# plt.imshow(img_building_keypoints)
# plt.show()


from image_match.goldberg import ImageSignature
gis = ImageSignature()
a = gis.generate_signature('paris_louvre_000004.jpg')

print a
# b = gis.generate_signature('https://pixabay.com/static/uploads/photo/2012/11/28/08/56/mona-lisa-67506_960_720.jpg')
# gis.normalized_distance(a, b)
