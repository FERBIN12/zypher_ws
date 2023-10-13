import cv2
import numpy as np


# now we define the hsl values valurs of the white and yellow for segmentation
## white

hue_l_w=0
lit_l_w=255
sat_l_w=0

## white
hue_l_y=30
hue_h_y=33
lit_l_y=160
sat_l_y=0



def color_segmentation(hls,lower_range,upper_range):
    mask_in_range=cv2.inRange(hls,lower_range,upper_range)
    # we gotta remobe the noises from the masked frame for that we us morphology_dilate also used for object segmentatkon
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    mask_dilated=cv2.morphologyEx(mask_in_range,cv2.MORPH_DILATE,kernel)
    return mask_dilated



## define a function for segmenting lanes
def segment_lanes(frame,min_area):
       
    # we convert the color framews from BGR to HLS for segmentation 
    hls=cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)
    # segmenting white region
    white_regions=color_segmentation(hls,np.array([hue_l_w,lit_l_w,sat_l_w]),np.array([255,255,255])) # we use only np becase cvinrange takes only np arrays
    yellow_regions=color_segmentation(hls,np.array([hue_l_y,lit_l_y,sat_l_y]),np.array([hue_h_y,255,255]))

    cv2.imshow("WHite_regions",white_regions)
    cv2.imshow("Yellow_regions",yellow_regions)

    cv2.waitKey(1)
