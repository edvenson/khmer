from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, Extension
#from distutils.core import setup, Extension

# the c++ extension module (needs to be linked in with ktable.o ...)
extension_mod = Extension("khmer._khmermodule",
                          ["_khmermodule.cc"],
                          extra_compile_args=['-g'],
                          include_dirs=['../lib',],
                          library_dirs=['../lib',],
                          extra_objects=['../lib/ktable.o',
                                         '../lib/hashtable.o',
                                         '../lib/parsers.o',
                                         '../lib/hashbits.o',
                                         '../lib/counting.o',
                                         '../lib/subset.o',
                                         '../lib/zlib-1.2.3/adler32.o',
                                         '../lib/zlib-1.2.3/compress.o',
                                         '../lib/zlib-1.2.3/crc32.o',
                                         '../lib/zlib-1.2.3/deflate.o',
                                         '../lib/zlib-1.2.3/gzio.o',
                                         '../lib/zlib-1.2.3/infback.o',
                                         '../lib/zlib-1.2.3/inffast.o',
                                         '../lib/zlib-1.2.3/inflate.o',
                                         '../lib/zlib-1.2.3/inftrees.o',
                                         '../lib/zlib-1.2.3/trees.o',
                                         '../lib/zlib-1.2.3/uncompr.o',
                                         '../lib/zlib-1.2.3/zutil.o',],
                          depends=['../lib/storage.hh',
                                   '../lib/khmer.hh',
                                   '../lib/ktable.hh',
                                   '../lib/hashtable.hh',
                                   '../lib/counting.hh',
                                   '../lib/hashtable.o',
                                   '../lib/ktable.o',
                                   '../lib/parsers.o',
                                   '../lib/hashbits.o',
                                   '../lib/counting.o',
                                   '../lib/subset.o',
                                   '../lib/zlib-1.2.3/adler32.o',
                                   '../lib/zlib-1.2.3/compress.o',
                                   '../lib/zlib-1.2.3/crc32.o',
                                   '../lib/zlib-1.2.3/deflate.o',
                                   '../lib/zlib-1.2.3/gzio.o',
                                   '../lib/zlib-1.2.3/infback.o',
                                   '../lib/zlib-1.2.3/inffast.o',
                                   '../lib/zlib-1.2.3/inflate.o',
                                   '../lib/zlib-1.2.3/inftrees.o',
                                   '../lib/zlib-1.2.3/trees.o',
                                   '../lib/zlib-1.2.3/uncompr.o',
                                   '../lib/zlib-1.2.3/zutil.o']
                          )

# python modules: only 'khmer'
py_mod = 'khmer'

# update version here, and in doc/conf.py, python/khmer/__init__.py,
#      and lib/khmer.hh.

setup(name = "khmer", version = "0.4",
      description = 'khmer k-mer counting library',
      author = 'C. Titus Brown, Jason Pell, and Adina Howe',
      author_email = 'ctb@msu.edu',
      url = 'http://ged.msu.edu/',
      license='New BSD License',
      packages = [py_mod,],
      setup_requires=['nose>=1.2.1'],
      test_suite = 'nose.collector',
      ext_modules = [extension_mod,])
