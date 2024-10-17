@echo off
chcp 65001 > nul
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

echo Все пакеты проверены и установлены.
pause

rem Запуск main.py
python main.py
