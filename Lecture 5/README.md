# Exercises - Lecture 5

## Exercise 1

- Use the biker.png template from Exercise materials to do **mean shift tracking** in the traffic video in Exercise materials. (Hint: use OpenCV's [`calcBackProject()`](https://docs.opencv.org/3.4/da/d7f/tutorial_back_projection.html) function to produce a similarity image for mean shift - see [this mean shift tutorial](https://docs.opencv.org/3.4/d7/d00/tutorial_meanshift.html) for more pointers)
- Note that for mean shift tracking you need to provide an initial tracking window manually, and the biker only shows up from frame 114, so wait until then to start tracking.
- What happens when the biker disappears over the horizon? Why?

## Exercise 2

- Use the biker.png template from Exercise materials to do **Kalman filter tracking** in the traffic video in Exercise materials.
- Hints: See [this Python implementation](https://raw.githubusercontent.com/tobybreckon/python-examples-cv/master/kalman_tracking_live.py) for pointers. You can define the state as the position and velocity of the biker, and use the output of mean shift or cam shift (or a detection method of your choice) for the measurement update (note: we only measure position!). You will need to define a measurement matrix, a state transition matrix (motion model), as well as covariance matrices for the measurement and process (model) noise. You can start with unit matrices, and experiment with the parameters.
- What happens if you skip the measurement step for certain frames?
- Extra: Visualize the position uncertainty (`errorCovPost` attribute in OpenCV) as an ellipse. Plot the measured vs. Kalman filtered position over time and compare.
