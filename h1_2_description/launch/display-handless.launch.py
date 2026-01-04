from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    pkg_share = get_package_share_directory('h1_2_description')
    urdf_path = os.path.join(pkg_share, 'urdf', 'h1_2_handless_bright.urdf')
    rviz_config = os.path.join(pkg_share, 'rviz', 'h1_2_display_marker.rviz')

    with open(urdf_path, 'r') as f:
        robot_description_content = f.read()

    robot_description = {'robot_description': robot_description_content}

    return LaunchDescription([

        # Publishes TF using the URDF
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            #arguments=[urdf_path]
            parameters=[robot_description],
            output='screen'
        ),

        # RViz visualization
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config],
            output='screen'
        ),
    ])

