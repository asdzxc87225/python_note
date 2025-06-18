# 📘 Pandas 入門筆記：基本操作練習（題 01～05）

## ✅ 資料匯入與基本使用

```python
import pandas as pd
df = pd.read_csv("./students.csv")
```
- pd.read_csv()：從 CSV 讀取資料為 DataFrame。
- 相對路徑要注意工作目錄，可以用 os.getcwd() 檢查。

##  顯示前五筆資料
```python 
df.head()
```
- head()：預設顯示前 5 筆資料，可傳入數字 head(10) 顯示前 10 筆。
- 用來快速預覽資料結構與欄位內容。

##  選取特定欄位
```python
df[['name', 'math']]
```
- 用雙中括號 [[]] 來選擇多個欄位。
- df[''] → 回傳 Series（單欄位）
- df[[]] → 回傳 DataFrame（維持表格格式）

##  單一條件篩選

```python 
df[df['math'] > 80]
```
- 篩選出 math > 80 的所有學生。
- Pandas 使用布林索引來進行篩選。

## 多重條件篩選

```PYTHON 
df[(df['age'] >= 16) & (df['science'] > 90)]
```
- 使用 & 表示「且」、| 表示「或」。
- 注意：條件必須用 () 包起來，否則會報錯！

