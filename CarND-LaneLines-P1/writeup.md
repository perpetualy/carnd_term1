P line one

# **Finding Lane Lines on the Road**

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./test_images_output/solidWhiteCurve.jpg "SolidWhiteCurve"
[image2]: ./test_images_output/solidWhiteRight.jpg "SolidWhiteRight"
[image3]: ./test_images_output/solidYellowCurve.jpg "SolidYellowCurve"
[image4]: ./test_images_output/solidYellowCurve2.jpg "SolidYellowCurve2"
[image5]: ./test_images_output/solidYellowLeft.jpg "SolidYellowLeft"
[image6]: ./test_images_output/whiteCarLaneSwitch.jpg "WhiteCarLaneSwitch"

[vedio1]: ./test_videos_output/solidYellowLeft.mp4 "SolidYellowLeftVedio"

---

### Reflection

### 1. My pipeline contains six steps.
* 1st load image as grayscale. 
* 2nd blur pictures using Gauss function.
* 3rd find edge using canny method. 
* 4th clip image region into triangle. 
* 5th find lane using houghlineP function. 
* 6th draw a line on the image.
	In the drawing line function. I've tried many times to keep the lines stable. Finally, I browse the comment in the function.
	So the gradient equation helped me to identity which lines belong to left or right. So I can save them to the correct array.
	After that I use the average function to calculate each x or y values, and then I use these values and the Two-point linear equation (y-y1)/(x-x1)=(y-y2)/(x-x2) to get the linear equation [y=ax+b].
	This equation is a easy way to find the relationship between x and y.
	So far I can use it to get x value after I fixed the y value.
	So that's the way I made the line marker more stable.

![alt text][image1]
![alt text][image3]
![alt text][image4]

### 2. Identify potential shortcomings with your current pipeline

The one is when the resolution of image changed. This pipeline cannot get correct result.
And when there is too much noise in the image, it's hard to find the correct point as the begin or the end of a line.Sometimes the line may jump to
an unknown position suddenly, it's weird..

### 3. Suggest possible improvements to your pipeline

Maybe one car should have a fixed resolution for recording, but the software can adapter different standard resolutions,like 960x540 1280x720 1920x1080
I heard that there is a way to blur picture again before call canny function.I don't know it works or not.
I can try it later.
