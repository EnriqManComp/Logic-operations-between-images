'''
Logic operations with binary images using two approaches 
'''
# Libraries
import cv2
import numpy as np

# Class definition
class logic:

    def __init__(self,dir):
        # Constructor
        self.dir = dir
        # Get image in the path dir
        self.image = cv2.imread(self.dir)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # Normalize image ( 255 -> 1.0 , 0 -> 0.0 )
        self.image = self.image.astype(np.float32) / 255.0

    def applyFirstLogicMethod(self,operator,image2,image3):
        # Apply first method of logic operation using numpy
        # Dictionary of logic options
        opcion_dict = {'AND': np.logical_and(self.image,np.logical_and(image2,image3)),
                        'OR':np.logical_or(self.image,np.logical_or(image2,image3)),
                        'XOR': np.logical_xor(self.image,np.logical_xor(image2,image3)),
                        'XNOR': np.logical_not(np.logical_xor(self.image,np.logical_xor(image2,image3))),
                        'NOR': np.logical_not(np.logical_or(self.image,np.logical_xor(image2,image3))),
                        'NAND': np.logical_not(np.logical_and(self.image,np.logical_xor(image2,image3)))}
        # Apply operation
        image2image = opcion_dict[operator]
        # Convert of boolean type to float type
        image2image = np.where(image2image==True,1.0,image2image)
        image2image = np.where(image2image==False,0.0,image2image)
        return image2image
    
    def applySecondLogicMethod(self,operator,image2,image3):
        # Apply second method of logic operation, bit level approach
        # Dictionary of logic options
        opcion_dict = {'AND': self & image2 & image3,
                        'OR': self | image2 | image3,
                        'XOR': self ^ image2 ^ image3,
                        'XNOR': ~(self ^ image2 ^ image3),
                        'NAND': ~(self & image2 & image3),
                        'NOR': ~(self | image2 | image3)}
        # Apply operation
        image2image = opcion_dict[operator]
        # Convert of boolean type to float type
        image2image = np.where(image2image==True,1.0,image2image)
        image2image = np.where(image2image==False,0.0,image2image)
        return image2image
    
    def getImage(self):
        return self.image

################################## MAIN ###################################################

# Create objects

image1Object = logic('geom1.JPG')
image2Object = logic('geom2.JPG')
image3Object = logic('geom3.JPG')

# Apply the two methods
# VALID LOGIC OPERATORS = 'AND', 'OR', 'XOR', 'XNOR', 'NAND', 'NOR'  

resultMethod_1 = image1Object.applyFirstLogicMethod('XOR',image2Object.image,image3Object.image)
resultMethod_2 = image1Object.applyFirstLogicMethod('XOR',image2Object.image,image3Object.image)

cv2.namedWindow('First Method Left || Second Method Right', cv2.WINDOW_FULLSCREEN)
resultMethod_1 = cv2.resize(resultMethod_1, (700,500))
resultMethod_2 = cv2.resize(resultMethod_2, (700,500))

dim = resultMethod_1.shape
separator = np.ones((dim[0],5))
results = np.concatenate((np.concatenate((resultMethod_1,separator),axis=1), resultMethod_2),axis=1)

# Visualize
cv2.imshow('First Method Left || Second Method Right',results)
#cv2.imshow('First Method of Logic Operation',resultMethod_1)
#cv2.imshow('Second Method of Logic Operation',resultMethod_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
