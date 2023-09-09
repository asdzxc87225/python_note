# time 模組

## 參考資料

- [基本](https://steam.oxxostudio.tw/category/python/library/time.html#a1)
- [官方](https://docs.python.org/zh-tw/3/library/time.html)

## 常用方法
|方法 	|參數 	|說明|
| -- | -- | -- |
|time() | |回傳到目前為止的秒數|
|sleep() 	|sec 	|將程式暫停指定的秒數|
|ctime() 	|t 	|轉換為本地時間|
|localtime()、time.gmtime() 	|t 	|轉換為 struct_time 格式的時間|
|mktime() 	|t 	|轉換 struct_time 格式的時間為秒數|
|asctime() 	|t 	|轉換 struct_time 格式的時間為文字|
|strftime()、time.strptime() 	|t |  回傳特定格式字串所表示的時間|

## strftime ( 格式 [ , t ] )

|方法 	|說明|
| -- |  -- |
|%a |本地化的縮寫星期中每日的名稱。|
|%A |本地化的星期中每日的完整名稱。|
|%b |本地化的月縮寫名稱。|
|%B |本地化的月完整名稱。|
|%c |本地化的適當日期和時間表示。|
|%d |十進制數[01,31] 表示的月中日。|
|%H |十進制數[00,23] 表示的小時（24小時制）。|
|%I |十進制數[01,12] 表示的小時（12小時制）。|
|%j |十進制數[001,366] 表示的年中日。|
|%m |十進制數[01,12] 表示的月。|
|%M |十進制數[00,59] 表示的分鐘。|
%p |本地化的AM 或PM 。 |

```py
from time import gmtime, strftime

strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
'Thu, 28 Jun 2001 14:17:15 +0000'
```
## 結構時間
返回的時間值序列的類型為 gmtime() 、 localtime() 和 strptime() 。 它是一個帶有 named tuple 接口的對象：可以通過索引和屬性名訪問值。 存在以下值

|索引|屬性 |值|
| -- | -- | -- |
|0 |tm_year |（例如，1993）
|1 |tm_mon|範圍 [1, 12]|
|2 |tm_mday|範圍 [1, 31]|
|3 |tm_hour|範圍 [0, 23]|
|4 |tm_min|範圍 [0, 59]|
|5 |tm_sec|range [0, 61]； 見 strftime()介紹中的 (2)|
|6 |tm_wday|range [0, 6] ，週一為0|
|7 |tm_yday|範圍 [1, 366]|
|8 |tm_isdst|0, 1 或-1|

