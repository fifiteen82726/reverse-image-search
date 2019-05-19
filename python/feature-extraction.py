import os
import sys


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


def generate_sign():
  gis = ImageSignature()

  if len(sys.argv) > 1:
    path = 'python/img/' + sys.argv[1] + '.jpg'
  else:
    path = 'new.jpg'

  a = gis.generate_signature(path)

  print a
  # b = gis.generate_signature('https://pixabay.com/static/uploads/photo/2012/11/28/08/56/mona-lisa-67506_960_720.jpg')
# gis.normalized_distance(a, b)



# Compare two image
gis = ImageSignature()
a = '../app/assets/images/paris/louvre/paris_louvre_000142.jpg'
b = '../app/assets/images/paris/louvre/paris_louvre_000142.jpg'

b = 'img/1557352391.jpg'



a_s = gis.generate_signature(a)
b_s = gis.generate_signature(b)

print gis.normalized_distance(a_s, b_s)

from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES

def add_image():
  es = Elasticsearch()
  ses = SignatureES(es)
  ses = SignatureES(es, distance_cutoff=0.3)
  ses.add_image('../app/assets/images/paris/louvre/paris_louvre_000142.jpg')
  ses.add_image('../app/assets/images/paris/louvre/paris_louvre_000004.jpg')
  ses.add_image('../app/assets/images/paris/louvre/paris_louvre_000008.jpg')


# # add_image()

# es = Elasticsearch()
# ses = SignatureES(es, distance_cutoff=1.0)
# print ses.search_image('../app/assets/images/paris/louvre/paris_louvre_000004.jpg')
# print ses.search_image('img/1557352391.jpg')

# # ses.add_image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg/687px-Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg')
# # ses.add_image('https://pixabay.com/static/uploads/photo/2012/11/28/08/56/mona-lisa-67506_960_720.jpg')
# # ses.add_image('https://upload.wikimedia.org/wikipedia/commons/e/e0/Caravaggio_-_Cena_in_Emmaus.jpg')
# # ses.add_image('https://c2.staticflickr.com/8/7158/6814444991_08d82de57e_z.jpg')
