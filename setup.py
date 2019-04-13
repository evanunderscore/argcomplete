#!/usr/bin/env python

import glob
from setuptools import setup, find_packages

install_requires = []
tests_require = ["coverage", "flake8", "pexpect", "wheel"]

setup(
    name='argcomplete',
    version='1.9.5',
    url='https://github.com/kislyuk/argcomplete',
    license='Apache Software License',
    author='Andrey Kislyuk',
    author_email='kislyuk@gmail.com',
    description='Bash tab completion for argparse',
    long_description=open('README.rst').read(),
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={"test": tests_require},
    packages=find_packages(exclude=['test']),
    scripts=glob.glob('scripts/*'),
    package_data={'argcomplete': ['bash_completion.d/python-argcomplete.sh']},
    entry_points={
        'console_scripts': [
            'activate-global-python-argcomplete=argcomplete.activate_global_python_argcomplete:main',
            'python-argcomplete-check-easy-install-script=argcomplete.python_argcomplete_check_easy_install_script:main',
            'register-python-argcomplete=argcomplete.register_python_argcomplete:main',
        ]
    },
    zip_safe=False,
    include_package_data=True,
    platforms=['MacOS X', 'Posix'],
    test_suite='test',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Shells',
        'Topic :: Terminals'
    ]
)
