# deep_sleep : Circuit Python互換環境でのDeep Sleep例
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

trg = alarm.wake_alarm
if isinstance(trg, alarm.time.TimeAlarm):       # DeepSleepからの復帰か?
    print("Wake Up")

ledg = digitalio.DigitalInOut(board.LEDG)   	# LED(緑)
ledg.direction = digitalio.Direction.OUTPUT  	# 出力ピン

ledg.value = True
t = time.monotonic()
ts = t
while t < (ts+3):		                        # 3秒間の待機
    t = int(time.monotonic())
ledg.value = False

print("Deep Sleep")
ts = time.monotonic() + 10			            # 10秒のAlarmを設定
talm = alarm.time.TimeAlarm(monotonic_time=ts)
alarm.exit_and_deep_sleep_until_alarms(talm)	# Deep Sleep
print("dummy")                                  # dummy / 復帰後は先頭に戻るため表示されない