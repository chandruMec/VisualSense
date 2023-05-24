from PySide6 import QtGui, QtWidgets, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VisualSense")
        self.setMinimumSize(800, 600)
        self.setup_ui()
        self.setup_actors()

    def setup_ui(self):
        # Create main widgets
        central_widget = QtWidgets.QWidget(self)
        main_layout = QtWidgets.QVBoxLayout(central_widget)

        # Create title bar
        title_bar_layout = QtWidgets.QHBoxLayout()
        title_bar_layout.setContentsMargins(10, 10, 10, 10)
        title_bar_layout.setAlignment(QtCore.Qt.AlignLeft)

        # Application logo, name, and version
        logo_label = QtWidgets.QLabel(self)
        #logo_label.setPixmap(QtGui.QPixmap("path/to/logo.png"))  # Replace with actual logo path

        app_name_label = QtWidgets.QLabel("VisualSense", self)
        app_name_label.setStyleSheet("font-weight: bold; font-size: 16px;")

        version_label = QtWidgets.QLabel("Version 1.0", self)

        # Username and logout/login button
        username_label = QtWidgets.QLabel("Username", self)
        logout_login_button = QtWidgets.QPushButton("Logout", self)

        # Add widgets to title bar layout
        title_bar_layout.addWidget(logo_label)
        title_bar_layout.addWidget(app_name_label)
        title_bar_layout.addWidget(version_label)
        title_bar_layout.addStretch()
        title_bar_layout.addWidget(username_label)
        title_bar_layout.addWidget(logout_login_button)

        # Create main buttons and enumerator section
        main_buttons_layout = QtWidgets.QHBoxLayout()
        main_buttons_layout.setContentsMargins(10, 10, 10, 10)

        # TODO: Add main buttons and enumerator widgets to main_buttons_layout

        # Create horizontal splitter
        horizontal_splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        horizontal_splitter.setHandleWidth(5)
        horizontal_splitter.addWidget(QtWidgets.QWidget())  # Placeholder widget
        horizontal_splitter.addWidget(QtWidgets.QWidget())  # Placeholder widget

        # Create vertical splitter
        vertical_splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        vertical_splitter.setHandleWidth(5)
        vertical_splitter.addWidget(QtWidgets.QWidget())  # Placeholder widget
        vertical_splitter.addWidget(QtWidgets.QWidget())  # Placeholder widget

        # Add widgets and splitters to the main layout
        main_layout.addLayout(title_bar_layout)
        main_layout.addWidget(horizontal_splitter)
        main_layout.addWidget(vertical_splitter)

        # Set the central widget and layout
        self.setCentralWidget(central_widget)

        # Connect the button click event to the analyze_image method
        # analyze_button.clicked.connect(self.analyze_image)

    def setup_actors(self):
        # Create the image analysis actor
        #self.image_analysis_actor = ImageAnalysisActor.start().proxy()
        pass

    def analyze_image(self):
        # TODO: Implement image analysis logic
        pass

    def closeEvent(self, event):
        # Terminate the image analysis actor  when the application is closed
        #self.image_analysis_actor.stop()
        pass


