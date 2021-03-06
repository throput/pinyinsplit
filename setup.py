from setuptools import setup
from setuptools import find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='pinyinsplit',
    version='0.1.4',
    author='Thomas Lee',
    author_email='thomaslee@throput.com',
    description='A Python library to split a Chinese Pinyin phrase into possible permutations of Chinese Pinyin words',
    long_description=readme(),
    url='https://github.com/throput/pinyinsplit',
    py_modules = ['pinyinsplit'],
    license='MIT',
    install_requires=['pygtrie>=2.3'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='chinese pinyin',
)
