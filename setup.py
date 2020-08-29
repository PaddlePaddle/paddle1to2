from setuptools import setup, find_packages

with open('requirements.txt') as f:
    REQUIREMENTS = f.read().splitlines()

with open("README.md", "r")as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='paddle1to2',
    version='0.0.1',
    install_requires=REQUIREMENTS,
    author='T8T9, PaddlePaddle',
    author_email='taoshibo@baidu.com',
    keywords=('paddle1to2', 'paddle', 'paddlepaddle'),
    url='https://github.com/T8T9/paddle1to2',
    packages = find_packages(),
    package_data={'fissix': ['*.txt']},
    description='Upgrade python project from paddle-1.x to paddle-2.0',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    python_requires=">=3.6",
    scripts=[],
    entry_points={
        'console_scripts': [
            'paddle1to2=paddle1to2.main:main',
            'find_pattern=tools.find_pattern:main',
            'find_match_node=tools.find_match_node:main',
        ],
    },
    build_dir="build",
    zip_safe=False,
    classifiers=(
        "License :: OSI Approved",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)