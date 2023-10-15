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

# we create a src variable for storing the original image and hls for storing the hue,saturation and lightness of the image.
hls=0
src=0

# we define a function to extract masks of white and yellow regions 

def mask_extract():
    mask_w=clr_segment(hls,(hue_l_w,lit_l_w,sat_l_w),(255,255,255)) 
    mask_y=clr_segment(hls,(hue_l_y,lit_l_y,sat_l_y),(hue_h_y,255,255))

    # now we create a binary mask by setting the mask not equal to 0 ie ) pixels within re1 range will be True and others False
    mask_w_= mask_w != 0
    # now the white regions are extracted from the source image (src) by multiplying using the mask
    dst_w=src*(mask_w_[:,:,None].astype(src.dtype))  

    # now we do the same for yellow
    mask_y_= mask_y != 0
    dst_y=src*(mask_y_[:,:,None].astype(src.dtype)) # using astypr fucntion we make sure that the image is in the same format as the source image

    # now we display the white and yellow regions

    cv2.imshow("White region",dst_w)
    cv2.imshow("Yellow region",dst_y)


# Now we create few callback fucntions for updatinng any changes the user makes in the hls values by defigning them globally 

# for white regions
def on_hue_low_change_w(val):
    global hue_l_w
    hue_l_w=val
    mask_extract()

def on_lit_low_change_w(val):
    global lit_l_w
    lit_l_w=val
    mask_extract()

def on_sat_low_change_w(val):
    global sat_l_w
    sat_l_w=val
    mask_extract()

# for yellow regions

def on_hue_low_change_y(val):
    global hue_l_y
    hue_l_y=val
    mask_extract()
def on_hue_high_change_y(val):
    global hue_h_y
    hue_h_y=val
    mask_extract()

def on_lit_low_change_y(val):
    global lit_l_y
    lit_l_y=val
    mask_extract()

def on_sat_low_change_y(val):
    global lit_l_y
    lit_l_y=val
    mask_extract()


# then we use cv2 named window function to display yellow and white regions after segmentation

cv2.namedWindow("White_regions")
cv2.namedWindow("Yellow_regions")

# now we use trackerbar function to enable the user to change the hls value of the white/yellow regions 
# the paramaters are (name,created_window,initial hue value,max value,fucntion to update the value)

cv2.createTrackerbar("Hue_L_w","White_regions",hue_l_w,255,on_hue_low_change_w)
cv2.createTrackerbar("Lit_L_w","White_regions",lit_l_w,255,on_lit_low_change_w)
cv2.createTrackerbar("Sat_L_w","White_regions",sat_l_w,255,on_sat_low_change_w)

cv2.createTrackerbar("Hue_L_y","Yellow_regions",hue_l_y,255,on_hue_low_change_y)
cv2.createTrackerbar("Hue_h_y","Yellow_regions",hue_l_y,255,on_hue_high_change_y)
cv2.createTrackerbar("Lit_L_y","Yellow_regions",lit_l_y,255,on_lit_low_change_y)
cv2.createTrackerbar("Sat_L_y","Yellow_regions",sat_l_y,255,on_sat_low_change_y)




def color_segmentation(hls,lower_range,upper_range):
    mask_in_range=cv2.inRange(hls,lower_range,upper_range)
    # we gotta remobe the noises from the masked frame for that we us morphology_dilate also used for object segmentatkon
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    mask_dilated=cv2.morphologyEx(mask_in_range,cv2.MORPH_DILATE,kernel)
    return mask_dilated

# we define a clr_segement function to segment the needed color from the other colors

def clr_segment(hls,lower_range,upper_range):

    # then we create a mask that highlights the pixels given in the hls between the lower and upper range
    mask_in_range =cv2.inRange(hls,lower_range,upper_range)
    # now we create a kernel for performing morphological operations like dilation 
    # dilation is used to clear the unnecessary noises present when performing segmentation

    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))  # here ellipse is used as an strutural element and not any symmetric one because ellipse 
                                                                # is more sensitive to changes as it is bidirectional so will be helpful in smoothening.
    # then we perform morphological dilation on the masked element
    mask_dilated=cv2.morphologicalEx(mask_in_range,cv2.MORPH_DILATE,kernel) 

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
