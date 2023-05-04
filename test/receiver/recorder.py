# Ghi âm tín hiệu nhận được qua GUI recorder và lưu dưới tên file rec.wav
# Có thể sử dụng các phần mềm khác để ghi lại âm thanh
import sys
import wave

import pyaudio as pa
from PyQt6.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import *


class RecordingThread(QThread):
    stopped = False
    sig_started = pyqtSignal()
    sig_stopped = pyqtSignal()

    def __init__(self, target_file):
        self.target_file = target_file
        super().__init__()

    def run(self) -> None:
        audio = pa.PyAudio()
        frames = []
        stream = audio.open(format=pa.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        self.stopped = False
        self.sig_started.emit()

        while not self.stopped:
            data = stream.read(1024)
            frames.append(data)

        stream.close()

        self.sig_stopped.emit()

        wf = wave.open(self.target_file, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(pa.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))
        wf.close()

    @pyqtSlot()
    def stop(self):
        self.stopped = True


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rec Audio")
        # Tạo luồng ghi âm 
        self.recording_thread = RecordingThread(target_file='rec.wav')
        self.recording_thread.sig_started.connect(self.recording_started)
        self.recording_thread.sig_stopped.connect(self.recording_stopped)

        vbox = QVBoxLayout()

        self.labelRec = QLabel('')
        self.labelRec.setFixedSize(260, 30)

        hbox = QHBoxLayout()
        self.recbtn = QPushButton('▶ RECORD')
        self.recbtn.setFixedSize(180, 60)
        
        """Nhấp vào nút ghi âm (recbtn), kích hoạt slot “start” của đối tượng QThread"""
        self.recbtn.clicked.connect(self.recording_thread.start)

        self.stopbtn = QPushButton('▪ STOP')
        self.stopbtn.setDisabled(True)
        self.stopbtn.setFixedSize(80, 60)

        """Nhấp vào nút dừng (stopbtn), kích hoạt slot “stop” của đối tượng QThread"""
        self.stopbtn.clicked.connect(self.recording_thread.stop)
        hbox.addWidget(self.recbtn)
        hbox.addWidget(self.stopbtn)

        vbox.addWidget(self.labelRec)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    @pyqtSlot()
    def recording_started(self):
        """Slot được gọi khi bắt đầu ghi âm"""
        self.labelRec.setText('◉ RECORDING...')
        self.stopbtn.setDisabled(False)
        self.recbtn.setDisabled(True)

    @pyqtSlot()
    def recording_stopped(self):
        """Slot này được gọi khi dừng ghi âm"""
        self.labelRec.setText('recording stopped')
        self.recbtn.setDisabled(False)
        self.stopbtn.setDisabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()