from setuptools import setup, find_packages

setup(name='stomp_ws_py',

      version='0.0.1',

      url='https://github.com/GlassyWing/stomp_ws_py',

      license='GPL 3.0',

      author='Manlier',

      author_email='dengjiaxim@gmail.com',

      description='simple python client for stomp over websocket.',

      keywords='stomp, websocket',

      packages=find_packages(exclude=['test', 'weights', 'config', 'data']),

      long_description=open('README.md', encoding='utf-8').read(),

      zip_safe=False,

      install_requires=['websocket_client>=0.57.0'])
