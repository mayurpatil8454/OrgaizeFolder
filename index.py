import ntpath
import shutil
import os
import glob
import time
import datetime

path ='C:\\Users\\MAYUR\\Downloads'
print(len(os.listdir(path)))
array = glob.glob(path + '\*');
print(len(array));

array.sort(key=os.path.getmtime);
modifieddates =[];
for pathindex in range(0,len(array)):
    value = datetime.datetime.strptime(time.ctime(os.path.getmtime(os.path.join(path, array[pathindex]))),
                               '%a %b %d %H:%M:%S %Y')
    value1 = value.strftime('%d-%m-%y');
    modifieddates.append(value1);
existdates =[];

for i in range(len(array)):
    if os.path.splitext(array[i])[1] == '':
        break;
    if(len(existdates) > 0):
        flag =0;
        for check in range(len(existdates)):
            if(modifieddates[i] == existdates[check]):
                getFilepath = os.path.join(path,existdates[check])
                shutil.copyfile(array[i], os.path.join(getFilepath,ntpath.basename(array[i])));
                flag =1;
                break;
        if flag == 0:
            os.mkdir(os.path.join(path, modifieddates[i]))
            getFilepath = os.path.join(path, modifieddates[i])
            shutil.copyfile(array[i], os.path.join(getFilepath, ntpath.basename(array[i])));
            existdates.append(modifieddates[i]);
    else:
        os.mkdir(os.path.join(path, modifieddates[i]))
        getFilepath = os.path.join(path,modifieddates[i] )
        shutil.copyfile(array[i], os.path.join(getFilepath, ntpath.basename(array[i])));
        existdates.append(modifieddates[i]);

print(array)