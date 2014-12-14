# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os.path

from fanstatic.compiler import LESS
from fanstatic.compiler import SOURCE
from fanstatic.compiler import TARGET
from fanstatic.registry import CompilerRegistry

from . import bootswatch_names


class BootstrapLessCompiler(LESS):

    def __init__(self, name, bootstrap_dir):
        self.name = name
        self.bootstrap_dir = bootstrap_dir

    @property
    def arguments(self):
        return ['--include-path=' + self.bootstrap_dir, SOURCE, TARGET]


def callback(theme_name):
    theme_dir = os.path.join(os.path.dirname(__file__), 'static', 'bootswatch',
                             theme_name)
    compiler = BootstrapLessCompiler(theme_name, theme_dir)
    compiler_name = 'less_bootswatch_' + theme_name
    CompilerRegistry.instance()[compiler_name] = compiler
    globals()[compiler_name] = compiler


map(callback, bootswatch_names)
