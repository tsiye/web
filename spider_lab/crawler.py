# -*- coding: utf-8 -*-
#encoding:utf-8

import sys
import re
import gevent
import requests
from bs4 import BeautifulSoup
from mydb import Data 
from myengine import new_headers

#get the every child url
def get_link(url, mysession):
    content = mysession.get(url).text
    results_ori = re.findall('normalthread_\d+', content)
    results = []
    for url in results_ori:
        id = url.split('_')[1]
        results.append("https://www.1point3acres.com/bbs/thread-" + id + "-1-1.html")
    return results
#get the content under"点击查看"
def get_hidden(td_list):
    a = td_list.find("a")
    if "onclick" in a.attrs:
        info = a["onclick"]
        #print(info)
    fra = info.split("'")[1]
    url = "https://www.1point3acres.com/bbs/" + fra
    text = requests.get(url, headers = new_headers).text
    res = str(re.findall(r'\[(.*?)\]', text)).split("'")[1][6:]
    return res 
    

def get_data_from_bbs(url, mysession):
    #tid = re.findall("tid=\d+",url)[0].split('=')[1]
    tid = str(url).split('-')[1]
    print(tid)
    text = mysession.get(url, headers = new_headers).text
    soup = BeautifulSoup(text, features = "lxml")
    table_list = soup.find_all("table")

    for item in table_list:
        if "summary" in item.attrs:
            if "分类信息" in item["summary"]:
                personal_information = item
    
    i = 0
    td_list = personal_information.find_all("td")
    #print(td_list)
    #print('\n')
    #print(personal_information.find_all("th"))
    for item in personal_information.find_all("th"):
        if item.get_text() == "申入学年度:":
            application_year = td_list[i].get_text().strip()
        if item.get_text() == "入学学期:":
            start_term = td_list[i].get_text().strip()
        if item.get_text() == "专业:":
            profession = td_list[i].get_text().strip()
        if item.get_text() == "学位:":
            degree =  td_list[i].get_text().strip()
        if item.get_text() == "全奖/自费:":
            pay = td_list[i].get_text().strip()
        if item.get_text() == "提交时间:":
            submission_time = td_list[i].get_text().strip()
        if item.get_text() == "申请结果:":
            application_result = td_list[i].get_text().strip()
        if item.get_text() == "学校名称:":
            school = td_list[i].get_text().strip()
        if item.get_text() == "通知时间:":
            notice_time = td_list[i].get_text().strip()
        if item.get_text() == "个人其他信息:":
            other_information = td_list[i].get_text().strip()
        if item.get_text() == "本科学校档次:":
            undergraduate_school = td_list[i].get_text().strip()
        if item.get_text() == "本科学校名称:":
            if td_list[i].get_text().strip() == "点击查看":
                undergraduate_school_name = get_hidden(td_list[i])
            else: 
                undergraduate_school_name = td_list[i].get_text().strip()
        if item.get_text() == "本科专业:":
            if td_list[i].get_text().strip() == "点击查看":
                undergraduate_profession = get_hidden(td_list[i])
            else: 
                undergraduate_profession = td_list[i].get_text().strip()
        if item.get_text() == "本科成绩和算法，排名:":
            if td_list[i].get_text().strip() == "点击查看":
                undergraduate_grades = get_hidden(td_list[i])
            else: 
                undergraduate_grades = td_list[i].get_text().strip()
        if item.get_text() == "研究生学校档次:":
            graduate_grade = td_list[i].get_text().strip()
        if item.get_text() == "研究生学校名称:":
            if td_list[i].get_text().strip() == "点击查看":
                graduate_school = get_hidden(td_list[i])
            else: 
                graduate_school = td_list[i].get_text().strip()
        if item.get_text() == "研究生专业:":
            if td_list[i].get_text().strip() == "点击查看":
                graduate_profession = get_hidden(td_list[i])
            else: 
                graduate_profession = td_list[i].get_text().strip()
        if item.get_text() == "研究生成绩和算法，排名:":
            if td_list[i].get_text().strip() == "点击查看":
                graduate_grades = get_hidden(td_list[i])
            else: 
                graduate_grades = td_list[i].get_text().strip()
        if item.get_text() == "T单项和总分:":
            if td_list[i].get_text().strip() == "点击查看":
                toefl = get_hidden(td_list[i])
            else: 
                toefl = td_list[i].get_text().strip()
        if item.get_text() == "G单项和总分:":
            if td_list[i].get_text().strip() == "点击查看":
                gre = get_hidden(td_list[i])
            else: 
                gre = td_list[i].get_text().strip()
        if item.get_text() == "sub专业和分数:":
            if td_list[i].get_text().strip() == "点击查看":
                sub_grades = get_hidden(td_list[i])
            else: 
                sub_grades = td_list[i].get_text().strip()
        if item.get_text() == "背景的其他说明（如牛推等）:":
            if td_list[i].get_text().strip() == "点击查看":
                other_bg = get_hidden(td_list[i])
            else: 
                other_bg = td_list[i].get_text().strip()
       
        i = i + 1
    print(application_year, start_term, profession, degree, pay, submission_time, application_result, school, notice_time, undergraduate_school, undergraduate_school_name, undergraduate_profession, undergraduate_grades, graduate_grade, graduate_school, graduate_profession, graduate_grades, toefl, gre, sub_grades, other_bg)

    new_data = Data(
        tid = tid,
        application_year = application_year,
        start_term = start_term,
        profession = profession,
        degree = degree,
        pay = pay,
        submission_time = submission_time,
        application_result = application_result,
        school = school,
        notice_time = notice_time,
        undergraduate_school = undergraduate_school,
        undergraduate_school_name = undergraduate_school_name,
        undergraduate_profession = undergraduate_profession,
        undergraduate_grades = undergraduate_grades,
        graduate_grade = graduate_grade,
        graduate_school = graduate_school,
        graduate_profession = graduate_profession,
        graduate_grades = graduate_grades,
        toefl = toefl,
        gre = gre,
        sub_grades = sub_grades,
        other_bg = other_bg
        )
    duplicate = Data.objects(application_year = new_data.application_year, gre = new_data.gre)
    #if len(duplicate) > 0 :
    #    print("duplicate!")
    #    return
    new_data.save()

if __name__ == "__main__":
    mysession = requests.session()
    get_data_from_bbs("https://www.1point3acres.com/bbs/thread-479105-1-1.html",mysession)
