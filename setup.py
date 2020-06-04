from setuptools import setup, find_packages

with open("README.md","r")as fh:
    long_description=fn.read()

with open("req.txt","r") as fh:
    requirements=list(fh.read().split("\n"))

setup(name='py_package',
      version='0.0.1',
      description='server send the fetched data from realtime firebase databse to client ',
      long_description=long_description,
      url='',
      author='kaushiki',
      author_email='chatbotintellectualsai@gmail.com',
      packages=setuptools.find_packages()
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',

      
     )
