from setuptools import setup, find_packages

REQUIRES = []
with open('requirements.txt') as f:
    for line in f:
        REQUIRES.append(line)

setup(
    name='blogrssparser',
    version='0.1',
    description="slack chatbot to notify articles",
    author="Seungha Son",
    author_email="linuxias@gmail.com",
    license="MIT",
    url="https://github.com/linuxias/blogrssparser",
    keywords=["RSS", "Chatbot", "Parser"],
    install_requires=REQUIRES,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
)
