#! /usr/bin/env python

#   Copyright (C) 2015 by Andrea Calzavacca <paranoid.nemo@gmail.com>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the
#   Free Software Foundation, Inc.,
#   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

import os
import configparser

def get_rc(rc_file):

    # define the global var
    global CSS
    global FILESYSTEM, FS_UPDATE_PERIOD, MNT, MNT_NUM
    global MAIL, MAIL_UPDATE_PERIOD, SECURITY, SERVER, USER, PASS, PLAIN
    global UP, UP_UPDATE_PERIOD
    global SERVICE
    global MUSIC, MPD_UPDATE_PERIOD, PORT, COVER_PATH
    global CLOUD, CLOUD_UPDATE_PERIOD, REMOTE, REMOTE1, REMOTE2, LOCAL, LOCAL1, LOCAL2, SIZE

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

    # gather keyring info
    SERVICE = conf_parser.get('mail', 'service')

    # gather music info
    MUSIC = conf_parser.get('twolame', 'start_music')
    MPD_UPDATE_PERIOD = conf_parser.get('music', 'update_period')
    PORT = conf_parser.get('music', 'port')
    COVER_PATH = conf_parser.get('music', 'cover_path')

    # gather cloud info
    CLOUD = conf_parser.get('twolame', 'start_cloud')
    CLOUD_UPDATE_PERIOD = conf_parser.get('cloud', 'update_period')
    REMOTE = conf_parser.get('cloud', 'remote')
    REMOTE = conf_parser.get('cloud', 'remote1')
    REMOTE = conf_parser.get('cloud', 'remote2')
    LOCAL = conf_parser.get('cloud', 'local')
    LOCAL = conf_parser.get('cloud', 'local1')
    LOCAL = conf_parser.get('cloud', 'local2')
    SIZE = conf_parser.get('cloud', 'size')
