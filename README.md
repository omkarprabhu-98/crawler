# SPRING 2022 Georgia Tech | CS 6675 | HW1 | Web Crawler

## Files:
- scrape.py: Web crawler written using [Scrapy](https://docs.scrapy.org/en/latest/)
- data_< i >.json: relevant metric pulled from the crawler for < i > no. of links
<!-- - colly_crawler:  -->

## Installation
1. Install Rust for cryptography package required by Scrapy
    ```
    https://rustup.rs
    ```

2. Installing cryptography 
    ```
    pip3 install cryptography
    ```
    May be required to do this: https://stackoverflow.com/questions/66035003/installing-cryptography-on-an-apple-silicon-m1-mac 

3. Install nltk, Beautifulsoup
    ```
    pip3 install nltk BeautifulSoup4
    ```

4. Update pip if needed
    ```
    python3 -m pip install --upgrade pip
    ```

5. Install Scrapy
    ```
    pip3 install Scrapy
    ```

5. Install SQLite
    ```
    brew install sqlite 
    ```

6. Install matplotlib, 
    ```
    pip3 install matplotlib
    ```


## Usage

1. Set max links variable in `scrape.py`
2. Run
    ```
    python3 -m scrapy runspider scrape.py 
    ```
2. Note relevant metric into data_.json files. To plot use
    ```
    python3 plot.py
    ```

## References
- https://github.com/pjcalvo/pjcalvo.github.io/blob/master/samples/web-crawler/script.py
- https://docs.python.org/3/library/sqlite3.html
- https://www.educative.io/edpresso/how-to-plot-graphs-using-json-files-in-python