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
from busio import I2C

i2cpu = digitalio.DigitalInOut(board.I2C_PUEN)	# I2C pull-up
i2cpu.direction = digitalio.Direction.OUTPUT
i2cpu.value = False                           	# ONに設定する / 負論理

i2c = I2C(board.SCL,board.SDA,frequency=100000)	# I2C初期化 / D0=SDA,D1=SCL / freq=100kHz

adr = 0x76										# センサのアドレス
reg = 0xD0										# 読み込むレジスタ
rdbuf = bytearray(1)                            # 受信バッファを用意
while True:
	while not i2c.try_lock():                    	# バスをロックする
		pass
	i2c.writeto(adr, bytes([reg]))					# レジスタを送信
	i2c.readfrom_into(adr, rdbuf)					# データ受信
	i2c.unlock()									# バスのロックを解除
	print(hex(rdbuf[0]))                         

	time.sleep(1)