from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def login(browser):
    # 打开淘宝首页，通过扫码登录
    browser.get("https://www.taobao.com")
    while True:
        try:
            browser.find_element(By.PARTIAL_LINK_TEXT, "亲，请登录").click()
            # browser.find_element(By.PARTIAL_LINK_TEXT, "亲，请登录").click()
            print("\033[0;35m已经点击登录\033[0m")
        except:
            pass
        try:
            browser.find_element(By.PARTIAL_LINK_TEXT, "我的淘宝")
            break
        except:
            pass
        time.sleep(1)


def picking(browser):
    # 打开购物车列表页面
    browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    # method = 0全选购物车
    method = 0
    if method == 0:
        while True:
            try:
                if browser.find_element(By.ID, "J_SelectAll1"):
                    browser.find_element(By.ID, "J_SelectAll1").click()
                    break
            except:
                print(f"找不到购买按钮")
    # method = 1 手动勾选
    else:
        print(f"请手动勾选需要购买的商品")
        time.sleep(5)


# 等待抢购时间，定时秒杀，这里我们定义一个buy函数
def buy(set_time):
    print(f"\033[0;32mset_time:\033[0;36m{set_time}\033[0m")
    set_timestamp = time.mktime(time.strptime(set_time, "%Y-%m-%d %H:%M:%S.%f"))
    while True:
        now_timestamp = time.time()

        # 对比时间，时间到的话就点击结算
        if now_timestamp >= set_timestamp:
            # 点击结算按钮
            while True:
                try:
                    if browser.find_element(By.PARTIAL_LINK_TEXT, "结 算"):
                        browser.find_element(By.PARTIAL_LINK_TEXT, "结 算").click()
                        print(f"结算成功，准备提交订单")
                        break
                except:
                    pass
            # 点击提交订单按钮
            while True:
                try:
                    if browser.find_element(By.PARTIAL_LINK_TEXT, '提交订单'):
                        browser.find_element(By.PARTIAL_LINK_TEXT, '提交订单').click()
                        print(f"抢购成功，请尽快付款")
                except:
                    print(f"再次尝试提交订单")
            time.sleep(0.01)


if __name__ == "__main__":
    browser = webdriver.Chrome(executable_path="./chromedriver")
    login(browser)
    picking(browser)

    set_time = "2023-03-12 14:56:00.000000"
    buy(set_time)
