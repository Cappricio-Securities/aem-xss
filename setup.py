from setuptools import setup

VERSION = '0.0.2'
DESCRIPTION = 'A Tool to find an Easy Bounty - aem-xss'
LONG_DESCRIPTION = 'This is a tool used by several security researchers to find aem-xss.'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aem-xss",
    version=VERSION,
    author="@karthithehacker",
    author_email="<contact@karthithehacker.com>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'aem-xss = aemxss.main:main',
        ],
    },
    install_requires=['urllib3', 'requests', 'click'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)