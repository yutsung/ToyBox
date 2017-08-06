#!/usr/local/bin/python3
"""
Python script for backup file or folder

This program can generate new folder by your username 
under storage-folder, so it can used by multi-user.

How to use: 1. list your backup source with full-path
               in *.txt file and save in backup_list directory
            2. you can set exception keyword just after your 
               backup source path and separate by ;
               ex: /home/myname/mycode; mycode/except-folder
            3. run this program
"""

import datetime
import json
import os
import shutil
import sys
import tarfile
if "linux" or "darwin" in sys.platform:
    import pwd


def read_backup_list(list_path, list_filename):
    """
    read file that backup list in.
    And return list of source directory

    :param list_path: path of backup-list folder
    :param list_filename: path of backup-list-file in backup-list folder
    :return: list of source directory
    """
    source_dir_list = []
    with open(list_path+"/"+list_filename, encoding="utf-8") as fid:
        for line in fid:
            line_exclude = line.strip().split(";")[1:]
            line = line.strip().split(";")[0]
            if not os.path.exists(line):
                continue
            source_dir_list.append((line, line_exclude))
    return source_dir_list


def get_size(path):
    """
    get size of folder or file

    :param path: the directory that you want to know total-size
    :return: total-size in bytes
    """
    if os.path.isfile(path):
        total_size = os.path.getsize(path)
        return total_size
    total_size = 0
    for ipath, _, ifilename_list in os.walk(path):
        for ifilename in ifilename_list:
            ifile_dir = os.path.join(ipath, ifilename)
            total_size += os.path.getsize(ifile_dir)
    return total_size


def tar_filter_func(tarinfo):
    with open("temp.json") as fid:
        exclude_list = json.load(fid)
    for iname in exclude_list:
        if iname.strip() in tarinfo.name:
            return None
    return tarinfo
    

def do_backup(source_dir, dest_dir, tar_file=False, 
              check_date=False, filter_func=None):
    """
    backup file or folder that recorded by source_dir variable
    to destination directory

    :param source_dir: the source which will be backup.
    :param dest_dir: destination directory of backup file.
    :param tar_file: tar the file/folder or not
    :param check_date: if True, the whether exists a tar-file which was
                       newer than modification time of source file/directory
    :return: none
    """
    basename = os.path.basename(source_dir)

    if check_date:
        if os.path.exists(dest_dir+"/"+basename+".tgz"):
            source_mtime = datetime.datetime.utcfromtimestamp(
                os.path.getmtime(source_dir))
            destin_mtime = datetime.datetime.utcfromtimestamp(
                os.path.getmtime(dest_dir+"/"+basename+".tgz"))
            if destin_mtime >= source_mtime:
                return

    if tar_file:
        with tarfile.open(dest_dir+"/"+basename+".tgz", "w:gz") as tarid:
            if filter_func == None:
                tarid.add(source_dir, arcname=basename)
            else:
                tarid.add(source_dir, arcname=basename, filter=filter_func)
    else:
        shutil.copy2(source_dir, dest_dir)


def main():

    main_pwd = os.path.dirname(os.path.realpath(__file__))
    list_path = main_pwd + "/backup_list"
    dest_dir0 = main_pwd + "/storage_zone"
    tmpfile_name = "temp"

    for list_filename in os.listdir(list_path):
        dest_dir = dest_dir0

        # avoid some irrelevant folders in list_path
        if ".txt" not in list_filename:
            continue

        # make destination folder by username
        # find username in different ways depended on OS
        if sys.platform == "win32" or "windows":
            list_ownername = os.getlogin()
            dest_dir += ("/" + list_ownername)
            if not os.path.exists(dest_dir):
                os.mkdir(dest_dir)
        elif sys.platform == "linux" or "linux2" or "darwin":
            list_uid = os.stat(list_path + "/" + list_filename).st_uid
            list_ownername = pwd.getpwuid(list_uid).pw_name
            dest_dir += ("/" + list_ownername)
            if not os.path.exists(dest_dir):
                os.mkdir(dest_dir)

        # read backup list
        source_dir_list = read_backup_list(list_path, list_filename)

        for source_dir, exclude_list in source_dir_list:
            with open(tmpfile_name+".json", "w") as fid:
                json.dump(exclude_list, fid)
            if source_dir[-1] == "/":
                source_dir = source_dir[:-1]
            # call do_backup()
            source_isfile = os.path.isfile(source_dir)
            if (get_size(source_dir) < 5*1024**2) and (source_isfile):
                do_backup(
                    source_dir,
                    dest_dir, 
                    tar_file=False,
                    check_date=True,
                    filter_func=tar_filter_func,
                    )
            else:
                do_backup(
                    source_dir,
                    dest_dir, 
                    tar_file=True,
                    check_date=True,
                    filter_func=tar_filter_func,
                    )
    os.remove(tmpfile_name+".json")


if __name__ == "__main__":
    main()
