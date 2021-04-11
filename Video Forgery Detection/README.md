<!-- ---
title: Video Forensics

Author: Himanshu Goyal 17CS02011
--- -->
# <center>Video Forensics</center>
## <center> Himanshu Goyal 17CS02011 </center> 
## Aim:
Location of the manipulations among the real and forged video sequences.

## Video Description:

**`Frame Details`**

> -   Height: 576
> -   Width: 768
> -   FPS: 30
> -   Total Frames: 390

There is movement of only one car in the real video throughout all the time. While, the only change in forged video is the movement of another car other than the original one for approximately _1sec_ i.e. _30-40 frames_. Afterwards, both forged and real videos are the *same* in appearance.  
![Frame1](./Results/original.png)
<center> Orginal video frame sequence</center>  

![Frame 1](./Results/forge.png)
<center> Forged video frame sequence
</center>

## Approach
![Approach](methodology.svg)

## Results
> 1. Orginal Frame
> 2. Forged Frame
> 3. Combined(Statistical+Optical Flow)
> 4. Optical Flow
> 5. Statistical
<!-- ![first](check.svg) 
![second](pcheck.png)         -->
### Result 1
![frames1](./Results/frames_1.png)
![results1](./Results/results_1.png)
### Result 2
![frames2](./Results/frames_2.png)
![results2](./Results/results_2.png)
### Result 3
![frames3](./Results/frames_3.png)
![results3](./Results/results_3.png)
### Result 4
![frames4](./Results/frames_4.png)
![results4](./Results/results_4.png)
## Conclusion
The modifications in the forged video was quite evident using both statistical and optical flow. The optical flow is obviously dominating in the overall error localization. 
I hope the results would have been more clearer if smaller block size is taken into consideration for feature calculation.
