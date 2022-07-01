from typing import Union
from pathlib import Path
import json
from collections import Counter
import pdb
from webbrowser import get
import argparse
from loguru import logger

from hazm import word_tokenize, Normalizer
from wordcloud import WordCloud
from bidi.algorithm import get_display
import arabic_reshaper
from src.data import DATA_DIR


class ChatStatistics:
    
    """ 
    
    generate chat statistics from telegarm chat json file
    
    
    """
    
    def __init__(self, path_json : Union[str, Path]):
        
        """
        
        initializing (get data from jsonfile and normilize)
        
        Args :
        
            path_json : path to telegram json file
            
        returns :
        
            no return 
        
        """
        
        with open(path_json) as f:
            
            self.chat_json = json.load(f)
            
            self.normalizer = Normalizer()
            
    def generate_word_cloud(self,  output_dir : Union[str, Path], Persian = True):
        
        """
        
        generates word cloud from chat data
        
        Args :

            Persian : treat data as persian language or not (False means any language other than persian )
        
            output_dir : where to drawen word cloud to be stored
            
        returns :
        
            no return 
        
        """
        
        text_content = ""

        for msg in self.chat_json["messages"]:
            
            if type(msg["text"]) is str:
                
                text_content += msg["text"]
                
            elif type(msg["text"]) is list:
                
                for sub_msg in msg["text"]:

                    if type(sub_msg) is dict:
                        
                        text_content += sub_msg["text"]
                        
                    elif type(sub_msg) is str:
                    
                        text_content += sub_msg
        
        word_cloud_list = self.purify_text(text_content = text_content)
        
        text_content = " ".join(word_cloud_list)

        if Persian:
        
            text = arabic_reshaper.reshape(text_content)

            text = get_display(text)
        
        wordcloud = WordCloud(
                font_path=str(DATA_DIR / "font.ttf"), 
                background_color="white",
                width=1200,
                height=1200).generate(text)
        
        wordcloud.to_file(Path(output_dir) / "wordcloud.png")
        
    
    def read_stop_words(self, file_name : str):
        
        """
        
        read stepwords to remove those from our main data
        
        Args :
        
            file_name  : stepwords file name with extension
            
        returns :
        
            stopwords : stepwords read from text file for spesific language
        
        """
        
        stopwordsPersian = DATA_DIR / file_name
        
        stopwords = open(stopwordsPersian).readlines()

        stopwords = list(map(str.strip, stopwords))
        
        stopwords = list(map(lambda x : self.normalizer.normalize(x), stopwords))
        
        return stopwords
    
    
    def purify_text(self, text_content):
        
                
        """
        
        clean our data based on stepwords we have got
        
        Args :
        
            text_content  : main data to apply wordcloud on that
            
        returns :
        
            word_cloud_list : list of words extracted from main text which are bieng selected wrt stepwords
        
        """
        
        text_content = self.normalizer.normalize(text_content)
        
        tokens = Counter(word_tokenize(text_content)).most_common()
        
        stop_words_persian, stop_words_english = self.read_stop_words("stopwords_per.txt"), self.read_stop_words("stopwords_en.txt")

        word_cloud_list = []
        
        for word, num_occur in tokens:
        
            if word not in stop_words_persian:

                if word in stop_words_english:

                    continue
                
                lst_words = list(word)
                
                if "\u200c" in list(lst_words):
                    
                    continue
                    
                if "." in lst_words:
                    
                    index = lst_words.index(".")
                    
                    word = word[:index]
                    
                if word.isdigit():
                    
                    continue
                    
                if Counter(lst_words)["\\"] >= 1:
                    
                    continue
                    
                if lst_words[0] in stop_words_english or lst_words[-1] in stop_words_english:
                    
                    continue
                    
                if num_occur <= 10:
                    
                    continue
                
                word_cloud_list.append(word)
                
        return word_cloud_list
        
        
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    
    #bfs
    
    parser.add_argument("--Persian", action = "store_false", help='treat data as persian or not')
    
    # parse args
    
    args = parser.parse_args()
    
    chat_stats = ChatStatistics(path_json = DATA_DIR / "data.json")
    
    chat_stats.generate_word_cloud(output_dir=DATA_DIR, Persian=args.Persian)
    
    print("Done!")
    