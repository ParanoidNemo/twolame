#! /usr/bin/env python

import os
import configparser

def get_rc(rc_file):

    # define the global var
    global CSS
    global FILESYSTEM, FS_UPDATE_PERIOD, MNT, MNT_NUM
    global MAIL, MAIL_UPDATE_PERIOD, SECURITY, SERVER, USER, PASS, PLAIN
    global UP, UP_UPDATE_PERIOD

    # create the parser
    conf_parser = configparser.ConfigParser()
    rc = conf_parser.read(rc_file)

    # set the CSS file
    CSS = conf_parser.get('twolame', 'css_file')

    # gather info for fs module
    FILESYSTEM = conf_parser.get('twolame', 'start_fs')
    FS_UPDATE_PERIOD = conf_parser.get('fs', 'update_period')
    MNT_NUM = conf_parser.get('fs', 'mnt_num')
    try:
        _MNT_NUM = int(MNT_NUM)
        MNT = []
        for i in range(_MNT_NUM):
            _i = str(i)
            if conf_parser.get('fs', 'mount_point' + _i) != '':
                MNT.append(conf_parser.get('fs', 'mount_point' + _i))
            else:
                pass

    except Exception as ex:
        print(ex)

    # gather info for email module
    MAIL = conf_parser.get('twolame', 'start_mail')
    MAIL_UPDATE_PERIOD = conf_parser.get('mail', 'update_period')
    SECURITY = conf_parser.get('mail', 'security')
    SERVER = conf_parser.get('mail', 'server')
    USER = conf_parser.get('mail', 'user')
    PASS = conf_parser.get('mail', 'password')
    PLAIN = conf_parser.get('mail', 'plain')

    # gather info for update module
    UP = conf_parser.get('twolame', 'start_update')
    UP_UPDATE_PERIOD = conf_parser.get('update', 'update_period')
