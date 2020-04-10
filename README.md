## Environment Set-up

These are instructions for how to get your computer ready to run this code.

1. Download [Anaconda](https://anaconda.com/distribution). This is a Python package management and virtual environment software. Similar softwares such as PIP (Package Installer for Python) and virtualenv will work too.

2. Create a new environment with the required libraries. The libraries included with Anaconda which are required for this code are numpy, pandas, py-opencv, scipy, matplotlib, tensorflow, keras, pillow, sphinx.
```
conda create --name dmd_env python=3.7 numpy, pandas, py-opencv, scipy, matplotlib, tensorflow, keras, pillow, sphinx
```

3. To start using this environment, it must be activated.
```
source activate dmd_env
```

4. Now the PyDMD library must be installed separately using pip.
``` 
python3 -m pip install pydmd
```

8. Now the files in this repository can be run using `python3 scriptname.py`. 
