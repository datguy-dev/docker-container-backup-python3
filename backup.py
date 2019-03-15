#!/usr/bin/python3
import sh, tarfile, os
import datetime

#images will be archived and then combined
#into a single gz archive. this is the first
#part of the filename of that file. enter
#any value
GZ_NICKNAME='rt'

containers_to_backup = [
    [
        'xxxxxxxxx', #containers info see "docker images"
        'xxxx' #any nickname you wish
    ],
    [
        'xxxxxxxxx', #containers info see "docker images"
        'xxxxx' #any nickname you wish
    ],
    #add more?
]
ADDITONAL_FILES= [
    '/home/xx/xxxxxxxx/', #add any additional things to be archived
]

BACKUP_WORKING_DIR='/home/xxxx/xxxx/' #the full backup archive ends up here
BACKUP_TEMP_DIR='/home/xxx/xxxx/temp/' #these are used to create ^ and will be deleted.

###
####
###

archives=[]
try:
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date = date.replace('-','_')
    date = date.replace(' ','_')
    DATE = date.replace(':','-')
    print('date: {0}'.format(date))
except Exception as e:
    print('date error in backup: \n\n{0}'.format(e))
    quit(1)


def make_archive():
    main_archive = '{0}{1}_{2}.tar.gz'.format(BACKUP_WORKING_DIR, GZ_NICKNAME, DATE)
    gzfile = tarfile.open(main_archive, 'w:gz')

    for f in ADDITONAL_FILES:
        #included additional files/dirs to archive
        archives.append(f)
    for tar in archives:
        gzfile.add(tar)
        print('\tomitting {0} to {1}'.format(tar, main_archive))
    gzfile.close()

    for f in os.listdir(BACKUP_TEMP_DIR):
        os.remove('{0}{1}'.format(BACKUP_TEMP_DIR,f))
        print('\tdeleted temp tar archive:{0}'.format(f))

    if os.path.isfile(main_archive):
        print('successfully created backup -> {0}'.format(main_archive))
    else:
        print('error creating archive. {0}'.format(main_archive))

def docker_commit(cont_dic):
    for c in cont_dic:
        c_name = c[0]
        c_nick = c[1]
        try:
            sh.docker('image', 'rm', c_nick)
            print('\tremoved image: {0} while commiting new image'.format(c_nick))
        except:
            pass
        print('\tdocker commit: container: {0} to image: {1}'.format(c_name,c_nick))
        sh.docker('commit', '-p', c_name, c_nick)
    print()
    print(sh.docker('images'))


def docker_save(cont_dic):
    for c in cont_dic:
        c_nick = c[1]
        #write images to a temporary directory and combine them into a single archive
        c_full_path = '{0}{1}_{2}.tar'.format(BACKUP_TEMP_DIR, c_nick, DATE)
        print('\tdocker save: (this will take awhile...) \n\t\tfile: {0} <- image: {1}'.format(c_full_path,c_nick))
        archives.append(c_full_path)
        sh.docker('save', '-o', c_full_path, c_nick)


def main():
    print('starting backup routine')
    docker_commit(containers_to_backup)
    docker_save(containers_to_backup)
    make_archive()
    print('done')


if __name__ == '__main__':
    main()
else:
    quit(1)
