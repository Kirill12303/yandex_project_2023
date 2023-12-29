"# yandex_project_2023" 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QListWidget, QMessageBox, QFileDialog


class NotesApp(QWidget):
    def __init__(self):
        super().__init__()
        self.categories = []
        self.notes = {}
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Заметки')
        self.setGeometry(100, 100, 600, 400)
        self.title_label = QLabel('Заголовок:')
        self.title_input = QLineEdit()
        self.category_label = QLabel('Категория:')
        self.category_input = QLineEdit()
        self.content_label = QLabel('Содержание:')
        self.content_input = QTextEdit()
        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.saveNote)
        self.delete_button = QPushButton('Удалить')
        self.delete_button.clicked.connect(self.deleteNote)
        self.category_list = QListWidget()
        self.category_list.itemClicked.connect(self.loadCategory)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.title_input)
        self.layout.addWidget(self.category_label)
        self.layout.addWidget(self.category_input)
        self.layout.addWidget(self.content_label)
        self.layout.addWidget(self.content_input)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.save_button)
        buttons_layout.addWidget(self.delete_button)
        self.layout.addLayout(buttons_layout)
        self.layout.addWidget(self.category_list)
        self.setLayout(self.layout)

    def saveNote(self):
        title = self.title_input.text().strip()
        category = self.category_input.text().strip()
        content = self.content_input.toPlainText().strip()

        if not title:
            QMessageBox.warning(self, 'Предупреждение',
                                'Заголовок не может быть пустым')
            return

        if category not in self.categories:
            self.categories.append(category)
            self.category_list.addItem(category)

        self.notes[title] = {'category': category, 'content': content}
        QMessageBox.information(
            self, 'Информация', 'Заметка сохранена успешно')

    def deleteNote(self):
        title = self.title_input.text().strip()
        if title in self.notes:
            del self.notes[title]
            QMessageBox.information(
                self, 'Информация', 'Заметка удалена успешно')
        else:
            QMessageBox.warning(self, 'Предупреждение', 'Заметка не найдена')

    def loadCategory(self, item):
        category = item.text()
        if category in self.categories:
            filtered_notes = {title: note for title, note in self.notes.items(
            ) if note['category'] == category}
            notes_text = '\n\n'.join(
                [f"{title}\n{note['content']}" for title, note in filtered_notes.items()])
            QMessageBox.information(self, 'Заметки', notes_text)
        else:
            QMessageBox.warning(self, 'Предупреждение', 'Категория не найдена')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NotesApp()
    window.show()
    sys.exit(app.exec_())
