from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    # Altere o caminho abaixo para o local onde você extraiu o chromedriver
    driver_path = '/path/to/chromedriver'
    url = 'https://www.camilaklein.com.br/products/brinco-argola-com-cristais-regeneracao-ouro-velho'
    
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(url)
    
    time.sleep(5)
    
    try:
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.price-item.price-item--regular"))
        )
        price_text = price_element.text
        print(f"Preço do brinco: {price_text}")
        
        price_value = float(price_text.split(' ')[1].replace(',', '.'))
        if price_value < 40.0:
            print("Compre Imediatamente")
        else: 
            print("Continueeeeeeeeeeeeeeeeeeeeeeeeee pesquisandooooooooooooooo")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
