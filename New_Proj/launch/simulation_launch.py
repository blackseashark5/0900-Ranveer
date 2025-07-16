from launch import LaunchDescription
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    warehouse_world = os.path.join(
        '/absolute/path/to/NXP_AIM_INDIA_2025/worlds',
        'warehouse_1.sdf'
    )

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gz', 'sim', warehouse_world, '--verbose', '-r'],
            output='screen'
        )
    ])
