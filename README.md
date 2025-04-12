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
