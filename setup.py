from setuptools import setup, find_packages

with open("README.md","r")as fn:
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
      packages=setuptools.find_packages(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Build Tools'
      ],
    python_requires='>=3.7',

      
     )
