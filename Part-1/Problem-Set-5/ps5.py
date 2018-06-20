# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid
        
    def get_title(self):
        return self.title
        
    def get_description(self):
        return self.description
        
    def get_link(self):
        return self.link
        
    def get_pubdate(self): 
        return self.pubdate
        
#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
        
    def is_phrase_in(self, text):
        self.phrase = self.phrase.lower()
        copy_phrase = self.phrase.split()
        text = text.lower()
        for char in text:
            if char in string.punctuation:
                text = text.replace(char, ' ',1)
        text = text.split()
        
        words_found = 0
        if copy_phrase[0] not in text or len(text) < len(copy_phrase):     
            return False
        else:
            words_found += 1
            index = text.index(copy_phrase[0])
            if(len(text) - (index + 1)) < len(copy_phrase) - 1:
                return False
            for i in range(1, len(copy_phrase)):
                if copy_phrase[i] == text[i + index]:
                    words_found += 1
                else:
                    return False
        if words_found == len(copy_phrase):
            return True
                
# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())
# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, string_EST):
        try:
            datetime.strptime(string_EST, "%d %b %Y %H:%M:%S")
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        self.time = datetime.strptime(string_EST, "%d %b %Y %H:%M:%S").replace(tzinfo = pytz.timezone("EST"))
# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, string_EST):
        TimeTrigger.__init__(self, string_EST)
    def evaluate(self, story):  
        return story.get_pubdate().replace(tzinfo = pytz.timezone("EST")) < self.time
    
class AfterTrigger(TimeTrigger):
    def __init__(self, string_EST):
        TimeTrigger.__init__(self, string_EST)
    def evaluate(self, story):
        return story.get_pubdate().replace(tzinfo = pytz.timezone("EST")) > self.time
# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, otherTrigger):
        self.otherTrigger = otherTrigger
    def evaluate(self, story):
        return not self.otherTrigger.evaluate(story)
    
# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, otherTrigger, anotherTrigger):
        self.otherTrigger = otherTrigger
        self.anotherTrigger = anotherTrigger
    def evaluate(self, story):
        return self.otherTrigger.evaluate(story) and self.anotherTrigger.evaluate(story)
  
# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, otherTrigger, anotherTrigger):
        self.otherTrigger = otherTrigger
        self.anotherTrigger = anotherTrigger
    def evaluate(self, story):
        return self.otherTrigger.evaluate(story) or self.anotherTrigger.evaluate(story)
  

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    fired_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                fired_stories.append(story)
                break
    return fired_stories        
    



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    all_triggers = {}
    list_lines = []
    for line in lines:
        list_lines.append(line.split(','))      
               
    for line in list_lines:
        if line[0] != 'ADD':            
            line_as_dict = {}
            line_as_dict['triggerType'] = line[1]
            line_as_dict['argumentslist'] = line[2:]
            all_triggers[line[0]] = line_as_dict
        
        triggers_list_dict = {}
    for trigger_name in all_triggers.keys():
        if all_triggers[trigger_name]['triggerType'] == 'TITLE':
            triggers_list_dict[trigger_name] = TitleTrigger(all_triggers[trigger_name]['argumentslist'][0])
        elif all_triggers[trigger_name]['triggerType'] == 'DESCRIPTION': 
            triggers_list_dict[trigger_name] = DescriptionTrigger(all_triggers[trigger_name]['argumentslist'][0])
        elif all_triggers[trigger_name]['triggerType'] == 'AFTER': 
            triggers_list_dict[trigger_name] = AfterTrigger(all_triggers[trigger_name]['argumentslist'][0])
        elif all_triggers[trigger_name]['triggerType'] == 'BEFORE': 
            triggers_list_dict[trigger_name] = BeforeTrigger(all_triggers[trigger_name]['argumentslist'][0])
            
    for trigger_name in all_triggers.keys():
        if all_triggers[trigger_name]['triggerType'] == 'NOT':
            triggers_list_dict[trigger_name] = NotTrigger(triggers_list_dict[all_triggers[trigger_name]['argumentslist'][0]])
        elif all_triggers[trigger_name]['triggerType'] == 'AND': 
            triggers_list_dict[trigger_name] = AndTrigger(triggers_list_dict[all_triggers[trigger_name]['argumentslist'][0]], \
                                                    triggers_list_dict[all_triggers[trigger_name]['argumentslist'][1]])
        elif all_triggers[trigger_name]['triggerType'] == 'OR': 
            triggers_list_dict[trigger_name] = OrTrigger(triggers_list_dict[all_triggers[trigger_name]['argumentslist'][0]], \
                                                    triggers_list_dict[all_triggers[trigger_name]['argumentslist'][1]])
    triggers_list = []
    for trigger_name in triggers_list_dict.keys():
        triggers_list.append(triggers_list_dict[trigger_name])
                
    return triggers_list


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

