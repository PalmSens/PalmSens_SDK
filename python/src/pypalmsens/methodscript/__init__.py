"""Submodule for parsing MethodSCRIPT"""

from __future__ import annotations

from .generated.MethodScriptLexer import MethodScriptLexer
from .generated.MethodScriptParser import MethodScriptParser

__all__ = [
    'MethodScriptLexer',
    'MethodScriptParser',
]
