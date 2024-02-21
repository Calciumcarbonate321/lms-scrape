from fastapi import FastAPI
from fastapi import Response
from helpers import get_driver
import asyncio

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/lms_ss", responses = {
    200 : {
        "content" : {"image/png" : {}}
    }
})
async def screenshot(username : str, password : str):
    driver = get_driver()
    driver.get("https://lms.vit.ac.in/login/index.php")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "loginbtn").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "page-header")))
    await asyncio.sleep(5)
    screenshot = driver.get_screenshot_as_png()
    return Response(content = screenshot, media_type = "image/png") 