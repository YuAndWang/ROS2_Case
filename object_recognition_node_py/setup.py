from setuptools import setup

package_name = 'object_recognition_node_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wang',
    maintainer_email='wangyx6432@gmail.com',
    description='object recognition using rclpy',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'object_recognition = object_recognition_node_py.object_recognition:main',
        ],
    },
)
