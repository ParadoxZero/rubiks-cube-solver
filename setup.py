from distutils.core import setup

setup(
    name='cubesolver',
    author="Sidhin S Thomas",
    author_email="sidhin.thomas@gmail.com",
    description="A simple app to solve rubiks-cube using webcam",
    version='0.1dev',
    packages=['cubesolver', ],
    license='GNU General Public License',
    long_description=open('README.md').read(),
)