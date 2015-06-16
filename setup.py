from setuptools import setup

setup(
    name='wi-git-tools',
    version='1.1.1',
    py_modules=['prune_branches', 'authors', 'git_common'],
    install_requires=['GitPython', 'blessings'],
    entry_points={'console_scripts': [
        'prune_branches=prune_branches:main',
        'git_authors=authors:main'
    ]}
)
