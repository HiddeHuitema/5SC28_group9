import setuptools
from setuptools import setup, find_namespace_packages

packages = [a for a in find_namespace_packages(where='.') if a.find('gym_unbalanced_disk')==0]

setuptools.setup(
      name='gym_unbalanced_disk',
      version='0.0.12',
      description='An OpenAI gym environment for unbalanced disk.',
      url="https://github.com/GerbenBeintema/gym-unbalanced-disk",
      author = 'Gerben Beintema',
      author_email = 'g.i.beintema@tue.nl',
      license = 'BSD 3-Clause License',
      python_requires = '>=3.6',
      packages=packages,
      install_requires = ['gym','numpy','scipy'],
      include_package_data=True
      )