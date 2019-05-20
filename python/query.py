# pylint: disable=invalid-name,missing-docstring,exec-used,too-many-arguments,too-few-public-methods,no-self-use
from __future__ import print_function

import sys
from src.color import Color
from src.daisy import Daisy
from src.DB import Database
from src.edge import Edge
from src.evaluate import infer
from src.gabor import Gabor
from src.HOG import HOG
from src.resnet import ResidualNet
from src.resnet import ResNetFeat
from src.vggnet import VGGNetFeat
import scipy.misc
import numpy as np
import torch

depth = 10
d_type = 'd1'
query_idx = 0
RES_model = 'resnet152'  # model type
means = np.array([103.939, 116.779, 123.68]) / \
    255.  # mean of three channels in the order of BGR
pick_layer = 'avg'        # extract feature of this layer




def create_query(d_img, d_cls):
  res_model = ResidualNet(model=RES_model)
  res_model.eval()
  img = scipy.misc.imread(d_img, mode="RGB")
  img = img[:, :, ::-1]  # switch to BGR
  img = np.transpose(img, (2, 0, 1)) / 255.
  img[0] -= means[0]  # reduce B's mean
  img[1] -= means[1]  # reduce G's mean
  img[2] -= means[2]  # reduce R's mean
  img = np.expand_dims(img, axis=0)

  inputs = torch.autograd.Variable(
    torch.from_numpy(img).float())
  d_hist = res_model(inputs)[pick_layer]
  d_hist = d_hist.data.cpu().numpy().flatten()
  d_hist /= np.sum(d_hist)  # normalize
  return {
    'img': d_img,
    'cls': d_cls,
    'hist': d_hist
  }


if __name__ == '__main__':
    db = Database()

    # methods to use
    methods = {
        "color": Color,
        "daisy": Daisy,
        "edge": Edge,
        "hog": HOG,
        "gabor": Gabor,
        "vgg": VGGNetFeat,
        "resnet": ResNetFeat
    }

    new_image = None
    # try:
    mthd = 'resnet'
    # print(mthd)
      # new_image = sys.argv[2]
    # except IndexError:
        # print("usage: {} <method>".format(sys.argv[0]))
        # print("supported methods:\ncolor, daisy, edge, gabor, hog, vgg, resnet")

    # call make_samples(db) accordingly
    samples = getattr(methods[mthd](), "make_samples")(db)
    # query the first img in data.csv
    # query = samples[query_idx]
    # print("\n[+] query: {}\n".format(query["img"]))

    make_query = create_query(sys.argv[1], sys.argv[2])

    print(make_query)

    # print(query == make_query)

    _, result = infer(make_query, samples=samples, depth=depth, d_type=d_type)

    r = []
    for match in result:
      # r.append(result['img'])
        print("{}:\t{},\tClass {}".format(match["img"],
                                          match["dis"],
                                          match["cls"]))
    # print(r)

    # f = open("", "a")
    # f.write("Now the file has more content!")
    # f.close()





