from setuptools import find_packages, setup

setup(
    name='qq_plot_2samp',
    packages=find_packages(include=['qq_plot_2samp']),
    version='0.1.0',
    description='Custom qq-plot implementation in python',
    author='FlorianDe',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest == 4.4.1'],
    test_suite='tests',
)
