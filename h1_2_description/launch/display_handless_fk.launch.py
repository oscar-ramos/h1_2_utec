from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    pkg_share = get_package_share_directory('h1_2_description')

    generic_launch = os.path.join(pkg_share, 'launch', 'display_handless.launch.py')
    fk_rviz = os.path.join(pkg_share, 'rviz', 'h1_2_display_marker_fk.rviz')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(generic_launch),
            launch_arguments={
                'rviz_config': fk_rviz
            }.items()
        )
    ])
