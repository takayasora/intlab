# image2pdfの使用方法
imageファイルの中身を全部pdf化するプログラムです！
対応ファイルは下記の通り！(png,jpg,gif)
↓動作例
[![image2pdf](https://gyazo.com/6c1583836a3325dfb926844f2c6654be.pdf)](https://gyazo.com/728af25baab0759840ca96171752b928.mp4)

## 初回利用
setup.batをダウンロードして、ダブルクリックしてください。

## 使用方法
フォルダを下記のようにしてください

### 実行前<br>
.<br>
├── image<br>
│   ├── photo1.jpg<br>
│   ├── photo2.png<br>
│   ├── graphic1.gif<br>
│   └── document.pdf (既存のPDF、変換対象外)<br>
└── script.py (このPythonスクリプト)<br>
![](https://gyazo.com/c9857c9a6163e3605ac98ff7eb2b3a15.png)


### 実行後<br>
.<br>
├── image<br>
│   ├── photo1.jpg<br>
│   ├── photo2.png<br>
│   ├── graphic1.gif<br>
│   └── document.pdf<br>
├── photo1.pdf (新たに生成されたPDF)<br>
├── photo2.pdf (新たに生成されたPDF)<br>
├── graphic1.pdf (新たに生成されたPDF)<br>
└── script.py<br>
![](https://gyazo.com/c9857c9a6163e3605ac98ff7eb2b3a15.png)