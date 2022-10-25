/* uart_trx.ino : Arduino互換環境でのUART送受信例
 *
 * Ver . 0.01    2022/10/01 test version
 * 
 * 本ソフトウェアは無保証です。
 * 本ソフトウェアの不具合により損害が発生した場合でも補償は致しません。
 * 改変・流用はご自由にどうぞ。
 * Copyright (C)2022 Interplan Co., Ltd. all rights reserved.
 */
unsigned long set, cnt;

void setup() {
  Serial.begin(19200);          // PC側のシリアルを設定
  Serial1.begin(9600);          // bps=9600 / A0をTX / A1をRXに設定

  set = millis();
}

void loop() {
  char c;
  cnt = millis();
  if ((cnt-set) >= 1000) {        // 1秒間隔で
    set = cnt;
    Serial1.println("Hello!!");     // A0に文字列を出力
  }

  if (Serial1.available()) {      // A1からデータを受信したら
    c = Serial1.read();             // 1文字取得して
    Serial.print(c);              // PCに表示する
  }
}
