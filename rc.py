#! /usr/bin/env python

#   This program was originally created by magpie240 <https://github.com/magpie240>
#   as part of skutter <https://github.com/Bedevil/skutter>

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
    global FILESYSTEM, FS_UPDATE_PERIOD, MNT, FM
    global MAIL, MAIL_UPDATE_PERIOD, SECURITY, SERVER, USER, PASS, PLAIN
    global UP, UP_UPDATE_PERIOD, PM
    global SERVICE
    global MUSIC, MPD_UPDATE_PERIOD, PORT, COVER_PATH
    global CLOUD, CLOUD_UPDATE_PERIOD, LOCAL, LOCAL1, LOCAL2
    global RCLONE, RCLONE_SECTIONS, RCLONE_CONFIG_FILE
    global MEGA, SIZE

    # create the parser
    conf_parser = configparser.ConfigParser()
    rc = conf_parser.read(rc_file)

    # set the CSS file
    CSS = conf_parser.get('twolame', 'css_file')

    # gather info for system module
    FILESYSTEM = conf_parser.get('twolame', 'start_system')
    FM = conf_parser.get('system', 'fm')
    FS_UPDATE_PERIOD = conf_parser.get('system', 'update_period')
    MNT = conf_parser.get('system', 'mnt')

    # gather info for email module
    MAIL = conf_parser.get('twolame', 'start_mail')
    MAIL_UPDATE_PERIOD = conf_parser.get('mail', 'update_period')
    SECURITY = conf_parser.get('mail', 'security')
    SERVER = conf_parser.get('mail', 'server')
    USER = conf_parser.get('mail', 'user')
    PASS = conf_parser.get('mail', 'password')
    PLAIN = conf_parser.getboolean('mail', 'plain')

    # gather info for update module
    UP = conf_parser.get('twolame', 'start_update')
    UP_UPDATE_PERIOD = conf_parser.get('update', 'update_period')
    PM = conf_parser.get("update", "pm")

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
    LOCAL = conf_parser.get('cloud', 'local')
    LOCAL1 = conf_parser.get('cloud', 'local1')
    LOCAL2 = conf_parser.get('cloud', 'local2')

    # gather rclone info
    RCLONE = conf_parser.get('cloud', 'use_rclone')
    RCLONE_SECTIONS = conf_parser.sections()
    RCLONE_CONFIG_FILE = conf_parser.get('cloud', 'rclone_config')

    # gather mega info
    MEGA = conf_parser.get('cloud', 'use_mega')
    SIZE = conf_parser.get('cloud', 'size')
