#!/usr/bin/env python3

import chess
import chess.svg

from pysvg.structure import *
from pysvg.core import *
from pysvg.text import *

def save_chessboard():
    board = chess.Board("8/8/8/8/8/8/8/N7 w - - 0 1")
    svg_str = chess.svg.board(board=board)
    with open('chessboard.svg', 'w') as f:
        f.write(svg_str)

def helloWorld():
    svg = Svg(0,0, width="100%", height="100%")
    t = Text("pySVG", x=0,y=100)
    group = G()
    group.set_transform("rotate(-30)")
    t.set_stroke_width('1px')
    t.set_stroke('#00C')
    t.set_fill('none')
    t.set_font_size("36")
    group.addElement(t)

    svg.addElement(group)
    svg.save('HelloWorld1.svg')

save_chessboard()
helloWorld()
