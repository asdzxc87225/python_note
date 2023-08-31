from PyQt5.QtSql import QSqlDatabase

# 创建数据库连接
db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('mydatabase.db')

# 打开数据库
if db.open():
    print("數據連接成功")
    # 在这里执行数据库操作，如查询、插入、更新等
else:
    print("數據庫連接失敗")

