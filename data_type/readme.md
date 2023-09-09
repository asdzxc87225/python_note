# data type 

Python 支援多種不同的資料型別（data types），這些型別用於存儲和處理不同種類的數據。下面是一些常見的 Python 資料型別以及它們的基本用法和操作：

- 整數（int）
- 浮點數（float）
- 字串（str）
- 布林值（bool）
- 列表（list）
- 元組（tuple）
- 字典（dict）

## 整數（int）
整數是沒有小數部分的數字。例如：1, 100, -10。

基本操作：
```py
x = 5
y = 10
result = x + y  # 加法
result = x - y  # 減法
result = x * y  # 乘法
result = x / y  # 除法
result = x // y  # 整數除法
result = x % y   # 取餘數
```

## 浮點數（float）
浮點數用於表示帶有小數部分的數字。例如：3.14, -0.01。

基本操作：

```py
x = 3.14
y = 2.0
result = x + y  # 加法
result = x - y  # 減法
result = x * y  # 乘法
result = x / y  # 除法
```

## 字串（str）
字串是一系列字符的序列，可以使用單引號（'）或雙引號（"）定義。例如："Hello, World!"。

基本操作：
```py
message = "Hello, World!"
length = len(message)  # 獲取字串長度
substring = message[0:5]  # 提取子字串
concatenated = message + " How are you?"  # 字串連接
```

## 布林值（bool）
布林值表示真（True）或假（False）的布林運算結果。

基本操作：
```py
x = True
y = False
result = x and y  # 邏輯與
result = x or y   # 邏輯或
result = not x    # 邏輯非
```
## 列表（list）
列表是有序的元素集合，可以包含不同類型的數據。

基本操作：
```py
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
numbers.append(6)  # 添加元素
element = numbers[2]  # 獲取元素
```
### 官方的參考資料
[python3.9](https://docs.python.org/3.9/tutorial/index.html)
版本的部份大家注意，因為有些新版會有套件不穩定的問題。
list.append()
list.extend()
```py
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```

## 元組（tuple）
元組類似於列表，但它們是不可變的，一旦創建就不能修改。

基本操作：
```py
point = (3, 4)
x, y = point  # 元組拆包
```
## 字典（dict）
字典是鍵-值對的集合，用於存儲和查找數據。

基本操作：
```py
person = {"name": "Alice", "age": 30}
name = person["name"]  # 獲取值
person["city"] = "New York"  # 添加鍵-值對
```
