try:
    import requests
except error:
    print("pip install requests")
    print(error)

url='https://httpbin.org/'
#args es un diccionario para el comando params
args={'nombre':'Luis', 'Curso':'python', 'Nivel':'Intermedio'}
response = requests.get(url, params=args)

print(response.status_code)
content=response.content
print(content)
