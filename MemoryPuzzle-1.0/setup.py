from setuptools import setup

'''with open('README.md', 'r') as f:
    long_description = f.read()
'''
setup (

    name = "MemoryPuzzle-1.0",
    version = "1.0",
    description = "A memory puzzle build on python",
    #long_description = long_description,
    author = "Adri-md-1208", 
    author_email = "a.morales.2019@alumnos.urjc.es",
    url = "https://github.com/Adri-md-1208/Memory-puzzle",
    install_requeries = ["pygame"],
    packages = ["memoryPuzzle", "memoryPuzzle.sprites"],
    license = "GPLv3",
    
)