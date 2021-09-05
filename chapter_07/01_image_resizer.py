# import the necessary libararies
import cv2


class SimplePreprocessing():
    """ the class if for preprocessing a pipeline which used to define the size of any input image"""""

    def __init__(self, width, height, inter=cv2.Inter):
        """ this funciton is a  constructor"""
        self.width = width
        self.height = height
        self.inter = inter

    def preprocessing(self, image):
        """ the function is going to resize the image """
        return cv2.resize(image, (self.width, self.height), interpolation=self.inter)
