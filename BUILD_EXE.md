# Как создать EXE из launcher.py

## Способ 1: PyInstaller (Рекомендуется)

### Установка:
```bash
pip install pyinstaller
```

### Компиляция в EXE:
```bash
cd C:\Users\8andr\OneDrive\Desktop\deepseek\terrible-website
pyinstaller --onefile --noconsole --icon=NONE --name="TerribleWebsite" launcher.py
```

**Параметры:**
- `--onefile` — один exe файл
- `--noconsole` — без консольного окна (если хочешь скрытый режим)
- `--name` — имя exe файла
- Для показа консоли убери `--noconsole`

**EXE будет в:** `dist\TerribleWebsite.exe`

### ⚠️ ВАЖНО:
- Скопируй `index.html` в ту же папку где `TerribleWebsite.exe`
- Или измени код и укажи полный путь к HTML

---

## Способ 2: Auto-py-to-exe (С GUI)

### Установка:
```bash
pip install auto-py-to-exe
```

### Запуск:
```bash
auto-py-to-exe
```

1. Выбери `launcher.py`
2. Режим: **One File**
3. Console: **Console Based** (чтобы видеть что происходит)
4. Нажми **CONVERT .PY TO .EXE**

---

## Способ 3: Nuitka (Самый быстрый EXE)

### Установка:
```bash
pip install nuitka
```

### Компиляция:
```bash
python -m nuitka --onefile --windows-disable-console launcher.py
```

---

## После компиляции:

### Структура папки:
```
dist/
├── TerribleWebsite.exe
└── index.html  ← ВАЖНО! Должен быть рядом с EXE
```

### Запуск:
1. Двойной клик на `TerribleWebsite.exe`
2. Откроется браузер с сайтом
3. При закрытии вкладки — откроется снова
4. Закрыть можно только через диспетчер задач или закрыв консоль launcher

---

## Для полного киоск-режима (невозможно закрыть):

Измени в `launcher.py`:
```python
# Вместо --kiosk используй:
browser_process = subprocess.Popen([
    chrome_path,
    "--kiosk",
    "--app=" + HTML_URL,  # Режим приложения
    "--disable-session-crashed-bubble",
    "--disable-infobars",
    "--overscroll-history-navigation=0"  # Отключить жесты
])
```

Или используй эту команду для **полного захвата экрана**:
```python
subprocess.Popen([
    chrome_path,
    "--kiosk",
    "--kiosk-printing",  # Блокировка печати
    "--disable-restore-session-state",
    "--disable-translate",
    HTML_URL
])
```

---

## Тестирование:

```bash
# Запусти Python-скрипт сначала:
python launcher.py

# Если работает, компилируй в EXE:
pyinstaller --onefile --name="TerribleWebsite" launcher.py

# Скопируй index.html в папку dist/
copy index.html dist\

# Запусти EXE:
dist\TerribleWebsite.exe
```

---

## Автозапуск при старте Windows (Опционально):

Скопируй `TerribleWebsite.exe` в:
```
C:\Users\8andr\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

Или создай ярлык в автозагрузке:
1. Win+R → `shell:startup`
2. Скопируй туда ярлык на EXE

---

## Проблемы и решения:

### "ModuleNotFoundError" при запуске EXE
→ Используй `--hidden-import` при сборке:
```bash
pyinstaller --onefile --hidden-import=webbrowser launcher.py
```

### EXE не находит index.html
→ Добавь в код абсолютный путь или упакуй HTML в EXE:
```python
HTML_FILE = Path(sys.executable).parent / "index.html"
```

### Браузер не открывается в kiosk режиме
→ Проверь путь к Chrome или используй Edge:
```python
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
```
