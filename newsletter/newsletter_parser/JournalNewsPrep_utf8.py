"""
JournalNewsPrep.py
Author: X Yu, Meng Wu
Date: 7-17-20
Description: Pre-processing data generating the template for "journal news announcement" emails. Most of these elements do not neeed to be modified often.
"""

from pathlib import Path
from datetime import date
from bs4 import BeautifulSoup

class JournalNews():
    """
    Blue print for contents of journal news announcement
    """
    def __init__(self, date, title, editor_notes, article_img_url, figure_caption, url, main_text, add_notes_title, add_notes_text):
        """
        create instance of the journal_news. Each argument is an element in the html that we need to modify.
        :param date: STR, date in YYYY-MM-DD format
        :param title: STR, title
        :param editor_notes: STR, editor's notes paragraph. FORMATTING SHOULD FOLLOW HTML SYTLE, e.g. using <b></b> for bold. COMPRESS html code.
        :param article_img_url: STR, url of the cover image of the article
        :param figure_caption: STR, figure caption
        :param url: STR, url of the article on on Oxford U press
        :param main_text: STR, main text (usually an abstract of the article). FORMATTING SHOULD FOLLOW HTML SYTLE COMPRESS html code.
        :param add_notes_title: STR, title for the note section.
        :param add_notes_text: STR, main text for the note section. FORMATTING SHOULD FOLLOW HTML SYTLE. COMPRESS html code.
        """
        self.date=date
        self.title=title
        self.editor_notes=editor_notes
        self.article_img_url=article_img_url
        self.figure_caption=figure_caption
        self.url=url
        self.main_text=main_text
        self.add_notes_title=add_notes_title
        self.add_notes_text=add_notes_text
        self.html_template="templates/New Article Alert.html"

    def getJournalNews(self):
        """
        Main function that adds the above fields above to the template
        :return: a feature in the object containing the html code of the modified template
        """
        with open(self.html_template) as fp:
            self.modified_html = BeautifulSoup(fp, "html.parser")

        self.modified_html.find(id='date').string = self.date
        self.modified_html.find(id='title').string = self.title
        self.modified_html.find(id='editor_notes').string = self.editor_notes
        self.modified_html.find(id='article-img-url')['src'] = self.article_img_url
        self.modified_html.find(id='figure_caption').string = self.figure_caption
        self.modified_html.find(id='url')['href'] = self.url
        self.modified_html.find(id='main_text').string = self.main_text
        self.modified_html.find(id='add_notes_title').string = self.add_notes_title
        self.modified_html.find(id='add_notes_text').string = self.add_notes_text

    def writeJournalNews(self, fn):
        """
        Write the output bs4 object from `getJournalNews()` to file;
        :param fn: STR, file prefix name (do NOT include .txt/.html)
        :return: None. Output will be written to 'output\' folder
        """

        # use formatter=None
        soup = self.modified_html.prettify(formatter=None)
        with open(("output"+ str(date.today()) + ' ' + fn + '.html'), "w") as f:
        #with open(Path.cwd().joinpath("output", str(date.today()) + ' ' + fn + '.html'), "w") as f:
            f.write(soup.encode("utf-8"))



