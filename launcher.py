"""
Terrible Website Launcher
Открывает сайт в браузере и автоматически переоткрывает вкладку при закрытии
"""
import os
import sys
import time
import webbrowser
import subprocess
import threading
import tempfile
from pathlib import Path

# Встроенный HTML (для упаковки в один EXE)
HTML_CONTENT = """

# Флаг работы
running = True
browser_process = None

def open_browser():
    """Открывает браузер с HTML файлом"""
    global browser_process
    try:
        # Пытаемся открыть в Chrome с полноэкранным режимом
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
        ]

        chrome_path = None
        for path in chrome_paths:
            if os.path.exists(path):
                chrome_path = path
                break

        if chrome_path:
            # Открываем в Chrome с киоск-режимом (fullscreen без кнопок)
            browser_process = subprocess.Popen([
                chrome_path,
                "--kiosk",
                "--no-first-run",
                "--disable-session-crashed-bubble",
                "--disable-infobars",
                HTML_URL
            ])
            print(f"✅ Браузер открыт: {HTML_URL}")
            return True
        else:
            # Fallback на стандартный браузер
            webbrowser.open(HTML_URL, new=1)
            print(f"✅ Браузер открыт: {HTML_URL}")
            return True

    except Exception as e:
        print(f"❌ Ошибка открытия браузера: {e}")
        return False

def monitor_browser():
    """Мониторит браузер и переоткрывает при закрытии"""
    global running, browser_process

    while running:
        # Если есть процесс Chrome
        if browser_process:
            poll = browser_process.poll()
            if poll is not None:
                # Процесс закрыт, переоткрываем
                print("⚠️ Вкладка закрыта! Переоткрываем через 1 секунду...")
                time.sleep(1)
                if running:
                    open_browser()
        else:
            # Процесс не отслеживается, открываем каждые 5 секунд если браузер закрыт
            time.sleep(5)
            if running:
                # Проверяем, открыт ли браузер с нашим URL
                # (Это упрощённая проверка, в реальности нужен psutil)
                print("🔄 Проверка браузера...")
                open_browser()

        time.sleep(2)

def main():
    """Главная функция"""
    global running

    print("=" * 60)
    print("🔥 TERRIBLE WEBSITE LAUNCHER 🔥")
    print("=" * 60)
    print()
    print(f"📁 HTML файл: {HTML_FILE}")
    print(f"🌐 URL: {HTML_URL}")
    print()
    print("⚠️ ВНИМАНИЕ:")
    print("   - Вкладка будет автоматически переоткрываться при закрытии")
    print("   - Чтобы выйти, закройте ЭТО ОКНО или нажмите Ctrl+C")
    print()
    print("=" * 60)
    print()

    # Проверяем наличие HTML файла
    if not HTML_FILE.exists():
        print(f"❌ ОШИБКА: Файл {HTML_FILE} не найден!")
        input("Нажмите Enter для выхода...")
        sys.exit(1)

    # Открываем браузер первый раз
    if not open_browser():
        print("❌ Не удалось открыть браузер!")
        input("Нажмите Enter для выхода...")
        sys.exit(1)

    # Запускаем мониторинг в отдельном потоке
    monitor_thread = threading.Thread(target=monitor_browser, daemon=True)
    monitor_thread.start()

    print()
    print("✅ Мониторинг запущен!")
    print("🔴 Нажмите Ctrl+C или закройте это окно для выхода")
    print()

    try:
        # Ждём прерывания
        while running:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n⏹️ Остановка...")
        running = False

        # Закрываем процесс браузера если он был запущен нами
        if browser_process:
            try:
                browser_process.terminate()
                browser_process.wait(timeout=5)
                print("✅ Браузер закрыт")
            except Exception as e:
                print(f"⚠️ Ошибка закрытия браузера: {e}")

        print("👋 Программа завершена")
        sys.exit(0)

if __name__ == "__main__":
    main()
