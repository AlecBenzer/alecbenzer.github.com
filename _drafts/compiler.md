---
layout: post
title: "Let's write a compiler"
---

Most compiler walk-thoughs build the compiler up in stages. They build their
lexer, then their parser, then they translate the parse tree to an IR, etc.
I want to try building a really simple language through to completion, and
then iterate on it.

Let's write a program that takes arithmetic expressions like `11 + 4 * (5 / 2.5)` and evaluates them.

## Lexing

The first step is to convert our arithmetic expression from strings of characters to strings of tokens.

The string "11 + 4.5" is represented as a sequence of 8 bytes: '1', '1', '
', '+', ' ', '4', '.', '5'. We want to convert this into a series of
_tokens_, like this: NUM(11), +, NUM(4.5). We've grouped together the bytes
representing numbers and operators, and removed whitespace. This
pre-processing of bytes to tokens greatly simplifies parsing our language.
