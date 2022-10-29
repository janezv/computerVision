import cv2      
import numpy as np
import matplotlib.pyplot as plt


fcap0=cv2.VideoCapture(0)
fcap1=cv2.VideoCapture(1)

while 1:
    b0, f0=fcap0.read()
    b1, f1=fcap1.read()

    ############################################################################################
    ## Kamera 0
    f0_mean=np.mean(f0)

    #set lower value to either 0 pr 70% of the median value whichever is greater
    lower=int(max(0,0.7*f0_mean))
    upper=int(min(255,1.3*f0_mean))
    f0_edges=cv2.Canny(image=f0, threshold1=lower+40,threshold2=upper)

    #blured picture
    f0_blured=cv2.blur(f0, ksize=(9,9))

     #set lower value to either 0 pr 70% of the median value whichever is greater
    f0_mean=np.mean(f0_blured)
    lower=int(max(0,0.7*f0_mean))
    upper=int(min(255,1.3*f0_mean))
    f0_blured_edges=cv2.Canny(image=f0_blured, threshold1=lower,threshold2=upper)


    plt.subplot(243)
    plt.imshow(f0_blured)

    print("F0 mean value: ", f0_mean )
    plt.subplot(241)
    plt.imshow(f0)

    plt.subplot(242)
    plt.imshow(f0_edges)

    plt.subplot(243)
    plt.imshow(f0_blured)

    plt.subplot(244)
    plt.imshow(f0_blured_edges)

    ############################################################################################
    ## Kamera 1
    f1_mean=np.mean(f1)

    #set lower value to either 0 pr 70% of the median value whichever is greater
    lower=int(max(0,0.7*f1_mean))
    upper=int(min(255,1.3*f1_mean))
    f1_edges=cv2.Canny(image=f1, threshold1=lower,threshold2=upper)

    #blured picture
    f1_blured=cv2.blur(f1, ksize=(4,4))

     #set lower value to either 0 pr 70% of the median value whichever is greater
    f1_mean_blured=np.mean(f1_blured)
    lowerb=int(max(0,0.7*f1_mean_blured))
    upperb=int(min(255,1.3*f1_mean_blured))
    f1_blured_edges=cv2.Canny(image=f1_blured, threshold1=lower,threshold2=upper)


    plt.subplot(245)
    plt.imshow(f1)

    plt.subplot(246)
    plt.imshow(f1_edges)

    plt.subplot(247)
    plt.imshow(f1_blured)

    plt.subplot(248)
    plt.imshow(f1_blured_edges)

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show(block=False)
    plt.pause(4)


