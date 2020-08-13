def freq_of_word(text):
    text =text.split()
    str=[]
    for i in text:
        if i not in str:
            str.append(i)
    for i in range(0, len(str)):
        text.sort()
        max_length= max(len(text) for word in text)
        print("{:{}}:{}".format(str[i], max_length, text.count(str[i])))





def main():
    text=str(input("Enter your text: "))
    freq_of_word(text)


main()