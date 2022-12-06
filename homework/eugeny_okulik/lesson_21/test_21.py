from time import sleep


def test_scroll(driver):
    driver.get('https://memes.com')
    sleep(5)
    # driver.execute_script("window.scrollTo(0, 300);")
    total_page_height = driver.execute_script("return document.body.scrollHeight")
    browser_window_height = driver.get_window_size(windowHandle='current')['height']
    current_position = driver.execute_script('return window.pageYOffset')
    while total_page_height - current_position > browser_window_height:
        driver.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
        current_position = driver.execute_script('return window.pageYOffset')
        sleep(1)  # It is necessary here to give it some time to load the content
    # sleep(3)
