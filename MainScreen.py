import pandas as pd
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLabel, QApplication, QLineEdit, QWidget, QVBoxLayout, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt
from datetime import datetime
import base64
import time
import json
from Logger import logger as log
import pyperclip as ppc
import re
import ast

class MainScreen(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.class_name = "MainScreen"
        self.setFixedSize(600, 900) # Set the fixed size of the QMainWindow
        self.today_date = datetime.today().strftime('%d-%b-%Y')
        self.today_day, self.today_month, self.today_year = self.today_date.split('-')
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()

        self.setLayout(layout)
        self.setWindowTitle('JSON Object <-> JSON File')

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout()

        # Create a QLabel widget
        self.input_json_label = QLabel("Input JSON", self)

        # Create a QLabel widget
        self.output_json_label = QLabel("Output JSON", self)



        # Create a QTextEdit widget
        self.input_json_edit = QTextEdit()
        # Set the number of visible lines (height) to 10
        self.input_json_edit.setFixedHeight(self.input_json_edit.fontMetrics().lineSpacing() * 20)

        # Create a QTextEdit widget
        self.output_json_edit = QTextEdit()
        # Set the number of visible lines (height) to 10
        self.output_json_edit.setFixedHeight(self.output_json_edit.fontMetrics().lineSpacing() * 20)
        self.output_json_edit.setPlainText("")
        self.output_json_edit.setDisabled(True)


        # Create Save and Close buttons
        self.format_button = QPushButton("Format")
        self.format_button.setContentsMargins(20, 20, 20, 20)  # Set margins for widget2
        self.copy_button = QPushButton("Copy Formatted JSON")
        self.download_button = QPushButton("Download JSON")
        self.close_button = QPushButton("Close")

        # Connect button click events to functions
        self.format_button.clicked.connect(self.formatJSON)
        self.close_button.clicked.connect(self.closeApp)
        self.copy_button.clicked.connect(self.copyJSON)
        self.copy_button.setEnabled(False)  # Initially disable the download button
        self.download_button.clicked.connect(self.downloadJSON)


        # Add buttons to the layout
        layout.addWidget(self.input_json_label)
        layout.addWidget(self.input_json_edit)
        layout.addSpacing(20)
        layout.addWidget(self.format_button)
        #layout.addSpacing(10)
        layout.addWidget(self.output_json_label)
        layout.addWidget(self.output_json_edit)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.download_button)
        layout.addWidget(self.close_button)
        # Set the layout for the central widget
        central_widget.setLayout(layout)


    def formatJSON(self):
        jsonInput = self.input_json_edit.toPlainText()
        if jsonInput == "":
            log.info("Please enter json input")
        else:
            log.info(f"{self.class_name} Format JSON")
            #self.output_json_edit.setDisabled(False)
            self.copy_button.setEnabled(True)

            if (self.checkValidJSON(jsonInput)):
                log.info('JSON Verified')
                result = self.format_json(jsonInput)
                self.output_json_edit.setText(result)
            else:
                log.info("Enter a valid JSON")
                self.output_json_edit.setPlainText("Enter a valid JSON")



    def copyJSON(self):
        ppc.copy(self.output_json_edit.toPlainText())
        self.copy_button.setEnabled(False)

    def downloadJSON(self):
        # Open a file dialog to save the edited data
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save JSON Data', '', 'JSON Files (*.json)')
        jsonOutput = self.output_json_edit.toPlainText()
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(json.loads(jsonOutput), f, indent=4, ensure_ascii=False)
                log.info(f"{self.class_name} - JSON data saved successfully: {file_path}")
            except (ValueError, Exception) as e:
                log.error(f"{self.class_name} - Error saving JSON data: {e}")
    

    def checkValidJSON(self, json_string):
        #pattern = r'^{[\s\r\n]*[a-zA-Z0-9_]+[\s\r\n]*:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\')[\s\r\n]*,?[\s\r\n]*(?:[a-zA-Z0-9_]+[\s\r\n]*:[\s\r\n]*\{(?:[\s\r\n]*[a-zA-Z0-9_]+[\s\r\n]*:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\')[\s\r\n]*,?[\s\r\n]*)*\}[\s\r\n]*,?[\s\r\n]*)*}$'
        ############pattern = r'^{[\s\r\n]*[a-zA-Z0-9_]+[\s\r\n]*:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|(?:\[(?:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|[a-zA-Z0-9_]+|[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?|true|false|null)[\s\r\n]*,?[\s\r\n]*)*[\s\r\n]*\])|\{(?:[\s\r\n]*[a-zA-Z0-9_]+[\s\r\n]*:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|(?:\[(?:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|[a-zA-Z0-9_]+|[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?|true|false|null)[\s\r\n]*,?[\s\r\n]*)*[\s\r\n]*\])|\{(?:[\s\r\n]*[a-zA-Z0-9_]+[\s\r\n]*:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|(?:\[(?:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|[a-zA-Z0-9_]+|[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?|true|false|null)[\s\r\n]*,?[\s\r\n]*)*[\s\r\n]*\])|\{(?:[\s\r\n]*[a-zA-Z0-9_]+[\s\r\n]*:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|(?:\[(?:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|[a-zA-Z0-9_]+|[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?|true|false|null)[\s\r\n]*,?[\s\r\n]*)*[\s\r\n]*\])|\{(?:[\s\r\n]*[a-zA-Z0-9_]+[\s\r\n]*:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|(?:\[(?:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|[a-zA-Z0-9_]+|[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?|true|false|null)[\s\r\n]*,?[\s\r\n]*)*[\s\r\n]*\])|\{(?:[\s\r\n]*[a-zA-Z0-9_]+[\s\r\n]*:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|(?:\[(?:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|[a-zA-Z0-9_]+|[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?|true|false|null)[\s\r\n]*,?[\s\r\n]*)*[\s\r\n]*\])|\{(?:[\s\r\n]*[a-zA-Z0-9_]+[\s\r\n]*:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|(?:\[(?:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|[a-zA-Z0-9_]+|[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?|true|false|null)[\s\r\n]*,?[\s\r\n]*)*[\s\r\n]*\])|\{(?:[\s\r\n]*[a-zA-Z0-9_]+[\s\r\n]*:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|(?:\[(?:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|[a-zA-Z0-9_]+|[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?|true|false|null)[\s\r\n]*,?[\s\r\n]*)*[\s\r\n]*\])|\{(?:[\s\r\n]*[a-zA-Z0-9_]+[\s\r\n]*:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|(?:\[(?:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|[a-zA-Z0-9_]+|[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?|true|false|null)[\s\r\n]*,?[\s\r\n]*)*[\s\r\n]*\])|\{(?:[\s\r\n]*[a-zA-Z0-9_]+[\s\r\n]*:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|(?:\[(?:[\s\r\n]*(?:"[^"]*?"|\'[^\']*?\'|[a-zA-Z0-9_]+|[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?|true|false|null)[\s\r\n]*,?[\s\r\n]*)*[\s\r\n]*\])|\{[\s\r\n]*\}[\s\r\n]*,?[\s\r\n]*)*\}[\s\r\n]*,?[\s\r\n]*)*\}[\s\r\n]*,?[\s\r\n]*)*\}$'
        #return bool(re.match(pattern, json_string))
        return True



    def checkValidJSON2(self, json_string):
        try:
            obj = ast.literal_eval(json_string)
            if isinstance(obj, dict):
                return True
            else:
                return False
        except (ValueError, SyntaxError) as e:
            return False


    def format_json(self, json_string):
        pattern = r'([\{\,]\s*)(\w+?)\s*:'
        
        def add_quotes(match):
            return f'{match.group(1)}"{match.group(2)}":'
        
        formatted_json = re.sub(pattern, add_quotes, json_string)
        
        formatted_json = formatted_json.replace("'", '"')
        
        return formatted_json


    def closeApp(self):
        self.close()



# 1 2 3 4 5 6 7
