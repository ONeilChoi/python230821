# ChatGPT Crolling 01

import requests
from bs4 import BeautifulSoup

def crawl_blog_info(search_keyword):
    url = f"https://search.naver.com/search.naver?where=nexarch&sm=top_hty&fbm=0&ie=utf8&query={search_keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    blog_info_list = []

    blog_entries = soup.find_all("li", class_="sh_blog_top")
    for entry in blog_entries:
        blog_name = entry.find("a", class_="sh_blog_title").text
        blog_post_address = entry.find("a", class_="sh_blog_title")["href"]
        post_date = entry.find("span", class_="txt_inline").text
        
        blog_info = {
            "blog_name": blog_name,
            "blog_post_address": blog_post_address,
            "post_date": post_date
        }
        blog_info_list.append(blog_info)

    return blog_info_list

if __name__ == "__main__":
    search_keyword = "맥북에어"
    blog_info_list = crawl_blog_info(search_keyword)
    
    for blog_info in blog_info_list:
        print("Blog Name:", blog_info["blog_name"])
        print("Blog Post Address:", blog_info["blog_post_address"])
        print("Post Date:", blog_info["post_date"])
        print("=" * 50)
