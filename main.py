import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QSlider, QComboBox, QGroupBox, QGridLayout,
                             QFrame)
from PyQt5.QtCore import Qt


class AnimeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор Оценки Аниме")
        self.setGeometry(200, 150, 920, 640)

        self.genre_presets = {
            "Фэнтези / Исэкай": {'plot': 12, 'lore': 18, 'characters': 10, 'style': 5, 'music': 5, 'humor': 0},
            "Исэкай-Комедия": {'plot': 5, 'lore': 10, 'characters': 15, 'style': 5, 'music': 5, 'humor': 10},
            "Экшн / Сёнэн": {'plot': 10, 'lore': 5, 'characters': 15, 'style': 15, 'music': 5, 'humor': 0},
            "Драма / Психология": {'plot': 15, 'lore': 5, 'characters': 20, 'style': 5, 'music': 5, 'humor': 0},
            "Романтика / Повседневность": {'plot': 5, 'lore': 0, 'characters': 25, 'style': 10, 'music': 5, 'humor': 5},
            "Триллер / Детектив": {'plot': 20, 'lore': 15, 'characters': 10, 'style': 5, 'music': 0, 'humor': 0},
            "Хоррор / Атмосфера": {'plot': 10, 'lore': 5, 'characters': 5, 'style': 20, 'music': 10, 'humor': 0},
            "Комедия / Слайс / Жвачка": {'plot': 5, 'lore': 0, 'characters': 10, 'style': 10, 'music': 5, 'humor': 20},
            "Меха / Сай-фай": {'plot': 15, 'lore': 15, 'characters': 5, 'style': 10, 'music': 5, 'humor': 0},
            "Психологический хоррор": {'plot': 15, 'lore': 10, 'characters': 15, 'style': 5, 'music': 5, 'humor': 0},
            "Ияшикэй / Уютное": {'plot': 5, 'lore': 5, 'characters': 15, 'style': 10, 'music': 5, 'humor': 10},
            "Спорт / Сёдзё": {'plot': 10, 'lore': 5, 'characters': 20, 'style': 10, 'music': 5, 'humor': 0},
        }

        self.criterion_descriptions = {
            'plot': {
                'name': 'Сюжет',
                'subtitle': 'Структура, конфликт, финал',
                'tooltip': (
                    "<b>Сюжет (Структура, конфликт, финал)</b><br><br>"
                    "<b>0–2:</b> Сюжета нет. Набор несвязанных сцен.<br>"
                    "<b>3–4:</b> Есть задумка, но она разваливается. Провисания, слитый финал.<br>"
                    "<b>5–6:</b> Рабочая, но предсказуемая структура. Стандартные ходы.<br>"
                    "<b>7–8:</b> Цельная история с работающим конфликтом. Есть неожиданные, но оправданные повороты.<br>"
                    "<b>9–10:</b> Идеальная структура. Каждая сцена работает на общую идею."
                ),
                'ranges': [
                    (0, 2, "Сюжета нет. Набор несвязанных сцен."),
                    (3, 4, "Есть задумка, но она разваливается."),
                    (5, 6, "Рабочая, но предсказуемая структура."),
                    (7, 8, "Цельная история с работающим конфликтом."),
                    (9, 10, "Идеальная структура. Финал меняет всё.")
                ]
            },
            'lore': {
                'name': 'Лор',
                'subtitle': 'Мир, правила, подача',
                'tooltip': (
                    "<b>Лор (Мир, правила, подача)</b><br><br>"
                    "<b>0–2:</b> Мира нет. Просто декорации.<br>"
                    "<b>3–4:</b> Мир есть, но он нелогичен или противоречит сам себе.<br>"
                    "<b>5–6:</b> Мир функционален, но вторичен. Правила есть, но не ощущаются.<br>"
                    "<b>7–8:</b> Продуманный мир с внятными правилами. Он влияет на сюжет и героев.<br>"
                    "<b>9–10:</b> Мир — полноценный персонаж. Его детали хочется изучать. Он уникален."
                ),
                'ranges': [
                    (0, 2, "Мира нет. Просто декорации."),
                    (3, 4, "Мир нелогичен или противоречив."),
                    (5, 6, "Мир функционален, но вторичен."),
                    (7, 8, "Продуманный мир, влияет на сюжет."),
                    (9, 10, "Мир — полноценный персонаж.")
                ]
            },
            'characters': {
                'name': 'Герои',
                'subtitle': 'Мотивация, арки, химия',
                'tooltip': (
                    "<b>Герои (Мотивация, арки, химия)</b><br><br>"
                    "<b>0–2:</b> Пустые функции. Хочется, чтобы их убили.<br>"
                    "<b>3–4:</b> Картонные. Мотивация притянута за уши.<br>"
                    "<b>5–6:</b> Понятные типажи, но без глубины. Работают на сюжет.<br>"
                    "<b>7–8:</b> Живые персонажи. Им сопереживаешь. Есть развитие.<br>"
                    "<b>9–10:</b> Ты их помнишь. Их решения неоднозначны и вызывают споры/обсуждения."
                ),
                'ranges': [
                    (0, 2, "Пустые функции. Хочется, чтобы их убили."),
                    (3, 4, "Картонные. Мотивация притянута."),
                    (5, 6, "Понятные типажи, но без глубины."),
                    (7, 8, "Живые персонажи. Им сопереживаешь."),
                    (9, 10, "Ты их помнишь. Вызывают бурные обсуждения")
                ]
            },
            'style': {
                'name': 'Стиль/Рисовка',
                'subtitle': 'Визуал, монтаж, подача',
                'tooltip': (
                    "<b>Стиль/Рисовка (Визуал, монтаж, подача)</b><br><br>"
                    "<b>0–2:</b> Больно смотреть.<br>"
                    "<b>3–4:</b> Стиль нестабилен. Часто выпадает из общего тона.<br>"
                    "<b>5–6:</b> Аккуратно, но безлико. Стандартный «рабочий» уровень.<br>"
                    "<b>7–8:</b> Узнаваемый стиль. Визуал работает на атмосферу. Есть запоминающиеся кадры.<br>"
                    "<b>9–10:</b> Визуал — язык повествования. Каждый кадр — фон рабочего стола."
                ),
                'ranges': [
                    (0, 2, "Больно смотреть. Технический брак."),
                    (3, 4, "Стиль нестабилен, выпадает из тона."),
                    (5, 6, "Аккуратно, но безлико."),
                    (7, 8, "Узнаваемый стиль, работает на атмосферу."),
                    (9, 10, "Визуал — язык повествования.")
                ]
            },
            'music': {
                'name': 'Музыка',
                'subtitle': 'Саундтрек, звук, атмосфера',
                'tooltip': (
                    "<b>Музыка (Саундтрек, звук, атмосфера)</b><br><br>"
                    "<b>0–2:</b> Звука нет или он мешает. Тишина была бы лучше.<br>"
                    "<b>3–4:</b> Музыка есть, но она не запоминается и не работает на сцены.<br>"
                    "<b>5–6:</b> Функциональный саундтрек. Появляется в нужных местах.<br>"
                    "<b>7–8:</b> Музыка усиливает эмоции. Есть темы, которые ты гуглишь после.<br>"
                    "<b>9–10:</b> Саундтрек — половина успеха. Ты слушаешь его отдельно."
                ),
                'ranges': [
                    (0, 2, "Звука нет или он мешает."),
                    (3, 4, "Музыка не запоминается, не работает на сцены."),
                    (5, 6, "Функциональный саундтрек."),
                    (7, 8, "Музыка усиливает эмоции."),
                    (9, 10, "Саундтрек — половина успеха.")
                ]
            },
            'humor': {
                'name': 'Юмор / Гэги',
                'subtitle': 'Смех, тайминг, абсурд',
                'tooltip': (
                    "<b>Юмор / Гэги (Смех, тайминг, абсурд)</b><br><br>"
                    "<b>0–2:</b> Шуток нет или они вызывают кринж. Лучше бы молчали.<br>"
                    "<b>3–4:</b> Шутки есть, но неуместные или несмешные. Мимо кассы.<br>"
                    "<b>5–6:</b> Рабочие гэги. Улыбнуло, но не засмеялся. Стандартный уровень.<br>"
                    "<b>7–8:</b> Реально смешно. Есть моменты, которые хочется пересмотреть ради шутки.<br>"
                    "<b>9–10:</b> Эталон комедии."
                ),
                'ranges': [
                    (0, 2, "Шуток нет или кринж."),
                    (3, 4, "Шутки неуместные или несмешные."),
                    (5, 6, "Рабочие гэги. Улыбнуло."),
                    (7, 8, "Реально смешно. Хочется пересмотреть."),
                    (9, 10, "Эталон комедии.")
                ]
            },
        }

        self.vibe_description = {
            'name': '«Затянуло» (Погружение, пересматриваемость)',
            'tooltip': (
                "<b>«Затянуло» (Погружение, пересматриваемость)</b><br><br>"
                "<b>0–2:</b> Хотелось выключить. Смотрел через силу.<br>"
                "<b>3–4:</b> Досмотрел, но без удовольствия. Пересматривать не буду.<br>"
                "<b>5–6:</b> Нормально. Посмотрел и забыл.<br>"
                "<b>7–8:</b> Затянуло. Смотрел запоем. Есть моменты, которые хочется пересмотреть.<br>"
                "<b>9–10:</b> Не мог оторваться. Пересматриваю. Рекомендую всем."
            ),
            'ranges': [
                (0, 2, "Хотелось выключить. Смотрел через силу."),
                (3, 4, "Досмотрел без удовольствия. Пересматривать не буду."),
                (5, 6, "Нормально. Посмотрел и забыл."),
                (7, 8, "Затянуло. Смотрел запоем."),
                (9, 10, "Не мог оторваться. Пересматриваю.")
            ]
        }

        self.sliders = {}
        self.value_labels = {}
        self.weight_labels = {}
        self.desc_labels = {}

        self.init_ui()
        self.calculate_score()

    def get_description(self, criterion_key, value):
        if criterion_key == 'vibe':
            ranges = self.vibe_description['ranges']
        else:
            ranges = self.criterion_descriptions[criterion_key]['ranges']
        for low, high, text in ranges:
            if low <= value <= high:
                return text
        return ""

    def make_criterion_block(self, key):
        """Создаёт визуальный блок для одного критерия"""
        crit = self.criterion_descriptions[key]

        block = QFrame()
        block.setStyleSheet(
            "QFrame { background-color: #333; border-radius: 8px; }"
        )
        block_layout = QVBoxLayout()
        block_layout.setSpacing(6)
        block_layout.setContentsMargins(12, 10, 12, 10)

        # Верхняя строка: название + вес
        top_row = QHBoxLayout()
        top_row.setSpacing(6)

        name_box = QVBoxLayout()
        name_box.setSpacing(0)
        name_label = QLabel(crit['name'])
        name_label.setStyleSheet("font-weight: bold; font-size: 14px; color: #fff;")
        name_label.setToolTip(crit['tooltip'])
        name_label.setToolTipDuration(15000)
        subtitle_label = QLabel(crit['subtitle'])
        subtitle_label.setStyleSheet("color: #777; font-size: 10px;")
        subtitle_label.setToolTip(crit['tooltip'])
        subtitle_label.setToolTipDuration(15000)
        name_box.addWidget(name_label)
        name_box.addWidget(subtitle_label)

        weight_label = QLabel("")
        weight_label.setAlignment(Qt.AlignRight | Qt.AlignTop)
        weight_label.setStyleSheet("color: #888; font-size: 11px;")

        top_row.addLayout(name_box)
        top_row.addStretch()
        top_row.addWidget(weight_label)
        block_layout.addLayout(top_row)

        # Слайдер + значение
        slider_row = QHBoxLayout()
        slider_row.setSpacing(8)
        slider = QSlider(Qt.Horizontal)
        slider.setRange(1, 10)
        slider.setValue(5)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(1)

        value_label = QLabel("5")
        value_label.setFixedWidth(28)
        value_label.setAlignment(Qt.AlignCenter)
        value_label.setStyleSheet("font-weight: bold; color: #4CAF50; font-size: 15px;")

        slider_row.addWidget(slider)
        slider_row.addWidget(value_label)
        block_layout.addLayout(slider_row)

        # Описание
        desc_label = QLabel(self.get_description(key, 5))
        desc_label.setWordWrap(True)
        desc_label.setMinimumHeight(30)
        desc_label.setStyleSheet("color: #aaa; font-size: 11px; font-style: italic;")
        block_layout.addWidget(desc_label)

        block.setLayout(block_layout)

        self.sliders[key] = slider
        self.value_labels[key] = value_label
        self.weight_labels[key] = weight_label
        self.desc_labels[key] = desc_label

        slider.valueChanged.connect(lambda val, k=key: self.on_slider_change(k, val))

        return block

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)

        # Выбор жанра
        genre_layout = QHBoxLayout()
        genre_layout.addWidget(QLabel("Жанр:"))
        self.genre_combo = QComboBox()
        self.genre_combo.addItems(self.genre_presets.keys())
        self.genre_combo.setStyleSheet("padding: 5px; font-size: 13px;")
        self.genre_combo.currentTextChanged.connect(self.calculate_score)
        genre_layout.addWidget(self.genre_combo, 1)
        main_layout.addLayout(genre_layout)

        # Сетка 3x2 для критериев
        criteria_group = QGroupBox("Оценка критериев (от 1 до 10)")
        grid = QGridLayout()
        grid.setSpacing(10)

        criteria_order = ['plot', 'lore', 'characters', 'style', 'music', 'humor']
        for i, key in enumerate(criteria_order):
            row = i // 3
            col = i % 3
            block = self.make_criterion_block(key)
            grid.addWidget(block, row, col)

        # Равные ширины колонок
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setColumnStretch(2, 1)

        criteria_group.setLayout(grid)
        main_layout.addWidget(criteria_group)

        bottom_row = QHBoxLayout()
        bottom_row.setSpacing(10)

        # Вайб-блок
        vibe_group = QGroupBox("Вайб / Затянуло (Множитель)")
        vibe_layout = QVBoxLayout()
        vibe_layout.setSpacing(4)

        vibe_top = QHBoxLayout()
        vibe_name = QLabel("«Затянуло»")
        vibe_name.setStyleSheet("font-weight: bold; font-size: 13px;")
        vibe_name.setToolTip(self.vibe_description['tooltip'])
        vibe_name.setToolTipDuration(15000)
        vibe_top.addWidget(vibe_name)
        vibe_top.addStretch()
        self.multiplier_label = QLabel("×1.444")
        self.multiplier_label.setStyleSheet("color: #FF9800; font-weight: bold; font-size: 12px;")
        vibe_top.addWidget(self.multiplier_label)
        vibe_layout.addLayout(vibe_top)

        vibe_slider_row = QHBoxLayout()
        self.vibe_slider = QSlider(Qt.Horizontal)
        self.vibe_slider.setRange(1, 10)
        self.vibe_slider.setValue(5)
        self.vibe_slider.setTickPosition(QSlider.TicksBelow)
        self.vibe_slider.setTickInterval(1)

        self.vibe_label = QLabel("5")
        self.vibe_label.setFixedWidth(28)
        self.vibe_label.setAlignment(Qt.AlignCenter)
        self.vibe_label.setStyleSheet("font-weight: bold; color: #4CAF50; font-size: 15px;")

        vibe_slider_row.addWidget(self.vibe_slider)
        vibe_slider_row.addWidget(self.vibe_label)
        vibe_layout.addLayout(vibe_slider_row)

        self.vibe_desc_label = QLabel(self.get_description('vibe', 5))
        self.vibe_desc_label.setWordWrap(True)
        self.vibe_desc_label.setStyleSheet("color: #aaa; font-size: 11px; font-style: italic;")
        vibe_layout.addWidget(self.vibe_desc_label)

        self.vibe_slider.valueChanged.connect(self.on_vibe_change)
        vibe_group.setLayout(vibe_layout)
        bottom_row.addWidget(vibe_group, 2)

        # Итог
        result_group = QGroupBox("Итоговый балл")
        result_layout = QVBoxLayout()

        self.result_label = QLabel("0 / 100")
        self.result_label.setStyleSheet("font-size: 42px; font-weight: bold; color: #2196F3;")
        self.result_label.setAlignment(Qt.AlignCenter)
        result_layout.addWidget(self.result_label)

        self.breakdown_label = QLabel("")
        self.breakdown_label.setAlignment(Qt.AlignCenter)
        self.breakdown_label.setWordWrap(True)
        self.breakdown_label.setStyleSheet("color: #aaa; font-size: 10px;")
        result_layout.addWidget(self.breakdown_label)

        result_group.setLayout(result_layout)
        bottom_row.addWidget(result_group, 3)

        main_layout.addLayout(bottom_row)

        self.setLayout(main_layout)

    def on_slider_change(self, key, val):
        self.value_labels[key].setText(str(val))
        self.desc_labels[key].setText(self.get_description(key, val))
        self.calculate_score()

    def on_vibe_change(self, val):
        self.vibe_label.setText(str(val))
        self.vibe_desc_label.setText(self.get_description('vibe', val))
        self.calculate_score()

    def calculate_score(self):
        genre = self.genre_combo.currentText()
        current_weights = self.genre_presets.get(genre, self.genre_presets["Фэнтези / Исэкай"])

        for key, weight in current_weights.items():
            if weight == 0:
                self.weight_labels[key].setText("вес 0")
                self.weight_labels[key].setStyleSheet("color: #F44336; font-size: 11px; font-weight: bold;")
            else:
                self.weight_labels[key].setText(f"вес {weight}")
                self.weight_labels[key].setStyleSheet("color: #888; font-size: 11px;")

        base_sum = 0
        for key, slider in self.sliders.items():
            val = slider.value()
            weight = current_weights[key]
            base_sum += (val / 10.0) * weight

        vibe_val = self.vibe_slider.value()
        multiplier = 1.0 + (vibe_val - 1) / 9.0
        self.multiplier_label.setText(f"×{multiplier:.3f}")

        final_score = base_sum * multiplier
        final_rounded = round(final_score)

        if final_rounded >= 85:
            color = "#4CAF50"
        elif final_rounded >= 70:
            color = "#2196F3"
        elif final_rounded >= 50:
            color = "#FF9800"
        else:
            color = "#F44336"

        self.result_label.setText(f"{final_rounded}")
        self.result_label.setStyleSheet(f"font-size: 42px; font-weight: bold; color: {color};")

        self.breakdown_label.setText(
            f"{genre}\nБаза: {base_sum:.1f}/50 | ×{multiplier:.3f} | Точный: {final_score:.2f}"
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyleSheet("""
        QWidget { background-color: #2b2b2b; color: #ffffff; font-family: Arial; }
        QGroupBox { border: 1px solid #555; border-radius: 5px; margin-top: 10px; padding-top: 15px; font-weight: bold; }
        QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; color: #4CAF50; }
        QSlider::groove:horizontal { border: 1px solid #999; height: 8px; background: #444; border-radius: 4px; }
        QSlider::handle:horizontal { background: #4CAF50; border: 1px solid #5c5c5c; width: 18px; margin: -5px 0; border-radius: 9px; }
        QSlider::handle:horizontal:hover { background: #66BB6A; }
        QSlider::sub-page:horizontal { background: #4CAF50; border-radius: 4px; }
        QComboBox { background-color: #3a3a3a; border: 1px solid #555; border-radius: 4px; padding: 5px; color: #fff; }
        QComboBox::drop-down { border: none; }
        QComboBox QAbstractItemView { background-color: #3a3a3a; color: #fff; selection-background-color: #4CAF50; }
        QToolTip { background-color: #1e1e1e; color: #fff; border: 1px solid #4CAF50; padding: 6px; font-size: 11px; }
    """)

    window = AnimeCalculator()
    window.show()
    sys.exit(app.exec_())