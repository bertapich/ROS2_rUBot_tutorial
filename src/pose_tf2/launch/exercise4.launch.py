#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description() -> LaunchDescription:
    """Launch the Exercise 4 broadcaster, target model and RViz2."""
    package_share = get_package_share_directory('pose_tf2')
    urdf_path = os.path.join(package_share, 'urdf', 'target_pose.urdf')
    rviz_path = os.path.join(package_share, 'rviz', 'exercise4.rviz')

    with open(urdf_path, 'r', encoding='utf-8') as urdf_file:
        robot_description = urdf_file.read()

    launch_arguments = [
        DeclareLaunchArgument('x', default_value='0.350'),
        DeclareLaunchArgument('y', default_value='-0.350'),
        DeclareLaunchArgument('z', default_value='0.170'),
        DeclareLaunchArgument('roll_deg', default_value='135.0'),
        DeclareLaunchArgument('pitch_deg', default_value='0.0'),
        DeclareLaunchArgument('yaw_deg', default_value='60.0'),
    ]

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}],
    )

    pose_broadcaster = Node(
        package='pose_tf2',
        executable='exercise4_rpy_spatialmath',
        name='exercise4_rpy_broadcaster',
        output='screen',
        parameters=[{
            'x': ParameterValue(LaunchConfiguration('x'), value_type=float),
            'y': ParameterValue(LaunchConfiguration('y'), value_type=float),
            'z': ParameterValue(LaunchConfiguration('z'), value_type=float),
            'roll_deg': ParameterValue(
                LaunchConfiguration('roll_deg'),
                value_type=float,
            ),
            'pitch_deg': ParameterValue(
                LaunchConfiguration('pitch_deg'),
                value_type=float,
            ),
            'yaw_deg': ParameterValue(
                LaunchConfiguration('yaw_deg'),
                value_type=float,
            ),
        }],
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_path],
    )

    return LaunchDescription(
        launch_arguments + [
            robot_state_publisher,
            pose_broadcaster,
            rviz,
        ]
    )
