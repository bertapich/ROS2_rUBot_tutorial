# pose_tf2

ROS 2 Humble package for Exercise 4: publish the transform
`ur5e_base -> target_b` with TF2 and display it in RViz2.

The exercise statement, theory and expected results are in
[ROS 2 TF2 - POSE Exercise 4](../../Documentation/04_ROS2_TF2_POSE_Exercise4.md).

## Install dependencies

From the ROS 2 workspace root:

```bash
python3 -m pip install --user \
  "numpy>=1.22,<1.25" \
  "setuptools>=30.3,<80" \
  "spatialmath-python[ros-humble]"
```

SpatialMath is required only by the `exercise4_rpy_spatialmath` executable.

## Build

```bash
colcon build --packages-select pose_tf2 --symlink-install
source install/setup.bash
```

## Run

Run the SpatialMath solution:

```bash
ros2 launch pose_tf2 exercise4.launch.py
```

The launch arguments `x`, `y`, `z`, `roll_deg`, `pitch_deg` and `yaw_deg`
can be used to change the target pose.

## Verify

```bash
ros2 run tf2_ros tf2_echo ur5e_base target_b
```
