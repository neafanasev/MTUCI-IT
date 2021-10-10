import requests
url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

headers = {
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "5f06fc98b4msh094642aebd9283bp1ae520jsn3e4556e00b29"
}
def get(text, lg):
    if lg == "en":
        payload = {'q': text, 'target': lg, 'source': 'ru'}
        response = requests.request("POST", url, data=payload, headers=headers)
        # return f"'{lg}' {text} '{lg}'"
    elif lg == "ru":
        payload = {'q': text, 'target': lg, 'source': 'en'}
        response = requests.request("POST", url, data=payload, headers=headers)
        # return f"'{lg}' {text} '{lg}'"
    response = response.text[44:-5]
    print(response)
    return response