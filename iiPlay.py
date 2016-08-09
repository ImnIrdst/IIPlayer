#!/usr/bin/env python
import os
import sys
import json
import subprocess

from tools.Play import play

# Constants
CONFIG_FILE_PATH = '/mnt/4E903A9B903A8A0B/Work/Gitlab/iiPlay/configs.json'
DATA_BASE_FILE_PATH = '/mnt/4E903A9B903A8A0B/Work/Gitlab/iiPlay/db.json'

# Global variables
db = None
configs = None


def load_configs():
    global configs
    if configs is not None:
        return
    with open(CONFIG_FILE_PATH, "r") as configs_file:
        configs = json.load(configs_file)


def load_db():
    global db
    if db is not None:
        return
    with open(DATA_BASE_FILE_PATH, "r") as db_file:
        db = json.load(db_file)


def flush_db():
    with open(DATA_BASE_FILE_PATH, "w") as db_file:
        json.dump(db, db_file)
    load_db()


def get_directory_of_arg(arg):
    if arg == configs['directory']['series']['arg']:
        return configs['directory']['series']['directory']

    elif arg == configs['directory']['movies']['arg']:
        return configs['directory']['movies']['directory']


def play_cur(short_name):
    directory = get_directory_of_arg(db['cur'][short_name]['arg'])
    name = db['cur'][short_name]['name'] + '*S' + db['cur'][short_name]['season'] + "E" + db['cur'][short_name][
        'episode']
    play(directory, name)


def play_next(short_name):
    episode = db['cur'][short_name]['episode']
    episode = int(episode) + 1
    db['cur'][short_name]['episode'] = "%02d" % episode

    flush_db()
    play_cur(short_name)


def play_prev(short_name):
    episode = db['cur'][short_name]['episode']
    episode = int(episode) - 1
    db['cur'][short_name]['episode'] = "%02d" % episode

    flush_db()
    play_cur(short_name)


def main():
    load_db()
    load_configs()

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    sub_cmd = sys.argv[2]

    directory = get_directory_of_arg(arg1)

    if arg1 == 'cur':
        play_cur(arg2)

    elif arg1 == 'next':
        play_next(arg2)

    elif arg1 == 'prev':
        play_prev(arg2)

    elif sub_cmd == 'ls':
        mkv_query = 'find ' + directory + ' -name "*mkv*"'
        process = subprocess.Popen(mkv_query, shell=True, stdout=subprocess.PIPE)
        mkv_files = '"' + ''.join(process.stdout.readlines()).strip() + '"'

        print(mkv_files)
    else:
        play(directory, arg2)


if __name__ == '__main__':
    main()
