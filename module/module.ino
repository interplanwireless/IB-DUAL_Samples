/* module.ino : Arduino互換環境でのモジュール起動/コマンド送信例
 *
 * Ver . 0.01    2022/10/01 test version
 * 
 * 本ソフトウェアは無保証です。
 * 本ソフトウェアの不具合により損害が発生した場合でも補償は致しません。
 * 改変・流用はご自由にどうぞ。
 * Copyright (C)2022 Interplan Co., Ltd. all rights reserved.
 */
// IM920sLとIMBLE2のUARTを設定
Uart im920Ser(&sercom4, IM_RXD, IM_TXD, SERCOM_RX_PAD_1, UART_TX_PAD_0);
Uart imBleSer(&sercom5, BLE_RXD, BLE_TXD, SERCOM_RX_PAD_1, UART_TX_PAD_0); 

unsigned long set,cnt;
String line;
void setup() {
  Serial.begin(19200);
                                    // IM920sLの初期設定
  pinMode(IM_BUSY, INPUT_PULLUP); // BUSYピンを入力設定
  pinMode(IM_RST, OUTPUT);          // RESETピンを出力設定
  digitalWrite(IM_RST, false);      // 最初はリセット状態
  delay(100);                       // 100ms間保持して
  digitalWrite(IM_RST, true);       // リセット解除
  delay(100);                       // 起動待ち
  while (digitalRead(IM_BUSY));
  im920Ser.begin(19200);            // UART初期化
                                    // IMBLE2の初期設定
  pinMode(BLE_BUSY, INPUT_PULLUP);
  pinMode(BLE_RST, OUTPUT);
  digitalWrite(BLE_RST, false);
  delay(100);
  digitalWrite(BLE_RST, true);
  delay(100);
  while (digitalRead(BLE_BUSY));
  imBleSer.begin(19200);  

  set = millis();
}

void loop() {
  cnt = millis();
  if ((cnt-set) >= 5000) {        // 5秒周期でコマンド送信
                                    // IM920sLへの送信処理
    while (digitalRead(IM_BUSY));     // コマンド受付可まで待機
    im920Ser.print("RDVR\r\n");       // コマンド送信
                                    // IMBLE2への送信処理
    while (digitalRead(BLE_BUSY));  
    imBleSer.print("RDVR\r\n");
    
    set = millis();
  }

  if (im920Ser.available()) {       // IM920sLの1行受信処理
    line = im920Ser.readStringUntil('\n');
    Serial.print(line);
  }
  if (imBleSer.available()) {       // IMBLE2の1行受信処理
    line = imBleSer.readStringUntil('\n');
    Serial.print(line);
  }
}

// SERCOM interrupt handler
void SERCOM4_0_Handler() {im920Ser.IrqHandler();}
void SERCOM4_1_Handler() {im920Ser.IrqHandler();}
void SERCOM4_2_Handler() {im920Ser.IrqHandler();}
void SERCOM4_3_Handler() {im920Ser.IrqHandler();}
void SERCOM5_0_Handler() {imBleSer.IrqHandler();}
void SERCOM5_1_Handler() {imBleSer.IrqHandler();}
void SERCOM5_2_Handler() {imBleSer.IrqHandler();}
void SERCOM5_3_Handler() {imBleSer.IrqHandler();}
