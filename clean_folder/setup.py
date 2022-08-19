from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='Sorting for folders',
    url='https://gitlab.com/temazubkov02/myfirst/-/tree/master/clean_folder',
    author='Artem Zubkov',
    author_email='temazubkov02@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)