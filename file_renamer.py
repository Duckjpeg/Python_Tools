import os

folder = "D:/Photos back up/photos/raw/2026/Cayman summer 2026"
files = os.listdir(folder)

start = 4 #Not set up currently
prefix='_HS_KY_' #What the filename begins with

index = 1 #initial number e.g. 00001


print(f'files selected:{files}')
proceed = input(f'enter yes if you wish to proceed an rename all the files above to have the new name of {prefix}... :\n')

print('processing\n'+'-'*50)
i=0
threshold = 10
if proceed == 'yes':
    for file in files:
        extension = file.rsplit('.',1)[1] #Gets the correct file extension
        newName = prefix+str('{:05d}'.format(index))+'.'+extension # prefix + index to 5 + file extension
        os.rename(f'{folder}/{file}',f'{folder}/{newName}')

        #if file[0:start] != prefix:
        #else:
            #print('prefix already in use')
        #Just for progress
        percent = (i / len(files)) * 100
        if percent >= threshold:
            print(f"{threshold}%")
            threshold += 10
        i+=1
        index+=1

print('100% \ncomplete')
print('total is :',index)