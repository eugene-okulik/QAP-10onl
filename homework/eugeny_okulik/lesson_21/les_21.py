from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_frames(driver):
    driver.get('https://demoqa.com/frames')
    i_frame = driver.find_element(By.ID, 'frame1')
    driver.switch_to.frame(i_frame)
    sample_heading = driver.find_element(By.ID, 'sampleHeading')
    print(sample_heading.text)
    driver.switch_to.default_content()
    main_text = driver.find_element(By.XPATH, '//div[@id="framesWrapper"]/div')
    print(main_text.text)


def test_hovers(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    # training_link = driver.find_element(By.ID, 'ui-id-7')
    training_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-7')))
    video_download = driver.find_element(By.ID, 'ui-id-28')
    actions = ActionChains(driver)
    actions.move_to_element(training_link)
    actions.click(video_download)
    actions.perform()
    sleep(3)


def test_drag_n_drop(driver):
    driver.get('https://demoqa.com/droppable')
    draggable = driver.find_element(By.ID, 'draggable')
    droppable = driver.find_element(By.ID, 'droppable')
    actions = ActionChains(driver)
    actions.move_to_element(draggable)
    actions.click_and_hold(draggable)
    actions.move_to_element(droppable)
    actions.release(droppable)
    actions.perform()
    assert droppable.text == 'Dropped!'


def test_drag_n_drop2(driver):
    driver.get('https://demoqa.com/droppable')
    draggable = driver.find_element(By.ID, 'draggable')
    droppable = driver.find_element(By.ID, 'droppable')
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable, droppable)
    actions.perform()
    assert droppable.text == 'Dropped!'


def test_alerts(driver):
    driver.get('https://demoqa.com/alerts')
    first_button = driver.find_element(By.ID, 'timerAlertButton')
    first_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    print(alert.text)
    alert.accept()
    driver.save_screenshot('file.png')
    sleep(2)
