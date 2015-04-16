
import os, sys

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension


VERSION = '0.8'
ICU_VERSION = '3.8'   # version 3.6 is also supported

INCLUDES = {
    'darwin': ['/usr/local/icu-%s/include' %(ICU_VERSION)],
    'linux2': [],
    'win32': [],
}

CFLAGS = {
    'darwin': [],
    'linux2': [],
    'win32': ['/Zc:wchar_t'],
}

LFLAGS = {
    'darwin': ['-L/usr/local/icu-%s/lib' %(ICU_VERSION)],
    'linux2': [],
    'win32': [],
}

LIBRARIES = {
    'darwin': ['icui18n', 'icuuc', 'icudata'],
    'linux2': ['icui18n', 'icuuc', 'icudata'],
    'win32': ['icuin', 'icuuc', 'icudt'],
}

if 'PYICU_INCLUDES' in os.environ:
    _includes = os.environ['PYICU_INCLUDES'].split(os.pathsep)
else:
    _includes = INCLUDES[sys.platform]

if 'PYICU_CFLAGS' in os.environ:
    _cflags = os.environ['PYICU_CFLAGS'].split(os.pathsep)
else:
    _cflags = CFLAGS[sys.platform]

if 'PYICU_LFLAGS' in os.environ:
    _lflags = os.environ['PYICU_LFLAGS'].split(os.pathsep)
else:
    _lflags = LFLAGS[sys.platform]

if 'PYICU_LIBRARIES' in os.environ:
    _libraries = os.environ['PYICU_LIBRARIES'].split(os.pathsep)
else:
    _libraries = LIBRARIES[sys.platform]


setup(name="PyICU",
      description='Python extension wrapping the ICU C++ API',
      long_description=open('README').read(),
      version=VERSION,
      test_suite="test",
      url='http://pyicu.osafoundation.org/',
      author='Open Source Applications Foundation',
      ext_modules=[Extension('_PyICU',
                             [filename for filename in os.listdir(os.curdir)
                              if filename.endswith('.cpp')],
                             include_dirs=_includes,
                             extra_compile_args=_cflags,
                             extra_link_args=_lflags,
                             libraries=_libraries,
                             define_macros=[('PYICU_VER', '"%s"' %(VERSION))])
                   ],
      py_modules=['PyICU'])