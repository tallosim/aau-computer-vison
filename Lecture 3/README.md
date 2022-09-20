# Exercises - Lecture 3

## Exercise 1

1. Load two partly overlapping images into OpenCV (`aau-city-1.jpg` and `aau-city-1.jpg` from Moodle, or take your own pictures)
2. Extract Harris Corners from both images. You may use the OpenCV function `cornerHarris()`
3. Design and implement your own simple corner matching procedure to find the same points in both images
    *Hint: Look for inspiration in this OpenCV demo: [Open CV: Harris Corner Detection](https://docs.opencv.org/master/dc/d0d/tutorial_py_features_harris.html)*

## Exercise 2

1. Change your solution from last exercise to extract SIFT keypoints and descriptors instead of Harris Corners and your own descriptors
2. Match feature descriptors using the `DescriptorMatcher` class
3. Visualize the matches using the `drawMatches` function

## Exercise 3

1. Use a homography which includes RANSAC to calculate the transformation between the two images (look at `findHomography()` and `warpPerspective()`)
