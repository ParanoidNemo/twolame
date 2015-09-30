#! /usr/bin/env python

import os
import configparser

def get_rc(rc_file):
    global FILESYSTEM, FS_UPDATE_PERIOD, MNT1, MNT2, CSS
    conf_parser = configparser.ConfigParser()
    rc = conf_parser.read(rc_file)
    FILESYSTEM = conf_parser.get('twolame', 'start_fs')
    FS_UPDATE_PERIOD = conf_parser.get('fs', 'update_period')
    MNT1 = conf_parser.get('fs', 'mount_point1')
    MNT2 = conf_parser.get('fs', 'mount_point2')
    CSS = conf_parser.get('twolame', 'css_file')
