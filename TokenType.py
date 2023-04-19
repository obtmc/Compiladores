# -*- coding: utf-8 -*-

# *******************************************************************
# Copyright (c) 2021 Universidade Federal de Pernambuco (UFPE).
#
# This file is part of the Compilers course at UFPE.
#
# During the 1970s and 1980s, Hewlett-Packard used RPN in all
# of their desktop and hand-held calculators, and continued to
# use it in some models into the 2020s. In computer science,
# reverse Polish notation is used in stack-oriented programming languages
# such as Forth, STOIC, PostScript, RPL and Joy.
#
# Contributors:
#     Henrique Rebelo      initial design and implementation
#     http://www.cin.ufpe.br/~hemr/
# ******************************************************************/

from enum import Enum

class TokenType(Enum):
    """
    Enumeration for Token Types.
    """
    # Literals.
    NUM = 1

    # Single-character tokens for operations.
    MINUS = 2
    PLUS = 3
    SLASH = 4
    STAR = 5

    EOF = 6
