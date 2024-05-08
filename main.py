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

# Left hand
L1K1 = KC.K()
L1K2 = KC.A()
L1K3 = KC.U()
L1K4 = KC.X()

L2K1 = KC.DOT()
L2K2 = KC.E()
L2K3 = KC.O()
L2K4 = KC.Z()

L3K1 = KC.COMMA()
L3K2 = KC.I()
L3K3 = KC.H()

L4K1 = KC.J()
L4K2 = KC.Y()
L4K3 = KC.Q()

# Right hand
R1K1 = KC.M()
R1K2 = KC.S()
R1K3 = KC.C()
R1K4 = KC.G()

R2K1 = KC.D()
R2K2 = KC.T()
R2K3 = KC.R()
R2K4 = KC.L()

R3K1 = KC.P()
R3K2 = KC.N()
R3K3 = KC.F()

R4K1 = KC.V()
R4K2 = KC.B()
R4K3 = KC.W()

# Left thumb
LT11 = KC.N0()
LT12 = KC.N0()
LT21 = KC.N0()
LT22 = KC.SPACE()
LT31 = KC.N0()
LT32 = KC.N0()

# Right thumb
RT11 = KC.N9()
RT12 = KC.N9()
RT21 = KC.SPACE()
RT22 = KC.N9()
RT31 = KC.N9()
RT32 = KC.N9()

keyboard.keymap = [[
RT21, 	RT22, 	LT22, 	LT21, 	LT12, 	LT11, 	RT11, 	RT12,\
RT32, 	RT31, 	LT31, 	LT32, 	L2K4, 	L1K4, 	R2K4, 	R1K4,\
R4K3, 	R3K3, 	L4K3, 	L3K3, 	L2K3, 	L1K3, 	R2K3, 	R1K3,\
R4K2, 	R3K2, 	L4K2, 	L3K2, 	L2K2, 	L1K2, 	R2K2, 	R1K2,\
R4K1, 	R3K1, 	L4K1, 	L3K1, 	L2K1, 	L1K1, 	R2K1, 	R1K1, ],]

if __name__ == '__main__':
	keyboard.go()


