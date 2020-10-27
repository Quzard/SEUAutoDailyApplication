# coding: utf-8
# Author：quzard

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
import time
import random
import smtplib
import requests
import datetime

subject = '入校申请'
msg = '入校申请名单' + '\n\n'
def main():
    global msg

    username = [""]
    password = [""]
    name =     [""]

    su = [""] # 住在校外的人需要苏康码
    si = [""] # 四牌楼人员，如果不在此添加，默认为无线谷人员入校申请
    pic = [""] # 住在校外的人需要苏康码照片
    tele_name = [""] # 部分人需要手动输入手机号码
    tele = [""] # 部分人需要手动输入手机号码
    
    for i in range(len(username)):
        if (name[i] == ""):
            continue
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.implicitly_wait("3")

        print(name[i] + '\t' + username[i] + '\t' + "开始上报")
        url="http://ehall.seu.edu.cn/qljfwapp3/sys/lwWiseduElectronicPass/index.do?t_s=1600149095335&amp_sec_version_=1&gid_=bjBib2hPR3hLSU4vdHRaK2oyd1o1ay9YcE4rUXBZN3owQ0hvMjkrR1dDcmUxdnBTZnliTnUvaEFRcjBZVVZqY0lsZXR4UnI3T2pON3JmTE1pQktXQmc9PQ&EMAP_LANG=zh&THEME=indigo"
        driver.get(url)
        time.sleep(15)

        checkUrl = driver.current_url
        if not checkUrl.startswith("http://ehall.seu.edu.cn/"):
            driver.find_element_by_xpath('//*[@id="username"]').send_keys(username[i])
            driver.find_element_by_xpath('//*[@id="password"]').send_keys(password[i])
            driver.find_element_by_xpath('//*[@id="casLoginForm"]/p[5]/button').click()
        time.sleep(50)
        
        checkUrl = driver.current_url
        if not checkUrl.startswith("http://ehall.seu.edu.cn/"):
            print("登录失败")
            msg += name[i]+'\t登录失败' + '\n\n'
            driver.quit()
            continue
    
        print("成功登录") 

        driver.find_element_by_xpath('/html/body/main/article/section/div[2]/div[1]').click()
        time.sleep(15)

        if '你现在暂时不满足申请条件，若有疑问请联系院系辅导员。' in driver.page_source:
            print('你现在暂时不满足申请条件，若有疑问请联系院系辅导员。')
            msg += name[i] + '现在暂时不满足申请条件，若有疑问请联系院系辅导员。' + '\n\n'
            driver.quit()
            continue
        
        print("添加")
        div = 14
        div_selec = 0
        for ii in range(2):
            try:
                if name[i] in tele_name:
                    driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[2]/div[2]/div[5]/div[1]/div/input').send_keys(tele[tele_name.index(name[i])])
                    time.sleep(5)
                    print('联系方式')

                if name[i] not in su:
                    driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[2]/div[2]/div[9]/div/div').click()
                    print("test")
                    time.sleep(5)
                    driver.find_element_by_xpath('/html/body/div[' + str(18 + div_selec) + ']/div/div/div/div[2]/div/div[2]').click()
                    time.sleep(5)
                    print("身份证类型")

                driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[2]/div[2]/div[19]/div/div').click()
                time.sleep(5)
                driver.find_element_by_xpath('/html/body/div[' + str(19 + div_selec) + ']/div/div/div/div[2]/div/div[2]/span').click()
                time.sleep(5)
                print("工作场所是否符合防护要求")

                driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[2]/div[2]/div[20]/div/div').click()
                time.sleep(5)
                driver.find_element_by_xpath('/html/body/div[' + str(20 + div_selec) + ']/div/div/div/div[2]/div/div[2]/span').click()
                time.sleep(5)
                print('工作人员能否做好个人防护')

                driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[3]/div[2]/div[5]/div/div').click()
                time.sleep(5)
                driver.find_element_by_xpath('/html/body/div[' + str(21 + div_selec) + ']/div/div/div/div[2]/div/div[2]/span').click()
                time.sleep(5)
                print('是否已在南京居家隔离满14天')

                driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[3]/div[2]/div[6]/div/div').click()
                time.sleep(5)
                driver.find_element_by_xpath('/html/body/div[' + str(22 + div_selec) + ']/div/div/div/div[2]/div/div[2]/span').click()
                time.sleep(5)
                print('目前身体是否健康')


                driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[4]/div[2]/div[1]/div[1]/div').click()
                time.sleep(5)
                driver.find_element_by_xpath('/html/body/div[' + str(25 + div_selec) + ']/div/div/div/div[2]/div/div/span').click()
                time.sleep(5)
                print('通行区域')

                if name[i] in su:
                    driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[4]/div[2]/div[4]/div[1]/div/input').send_keys("橘园")
                    time.sleep(5)
                    print('所到楼宇（具体到门牌号）')
                elif name[i] in si:
                    driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[4]/div[2]/div[4]/div[1]/div/input').send_keys("中山院")
                    time.sleep(5)
                    print('所到楼宇（具体到门牌号）')
                else:
                    driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[4]/div[2]/div[4]/div[1]/div/input').send_keys("无线谷")
                    time.sleep(5)
                    print('所到楼宇（具体到门牌号）')
                if name[i] in si:
                    driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[4]/div[2]/div[6]/div/div').click()
                    time.sleep(5)
                    driver.find_element_by_xpath('/html/body/div[' + str(27 + div_selec) + ']/div/div/div/div[1]/input').send_keys("到教学楼上课")
                    time.sleep(5)
                    driver.find_element_by_xpath('/html/body/div[' + str(27 + div_selec) + ']/div/div/div/div[2]/div/div[1]/span').click()
                    time.sleep(5)
                    print('申请理由')
                else:
                    driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[4]/div[2]/div[6]/div/div').click()
                    time.sleep(5)
                    driver.find_element_by_xpath('/html/body/div[' + str(27 + div_selec) + ']/div/div/div/div[1]/input').send_keys("往返无线谷")
                    time.sleep(5)
                    driver.find_element_by_xpath('/html/body/div[' + str(27 + div_selec) + ']/div/div/div/div[2]/div/div[1]/span').click()
                    time.sleep(5)
                    print('申请理由')

                now_time=datetime.datetime.now()
                driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[4]/div[2]/div[2]/div/div/div[2]/input').send_keys((now_time+datetime.timedelta(days=+1)).strftime("%Y-%m-%d 07:31:00") )
                time.sleep(5)
                print('通行开始时间')
                driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[4]/div[2]/div[3]/div/div/div[2]/input').send_keys((now_time+datetime.timedelta(days=+1)).strftime("%Y-%m-%d 21:59:00") )
                time.sleep(5)
                print('通行结束时间')

                if name[i] in su:
                    driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[1]/div/div[4]/div[2]/div[10]/div/div').click()
                    time.sleep(15)
                    driver.find_element_by_xpath('/html/body/div[' + str(28 + div_selec) + ']/div/div/div/div[2]/div/div[2]').click()
                    time.sleep(15)
                    print('苏康码是否为绿码')

                    driver.find_element_by_xpath('//*[@id="emapForm"]/div/div[4]/div[2]/div[11]/div[1]/div/div[2]/div/div/input').send_keys(pic[su.index(name[i])])
                    time.sleep(15)
                    print('上传苏康码')

                
                driver.find_element_by_xpath('/html/body/div[' + str(div) + ']/div/div[1]/section/div[2]/div[1]/div[1]/button[1]/span').click()
                time.sleep(5)
                if ('存在可用通行' in driver.page_source):
                    print('存在可用通行证，不可重复提交！')
                    msg += name[i]+'\t存在可用通行证，不可重复提交！' + '\n\n'
                    driver.quit()
                    break
                driver.find_element_by_xpath('/html/body/div[' + str(29) + ']/div[1]/div[1]/div[2]/div[2]/a[1]').click()
                print('提交')
                time.sleep(5)
                print('入校申请成功' + '\n\n')
                msg += name[i]+'\t入校申请成功' + '\n\n'
                driver.quit()
                break  
            except Exception as e:
                print(str(e))
                if(div == 15):  
                    if("/html/body/div[18]" in str(e) ):
                        msg += name[i]+'\tBUG' + '\n\n' + str(e) + '\n\n'
                    else:
                        msg += name[i]+'\t入校申请失败' + '\n\n' + str(e) + '\n\n'
                    print("入校申请失败")
                    driver.quit()
                    break
                div = 15

if __name__ == '__main__':
    main()
    #  Server酱key 微信推送部分
    # sckey = '' # Server酱key  详见http://sc.ftqq.com/3.version
    # posturl = 'https://sc.ftqq.com/' + sckey + '.send'
    # d = {'text':subject, 'desp':msg}
    # r = requests.post(posturl,data=d)
    # print(r.text)
