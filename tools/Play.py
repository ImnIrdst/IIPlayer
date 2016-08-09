import os
import subprocess


def play(directory, name):
    mkv_query = 'find ' + directory + ' -name "*' + name + '*mkv*"'
    process = subprocess.Popen(mkv_query, shell=True, stdout=subprocess.PIPE)
    mkv_file = '"' + ''.join(process.stdout.readlines()).strip() + '"'

    srt_query = 'find ' + directory + ' -name "*' + name + '*srt*"'
    process = subprocess.Popen(srt_query, shell=True, stdout=subprocess.PIPE)
    srt_file = '"' + ''.join(process.stdout.readlines()).strip() + '"'

    sub_scale = '--sub-scale=.3'
    sub_file = '--sub-file=' + srt_file

    if srt_file == '""':
        sub_file = ''

    mpv_cmd = 'mpv ' + mkv_file + ' ' + sub_file + ' ' + sub_scale

    print('mkv_file: ' + mkv_file)
    print('srt_file: ' + srt_file)
    print(mpv_cmd)

    os.system(mpv_cmd)
