from cov_ui import Ui_MainWindow

from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from typing import List
class ui_run(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
                # 设置窗口图标
        logo = QtGui.QIcon()
        logo.addPixmap(QtGui.QPixmap('engineerlogo.ico'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_cov_clicked)

    def on_cov_clicked(self):
        #get source type
        source_type = self.ui.comboBox.currentText()
        stype = 0
        source_data = []
        if source_type == "十进制":
            stype = 10
        elif source_type == "二进制":
            stype = 2
        elif source_type == "十六进制":
            stype = 16
        elif source_type == "ASCII":
            stype  = 0
        #get sourve data
        source_data = self.get_input_data(stype)
        #get traget type
        target_type = self.ui.comboBox_2.currentText()
        ttype = 0
        if target_type == "十进制":
            ttype = 10
        elif target_type == "二进制":
            ttype = 2
        elif target_type == "十六进制":
            ttype = 16
        elif target_type == "ASCII":
            ttype  = 0
        #get traget data
        if source_data == None:
            self.show_data('输入错误,请输入整数')
            return 0
        target_data = self.num_cov_text(ttype,source_data)
        #show traget data
        show_data = ''
        for s in target_data:
            show_data = show_data+s+" "
        self.show_data(show_data)

    def get_input_data(self,type:int)->list[int]:
        try:
            # 读取文本框的数据
            text = self.ui.textEdit.toPlainText()
            data = []
            if type != 0:
                nums = text.split(" ")
                for i in nums:
                    sig = int(i,type) # 尝试转换为整数
                    data.append(sig)  
            else:
                try:
                    for i in text:
                        for j in i:
                            sig = ord(j) # 尝试转换为整数
                            data.append(sig) 
                except ValueError:
                    self.show_data('输入错误,请输入ASCII')
            return data
        except ValueError:
            # 如果转换失败，显示错误信息
            self.show_data('输入错误，请输入{0}进制整数'.format(type))

    def num_cov_text(self, type: int, data: list[int]) -> list[str]:
        buf = []
        if type == 0:
            buf.extend(chr(value) for value in data)
        elif type == 2:
            buf.extend(format(value, 'b') for value in data)
        elif type == 8:
            buf.extend(format(value, 'o') for value in data)
        elif type == 10:
            buf.extend(str(value) for value in data)
        elif type == 16:
            buf.extend(format(value, 'x') for value in data)
        return buf
    
    def show_data(self,data:str):
        # 清空文本浏览器
        self.ui.textBrowser.clear()
        self.ui.textBrowser.setPlainText(data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ui_run()
    ui.show()  # 显示窗口
    sys.exit(app.exec_())  # 启动事件循环并等待退出
