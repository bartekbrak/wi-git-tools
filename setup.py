from setuptools import setup

setup(
    name='wi-git-tools',
    version='1.1.0',
    py_modules=['prune_branches', 'authors'],
    install_requires=['GitPython', 'blessings'],
    entry_points={'console_scripts': [
        'prune_branches=prune_branches:main',
        'git_authors=authors:main'
    ]}
)
