import threading
import pyqt5app
import receiveimage


threading.Thread(target = receiveimage.main).start()
threading.Thread(target = pyqt5app.main).start()

