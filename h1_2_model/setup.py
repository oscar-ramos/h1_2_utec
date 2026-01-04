from setuptools import find_packages, setup

package_name = 'h1_2_model'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='oramos',
    maintainer_email='oramos@todo.todo',
    description='Kinematic and dynamic tests for H1-2 Model',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'joint_publisher = h1_2_model.joint_publisher:main',
            'fk_test_node = h1_2_model.fk_test_node:main',
        ],

    },
)
