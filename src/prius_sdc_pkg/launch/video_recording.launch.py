import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    

    return LaunchDescription( [
        

        Node(
            package='prius_sdc_pkg',
            executable='video_recorder',
            name='Video_recorder',
            output='screen'),

        Node(
            package='teleop_twist_keyboard',
            executable='teleop_twist_keyboard',
            name='car_driver',
            output='Screen'
        )

    ]
    )