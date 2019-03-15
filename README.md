# docker-container-backup-python3
A script I use to backup my containers and archive them

### requires sh

# Directory setup example:
```
dev@node:~$ tree ./backups/
./backups/ #BACKUP_WORKING_DIR
├── rt_2019_03_14_22-45-27.tar.gz   #a backup
├── rt_backup_03_14_19_15_45_53.tar #another backup
└── temp #BACKUP_TEMP_DIR. folder used to hold temp archives

1 directory, 2 files
```


# Output:
```
dev@node:~/scripts$ sudo ./backup.py
date: 2019_03_14_22:45:27
        removed image: rt_wp while commiting new image
        docker commit: container: xxxxx_wp to image: rt_wp
        removed image: rt_db while commiting new image
        docker commit: container: xxxxx_db to image: rt_db

REPOSITORY          TAG                 IMAGE ID            CREATED                  SIZE
rt_db               latest              4556d16ca289        Less than a second ago   368MB
rt_wp               latest              7e037fe1f37f        Less than a second ago   421MB
mariadb             latest              e93652b8b80d        3 days ago               368MB
wordpress           latest              05e305efac8d        3 days ago               421MB

        docker save: (this will take awhile...)
                file: /home/xxxx/backups/temp/rt_wp_2019_03_14_22-45-27.tar <- image: rt_wp
        docker save: (this will take awhile...)
                file: /home/xxxx/backups/temp/rt_db_2019_03_14_22-45-27.tar <- image: rt_db
        omitting /home/xxx/backups/temp/rt_wp_2019_03_14_22-45-27.tar to /home/xxx/backups/rt_2019_03_14_22-45-27.tar.gz
        omitting /home/xxx/backups/temp/rt_db_2019_03_14_22-45-27.tar to /home/xxx/backups/rt_2019_03_14_22-45-27.tar.gz
        omitting /home/xxxx/xxxxx/ to /home/dev/backups/rt_2019_03_14_22-45-27.tar.gz
        deleted temp tar archive:rt_db_2019_03_14_22-45-27.tar
        deleted temp tar archive:rt_wp_2019_03_14_22-45-27.tar
successfully created backup -> /home/xxxx/backups/rt_2019_03_14_22-45-27.tar.gz
done

```
