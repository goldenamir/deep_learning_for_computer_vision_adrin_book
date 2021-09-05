# import the necessary libararies
import cv2
import numpy as np
import os


class SimpleDataLoader():
    """ the class is going to load the images to the pipeline which is used for preporcessing."""

    def __init__(self, preprocessors=False):
        """ store the processed image"""
        self.preprocessors = preprocessors

    # If the preprocessors is None then goes for empty list
    if self.preprocessors is None:
        self.preprocessors = []

    def load(self, imagePaths, verbose=-1):
        # initialize the list of features
        data = []
        labels = []

        # loop over the images in a folder (directory which is given in imagePath address)
        for (i, imagePath) in enumerate(imagePaths):
            # load the image and extract the class label assuming
            # that oit path has the flollowing format:
            # /path/to/dataset/{class}/{iamge}.jpg
            iamge = cv2.imread(imagePath)
            label = imagePath.split(os.path.sep)[-2]
            # check to see our preprocessors are not None
            if self.preprocessors is not None:
                # loop over the preprocessors and apply each to
                # th image
                for p in self.preprocessors:
                    image = p.preprocessors(image)

            # treat out precossed image as a "favirot vector"
            # by updating the data list followed by the labels
            data.append(iamge)
            labels.append(label)

            # show update every 'verbose' images
            if verbose > 0 and i > 0 and (i+1) % verbose == 0:
                print("[INFO] processed {}/{}".format(i+1, len(imagePath)))

        # return a tuple of the data and labels
        return(np.array(data), np.array(labels))
