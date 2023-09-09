# Serial 模組

## 參考資料

- [基本](https://swf.com.tw/?p=1188)
- [官方](https://pyserial.readthedocs.io/en/latest/pyserial.html)
- [git hub](https://github.com/pyserial/pyserial/blob/master/documentation/pyserial.rst)
## 範例
使用這個模組要先初始化序列通訊埠，再來進行讀取資料。
```py
import serial  # 引用pySerial模組

COM_PORT = 'COM6'    # 指定通訊埠名稱
BAUD_RATES = 9600    # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)   # 初始化序列通訊埠

try:
    while True:
        while ser.in_waiting:          # 若收到序列資料…
            data_raw = ser.readline()  # 讀取一行
            data = data_raw.decode()   # 用預設的UTF-8解碼
            print('接收到的原始資料：', data_raw)
            print('接收到的資料：', data)

except KeyboardInterrupt:
    ser.close()    # 清除序列通訊物件
    print('再見！')
```

## serial.Serial

### init

```py
__init__(port=None, baudrate=9600, bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None, exclusive=None)
```

-    port – 設備名稱或 None.
-    baudrate ( int ) – 波特率，例如 9600 或 115200 等。
-    bytesize – 數據位數。 可能的值： FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS
-    parity – 啟用奇偶校驗檢查。 可能的值： PARITY_NONE, PARITY_EVEN, PARITY_ODD PARITY_MARK, PARITY_SPACE
-    stopbits – 停止位的數量。 可能的值： STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO
-    timeout ( float ) – 設置讀取超時值（以秒為單位）。
-    xonxoff ( bool ) – 啟用軟件流控制。
-    rtscts ( bool ) – 啟用硬件 (RTS/CTS) 流控制。
-    dsrdtr ( bool ) – 啟用硬件 (DSR/DTR) 流控制。
-    write_timeout ( float ) – 設置寫入超時值（以秒為單位）。
-    inter_byte_timeout ( float ) – 字符間超時， None禁用（默認）。
-    Exclusive ( bool ) – 設置獨占訪問模式（僅限 POSIX）。 無法打開端口 獨占訪問模式（如果已在獨占訪問模式下打開）。

最少要給port變數，其他的就依據需求在給參數。

## read 

```py
read (size=1)
```
----

參數： 	size – 要讀取的字節數。\
返回： 	從端口讀取的字節數。\
返回類型： 	字節 



讀取 size 從串行端口 字節。 如果設置了超時，可能會 返回的字符數少於請求的字符數。 如果沒有超時，它將阻塞 直到讀取到請求的字節數。 

### readline(size=-1)
Provided via io.IOBase.readline() See also ref:shortintro_readline.

## write(data)

參數： 	data—— 要發送的數據。\
返回： 	寫入的字節數。\
返回類型： 	整數 

將字節 數據 寫入端口。 這應該是類型 bytes （或兼容，例如 bytearray或者 memoryview）。 統一碼 字符串必須被編碼（例如 'hello'.encode('utf-8')
