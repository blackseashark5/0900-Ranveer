from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    rviz_config = os.path.join(
        '/absolute/path/to/NXP_AIM_INDIA_2025/rviz',
        'default_view.rviz'
    )

    return LaunchDescription([
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],
            output='screen'
        )
    ])
