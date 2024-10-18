@echo off
chcp 65001 > nul

rem Проверка наличия Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python не установлен. Открываю браузер для загрузки...

    rem Открываем ссылку в браузере
    start https://www.python.org/downloads/release/python-3120/
    exit /b
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
