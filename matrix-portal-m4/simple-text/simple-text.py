from adafruit_matrixportal.matrix import Matrix
#exactly what is needed for simple text display?
#matrixportal = MatrixPortal()
#network = matrixportal.network
#graphics = matrixportal.graphics
#from adafruit_matrixportal.graphics import Graphics
#from adafruit_matrixportal.network import Network

import time
import random
import board
import terminalio
from adafruit_matrixportal.matrixportal import MatrixPortal
import displayio
import rgbmatrix
import framebufferio
import adafruit_display_text.label

# If there was a display before (protomatter, LCD, or E-paper), release it so
# we can create ours
displayio.release_displays()

matrix = rgbmatrix.RGBMatrix(
    width=64, bit_depth=4,
    rgb_pins=[board.MTX_R1, board.MTX_G1, board.MTX_B1, board.MTX_R2, board.MTX_G2, board.MTX_B2],
    addr_pins=[board.MTX_ADDRA, board.MTX_ADDRB, board.MTX_ADDRC, board.MTX_ADDRD],
    clock_pin=board.MTX_CLK, latch_pin=board.MTX_LAT, output_enable_pin=board.MTX_OE)

# Associate the RGB matrix with a Display so that we can use displayio features
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)
display.rotation = 0

R = adafruit_display_text.label.Label(
    terminalio.FONT,
    color=0xff0000,
    scale=3, x=2, y=13,
    text="R")
B = adafruit_display_text.label.Label(
    terminalio.FONT,
    color=0x0000ff,
    scale=3, x=24, y=13,
    text="B")
G = adafruit_display_text.label.Label(
    terminalio.FONT,
    color=0x00ff00,
    scale=3, x=46, y=13,
    text="G")

# Put each line of text into a Group, then show that group.
g = displayio.Group()
g.append(R)
g.append(B)
g.append(G)
display.show(g)
display.auto_refresh = True

# Put each line of text into a Group, then show that group.
g = displayio.Group()
g.append(R)
g.append(B)
g.append(G)
display.show(g)
display.auto_refresh = True