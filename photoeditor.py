from PyQt5.QtWidgets import *
import os
from PIL import Image
from  PyQt5.QtGui import QPixmap

app = QApplication([]) #створюю саме вікно
main_win = QWidget() #створюю віджети
main_win.resize(600, 600)

buttonFolder = QPushButton("Папка")#
buttonLeft = QPushButton("Вліво")#
buttonRight = QPushButton("Вправо")#
buttonMirror = QPushButton("Відзеркалення")#
buttonSharp = QPushButton("РІзкість")#
buttonWhiteBlack = QPushButton("Ч/Б")#
photoLabel = QLabel("Картинка")
fileList = QListWidget()


mainHLine = QHBoxLayout()
column1 = QVBoxLayout()
column2 = QVBoxLayout()
row1 = QHBoxLayout()
mainHLine.addLayout(column1)
mainHLine.addLayout(column2)


column1.addWidget(buttonFolder)
column1.addWidget(fileList)
column2.addWidget(photoLabel)
row1.addWidget(buttonLeft)
row1.addWidget(buttonRight)
row1.addWidget(buttonMirror)
row1.addWidget(buttonSharp)
row1.addWidget(buttonWhiteBlack)
column2.addLayout(row1)


def showFileNames():
    global wordir
    extension = ["jpg", "jpeg", 'png', 'jfif', 'webp']
    wordir = QFileDialog.getExistingDirectory()
    files = os.listdir(wordir)
    fileList.clear()
    for file in files:
        ext = file.split(".")
        if len(ext) >= 2:
            if ext[1] in extension:
                fileList.addItem(file)

class ImageEditor():
    def __init__(self):
        self.image = None
        self.folder = None
        self.fileName = None

    def loadImage(self):
        path = os.path.join(self.folder, self.fileName)
        self.image = Image.open(path)

    def showImage(self):
        path = os.path.join(self.folder, self.fileName)
        pixels = QPixmap(path)
        photoLabel.setPixmap(pixels)

imageEditor = ImageEditor()
def blackWhite(self):
        self.image = self.image.convert("L")
        self.showImage()

def showChosenImage():
        imageEditor.folder = wordir
        imageEditor.fileName = fileList.currentItem().text()
        imageEditor.showImage()

fileList.currentRowChanged.connect(showChosenImage)
















buttonFolder.clicked.connect(showFileNames)
main_win.setLayout(mainHLine )
main_win.show()#щоб вікно було видно
app.exec_()
