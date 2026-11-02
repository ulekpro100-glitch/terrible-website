"""
Terrible Website Launcher v2
Со встроенным HTML и неправильным календарём
"""
import os
import sys
import time
import webbrowser
import subprocess
import threading
import tempfile
from datetime import datetime
import random

# Флаг работы
running = True
browser_process = None

def get_wrong_datetime():
    """Генерирует неправильные дату и время"""
    # Неправильные часы (25-99)
    wrong_hours = random.randint(25, 99)
    # Неправильные минуты (60-999)
    wrong_minutes = random.randint(60, 999)
    # Неправильные секунды (60-999)
    wrong_seconds = random.randint(60, 999)
    # Неправильные наносекунды (миллионы)
    wrong_nanos = random.randint(1000000, 9999999)

    # Неправильная дата
    wrong_day = random.randint(32, 99)
    wrong_month = random.randint(13, 25)
    wrong_year = random.randint(2027, 3000)

    # Неправильные дни недели
    wrong_weekdays = ["Понидельнек", "Вторнек", "Сриду", "Четверк", "Пятнеца", "Субота", "Воскресеня", "Одинадцатница"]
    wrong_weekday = random.choice(wrong_weekdays)

    return {
        "hours": wrong_hours,
        "minutes": wrong_minutes,
        "seconds": wrong_seconds,
        "nanos": wrong_nanos,
        "day": wrong_day,
        "month": wrong_month,
        "year": wrong_year,
        "weekday": wrong_weekday
    }

def create_html_with_calendar():
    """Создаёт HTML со встроенным неправильным календарём"""
    dt = get_wrong_datetime()

    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ВХАД АБЯЗАТЕЛЕН!!1</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body.register-mode {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: #ffffff;
            overflow: hidden;
        }}

        body.login-mode {{
            font-family: 'Comic Sans MS', cursive;
            overflow-x: hidden;
        }}

        /* НЕПРАВИЛЬНЫЙ КАЛЕНДАРЬ */
        .wrong-calendar {{
            position: fixed;
            top: 10px;
            right: 10px;
            background: linear-gradient(135deg, #ff0000, #ff00ff, #00ffff);
            border: 5px solid #ffff00;
            padding: 20px;
            border-radius: 15px;
            z-index: 999999999;
            animation: calendarSpin 2s infinite;
            box-shadow: 0 0 50px rgba(255, 0, 0, 0.8);
            font-family: 'Comic Sans MS', cursive;
        }}

        @keyframes calendarSpin {{
            0% {{ transform: rotate(0deg) scale(1); }}
            50% {{ transform: rotate(180deg) scale(1.2); }}
            100% {{ transform: rotate(360deg) scale(1); }}
        }}

        .calendar-date {{
            font-size: 42px;
            color: #ffff00;
            text-shadow: 3px 3px #000;
            margin-bottom: 10px;
            animation: textBlink 0.3s infinite;
        }}

        .calendar-time {{
            font-size: 36px;
            color: #00ff00;
            text-shadow: 2px 2px #ff0000;
            animation: timeGlitch 0.2s infinite;
        }}

        .calendar-weekday {{
            font-size: 24px;
            color: #ff00ff;
            text-shadow: 2px 2px #00ffff;
            margin-top: 10px;
        }}

        @keyframes textBlink {{
            0%, 50%, 100% {{ opacity: 1; }}
            25%, 75% {{ opacity: 0; }}
        }}

        @keyframes timeGlitch {{
            0% {{ transform: translateX(0); color: #00ff00; }}
            25% {{ transform: translateX(-5px); color: #ff0000; }}
            50% {{ transform: translateX(5px); color: #0000ff; }}
            75% {{ transform: translateX(-3px); color: #ffff00; }}
            100% {{ transform: translateX(0); color: #00ff00; }}
        }}

        /* Минималистичный стиль регистрации */
        .register-page {{
            display: block;
            background: #ffffff;
            min-height: 100vh;
            padding: 0;
            margin: 0;
        }}

        .register-container {{
            max-width: 360px;
            margin: 0 auto;
            padding: 0 20px;
            padding-top: 25vh;
        }}

        .register-container h1 {{
            font-size: 28px;
            color: #1a1a1a;
            margin-bottom: 40px;
            font-weight: 600;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            letter-spacing: -0.5px;
        }}

        .register-container input {{
            width: 100%;
            padding: 14px 0;
            margin-bottom: 24px;
            border: none;
            border-bottom: 1px solid #e0e0e0;
            font-size: 16px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: transparent;
            transition: border-color 0.3s;
            outline: none;
        }}

        .register-container input:focus {{
            border-bottom: 1px solid #1a1a1a;
        }}

        .register-container input::placeholder {{
            color: #999;
        }}

        .register-container button {{
            width: 100%;
            padding: 16px;
            background: #1a1a1a;
            color: white;
            border: none;
            font-size: 16px;
            cursor: pointer;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            font-weight: 500;
            transition: background 0.3s;
            margin-top: 16px;
        }}

        .register-container button:hover {{
            background: #333;
        }}

        /* УЖАСНЫЙ стиль после регистрации */
        .login-page {{
            display: none;
            background: linear-gradient(45deg, #ff0000, #ff00ff, #00ffff, #00ff00, #ffff00, #ff0000);
            background-size: 400% 400%;
            animation: rainbowShift 0.1s infinite, screenShake 0.2s infinite;
            min-height: 100vh;
            overflow: hidden;
            position: relative;
            filter: contrast(200%) saturate(500%);
        }}

        @keyframes rainbowShift {{
            0% {{ background-position: 0% 50%; filter: hue-rotate(0deg); }}
            50% {{ background-position: 100% 50%; filter: hue-rotate(180deg); }}
            100% {{ background-position: 0% 50%; filter: hue-rotate(360deg); }}
        }}

        @keyframes screenShake {{
            0% {{ transform: translate(0, 0) rotate(0deg); }}
            10% {{ transform: translate(-10px, 5px) rotate(1deg); }}
            20% {{ transform: translate(10px, -5px) rotate(-1deg); }}
            30% {{ transform: translate(-5px, 10px) rotate(2deg); }}
            40% {{ transform: translate(5px, -10px) rotate(-2deg); }}
            50% {{ transform: translate(-10px, -5px) rotate(1deg); }}
            60% {{ transform: translate(10px, 5px) rotate(-1deg); }}
            70% {{ transform: translate(-5px, -10px) rotate(2deg); }}
            80% {{ transform: translate(5px, 10px) rotate(-2deg); }}
            90% {{ transform: translate(-10px, 0) rotate(1deg); }}
            100% {{ transform: translate(0, 0) rotate(0deg); }}
        }}

        .login-container {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            animation: containerChaos 0.3s infinite;
            z-index: 10;
        }}

        @keyframes containerChaos {{
            0% {{ transform: translate(-50%, -50%) rotate(-10deg) scale(0.8); }}
            25% {{ transform: translate(-45%, -55%) rotate(15deg) scale(1.3); }}
            50% {{ transform: translate(-55%, -45%) rotate(-20deg) scale(0.7); }}
            75% {{ transform: translate(-48%, -52%) rotate(25deg) scale(1.4); }}
            100% {{ transform: translate(-50%, -50%) rotate(-10deg) scale(0.8); }}
        }}

        .login-container h1 {{
            color: #ffff00;
            font-size: 82px;
            text-shadow:
                5px 5px 0 #ff00ff,
                10px 10px 0 #00ffff,
                15px 15px 0 #ff0000,
                20px 20px 0 #00ff00;
            animation: titleChaos 0.1s infinite;
            margin-bottom: 20px;
            transform: skew(-5deg) rotate(3deg);
            letter-spacing: -5px;
        }}

        @keyframes titleChaos {{
            0% {{
                transform: translateY(0) skew(-30deg) rotate(20deg) scaleX(0.5);
                color: #ff0000;
                letter-spacing: 20px;
            }}
            25% {{
                transform: translateY(-50px) skew(40deg) rotate(-30deg) scaleX(2);
                color: #00ff00;
                letter-spacing: -10px;
            }}
            50% {{
                transform: translateY(30px) skew(-50deg) rotate(45deg) scaleY(0.3);
                color: #0000ff;
                letter-spacing: 30px;
            }}
            75% {{
                transform: translateY(-20px) skew(60deg) rotate(-50deg) scale(0.4);
                color: #ff00ff;
                letter-spacing: -20px;
            }}
            100% {{
                transform: translateY(0) skew(-30deg) rotate(20deg) scaleX(0.5);
                color: #ff0000;
                letter-spacing: 20px;
            }}
        }}

        marquee {{
            font-size: 38px;
            color: #ff00ff;
            font-weight: bold;
            background: #00ff00;
            padding: 15px;
            text-shadow: 3px 3px #000;
            animation: marqueeGlitch 0.1s infinite;
            opacity: 0.9;
        }}

        @keyframes marqueeGlitch {{
            0% {{
                transform: translateX(0) scaleY(1);
                color: #ff00ff;
                background: #00ff00;
            }}
            25% {{
                transform: translateX(-50px) scaleY(3);
                color: #00ffff;
                background: #ff0000;
            }}
            50% {{
                transform: translateX(50px) scaleY(0.3);
                color: #ffff00;
                background: #0000ff;
            }}
            75% {{
                transform: translateX(-30px) scaleY(5);
                color: #ff0000;
                background: #ff00ff;
            }}
            100% {{
                transform: translateX(0) scaleY(1);
                color: #ff00ff;
                background: #00ff00;
            }}
        }}

        button {{
            padding: 25px 50px;
            font-size: 32px;
            background: linear-gradient(45deg, #ff0000, #ff00ff, #0000ff, #00ff00);
            cursor: pointer;
            animation: buttonJump 0.3s infinite;
        }}

        @keyframes buttonJump {{
            0% {{ top: 0; left: 0; transform: rotate(0deg); }}
            25% {{ top: -80px; left: 60px; transform: rotate(15deg); }}
            50% {{ top: 40px; left: -70px; transform: rotate(-20deg); }}
            75% {{ top: -50px; left: 30px; transform: rotate(10deg); }}
            100% {{ top: 0; left: 0; transform: rotate(0deg); }}
        }}
    </style>
</head>
<body class="register-mode">
    <!-- НЕПРАВИЛЬНЫЙ КАЛЕНДАРЬ -->
    <div class="wrong-calendar" id="wrongCalendar">
        <div class="calendar-weekday" id="calWeekday">{dt['weekday']}</div>
        <div class="calendar-date" id="calDate">{dt['day']}.{dt['month']}.{dt['year']}</div>
        <div class="calendar-time" id="calTime">{dt['hours']}:{dt['minutes']}:{dt['seconds']}</div>
        <div style="font-size: 18px; color: #ffff00; margin-top: 5px;">
            НАНОСЕКУНДЫ: <span id="calNanos">{dt['nanos']}</span>
        </div>
    </div>

    <!-- Регистрация -->
    <div class="register-page" id="registerPage">
        <div class="register-container">
            <h1>Регистрация</h1>
            <input type="text" id="regName" placeholder="Имя">
            <input type="text" id="regPassword" placeholder="Пароль">
            <button onclick="register()">Зарегистрироваться</button>
        </div>
    </div>

    <!-- Вход (УЖАСНЫЙ) -->
    <div class="login-page" id="loginPage">
        <marquee scrollamount="20">!!! ВНИМАНИЕ !!! ЗАЩИЩЕНО ПАРОЛЕМ !!!</marquee>
        <div class="login-container">
            <h1>🔒 ВХАД 🔒</h1>
            <div>
                <input type="text" id="loginName" placeholder="ИМЯ">
                <input type="text" id="loginPassword" placeholder="ПАРОЛ">
            </div>
            <button onclick="login()">ВАЙТИ</button>
            <div id="error" style="color: #ff0000; font-size: 32px; margin-top: 20px;"></div>
        </div>
    </div>

    <script>
        let userData = null;

        // Обновление неправильного времени каждую секунду
        setInterval(() => {{
            const time = document.getElementById('calTime');
            const nanos = document.getElementById('calNanos');
            if (time) {{
                const h = Math.floor(Math.random() * 75) + 25;
                const m = Math.floor(Math.random() * 940) + 60;
                const s = Math.floor(Math.random() * 940) + 60;
                time.textContent = h + ':' + m + ':' + s;
                nanos.textContent = Math.floor(Math.random() * 9000000) + 1000000;
            }}
        }}, 1000);

        function register() {{
            const name = document.getElementById('regName').value.trim();
            const password = document.getElementById('regPassword').value.trim();
            if (!name || !password) {{
                alert('Заполните все поля');
                return;
            }}
            userData = {{ name, password }};
            document.body.className = 'login-mode';
            document.getElementById('registerPage').style.display = 'none';
            document.getElementById('loginPage').style.display = 'block';
        }}

        function login() {{
            const name = document.getElementById('loginName').value;
            const password = document.getElementById('loginPassword').value;
            const error = document.getElementById('error');

            if (userData && name === userData.name && password === userData.password) {{
                alert('✅ ПОЗДРАВЛЯЕМ! ВЫ ВЗЛОМАЛЕ САИТ!!!');
            }} else {{
                error.textContent = '❌ НИПРОВЕЛЬНА!!!';
            }}
        }}
    </script>
</body>
</html>'''
    return html

def open_browser():
    """Открывает браузер с HTML"""
    global browser_process

    try:
        # Создаём временный HTML файл
        temp_dir = tempfile.gettempdir()
        html_file = os.path.join(temp_dir, 'terrible_website.html')

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(create_html_with_calendar())

        html_url = f"file:///{html_file.replace(chr(92), '/')}"

        # Ищем Chrome
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
            browser_process = subprocess.Popen([
                chrome_path,
                "--kiosk",
                "--no-first-run",
                "--disable-session-crashed-bubble",
                html_url
            ])
            print(f"✅ Браузер открыт: {html_url}")
            return True
        else:
            webbrowser.open(html_url, new=1)
            print(f"✅ Браузер открыт: {html_url}")
            return True

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def monitor_browser():
    """Мониторит и переоткрывает браузер"""
    global running, browser_process

    while running:
        if browser_process:
            poll = browser_process.poll()
            if poll is not None:
                print("⚠️ Вкладка закрыта! Переоткрываем...")
                time.sleep(1)
                if running:
                    open_browser()
        time.sleep(2)

def main():
    global running

    print("=" * 60)
    print("🔥 TERRIBLE WEBSITE LAUNCHER v2 🔥")
    print("=" * 60)
    print()
    print("⚠️ ФИЧИ:")
    print("   - Неправильный календарь (25:99:999 час/мин/сек)")
    print("   - Вкладка переоткрывается автоматически")
    print("   - Закрыть: Ctrl+C")
    print()
    print("=" * 60)
    print()

    if not open_browser():
        print("❌ Не удалось открыть браузер!")
        input("Enter для выхода...")
        sys.exit(1)

    monitor_thread = threading.Thread(target=monitor_browser, daemon=True)
    monitor_thread.start()

    print("✅ Запущено!")
    print("🔴 Ctrl+C для выхода")
    print()

    try:
        while running:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n⏹️ Остановка...")
        running = False
        if browser_process:
            try:
                browser_process.terminate()
                browser_process.wait(timeout=5)
            except:
                pass
        print("👋 Завершено")
        sys.exit(0)

if __name__ == "__main__":
    main()
