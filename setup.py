from setuptools import setup

setup(
    name="image_captioning_app",
    version="0.1",
    install_requires=[
        "streamlit",
        "torch",
        "transformers",
        "pillow"
    ],
)
