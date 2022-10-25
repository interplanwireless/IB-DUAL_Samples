# i2c_rx : Circuit Python互換環境でのI2C受信例
#
# Ver . 0.01    2022/10/01 test version
#
# 本ソフトウェアは無保証です。
# 本ソフトウェアの不具合により損害が発生した場合でも補償は致しません。
# 改変・流用はご自由にどうぞ。
# Copyright (C)2022 Interplan Co., Ltd. all rights reserved.

import time
import board
import digitalio
from busio import UART

                                               	# IM920sLの初期設定
imbusy = digitalio.DigitalInOut(board.IM_BUSY)	# BUSYピンを入力設定
imbusy.direction = digitalio.Direction.INPUT        
imbusy.pull = digitalio.Pull.UP
imrst = digitalio.DigitalInOut(board.IM_RST)  	# RESETピンを出力設定
imrst.direction = digitalio.Direction.OUTPUT
imrst.value = False                             	# 最初はリセット状態
time.sleep(0.1)                                 	# 100ms間保持して
imrst.value = True                              	# リセット解除
time.sleep(0.1)                                 	# 起動待ち処理
while imbusy.value:
    pass
imcom = UART(board.IM_TXD, board.IM_RXD, baudrate=19200)# UART初期化
                                              	# IMBLE2の初期設定
blebusy = digitalio.DigitalInOut(board.BLE_BUSY)
blebusy.direction = digitalio.Direction.INPUT
blebusy.pull = digitalio.Pull.UP
blerst = digitalio.DigitalInOut(board.BLE_RST)
blerst.direction = digitalio.Direction.OUTPUT
blerst.value = False
time.sleep(0.1)
blerst.value = True
time.sleep(0.1)
while blebusy.value:
    pass
blecom = UART(board.BLE_TXD, board.BLE_RXD, baudrate=19200)

set = time.monotonic()
while True:
    cnt = time.monotonic()
    if (cnt-set) >= 5:                          	# 5秒周期でコマンド送信
                                                 		# IM920sLへの送信処理
        while imbusy.value:                        	# コマンド受付可まで待機
            pass
        imcom.write(b'RDVR\r\n')                   	# コマンド送信
                                                 		# IMBLE2への送信処理
        while blebusy.value:
            pass
        blecom.write(b'RDVR\r\n')

        set = time.monotonic()
    
    if imcom.in_waiting:                        	# IM920sLの1行受信処理
        line = imcom.readline()
        print(line)
    if blecom.in_waiting:                       	# IMBLE2の1行受信処理
        line = blecom.readline()
        print(line)
