from Utils.config import *
import requests










def iplookup():
    try:
        ip = input(f"{now_time()}~ Insert Ip ~ {purple}[ {end}> {purple}]  {end}")

        try:
            response = requests.get(f"http://ip-api.com/json/{ip}")
            api = response.json()

            ip = api.get('ip')
            status = api.get('status')
            country = api.get('country')
            country_code = api.get('country_code')
            region = api.get('region')
            region_code = api.get('region_code')
            zip = api.get('zip')
            city = api.get('city')
            latitude = api.get('latitude')
            longitude = api.get('longitude')
            timezone = api.get('timezone')
            isp = api.get('isp')
            org = api.get('org')
            as_host = api.get('as')

        except:
            response = requests.get(f"http://ip-api.com/json/{ip}")
            api = response.json()

            status = "Valid" if api.get('status') == "success" else "Invalid"
            country = api.get('country', "None")
            country_code = api.get('countryCode', "None")
            region = api.get('regionName', "None")
            region_code = api.get('region', "None")
            zip = api.get('zip', "None")
            city = api.get('city', "None")
            latitude = api.get('lat', "None")
            longitude = api.get('lon', "None")
            timezone = api.get('timezone', "None")
            isp = api.get('isp', "None")
            org = api.get('org', "None")
            as_host = api.get('as', "None")

        Slow(f"""
    {now_time()} Status     : {white}{status}
    {now_time()} Country    : {white}{country} ({country_code})
    {now_time()} Region     : {white}{region} ({region_code})
    {now_time()} Zip        : {white}{zip}
    {now_time()} City       : {white}{city}
    {now_time()} Latitude   : {white}{latitude}
    {now_time()} Longitude  : {white}{longitude}
    {now_time()} Timezone   : {white}{timezone}
    {now_time()} Isp        : {white}{isp}
    {now_time()} Org        : {white}{org}
    {now_time()} As         : {white}{as_host}
    """)
        print(f"{purple}>>>{end}  to exit print  15")
        main()
    except Exception as e:
        print(e)