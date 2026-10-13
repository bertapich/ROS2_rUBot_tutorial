# ROS 2 TF2 — POSE Exercises

## Objective

Represent the pose of `Target B` with respect to the `UR5e Base` using ROS 2
TF2, compare the RPY, rotation-matrix, Euler ZYZ, AO-vector, angle-axis and
quaternion representations, and verify the result in RViz2.

The exercise uses the same target as `Ex4_RPY.py`:

```text
Position [mm] = [350, -350, 170]
RPY [deg]     = [135, 0, 60]
```

ROS uses metres, so the published translation is:

```text
[0.350, -0.350, 0.170]
```

## Questions

1. Which is the RPY orientation of `Target B` with respect to `UR5e Base`?
2. Find analytically the rotation matrix that represents this orientation.
3. Find the Euler ZYZ angles and the Approach and Orthogonal vectors.
4. Obtain the angle-axis and quaternion representations.
5. Publish the transform `ur5e_base -> target_b` with TF2.
6. Verify the numerical result with `tf2_echo` and the graphical result in
   RViz2.
7. Explain why SpatialMath `[w, x, y, z]` quaternion output must be reordered
   before assigning a ROS `geometry_msgs/Quaternion` `[x, y, z, w]`.

## Expected analytical results

Using the fixed-axis XYZ RPY convention:

```text
R = Rz(yaw) @ Ry(pitch) @ Rx(roll)
```

the rotation matrix is:

```text
[[ 0.500000,  0.612372,  0.612372],
 [ 0.866025, -0.353553, -0.353553],
 [ 0.000000,  0.707107, -0.707107]]
```

Additional representations:

```text
Euler ZYZ [deg]             = [-30.0, 135.0, 90.0]
Approach vector             = [0.612372, -0.353553, -0.707107]
Orthogonal vector           = [0.612372, -0.353553, 0.707107]
Angle-axis                  = 141.290808 deg
Axis                        = [0.848029, 0.489610, 0.202803]
Quaternion ROS [x, y, z, w] = [0.800103, 0.461940, 0.191342, 0.331414]
```

Equivalent Euler-angle triples may exist. They are valid only if they reproduce
the same rotation matrix.

## Build and run the solution

```bash
cd ~/ROS2_rUBot_tutorial_ws
colcon build --packages-select pose_tf2 --symlink-install
source install/setup.bash
ros2 launch pose_tf2 exercise4.launch.py
```

RViz2 opens with:

- `Fixed Frame = ur5e_base`;
- a Grid display;
- the TF axes and frame names;
- an asymmetric orange object attached to `target_b`.

## Numerical and tree verification

Open two additional terminals and source the workspace in both:

```bash
ros2 run tf2_ros tf2_echo ur5e_base target_b
```

```bash
ros2 run tf2_tools view_frames
```

`tf2_echo` must report the translation and quaternion shown above.
`view_frames` must show one connected edge:

```text
ur5e_base -> target_b
```

## Experiment

Repeat the exercise with a different orientation:

```bash
ros2 launch pose_tf2 exercise4.launch.py \
  roll_deg:=90.0 pitch_deg:=30.0 yaw_deg:=45.0
```

Compare the new rotation matrix and quaternion with the orientation shown by
the TF axes and the asymmetric object in RViz2.
