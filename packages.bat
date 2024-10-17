@echo off
chcp 65001 > nul

rem Проверка наличия Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python не установлен. Начинаем скачивание и установку...

    rem Скачиваем установщик Python
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe -OutFile python_installer.exe"

    rem Устанавливаем Python тихо и добавляем в PATH
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    rem Проверка установки Python
    python --version >nul 2>&1
    if errorlevel 1 (
        echo Ошибка: Python не установлен. Пожалуйста, установите его вручную.
        pause
        exit /b
    )
) else (
    echo Python уже установлен.
)

echo Для установки библиотек нажмите любую клавишу
pause

rem Список пакетов для проверки
set packages=fade colorama requests selenium beautifulsoup4 pystyle ipaddress ping3

for %%p in (%packages%) do (
    pip show %%p >nul 2>&1
    if errorlevel 1 (
        echo Установка %%p...
        pip install %%p
    ) else (
        echo %%p уже установлен.
    )
)

echo ______________________________________________________________________________
echo Все пакеты проверены и установлены. Нажмите любую клавишу для запуска программы.
pause

rem Запуск main.py
python main.py

