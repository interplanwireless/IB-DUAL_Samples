/* i2crd.ino : Arduino互換環境でのI2C受信例
 *
 * Ver . 0.01    2022/10/01 test version
 * 
 * 本ソフトウェアは無保証です。
 * 本ソフトウェアの不具合により損害が発生した場合でも補償は致しません。
 * 改変・流用はご自由にどうぞ。
 * Copyright (C)2022 Interplan Co., Ltd. all rights reserved.
 */
#include "Wire.h"

const byte adr = 0x76;            // センサのアドレス   
const byte reg = 0xD0;            // 読み込むレジスタ 
byte c;

void setup() {
  Serial.begin(19200);

  pinMode(I2C_PUEN, OUTPUT);       // I2C Pull-upを
  digitalWrite(I2C_PUEN, LOW);      // ONに設定する / 負論理
  Wire.begin();                   // I2C初期化 / D0=SDA,D1=SCL
  Wire.setClock(100000);          // freq=100kHz
}

void loop() {
  Wire.beginTransmission(adr);      // 送信処理の開始
  Wire.write(reg);                // レジスタを送信
  Wire.endTransmission(false);    // 送信完了 / stopなし
  Wire.requestFrom(adr, 1, true); // 1Byte要求 / stopあり
  c = Wire.read();                  // データ受信
  Serial.println(c, HEX);                

  delay(1000);
}
