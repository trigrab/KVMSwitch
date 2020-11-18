from setuptools import setup


pkg = __import__('ESPDashClient')

setup(name='espclient',
      version=pkg.__version__,
      description=pkg.__description__,
      author=pkg.__author__,
      author_email=pkg.__author_email__,
      packages=['ESPDashClient'],
      package_data={'': ['config.yml.dist']},
      install_requires=[
          'pyyaml',
          'websockets',
      ],
      entry_points={
          'console_scripts': ['espclient=ESPDashClient.client:main']
      },
      license='GPL3')

