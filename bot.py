from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import pickle


def attach_to_session(executor_url, session_id):
    original_execute = WebDriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)
    # Patch the function before creating the driver object
    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id
    # Replace the patched function with original function
    WebDriver.execute = original_execute
    return driver


browser = webdriver.Chrome('./chromedriver')

f = open('sessao.txt', 'r')

sessao = f.read()

f = open('url.txt', 'r')

url = f.read()

if sessao=="":
    print('oi')
    browser.get('https://web.whatsapp.com/')
    
    url = browser.command_executor._url 

    session_id = browser.session_id

    f = open("sessao.txt","w+")

    f.write(session_id)

    f.close()

    f = open("url.txt","w+")

    f.write(url)

    f.close()
else:
    browser = attach_to_session(url, sessao)
    browser.get("https://web.whatsapp.com/")

print("Digite start para o bot começar a funcionar:\n")
startBot = input()

if startBot == 'start':

    conversas = browser.find_elements_by_class_name('_2wP_Y')
    rodar = ""
    while rodar!="parar":
        print("Digite o nome de uma pessoa que esteja entre 0 e " + str(len(conversas)))
        pessoa = input()
        for conversa in conversas:
            array = conversa.text.split("\n")
            if(array[0]==pessoa):
                conversa.click()
                boxTexto = browser.find_element_by_css_selector('#main > footer > div._3pkkz.copyable-area > div._1Plpp > div > div._2S1VP.copyable-text.selectable-text')
                boxTexto.send_keys("Olá eu sou um bot e escrevo mensagens :)")
                botaoSubmit = browser.find_element_by_css_selector('#main > footer > div._3pkkz.copyable-area > div:nth-child(3) > button')
                botaoSubmit.click()
        print("Deseja continuar? ")
        rodar = input()
else:
    print('Digite start para iniciar.')