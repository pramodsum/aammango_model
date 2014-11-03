import os

#get word list file
wordlistpath = os.getcwd() + '/words'
wordlist = open(wordlistpath, 'r').readlines()

#create training fileids file
fileidspath = os.getcwd() + '/etc/aammango_train.fileids'
fileids = open(fileidspath, 'w')

#create training transcription file
promptspath = os.getcwd() + '/etc/aammango_train.transcription'
prompts = open(promptspath, 'w')

#list each test file in each subdirectory
index = 1
for x in range(5):
    for prompt in wordlist:
        # print(template_name + str(index) + '\t' + prompt)
        prompt = prompt.strip()
        for i in range(5):
            fileids.write('train/train_' + str(index) + '\n')
            prompts.write('<s> ' + prompt + ' </s> (train_' +  str(index) + ')\n')
            index = index + 1
            i = i + 1

prompts.close()
fileids.close()
