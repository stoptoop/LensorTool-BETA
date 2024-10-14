from Utils.config import *
import requests







def cleardm():
    try:
        token = Choice1TokenDiscord()
        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        if r.status_code == 200:
            pass
        else:
            print("Error")

        def DmDeleter(token, channels):
            for channel in channels:
                try:
                    requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'], headers={'Authorization': token})
                    print(f" Status: Delete| Channel: {channel['id']}")
                except Exception as e:
                    print(f"Status: Error: {e}")

        processes = []
        channel_id = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token}).json()
        if not channel_id:
            print(f"No Dm found.")
            main()

        for channel in [channel_id[i:i+3] for i in range(0, len(channel_id), 3)]:
                t = threading.Thread(target=DmDeleter, args=(token, channel))
                t.start()
                processes.append(t)
        for process in processes:
            process.join()

    except Exception as e:
        print(e)