from setuptools import setup, find_packages

VERSION = "1.0.1" 
DESCRIPTION = "Simple implementation of Latin Hypercube Sampling."
LONG_DESCRIPTION = "This simple implementation of Latin Hypercube Sampling can be used to find collection of points that cover a predefined space. Currently, a random and a maxmin design are supported."

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="simplelhs", 
        version=VERSION,
        author="Mike Diessner",
        author_email="<mikediessner@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["numpy", "scipy"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=["Python", "Latin Hypercube Sampling", "Space filling design"],
        classifiers= [
            "Development Status :: 4 - Beta",
            "Intended Audience :: Science/Research",
            "Programming Language :: Python",
            "Operating System :: POSIX :: Linux",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            ]
)
