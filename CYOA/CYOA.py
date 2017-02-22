#if you open your ipython session in the same dir as your .py file you can just hit
#run filename.py and it will run the program

def parse_cyoa_to_dict(path_to_text_file, startsection=100):

    file_line_reader = open(path_to_text_file)
    #file_line_reader.readlines() puts all file into a list
    #file_line_reader.readline() reads first line
    #file_line_reader.close()  #closes the open connection



    #should have done this, make sure indent below
    #with open(path_to_textfile) as file_line_reader

    #for line in file_line_reader:
    #    print line,  #the comma makes it look better by elminating the stuff like /n

    parsed_cyoa={}
    section=100
    current_chunk = [] #don't want to do sets because we'll lose order
    for line in file_line_reader:
        if line== str(section)+' \n': #we noticed this with the readlines command
            parsed_cyoa[section-1]=current_chunk
            section+=1
            current_chunk=[] #empty it

        else:
            #save the opening chunk
            current_chunk.append(line)
    file_line_reader.close()
    return parsed_cyoa

def pretty_print(parsed_cyoa, key):
    for line in parsed_cyoa[key]:
        print line,
#'/Users/kevinweiler/Desktop/Data_Science/Class6/Stories/narnia.txt'

#assign variable to the first function to pass into the second funtion
#parsed_narnia_story=parse_cyoa_to_dict('Stories/narnia.txt')
#run the pretty print function pretty_print(parsed_narnia_story,100)

def adventure(path_to_text_file,start_key=99):

    parsed_cyoa = parse_cyoa_to_dict(path_to_text_file, startsection=start_key+1)

    pretty_print(parsed_cyoa,start_key)

    while True:
        section=raw_input("Please choose your destination: ")
        if section.isdigit():
            pretty_print(parsed_cyoa,int(section))


if __name__ == '__main__':
    adventure("Stories/narnia.txt")
    #this is used for use only in the command line
    #this also allows it to be imported in ipython without automatically run

#import cyoa will import it like numpy so we can call on it
    #import cyoa.pretty_print
