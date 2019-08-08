import requests
import json

def api():
    url = "https://api.exchangeratesapi.io/latest?symbols=USD,GBP"

    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    date = parsed["date"]

    gbp_rate = parsed["rates"]["GBP"]
    usd_rate = parsed["rates"]["USD"]
    print("On " + date + " EUR equals " + str(gbp_rate) + " GBP")
    print("On " + date + " EUR equals " + str(usd_rate) + " USD")

def api():
    url= "http://api.exchange.io/latest?id=001"

    response =requests.get(url)
    data = json.loads(response.content)

    date = data['date']

    rate = data['rate']['usd']

    print("on")
def file():
    # Open the file with read only permit
    f = open('word.txt', "r")
    # use readlines to read all lines in the file
    # The variable "lines" is a list containing all lines in the file
    lines = f.readlines()
    print(lines)
    # close the file after reading the lines.
    f.close()
def file():
    f = open("word.text", "r")
    lines = f.readlines()

    f.close()


def file2():
    # Open the file with read only permit
    f = open('my_text_file.txt')
    # use readline() to read the first line
    line = f.readline()
    # use the read line to read further.
    # If the file is not empty keep reading one line
    # at a time, till the file is empty
    while line:
        # in python 2+
        # print line
        # in python 3 print is a builtin function, so
        print(line)
        # use realine() to read next line
        line = f.readline()
    f.close()

    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    f.close()

def file3():
    with open("word.txt", 'r') as fh:
        all_lines = fh.readlines()




if __name__ == '__main__':
    file()
