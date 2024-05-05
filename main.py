import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.extensions.international import International



keyboard = KMKKeyboard()
keyboard.extensions.append(International())

keyboard.col_pins = (board.P0_31, board.P0_29, board.P0_02, board.P1_15, board.P1_13, board.P1_11, board.P0_10, board.P0_09)
keyboard.row_pins = (board.P0_24, board.P1_00, board.P0_11, board.P1_04, board.P1_06)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

KOMMA = KC.LSFT(KC.DOT)

# Left hand
L1K1 = KC.N1()
L1K2 = KC.N1()
L1K3 = KC.N1()
L1K4 = KC.N1()

L2K1 = KC.N2()
L2K2 = KC.N2()
L2K3 = KC.N2()
L2K4 = KC.N2()

L3K1 = KC.N3()
L3K2 = KC.N3()
L3K3 = KC.N3()

L4K1 = KC.N4()
L4K2 = KC.N4()
L4K3 = KC.N4()

LT11 = KC.N0()
LT12 = KC.N0()
LT21 = KC.N0()
LT22 = KC.N0()
LT31 = KC.N0()
LT32 = KC.N0()

# Right hand
R1K1 = KC.N5()
R1K2 = KC.N5()
R1K3 = KC.N5()
R1K4 = KC.N5()

R2K1 = KC.N6()
R2K2 = KC.N6()
R2K3 = KC.N6()
R2K4 = KC.N6()

R3K1 = KC.N7()
R3K2 = KC.N7()
R3K3 = KC.N7()

R4K1 = KC.N8()
R4K2 = KC.N8()
R4K3 = KC.N8()

RT11 = KC.N9()
RT12 = KC.N9()
RT21 = KC.N9()
RT22 = KC.N9()
RT31 = KC.N9()
RT32 = KC.N9()


keyboard.keymap = [[
RT22, 	RT21, 	LT21, 	LT22, 	LT12, 	LT11, 	RT11, 	RT12,\
RT32, 	RT31, 	LT31, 	LT32, 	L2K4, 	L1K4, 	R2K4, 	R1K4,\
R4K3, 	R3K3, 	L4K3, 	L3K3, 	L2K3, 	L1K3, 	R2K3, 	R1K3,\
R4K2, 	R3K2, 	L4K2, 	L3K2, 	L2K2, 	L1K2, 	R2K2, 	R1K2,\
R4K1, 	R3K1, 	L4K1, 	L3K1, 	L2K1, 	L1K1, 	R2K1, 	R1K1, ],]

if __name__ == '__main__':
	keyboard.go()


