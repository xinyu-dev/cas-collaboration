"""
JournalNewsPrep.py
Author: X Yu, Meng Wu
Date: 7-17-20
Description: Pre-processing data generating the template for "journal news announcement" emails. Most of these elements do not neeed to be modified often.
"""

from pathlib import Path
from datetime import date
import bs4

class JournalNews():
    """
    Blue print for contents of journal news announcement
    """
    def __init__(self, date, title, editor_notes, figure_caption, url, main_text, add_notes_title, add_notes_text):
        """
        create instance of the journal_news. Each argument is an element in the html that we need to modify.
        :param date: STR, date in YYYY-MM-DD format
        :param title: STR, title
        :param editor_notes: STR, editor's notes paragraph. FORMATTING SHOULD FOLLOW HTML SYTLE, e.g. using <b></b> for bold. COMPRESS html code.
        :param figure_caption: STR, figure caption
        :param url: STR, url of the article on on Oxford U press
        :param main_text: STR, main text (usually an abstract of the article). FORMATTING SHOULD FOLLOW HTML SYTLE COMPRESS html code.
        :param add_notes_title: STR, title for the note section.
        :param add_notes_text: STR, main text for the note section. FORMATTING SHOULD FOLLOW HTML SYTLE. COMPRESS html code.
        """
        self.date=date
        self.title=title
        self.editor_notes=editor_notes
        self.figure_caption=figure_caption
        self.url=url
        self.main_text=main_text
        self.add_notes_title=add_notes_title
        self.add_notes_text=add_notes_text

    def getJournalNews(self, template_soup):
        """
        Main function that adds the above fields above to the template

        :param template_soup: bs4 soup object of the original template
        :return: bs4 soup object containing the html code of the modified template
        """
        pass

    def writeJournalNews(self, modified_soup, fn):
        """
        Write the output bs4 object from `getJournalNews()` to file;
        :param modified_soup: bs4 soup object containing the html code of the modified template. Generally, this is the output of the getJournalNews function
        :param fn: STR, file name (do NOT include .txt)
        :return: None. Output will be written to 'output\' folder
        """

        # use formatter=None
        soup = modified_soup.prettify(formatter=None)
        with open(Path.cwd().parent.joinpath("output", str(date.today()) + ' ' + fn + '.txt'), "w") as f:
            f.write(soup)



