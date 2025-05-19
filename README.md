# cji101

## Web Crawler
- slide
    > https://docs.uuboyscy.dev/docs/category/web-crawler
- sample code
    > https://github.com/uuboyscy/course-PyETL

## Selector
- id: #
- class: .
- `<a class="right small" href="/about.html">關於我們</a>`
  - a.right.samll
- `<div id="topbar" class="bbs-content">`
  - div#topbar.bbs-content

## Payload
- How browser collect data
  - attached on url, e.g. url?arg=1&arg=2
    - > QueryString parameters
  - By POST
    - > Form data

## Project Management
### Poetry
- poetry init
  - Type `n` to skip author section
  - Project name can not contain "blank"
  - `poetry install` to set up virtual environment
  - `poetry add <package_name>` to install new packages
  - If VSCode cannot recognize virtual environment, execute `poetry env info` to find executable

### 20250419
1. Setup environment Poetry
2. Install `requests` and `BeautifulSoup`
3. Usage of packages
4. PTT (static web) for example
    - Crawl titles and links
    - Multiple pages
    - Crawl article content
    - Load to file
5. Dynamic web page
6. Pandas
https://docs.uuboyscy.dev/docs/category/pandas-tutorial

### When to use `GET`/`POST`
- requests.post(data=data<Form data>, json=json<request payload>)
- Form data example
  - https://github.com/uuboyscy/course-PyETL/blob/main/part03_requestWithPost/04_organic_gov.ipynb

## Note
- [Flask 20250510](note/flask-20250510.md)
- [ETL 20250518](note/etl-20250518.md)
