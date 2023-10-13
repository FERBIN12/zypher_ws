from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'prius_sdc_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,'launch'), glob('launch/*')),
        (os.path.join('share', package_name,'world'), glob('world/*')),
        (os.path.join('lib', package_name), glob('scripts/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kanja-koduki',
    maintainer_email='fjferbin@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 
            'video_recorder=prius_sdc_pkg.video_recorder:main',
            'driver_node=prius_sdc_pkg.driving_node:main',
            'spawner_node=prius_sdc_pkg.sdf_spawner:main'

        ],
    },
)
