/* spird.ino : Arduino互換環境でのSPI受信例
 *
 * Ver . 0.01    2022/10/01 test version
 * 
 * 本ソフトウェアは無保証です。
 * 本ソフトウェアの不具合により損害が発生した場合でも補償は致しません。
 * 改変・流用はご自由にどうぞ。
 * Copyright (C)2022 Interplan Co., Ltd. all rights reserved.
 */
#include "SPI.h"

const byte reg = 0xD0;            // 読み込むレジスタ 
byte c;

void setup() {
  Serial.begin(19200);

  pinMode(CS, OUTPUT);      // CSピンを出力に設定 / CS=D2
  digitalWrite(CS, HIGH); 
  SPI.begin();              // SPI初期化 / D3=SCK / D4=MISO / D5=MOSI
}

void loop() {
  digitalWrite(CS, LOW);    // CS Lo
  SPI.transfer(rec);        // レジスタ指定して
  c = SPI.transfer(0);      // 1Byte受信
  digitalWrite(CS, HIGH);   // CS Hi
  Serial.println(c);        // 受信データをPCに表示
  
  delay(1000);
}
