#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import re
import collections

# Token specification
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>\-)'
TIMES = r'(?P<TIMES>\*)'
DIVID = r'(?P<DIVID>/)'
LPAREN = r'(?P<LAPREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIVID, LPAREN,
    RPAREN, WS]))
Token = collections.namedtuple('Token', ['type', 'value'])

def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok

# Parser
class ExpressionEvaluator(object):
    '''
    Implementation of a recursive descent parser. Each method
    implements a single grammar rule. Use the ._accept() method
    to test and accept the current lookahead token. Use the ._expect()
    method to exactly match and discard the next token on on the input
    (or raise a SyntaxError if it doesn't match).
    '''
    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None # Last symbol consumed
        self.nexttok = None # Next symbol tokenized
        self._advance() # Load first lookahead token
        return self.expr()

    def _advance(self):
        'Advance on token ahead'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        'Test and consume the next token if it matches toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _except(self, toktype):
        'Consume next token if it matched toktype or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Expected' + toktype)

    # Grammar rules follow

    def expr(self):
        "expression ::= term { (+|-) term}*"

        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= rignt
        return exprval

    def term(self):
        "term ::= factor { (*|/) factor}"

        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == "TIMES":
                termval *= right
            elif op == "DIVIDE":
                termval /= right
        return termval

    def factor(self):
        "factor ::= (expr) | NUM"

        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')

class ExpressionTreeBuilder(ExpressionEvaluator):
    """
    重写父类方法
    """
    def expr(self):
        "expression ::= term { (+|-) term}"

        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval = ('+', exprval, right)
            elif op == 'MINUS':
                exprval = ('-', exprval, right)
            return exprval

    def term(self):
        "term ::= factor { (*|/) factor}"

        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == "TIMES":
                exprval = ('*', termval, right)
            elif op == "DIVIDE":
                exprval = ('/', termval, right)
            return termval

    def factor(self):
        "factor ::= NUM | (expr)"

        if self._accept('NUM'):
            return int(self.tok.type)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER pr LPAREN')

