/* analogin_out.ino : Arduino互換環境でのアナログ入出力例
 * A0とA1を接続してください
 *
 * Ver . 0.01    2022/10/01 test version
 * 
 * 本ソフトウェアは無保証です。
 * 本ソフトウェアの不具合により損害が発生した場合でも補償は致しません。
 * 改変・流用はご自由にどうぞ。
 * Copyright (C)2022 Interplan Co., Ltd. all rights reserved.
 */
const unsigned short dabuf[] = {0, 1023, 2047, 3071, 4095};
byte daidx = 0;

void setup() {
  Serial.begin(19200); 
}

void loop() {
  unsigned short rdval;
  float volt;

  analogWrite(A1, dabuf[daidx]); // A1からDAC出力を行う
  daidx++;                        // 次回出力値の更新
  if (daidx >= 5) daidx = 0;
  delay(10);
  
  rdval = analogRead(A0);         // A0のアナログ値を読み込む
  volt = rdval * 3.3 / 1024;     // 電圧に変換する
  Serial.print("A1 Val[V] = ");  // PCに電圧を表示する
  Serial.println(volt);

  delay(990);
}
