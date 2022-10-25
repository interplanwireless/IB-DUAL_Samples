# analogin_out : Circuit Python互換環境でのアナログ入出力例
#
# Ver . 0.01    2022/10/01 test version
#
# 本ソフトウェアは無保証です。
# 本ソフトウェアの不具合により損害が発生した場合でも補償は致しません。
# 改変・流用はご自由にどうぞ。
# Copyright (C)2022 Interplan Co., Ltd. all rights reserved.

import ipcbox
import time

ib = ipcbox.IPCBox()

while True:
	ib.ledg_on()
	ib.ledr_off()
	time.sleep(0.5)
	ib.ledg_off()
	ib.ledr_on()
	time.sleep(0.5)
# (C)2022 interplan Co., Ltd.
import time
import board
import analogio

analog_in = analogio.AnalogIn(board.A0)   		# Analog Input
analog_out = analogio.AnalogOut(board.A1)   	# Analog Out

dabuf = [0, 16383, 32767, 49151, 65535]
daidx = 0
while True:
    analog_out.value = dabuf[daidx]       			# A1からDAC出力を行う
    daidx += 1                                 		# 次回出力値の更新
    if daidx >= 5:
        daidx = 0
    time.sleep(0.01)

    rdval = analog_in.value                   		# A0のアナログ値を読み込む 
    volt = rdval * 3.3 / 65536                		# 電圧に変換する
    print('A0 Val[V] = %3.2f' %volt)          		# PCに電圧を表示する
    time.sleep(0.99)