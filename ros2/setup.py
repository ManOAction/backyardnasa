from setuptools import setup

package_name = 'matilda_sensors'

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
    maintainer='jacob',
    maintainer_email='jacob@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'atmo_pub = matilda_sensors.publisher_atmo_function:main',
            'atmo_sub = matilda_sensors.subscriber_atmo_function:main',
        ],
    },
)
