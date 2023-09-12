# 對話匡的練習

對話匡根據gpt的說法有幾個用法

對話框是GUI應用程式中常見的一個元件，用來執行不同的任務。以下是一些對話框的使用情境：

1.    消息通知：對話框可以用來顯示訊息、警告或錯誤訊息，以提供重要資訊或警告。
1.    使用者輸入：當你需要從使用者那裡獲取文字、數字、密碼等輸入時，可以使用輸入對話框。例如，登錄名稱和密碼的輸入。
1.    檔案操作：檔案對話框用於打開、儲存或選擇檔案和資料夾。這對於檔案管理應用程式非常有用。
1.    字型和顏色選擇：字型對話框用於選擇文字的字型，顏色對話框用於選擇顏色。這對於圖形和文字處理應用程式很有用。
1.    進度監控：進度對話框用於顯示某項任務的進度，通常伴隨進度條或百分比。
1.    自訂功能：你可以建立自訂對話框，以滿足應用程式的特定需求。這可以是包含特定控制項、表單或自訂UI的對話框。
1.    確認和選擇：有時需要使用者的確認或選擇，例如，刪除檔案時彈出一個確認對話框以確保使用者的選擇。

總之，對話框是與使用者互動的一種重要方式，可以增強應用程式的使用者友善性，提供反饋和控制，以及實現各種不同的功能。你可以根據應用程式的需求選擇合適的對話框類型。

-------------------------------------------------------------------------------------

| 方法                  | 描述                                                            |
|-----------------------|-----------------------------------------------------------------|
| exec_()               | 以模态方式執行對話框，阻塞程式執行，直到對話框關閉。                |
| show()                | 以非模態方式顯示對話框，不會阻塞程式執行，允許用戶與應用程式的其他部分互動。 |
| setWindowTitle(title) | 設定對話框的標題。                                                  |
| setWindowIcon(icon)   | 設定對話框的圖示。                                                  |
| setGeometry(x, y,)    | 設定對話框的位置和大小。                                           |
| setModal(modal)       | 設定對話框的模態性，可以是True（模態）或False（非模態）。             |
| accept()              | 接受對話框並關閉它，通常與確定按鈕相關聯。                             |
| reject()              | 拒絕對話框並關閉它，通常與取消按鈕相關聯。                         |
| done(result)          | 設定對話框的返回值（通常用於自訂對話框的返回值），然後關閉對話框。    |
| exec()                | 用於以模態方式顯示對話框，並返回用戶的操作結果，通常與標準對話框一起使用。  |
| isVisible()           | 檢查對話框是否可見。                                                |
| close()               | 關閉對話框。                                                       |

-------------------------------------------------------------------------------------

## 使用方法
使用方法基本跟主視窗一樣。

### step1 
我的作法會用class 定義一個對話匡物件，計的讓它繼承QDialog。
```py
class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
```

### step2
加入元件並且排版，方法跟之前的作法一樣。
```py
# 設定對會框title
self.setWindowTitle("輸入對話框")

# 建立對話框的布局
layout = QVBoxLayout()

# 建立文字輸入框
self.text_input = QLineEdit(self)
layout.addWidget(self.text_input)

# 建立確定按鈕
self.ok_button = QPushButton("確定", self)
layout.addWidget(self.ok_button)
self.ok_button.clicked.connect(self.on_ok_button_click)

# 設定對話框的布局
self.setLayout(layout)
```

### step3
設計觸發對話匡的情況，可以是用按鈕或是監控某個變數透過檢查該變數來觸發。
這裡以按鈕觸發為例
```py
self.open_dialog_button = QPushButton("打開對話框", self)
self.open_dialog_button.clicked.connect(self.open_dialog)
self.setCentralWidget(self.open_dialog_button)
```
### step4
設定觸發的模式，如最上面的表大家選用適合的方式觸發。

```py

    def open_dialog(self):
        # 建立並顯示對話框
        dialog = MyDialog()
        result = dialog.exec_()#再者裡觸發對話匡
        if result == QDialog.Accepted:
            print("使用者按了確定按鈕")
```


