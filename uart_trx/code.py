# uart_trx : Circuit Python互換環境でのUART送受信例
#
# Ver . 0.01    2022/10/01 test version
#
# 本ソフトウェアは無保証です。
# 本ソフトウェアの不具合により損害が発生した場合でも補償は致しません。
# 改変・流用はご自由にどうぞ。
# Copyright (C)2022 Interplan Co., Ltd. all rights reserved.

import time
import board
from busio import UART

com = UART(board.TX, board.RX, baudrate=9600)	# bps=9600 / A0をTX / A1をRXに設定

set = time.monotonic()
while True:
	cnt = time.monotonic()
	if (cnt-set) >= 1:								# 1秒間隔で文字列を送信する	
		set = cnt
		com.write(b'Hello!!\r\n')						# A0に出力
	
	if com.in_waiting != 0:							# A1からデータ受信したら
		print(com.read())								# コンソールに表示する