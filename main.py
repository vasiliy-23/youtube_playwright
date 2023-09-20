from playwright.async_api import async_playwright, Browser
import time, os, random, secrets, re, asyncio



file_path = 'google_accounts.txt'

s = "abcdefghijklmnopqrstuvwxyz"


async def create_google_accounts():
    

    n = 13 

    target_line = '   '

    lines_found = 0

    offset = -1

    check_file = os.path.exists(file_path)

    if check_file == True: 

        with open(file_path, 'rb') as file:


            file.seek(0, 2) 

            file_length = file.tell()

            while abs(offset) <= file_length:


                file.seek(offset, 2)

                char = file.read(1)

                if char == b'\n': 

                    lines_found += 1

                if lines_found == n:

                    target_line = file.readline().decode().strip()

                    break

                offset -= 1
        
        file.close()

        number = 100

        last_number = target_line[:len(str(number))]

        if last_number == '   ':

            last_number = 0

        else:
            
            last_number = re.sub('[account_=[]', '', target_line)

            last_number = int(last_number)

        if last_number != number:

            with open(file_path) as file:


                t=file.read()

            last_number += 1
                      
            t=t[:-1]+' '

            t += '\n\n   account_' + str(int(last_number)) + '=[\n\n' + "                 Email=" + ''.join(random.sample(s,len(s))) + "@gmail.com" + ",\n\n" + "                 Name=" + ''.join(random.sample(s,len(s))) + ",\n\n" + "                 Password=" + ''.join(random.sample(s,len(s))) + ",\n\n" + "                 Date=" + str(random.randint(1, 28)) + "." + str(random.randint(1, 12)) + "." + str(random.randint(1999, 2004)) + '\n\n             ],\n\n' + '         ]'

            file.close()
            

            with open(file_path, 'w') as file:


                file.write(t)

            file.close()
            
            with open(file_path) as file:


                first_line = file.readline()

                lines = file.readlines()
            
            if first_line != 'accounts=[':

                text = 'accounts=[\n'

                lines.insert(0, text)

                with open(file_path, 'w') as file:


                    file.write(''.join(lines))

                file.close()

            file.close()

    else:

        file = open(file_path, "a+")

        file.close()

        await create_google_accounts()
    
    return last_number

async def SignUp_google_accounts(browser: Browser, i: int):
   

    with open(file_path, 'r') as file:
    
        data = file.read()

    parametr = await create_google_accounts()

    print(parametr)

    pattern = fr"account_{str(parametr)}\s*=\s*\[(.*?)\]"

    print(pattern)


    my_list = re.findall(pattern, data, re.DOTALL)


    if my_list:
        my_list = my_list[0].split(',')
        my_list = str([item.strip() for item in my_list])
        print(my_list)
    else:
        print('Список с таким названием не найден')
    
    pattern_email = r'(Email=)([^,;\s]+)'

    pattern_name = r'(Name=)([^,;\s]+)'

    pattern_password = r'(Password=)([^,;\s]+)'

    pattern_data = r'(Date=)([^,;\s]+)'

    result_email = re.search(pattern_email, my_list)

    result_name = re.search(pattern_name, my_list)

    result_password = re.search(pattern_password, my_list)

    result_data = re.search(pattern_data, my_list)

    Email = result_email.group(2)

    Name = result_name.group(2)

    Password = result_password.group(2)

    Data = result_data.group(2)

    page = await browser.new_page()

    page.set_default_timeout(timeout = 30000000)

    await page.goto("https://accounts.google.com/signup")

    name = page.locator("input[name = 'firstName']")
    
    s = "abcdefghijklmnopqrstuvwxyz"

    await name.type(''.join(random.sample(s,len(s))), delay=100) 

    await page.get_by_text("Далее").click()

    day = page.locator("input[name = 'day']")

    await day.fill(str(random.randint(1, 28)))

    month = page.locator("select[id = 'month']")

    await month.select_option("2")

    year = page.locator("input[name = 'year']")

    await year.type(str(random.randint(1999, 2004)), delay=100)

    gender = page.locator("select[id = 'gender']")

    await gender.select_option("1")

    await page.get_by_text("Далее").click()

    await page.locator("div[class = 't5nRo Id5V1']").last.click()

    email = page.locator("input[aria-label = 'Создайте адрес Gmail']")

    await email.type(''.join(random.sample(s,len(s))), delay=100)

    await page.get_by_text("Далее").first.click()

    password = page.locator("input[aria-label = 'Пароль']")

    await password.type("sewerklkgrgrgmrgr", delay=100)

    confirmation_password = page.locator("input[aria-label = 'Подтвердить']")

    await confirmation_password.type("sewerklkgrgrgmrgr", delay=100)

    await page.get_by_text("Далее").last.click()

    time.sleep(20)


async def start(browser: Browser, i: int):
    

    page = await browser.new_page()

    page.set_default_timeout(timeout = 30000000)

    await page.goto("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")

    await page.goto("chrome-extension://bhchdcejhohfmigjafbampogmaanbfkg/data/popup/index.html") 

    await page.locator("input[type='radio']").nth(random.randint(0, 400)).click()

    await page.locator("input[value='Применить (все окна)']").click()

    await page.goto("chrome-extension://adlpodnneegcnbophopdmhedicjbcgco/popup.html")  
    
    time.sleep(2)

    await page.locator("div[class='connect-button']").click()

    await page.goto("https://youtube.com")

    time.sleep(5)


async def main():


    async with async_playwright() as p:

        path_to_extension = "C:\\Users\\Zemlyanin\\AppData\\Local\\Microsoft\\Edge\\User Data 1\\Default\\Extensions\\bhchdcejhohfmigjafbampogmaanbfkg\\0.5.0_0"

        path_to_extension1 = "C:\\Users\\Zemlyanin\\AppData\\Local\\Microsoft\\Edge\\User Data 1\\Default\\Extensions\\adlpodnneegcnbophopdmhedicjbcgco\\1.10.2_0"

        browser = await p.chromium.launch_persistent_context(user_data_dir="C:\\Users\\Zemlyanin\\AppData\\Local\\Microsoft\\Edge\\User Data 1",
                                                        headless=False,
                                                        channel='msedge',
                                                        no_viewport=True,
                                                        args=['--start-maximized',
                                                              '--disable-blink-features=AutomationControlled',
                                                              f'--disable-extensions-except={path_to_extension},{path_to_extension1}',
                                                              f'--load-extension={path_to_extension},{path_to_extension1}'])
        await create_google_accounts()

        await asyncio.wait([asyncio.create_task(SignUp_google_accounts(browser, i)) for i in range(1)])

        #await asyncio.wait([asyncio.create_task(start(browser, i)) for i in range(10)])  #,return_when=asyncio.ALL_COMPLETED,
        
        #await browser.close()




if __name__ == '__main__':

    asyncio.run(main())