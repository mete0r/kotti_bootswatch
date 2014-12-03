# -*- coding: utf-8 -*-
from __future__ import absolute_import
from fanstatic.compiler import LESS
from fanstatic.compiler import SOURCE
from fanstatic.compiler import TARGET
from fanstatic.registry import CompilerRegistry


class BootstrapLessCompiler(LESS):

    name = 'bootstrapless'

    @property
    def arguments(self):
        return ['--include-path=' + self.include_path, SOURCE, TARGET]


BOOTSTRAP_LESS_COMPILER = BootstrapLessCompiler()
CompilerRegistry.instance()['bootstrapless'] = BOOTSTRAP_LESS_COMPILER
