/* digitalin_out.ino : Arduino互換環境でのデジタル入出力例
 *
 * Ver . 0.01    2022/10/01 test version
 * 
 * 本ソフトウェアは無保証です。
 * 本ソフトウェアの不具合により損害が発生した場合でも補償は致しません。
 * 改変・流用はご自由にどうぞ。
 * Copyright (C)2022 Interplan Co., Ltd. all rights reserved.
 */
void setup() {
  pinMode(D0, INPUT_PULLUP);    // D0を入力ピンに設定 / Pull-up
  pinMode(LEDG, OUTPUT);        // LEDGを出力ピンに設定
}

void loop() {
  int sts;

  sts = digitalRead(D0);          // D0の状態を取得
  if (!sts) {                     // D0をGNDに接続すると
    digitalWrite(LEDG, LOW);      // LEDGを消灯する / Loを出力
  } else {                        // それ以外なら
    digitalWrite(LEDG, HIGH);       // LEDGを点灯する / Hiを出力
  }
}
