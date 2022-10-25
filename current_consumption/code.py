# -*- coding: utf-8 -*-
#
# 電流計測 / for CircuitPython 7.1.0
#
# Ver . 0.01    2022/10/01 test version
#
# 本ソフトウェアは無保証です。
# 本ソフトウェアの不具合により損害が発生した場合でも補償は致しません。
# 改変・流用はご自由にどうぞ。
# Copyright (C)2022 Interplan Co., Ltd. all rights reserved.

from ipcbox import *
import time
import alarm
import supervisor
from busio import UART
import microcontroller as mc

                # マクロ
DSW_FIX = 0         # 1ならDSWの値を無視して決まったテストを行う
DSW_RES = 2         # DSWの返答値
                # 変数
ib = IPCBox()

# CPU:Active / IM920sL:受信待機 / IMBLE2:アドバタイズ
def dsw_proc00():
    while True:
        pass

# CPU:Active / IM920sL:受信待機 / IMBLE2:Sleep
def dsw_proc01():
    ib.ledg_on()
    ib.ble_sleep()
    ib.ledg_off()
    while True:
        pass

# CPU:Active / IM920sL:10mW送信 / IMBLE2:Sleep
def dsw_proc02():
    ib.ledg_on()
    ib.ble_sleep()
    while not ib.put_line(b"ECIO\r\n"):
        pass
    while not ib.put_line(b"STPO2\r\n"):
        pass
    while not ib.put_line(b"STRT3\r\n"):
        pass
    while not ib.put_line(b"DSHP\r\n"):
        pass
    ib.ledg_off()
    while True:
        while not ib.put_line(b"TXDA0123456789ABCDEFGHIJKLMNOPQRSTUV\r\n"):
            pass
        t = time.monotonic()
        while True:
            ts = time.monotonic()
            if (ts-t) >= 1:
                break
        

# CPU:Active / IM920sL:Sleep / IMBLE2:アドバタイズ
def dsw_proc03():
    ib.ledg_on()
    ib.im_sleep()
    ib.ledg_off()
    while True:
        pass

# CPU:Light Sleep / IM920sL:Sleep / IMBLE2:Sleep
def dsw_proc04():
    ib.ledg_on()
    ib.im_sleep()
    ib.ble_sleep()
    while True:
        ib.ledg_off()
        time.sleep(1000)
        ib.ledg_on()
        time.sleep(1)

# CPU:Deep Sleep / IM920sL:Sleep / IMBLE2:Sleep
def dsw_proc05():
    ib.ledg_on()
    ib.im_sleep()
    ib.ble_sleep()

    while True:
        ib.ledg_off()
        talm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 1000)
        alarm.exit_and_deep_sleep_until_alarms(talm)
        ib.ledg_on()

current_proc = [dsw_proc00,dsw_proc01,dsw_proc02,dsw_proc03,dsw_proc04,dsw_proc05]
dsw = ib.get_dsw()
if DSW_FIX:
    dsw = DSW_RES
print(dsw, len(current_proc))
if dsw < len(current_proc):     # 登録されているなら
    current_proc[dsw]()             # 計測用の処理へ
else:                           # 未登録なら
    while True:                     # エラー表示
        ib.ledr_on()
        ib.ledg_off()
        time.sleep(0.1)
        ib.ledr_off()
        ib.ledg_on()
        time.sleep(0.1)

while True:                     # dummy
    pass