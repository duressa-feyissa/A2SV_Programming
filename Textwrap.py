import textwrap

def wrap(string, max_width):
    wraptext=""
    count=0
    for index in range(len(string)):
        if count == max_width:
            print(wraptext)
            wraptext=string[index]
            count = 1
            if index == len(string) - 1:
                break
        else:
            count+=1
            wraptext+=string[index]
    return wraptext
            
            
if __name__ == '__main__':
