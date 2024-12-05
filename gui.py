import sys

from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QProgressDialog,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from main import main


class WorkerThread(QThread):
    finished = Signal()
    error = Signal(str)

    def __init__(self, word_count, prompt):
        super().__init__()
        self.word_count = word_count
        self.prompt = prompt

    def run(self):
        try:
            main(self.word_count, self.prompt)
        except Exception as e:
            self.error.emit(str(e))
        finally:
            self.finished.emit()


class CustomPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Video Complete!")
        self.setModal(True)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        message_label = QLabel("Video generation complete!")
        message_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        message_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(message_label)

        button_layout = QHBoxLayout()

        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.close_application)
        button_layout.addWidget(self.quit_button)

        self.regenerate_button = QPushButton("Regenerate")
        self.regenerate_button.clicked.connect(self.reset_form)
        button_layout.addWidget(self.regenerate_button)

        self.layout.addLayout(button_layout)

    def close_application(self):
        QApplication.instance().quit()

    def reset_form(self):
        self.done(1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Content Generation System")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)

        title_label = QLabel("AI Content Generation System")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(title_label)

        self.word_count_label = QLabel("Word Count (30-200):")
        self.word_count_label.setStyleSheet("font-size: 18px;")
        self.layout.addWidget(self.word_count_label)

        self.word_count_input = QLineEdit()
        self.word_count_input.setPlaceholderText("Enter word count (e.g., 50)")
        self.layout.addWidget(self.word_count_input)

        self.prompt_label = QLabel("Prompt:")
        self.prompt_label.setStyleSheet("font-size: 18px;")
        self.layout.addWidget(self.prompt_label)

        self.prompt_input = QLineEdit()
        self.prompt_input.setPlaceholderText("Enter your prompt")
        self.layout.addWidget(self.prompt_input)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.start_generation)
        self.layout.addWidget(self.submit_button)

        central_widget.setLayout(self.layout)

        self.progress_dialog = None

        self.worker_thread = None

    def start_generation(self):
        word_count = self.word_count_input.text()
        prompt = self.prompt_input.text()

        if not word_count.isdigit() or not 30 <= int(word_count) <= 200:
            QMessageBox.warning(
                self, "Invalid Input", "Word count must be between 30 and 200."
            )
            return
        if not prompt.strip():
            QMessageBox.warning(
                self, "Invalid Input", "Prompt cannot be empty."
            )
            return

        self.submit_button.setEnabled(False)

        self.progress_dialog = QProgressDialog(
            "Generating video, please wait...", None, 0, 0, self
        )
        self.progress_dialog.setWindowTitle("Processing")
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.show()

        self.worker_thread = WorkerThread(word_count, prompt)
        self.worker_thread.finished.connect(self.complete_generation)
        self.worker_thread.error.connect(self.show_error)
        self.worker_thread.start()

    def complete_generation(self):
        if self.progress_dialog:
            self.progress_dialog.close()
            self.progress_dialog = None

        popup = CustomPopup(self)
        if popup.exec() == 1:
            self.reset_form()

    def reset_form(self):
        self.word_count_input.clear()
        self.prompt_input.clear()
        self.submit_button.setEnabled(True)

    def show_error(self, error_message):
        if self.progress_dialog:
            self.progress_dialog.close()
            self.progress_dialog = None

        self.submit_button.setEnabled(True)

        QMessageBox.critical(
            self, "Error", f"An error occurred:\n{error_message}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
