import xlrd
import nltk
from nltk.corpus import stopwords
from string import punctuation
stopwords = set(stopwords.words('english') + list(punctuation))
stopwords.add('This')
# nltk.download('punkt')
# nltk.download('stopwords')


class ReadKeywords(object):

    def __init__(self):
        self.list_key = []

    def Keywords(self, str):
        lsit_str = nltk.word_tokenize(str)
        for key in lsit_str:
            if key.lower() in stopwords:
                self.list_key.append('&')
            elif key.isupper() or key.istitle():
                self.list_key.append(key)
            else:
                self.list_key.append('&')
        return self.list_key

    def splice_Keywords(self, list):
        a = []
        for item in list:
            if len(a):
                if a[-1] != item:
                    a.append(item)
            else:
                a.append(item)
        keywords = " ".join(a).replace(' & ', '&').strip(' &')
        return keywords

    def read_execl(self):
        wb = xlrd.open_workbook(filename='2.xlsx')
        sheet1 = wb.sheet_by_index(0)
        for i in range(1, 25):
            self.list_key = []
            rows = sheet1.row_values(i)
            item = self.Keywords(rows[1])
            keywords = self.splice_Keywords(item)
            print(keywords)

    # def Summarize(self, text):
    #     # 首先分出句子
    #     sents = sent_tokenize(text)
    #
    #     word_sent = [word_tokenize(s.lower()) for s in sents]
    #
    #     # 把停用词去除
    #     for i in range(len(word_sent)):
    #         for word in word_sent[i]:
    #             if word in stopwords:
    #                 word_sent[i].remove(word)
    #
    #     for key in word_sent[0]:
    #         if key.isupper() or key.istitle():
    #             self.list_key.append(key)
    #     print(self.list_key)
    #     # print(word_sent[0])


if __name__ == '__main__':
    # aaa = "Adrian Dantley Returned To The Site Of A Legendary Prep Hoops Debacle, This Time As A Kids' Rec League Ref"
    r = ReadKeywords()
    # r.Summarize(aaa)
    r.read_execl()
