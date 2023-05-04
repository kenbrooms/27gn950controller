pyinstaller --noconsole會找不到dll，解決方法如下

1. 先pre-compile一次
   pyinstaller -F app.py --noconsole
2. 修改app.spec
   將datas加入hidapi.dll路徑
   datas=[('hidapi.dll', '.')],
3. pyinstaller app.spec --noconsole

https://blog.csdn.net/qq_42521542/article/details/128773750