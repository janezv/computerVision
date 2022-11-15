import cv2
import numpy as np
import matplotlib.pyplot as plt


road=cv2.imread('../DATA/road_image.jpg')
road_copy=road.copy()
# plt.imshow(road_copy)




marker_image=np.zeros(road.shape[:2],dtype=np.int32)
segment=np.zeros(road.shape,dtype=np.uint8)


# plt.show()


from matplotlib import cm
cm.tab10(0)

def create_rgb(i):
   return tuple(np.array(cm.tab10(i)[:3])*255)

colors=[]
for i in range(10):
    colors.append(create_rgb(i))

print(colors)


####
# global variables
n_markers = 10
current_marker=1 # color position in the list of color color=[]
marks_updated=False # checks if the markers bave been updated by WATERSHED


# callback funcgion
def mouse_callback(event,x,y,flags,pramam):
    global marks_updated

    if event==cv2.EVENT_LBUTTONDOWN:
        # MARKERS PASSE TO THE WATERSHED ALGORITHM
        cv2.circle(marker_image,(x,y),10,(current_marker),-1)

        # USER SEES ON THE ROAM IMAGE
        cv2.circle(road_copy,(x,y),10,colors[current_marker],-1)

        marks_updated = True

# while true
cv2.namedWindow('Road Image')
cv2.setMouseCallback('Road Image', mouse_callback)


while True:
    cv2.imshow('Watershed Segments', segment)
    cv2.imshow('Road Image', road_copy)
    
    # CLOSE ALL WINDOWS
    k=cv2.waitKey(1)

    if k== 27: # 27 is ESCAPE key
        break
    
    # clearing all the colors, when user press c key; RESET IMAGES
    elif k == ord('c'):
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[:2],dtype=np.int32)
        segment = np.zeros(road.shape,dtype=np.uint8)
    
    
    # UPDATE COLOR CHOICE
    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))

    # UPDATE THE MARKINGS
    if marks_updated:
        marker_image_copy = marker_image.copy()
        cv2.watershed(road, marker_image_copy)

        segments = np.zeros(road.shape, dtype=np.uint8)

        for color_ind in range(n_markers):
            segment[marker_image_copy==(color_ind)]=colors[color_ind]


cv2.destroyAllWindows()












