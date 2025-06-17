#!/usr/bin/env python

"""
setup.py file for MOODS
"""

from setuptools import setup, Extension
from setuptools.command.build_py import build_py as _build_py

common_includes = ["core/"]
common_compile_args = ['-O3', '-fPIC', '-std=c++11']
swig_opts = ["-c++", "-outdir",  "MOODS/"]

tools_mod = Extension('MOODS._tools',
                           sources=['core/tools.i',
                                    'core/moods_tools.cpp',
                                    'core/moods_misc.cpp',
                                    'core/match_types.cpp'],
                           include_dirs=common_includes,
                           extra_compile_args=common_compile_args,
                           swig_opts = swig_opts
                           )

scan_mod = Extension('MOODS._scan',
                           sources=['core/scan.i',
                                    'core/moods_scan.cpp',
                                    'core/motif_0.cpp',
                                    'core/motif_h.cpp',
                                    'core/moods_misc.cpp',
                                    'core/scanner.cpp',
                                    'core/moods_tools.cpp',
                                    'core/match_types.cpp'
                                ],
                           include_dirs=common_includes,
                           extra_compile_args=common_compile_args,
                           swig_opts = swig_opts
                           )

parsers_mod = Extension('MOODS._parsers',
                           sources=['core/parsers.i',
                                    'core/moods_parsers.cpp',
                                    'core/moods_misc.cpp',
                                    'core/moods_tools.cpp',
                                    'core/match_types.cpp'],
                           include_dirs=common_includes,
                           extra_compile_args=common_compile_args,
                           swig_opts = swig_opts
                           )

# Make sure that build_ext gets run first.
# (From https://stackoverflow.com/a/48942866/)
class build_py(_build_py):
    def run(self):
        self.run_command("build_ext")
        return super().run()

setup (name = 'MOODS-python',
       version = '1.9.4.1',
       packages = ["MOODS"],
       ext_modules = [tools_mod, scan_mod, parsers_mod],
       cmdclass = {"build_py": build_py}
)
