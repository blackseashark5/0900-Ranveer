from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    nav2_params = os.path.join(
        '/absolute/path/to/cognipilot/cranium/src/b3rb/b3rb_nav2/config',
        'nav2.yaml'
    )
    slam_params = os.path.join(
        '/absolute/path/to/cognipilot/cranium/src/b3rb/b3rb_nav2/config',
        'slam.yaml'
    )

    return LaunchDescription([
        Node(
            package='nav2_bringup',
            executable='bringup_launch.py',
            name='nav2_bringup',
            output='screen',
            parameters=[nav2_params, slam_params]
        )
    ])
