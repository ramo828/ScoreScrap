import csv

class UrlSniffer:
    def __init__(self):
        self.jsLink = ""
        self.links = []


    def dataLinks(self, linkID):
        href = ""
        if(len(linkID) > 10):
            href = f"https://analyse.7msport.com/{linkID}/index.shtml"

        return href

    def matches(self, match):
        for mch in match:
            jsLink = mch.get_attribute("href")
            jsLink = jsLink.strip("abcdefghijklmnopqrstuvxyzw:()_T")
            self.links.append(self.dataLinks(jsLink))

    def unique_values(self, data):
        return list(set(data))

    def replace_strings(self, strings_list, old_substring, new_substring):
        """
        This function takes a list of strings, an old substring to be replaced, and a new substring to replace it with.
        It then replaces the old substring with the new substring in each string in the list and returns the updated list.
        """
        updated_strings_list = []
        for string in strings_list:
            updated_string = string.replace(old_substring, new_substring)
            updated_strings_list.append(updated_string)
        return updated_strings_list

    def filter_unwanted_string(self, sentence_list, unwanted):
        filtered_sentences = []
        for sentence in sentence_list:
            if unwanted in sentence:
                continue
            else:
                filtered_sentences.append(sentence)
        return filtered_sentences

class ParserTools:
    def __init__(self):
        self.csv_counter = 0
        self.index = 0


    def write_to_csv(self, fileName="output/test.csv", *args, mode="a"):
        if(self.csv_counter > 2):
            self.index = 1
        print(len(args))
        # print(args[self.index:])
        with open(fileName, mode=mode, newline='') as csv_file:
            writer = csv.writer(csv_file)
            for i in range(len(args[self.index:])):

                writer.writerow(args[i])
        
        self.csv_counter +=1
                



    def extract1(self, data, fileName= "data.csv"):
        d = data.text.splitlines()
        label = []
        label_1 = self.split_two(d[0],2).split(",")
        for i in label_1:
            label.append(i)
        count = d[1].split(" ")
        interesting = d[2].split(" ")
     
        self.write_to_csv(fileName, label, count, interesting)
            

    def extract2(self, data1, data2, fileName = "output/totalGoals.csv"):
        label = []
        count = []

        for i in range(len(data2)):
            label.append(data1[i].text)
            count.append(data2[i])
        
        self.write_to_csv(fileName,label[1:], count[1:])

    def split_two(self, data, limit = 3):
        counter = 0
        ydata = ""
        for n in data:
            if(counter == limit):
                ydata += ","
                counter = 0
                
            if n == ' ':
                if(counter< limit):
                    ydata+= " "
                counter+=1
            else:
                ydata +=n
        return ydata.replace(" ,",",")
        
    def web_to_list(self, data):
        dataList = []
        for i in data:
            dataList.append(i.text.replace("\n"," "))
        return dataList

    def extract3(self, *args, fileName = "goals_counts.csv"):
        a1 = []
        try:
            for i in range(len(args)):
                a1.append(args[i])
        except IndexError:
            pass
        # print(a1)
        self.write_to_csv(fileName,a1[0],a1[1],a1[2],a1[3],a1[4],a1[5],a1[6],a1[7],a1[8])


class Log:
    def __init__(self):
        pass

    def write(self, logMessage:str):
        with open("log/log.txt","a") as logData:
            logData.write(logMessage)
            
