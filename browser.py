#!/usr/bin/python 

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QWebEngineView object and set it as the central widget
        # of the main window
        self.view = QWebEngineView(self)
        self.setCentralWidget(self.view)

        # Create a address bar and navigate button
        self.address_bar = QLineEdit(self)
        self.navigate_button = QPushButton('Go', self)

        # Connect the navigate button to the load method of the QWebEngineView
        self.navigate_button.clicked.connect(self.navigate_to_url)

        # Create a layout to hold the address bar and navigate button
        layout = QHBoxLayout()
        layout.addWidget(self.address_bar)
        layout.addWidget(self.navigate_button)

        # Set the layout of the main window
        self.setLayout(layout)

    def navigate_to_url(self):
        url = self.address_bar.text()
        self.view.load(QUrl(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
