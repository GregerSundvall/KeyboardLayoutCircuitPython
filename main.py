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

AWE = KC.RALT(KC.W)
AEH = KC.RALT(KC.Q)
UHH = KC.RALT(KC.P)


#	BEAKL27-ish#
#	  WX DG
#	QHOU CMRV
#	YIEA STNB
#	J??K FLPZ

# Colemak-ish #
#   DG HM
# QWFP JLUY
# ARST NEIO
# ZXCV KB,.

# Workman-ish #
#   BG YJ
# QDRW FUP?
# ASHT NEOI
# ZXMC KLV?

#===============================================
#	BEAKL Effort grid (doubled, for whole nrs)
#
#	24	2	2	2	10	=	10	2	2	2	24
#	10	1	1	1	3	=	3	1	1	1	10
#	14	4	10	3	14	=	14	3	10	4	14
#===============================================
#	BEAKL 15
#
#	Q	H	O	U	X	=	G	C	R	F	Z
#	Y	I	E	A	.	=	D	S	T	N	B
#	J	/	,	K	'	=	W	M	L	P	V
#===============================================
#	BEAKL 15-ish
#
#			Z	X		=		G	L
#	Q	H	O	U		=		C	R	F	W
#	Y	I	E	A		=		S	T	N	B
#	J	,	.	K		=		M	D	P	V
#===============================================

map1 = [
                    KC.Z,   KC.X,           KC.G,   KC.L,
    KC.Q,   KC.H,   KC.O,   KC.U,           KC.C,   KC.R,   KC.F,   KC.W,
    KC.Y,   KC.I,   KC.E,   KC.A,           KC.S,   KC.T,   KC.N,   KC.B,
    KC.J,   AEH,    AWE,    KC.K,           KC.M,   KC.D,   KC.P,   KC.V,

                KC.BSPC,    KC.Q,           KC.Q,       KC.TAB,
                KC.SPC,     KC.ESC,         KC.COMM,    KC.DOT,
                KC.DEL,     KC.Q,           KC.Q,       KC.ENT                
    ]



keyboard.keymap = [[
map1[35], 	map1[34], 	map1[33], 	map1[32], 	map1[29],   map1[28], 	map1[30], 	map1[31],\
map1[39], 	map1[38], 	map1[36], 	map1[37], 	map1[0],	map1[1], 	map1[3], 	map1[2],\
map1[11], 	map1[10], 	map1[4], 	map1[5], 	map1[6], 	map1[7], 	map1[9], 	map1[8],\
map1[19], 	map1[18], 	map1[12], 	map1[13], 	map1[14], 	map1[15], 	map1[17], 	map1[16],\
map1[27], 	map1[26], 	map1[20], 	map1[21], 	map1[22], 	map1[23], 	map1[25], 	map1[24], ],]

if __name__ == '__main__':
	keyboard.go()


