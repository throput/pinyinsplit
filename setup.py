from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='pinyinsplit',
    version='0.1.1',
    description='A Python library to split a Chinese Pinyin phrase into possible permutations of Chinese Pinyin words',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='chinese pinyin',
    url='https://github.com/throput/pinyinsplit',
    author='Thomas Lee',
    author_email='thomaslee@throput.com',
    pymodule='pinyinsplit',
    install_requires=[
        'pygtrie>=2.3',
    ],
    include_page_data=True,
    zip_safe=False
)
