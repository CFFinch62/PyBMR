import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                            QComboBox, QFrame, QCheckBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor, QPalette

class BMRCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basal Metabolic Rate & Weight Loss Calculator")
        self.setFixedSize(919, 642)
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)
        
        # Create BMR section
        bmr_frame = QFrame()
        bmr_frame.setFrameStyle(QFrame.Shape.Box)
        bmr_frame.setStyleSheet("background-color: #006400;")
        bmr_layout = QVBoxLayout(bmr_frame)
        
        # Units selection
        units_label = QLabel("UNITS:")
        units_label.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.units_combo = QComboBox()
        self.units_combo.addItems(["STANDARD (IN,LB)", "METRIC (CM,KG)"])
        self.units_combo.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        
        # Sex selection
        sex_label = QLabel("SEX:")
        sex_label.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.sex_combo = QComboBox()
        self.sex_combo.addItems(["FEMALE", "MALE"])
        self.sex_combo.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        
        # Height input
        height_label = QLabel("HEIGHT:")
        height_label.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.height_input = QLineEdit()
        self.height_input.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.height_input.setStyleSheet("background-color: #000066;")
        
        # Weight input
        weight_label = QLabel("WEIGHT:")
        weight_label.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.weight_input = QLineEdit()
        self.weight_input.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.weight_input.setStyleSheet("background-color: #000066;")
        
        # Age input
        age_label = QLabel("AGE:")
        age_label.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.age_input = QLineEdit()
        self.age_input.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.age_input.setStyleSheet("background-color: #000066;")
        
        # Activity level
        activity_label = QLabel("ACTIVITY:")
        activity_label.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.activity_combo = QComboBox()
        self.activity_combo.addItems(["SEDENTARY", "LIGHT", "MODERATE", "VERY", "EXTRA"])
        self.activity_combo.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        
        # Equation selection
        equation_label = QLabel("EQUATION:")
        equation_label.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.equation_combo = QComboBox()
        self.equation_combo.addItems(["HARRIS-BENEDICT ORIGINAL", "HARRIS-BENEDICT REVISED", "MIFFLIN ST JOER", "KATCH-MCARDLE"])
        self.equation_combo.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        
        # BMR result
        bmr_label = QLabel("BMR:")
        bmr_label.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.bmr_result = QLineEdit()
        self.bmr_result.setReadOnly(True)
        self.bmr_result.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.bmr_result.setStyleSheet("background-color: #000066;")
        
        # BMR buttons
        bmr_buttons_layout = QHBoxLayout()
        self.bmr_calculate_btn = QPushButton("BMR")
        self.bmr_calculate_btn.setFont(QFont("Helvetica", 16, QFont.Weight.Bold))
        self.bmr_calculate_btn.setStyleSheet("background-color: #00FF00; color: black;")
        self.bmr_reset_btn = QPushButton("RESET")
        self.bmr_reset_btn.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.bmr_reset_btn.setStyleSheet("background-color: #FF0000; color: white;")
        bmr_buttons_layout.addWidget(self.bmr_calculate_btn)
        bmr_buttons_layout.addWidget(self.bmr_reset_btn)
        
        # Add widgets to BMR layout
        bmr_layout.addWidget(units_label)
        bmr_layout.addWidget(self.units_combo)
        bmr_layout.addWidget(sex_label)
        bmr_layout.addWidget(self.sex_combo)
        bmr_layout.addWidget(height_label)
        bmr_layout.addWidget(self.height_input)
        bmr_layout.addWidget(weight_label)
        bmr_layout.addWidget(self.weight_input)
        bmr_layout.addWidget(age_label)
        bmr_layout.addWidget(self.age_input)
        bmr_layout.addWidget(activity_label)
        bmr_layout.addWidget(self.activity_combo)
        bmr_layout.addWidget(equation_label)
        bmr_layout.addWidget(self.equation_combo)
        bmr_layout.addWidget(bmr_label)
        bmr_layout.addWidget(self.bmr_result)
        bmr_layout.addLayout(bmr_buttons_layout)
        
        # Create Weight Loss section
        wl_frame = QFrame()
        wl_frame.setFrameStyle(QFrame.Shape.Box)
        wl_frame.setStyleSheet("background-color: #006464;")
        wl_layout = QVBoxLayout(wl_frame)
        
        # Target weight
        tgt_weight_label = QLabel("TARGET WEIGHT:")
        tgt_weight_label.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.tgt_weight_input = QLineEdit()
        self.tgt_weight_input.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.tgt_weight_input.setStyleSheet("background-color: #000066;")
        
        # Target calories
        tgt_calories_label = QLabel("TARGET CALORIES:")
        tgt_calories_label.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.tgt_calories_input = QLineEdit()
        self.tgt_calories_input.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.tgt_calories_input.setStyleSheet("background-color: #000066;")
        
        # Activity checkbox
        self.activity_checkbox = QCheckBox("Include Activity")
        self.activity_checkbox.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.activity_checkbox.setChecked(True)
        
        # Weekly weight loss
        loss_label = QLabel("WEEKLY WEIGHT LOSS:")
        loss_label.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.loss_result = QLineEdit()
        self.loss_result.setReadOnly(True)
        self.loss_result.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.loss_result.setStyleSheet("background-color: #000066; color: white;")
        
        # Time to target
        time_label = QLabel("TIME TO TARGET:")
        time_label.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.time_result = QLineEdit()
        self.time_result.setReadOnly(True)
        self.time_result.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.time_result.setStyleSheet("background-color: #000066; color: white;")
        
        # Weight Loss buttons
        wl_buttons_layout = QHBoxLayout()
        self.wl_calculate_btn = QPushButton("WEIGHT LOSS")
        self.wl_calculate_btn.setFont(QFont("Helvetica", 16, QFont.Weight.Bold))
        self.wl_calculate_btn.setStyleSheet("background-color: #00FF00; color: black;")
        self.wl_calculate_btn.setEnabled(False)  # Disable by default
        self.wl_reset_btn = QPushButton("RESET")
        self.wl_reset_btn.setFont(QFont("Helvetica", 12, QFont.Weight.Bold))
        self.wl_reset_btn.setStyleSheet("background-color: #FF0000; color: white;")
        self.wl_reset_btn.setEnabled(False)  # Disable by default
        wl_buttons_layout.addWidget(self.wl_calculate_btn)
        wl_buttons_layout.addWidget(self.wl_reset_btn)
        
        # Add widgets to Weight Loss layout
        wl_layout.addWidget(tgt_weight_label)
        wl_layout.addWidget(self.tgt_weight_input)
        wl_layout.addWidget(tgt_calories_label)
        wl_layout.addWidget(self.tgt_calories_input)
        wl_layout.addWidget(self.activity_checkbox)
        wl_layout.addWidget(loss_label)
        wl_layout.addWidget(self.loss_result)
        wl_layout.addWidget(time_label)
        wl_layout.addWidget(self.time_result)
        wl_layout.addLayout(wl_buttons_layout)
        
        # Add frames to main layout
        layout.addWidget(bmr_frame)
        layout.addWidget(wl_frame)
        
        # Connect signals
        self.bmr_calculate_btn.clicked.connect(self.calculate_bmr)
        self.bmr_reset_btn.clicked.connect(self.reset_bmr)
        self.wl_calculate_btn.clicked.connect(self.calculate_weight_loss)
        self.wl_reset_btn.clicked.connect(self.reset_weight_loss)
        
        # Set window background color
        self.setStyleSheet("background-color: #008000;")
    
    def calculate_bmr(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            age = float(self.age_input.text())
            sex = self.sex_combo.currentText()
            equation = self.equation_combo.currentText()
            
            # Calculate BMR based on selected equation
            if equation == "HARRIS-BENEDICT ORIGINAL":
                if sex == "MALE":
                    bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
                else:
                    bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
            elif equation == "HARRIS-BENEDICT REVISED":
                if sex == "MALE":
                    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
                else:
                    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
            elif equation == "MIFFLIN ST JOER":
                if sex == "MALE":
                    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
                else:
                    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
            else:  # KATCH-MCARDLE
                bmr = 370 + (21.6 * weight)
            
            self.bmr_result.setText(f"{bmr:.2f}")
            # Enable weight loss buttons after successful BMR calculation
            self.wl_calculate_btn.setEnabled(True)
            self.wl_reset_btn.setEnabled(True)
        except ValueError:
            self.bmr_result.setText("Invalid input")
            # Keep weight loss buttons disabled if BMR calculation fails
            self.wl_calculate_btn.setEnabled(False)
            self.wl_reset_btn.setEnabled(False)
    
    def calculate_weight_loss(self):
        try:
            current_weight = float(self.weight_input.text())
            target_weight = float(self.tgt_weight_input.text())
            target_calories = float(self.tgt_calories_input.text())
            
            # Calculate weekly weight loss
            weekly_loss = (current_weight - target_weight) / 4  # Assuming 4 weeks per month
            
            # Calculate time to target
            total_loss = current_weight - target_weight
            time_to_target = total_loss / weekly_loss
            
            self.loss_result.setText(f"{weekly_loss:.2f} lbs/week")
            self.time_result.setText(f"{time_to_target:.1f} weeks")
        except ValueError:
            self.loss_result.setText("Invalid input")
            self.time_result.setText("Invalid input")
    
    def reset_bmr(self):
        self.height_input.clear()
        self.weight_input.clear()
        self.age_input.clear()
        self.bmr_result.clear()
        # Disable weight loss buttons when BMR is reset
        self.wl_calculate_btn.setEnabled(False)
        self.wl_reset_btn.setEnabled(False)
        # Reset weight loss section
        self.reset_weight_loss()
    
    def reset_weight_loss(self):
        self.tgt_weight_input.clear()
        self.tgt_calories_input.clear()
        self.loss_result.clear()
        self.time_result.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BMRCalculator()
    window.show()
    sys.exit(app.exec()) 