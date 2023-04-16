from setuptools import setup

setup(
    name='textrecog',
    version='0.1',
    python_requires='>=3.9.13',
    install_requires=[
        'streamlit==1.21.0',
        'opencv-python==4.7.0.72',
        'numpy==1.23.5',
        'tensorflow==2.12.0',
        'keras==2.12.0',
        'gdown==4.7.1'
    ],
)