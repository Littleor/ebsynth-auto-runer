import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EbSynth-Auto-Runer",
    version="0.0.1",
    author="Littleor",
    license='Apache License 2.0',
    author_email="me@littleor.cn",
    description="Support Mac for fully automated running of EbSynth(.ebs).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'opencv-python>=4.8.1.78',
        'PyAutoGUI>=0.9.54',
        'rich>=13.7.0',
        'tqdm>=4.66.1',
    ],
    url="https://github.com/Littleor/ebsynth-auto-runer",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: Apache Software License',
    ],
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'ebsynth-run=main:main'
        ]
    }
)
