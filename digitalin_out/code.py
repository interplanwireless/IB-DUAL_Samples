# digitalin_out : Circuit Python互換環境でのデジタル入出力例
#
# Ver . 0.01    2022/10/01 test version
#
# 本ソフトウェアは無保証です。
# 本ソフトウェアの不具合により損害が発生した場合でも補償は致しません。
# 改変・流用はご自由にどうぞ。
# Copyright (C)2022 Interplan Co., Ltd. all rights reserved.

import board
import digitalio


d0 = digitalio.DigitalInOut(board.D0)		# D0を設定
d0.direction = digitalio.Direction.INPUT		# 入力ピン
d0.pull = digitalio.Pull.UP						# Pull-up

ledg = digitalio.DigitalInOut(board.LEDG)	# LED(緑)
ledg.direction = digitalio.Direction.OUTPUT		# 出力ピン

while True:
	sts = d0.value							# D0の状態を取得
	if not sts:								# D0をGNDに接続すると
		ledg.value = False						# LEDGを消灯 / Loを出力
	else:									# それ以外は
		ledg.value = True						# LEDGを点灯 / Hiを出力