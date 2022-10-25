# light_sleep : Circuit Python互換環境でのLight Sleep例
#
# Ver . 0.01    2022/10/01 test version
#
# 本ソフトウェアは無保証です。
# 本ソフトウェアの不具合により損害が発生した場合でも補償は致しません。
# 改変・流用はご自由にどうぞ。
# Copyright (C)2022 Interplan Co., Ltd. all rights reserved.

import time
import alarm
import board
import digitalio

TRG_PIN = 1                                     # Wakuepトリガを選択 0=10s, 1=10s&A0 Lo

ledg = digitalio.DigitalInOut(board.LEDG)   	# LED(緑)
ledg.direction = digitalio.Direction.OUTPUT  	# 出力ピン

while True:
    ledg.value = True
    t = time.monotonic()
    ts = t
    while t < (ts+3):		                        # 3秒間の待機
        t = int(time.monotonic())
    ledg.value = False

    print("Light Sleep");
    if not TRG_PIN:                                 # timerのみ
        time.sleep(10)  			                    # 10秒のLight Sleep
    else:                                           # timerとpin (片方も可能)
        ts = time.monotonic() + 10			            # 10秒のAlarmを設定
        talm = alarm.time.TimeAlarm(monotonic_time=ts)
        palm = alarm.pin.PinAlarm(pin=board.A0,         # A0をLoにするとWakeup
                            value=False, edge=True, pull=True)
        trg = alarm.light_sleep_until_alarms(talm,palm)	# Light Sleep / 消費電流XXuA程度up
        print(trg)                                      # pinとtimerどちらで起きたか表示
    print("Wakeup")