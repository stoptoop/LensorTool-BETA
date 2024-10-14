from Utils.config import *
import requests




def discordstatus():
    try:
        response = requests.get(f"https://discordstatus.com/api/v2/summary.json")
        api = response.json()

        # Получаем все компоненты
        components = api.get('components', [])

        # Устанавливаем список нужных id
        target_ids = ["rhznvxg4v7yh", "ly7bf56hshjc", "dmyjqtpgpjkr", "8r4xqnt9jslk", "gvg1c6688r5y", "x7rnz0t7dpnp", "6j5lgxtyjfc2", "jk03xttfcz9b"]

        # Проходим по каждому компоненту и выводим только те, у которых id совпадает
        for component in components:
            if component.get('id') in target_ids:   
                print(now_time(), colored_yellow(f"ID: {component.get('id')}"))
                print(now_time(), colored_yellow(f"Name: {component.get('name')}"))
                print(now_time(), colored_yellow(f"Description: {component.get('description')}"))
                print(now_time(), colored_green(f"Status: {component.get('status')}"))
                print(now_time(), colored_yellow(f"Updated at: {component.get('updated_at')}"))
                print("-" * 40)  # Разделитель для наглядности между компонентами
        main()





    except Exception as e:
        print(colored_red_purple(f"Error occured try again later or Contact the developer"))