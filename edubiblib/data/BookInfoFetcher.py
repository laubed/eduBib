import urllib2
import json


class BookInfoFetcher(object):
    """
    Book fetcher class.
    Used to get info about a book with a given ISBN
    """
    def __init__(self):
        self.url = "https://www.googleapis.com/books/v1/volumes?q=isbn:%s"

    def getBookInfo(self, isbn):
        """
        Fetches book data with given ISBN, returns a dict with all relevant data
        :param isbn:
        :return: dic with all relevant data
        """
        raw_data = urllib2.urlopen(url=self.url % (str(isbn),)).read()
        json_data = json.loads(raw_data)
        raw_info = json_data["items"][0]["volumeInfo"]
        #print raw_info
        info = {
            "title" : raw_info["title"],
            "subtitle" : raw_info["subtitle"],
            "author" : raw_info["authors"],
            "isbn" : str(isbn),
            "thumbnail" : raw_info["imageLinks"]["thumbnail"]

            #"publisher" : raw_info["publisher"]
        }
        return info

if __name__ == "__main__":
    # Just test code
    b = BookInfoFetcher()
    print b.getBookInfo("9783507879201")