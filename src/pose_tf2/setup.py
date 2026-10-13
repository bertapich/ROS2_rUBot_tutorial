from glob import glob
import os

from setuptools import find_packages, setup


package_name = 'pose_tf2'


setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            os.path.join('share', package_name),
            ['package.xml', 'README.md'],
        ),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py'),
        ),
        (
            os.path.join('share', package_name, 'rviz'),
            glob('rviz/*.rviz'),
        ),
        (
            os.path.join('share', package_name, 'urdf'),
            glob('urdf/*.urdf'),
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Manel Puig',
    maintainer_email='manel.puig@ub.edu',
    description=(
        'ROS 2 TF2 exercise for representing a 3D target pose with '
        'RPY angles and quaternions.'
    ),
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'exercise4_rpy = pose_tf2.exercise4_rpy:main',
            'exercise4_rpy_spatialmath = pose_tf2.exercise4_rpy_spatialmath:main',
        ],
    },
)
