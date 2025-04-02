from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запуск WinAppDriver перед этим должен быть активирован
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723',
    desired_capabilities={
        "app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    }
)

# Ожидание открытия калькулятора
time.sleep(2)

try:
    # Поиск элементов и нажатие на кнопки
    driver.find_element(By.NAME, "One").click()
    driver.find_element(By.NAME, "Plus").click()
    driver.find_element(By.NAME, "Two").click()
    driver.find_element(By.NAME, "Equals").click()

    # Получение результата
    result = driver.find_element(By.ACCESSIBILITY_ID, "CalculatorResults").text

    # Проверка результата
    assert "3" in result, f"Test Failed: Expected result was 3, but got {result}"
    print("Test Passed: Result is 3")
    
finally:
    # Закрытие драйвера
    driver.quit()