#!/usr/bin/env python

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

#import std module(s)
import os, sys, re
import threading
import logging
import configparser
import time
import importlib

#import custom module(s)
import filesystem, rc, mail, update
from spam import beshell

#Replacement for string.format
def insert_data(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in rep_dict.keys()]), re.M)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

class FS(threading.Thread):

    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.outstring = ''
        self.format_string = ''

        try:
            os.mkfifo(os.path.expanduser('~/.local/share/be.shell/fifo/twolame_fs'))
        except:
            pass

        with open(os.path.expanduser('~/.kde4/share/apps/be.shell/Themes/Hydrogen/twolame/fs.format')) as f:
            for line in f:
                if line.startswith('#'):
                    continue
                self.format_string += line

        self.format_string = re.sub(r'>\s<', '><', self.format_string)

    def run(self):
        while True:
            importlib.reload(filesystem)
            self.out()
            time.sleep(int(rc.FS_UPDATE_PERIOD))

    def out(self):
        self.info = filesystem._info
        self.outstring = insert_data(self.format_string, self.info)

        with open(os.path.expanduser('~/.local/share/be.shell/fifo/twolame_fs'), 'w') as f:
            f.write(self.outstring)
            f.write('\n')

class MAIL(threading.Thread):

    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.outstring = ''
        self.format_string = ''

        try:
            os.mkfifo(os.path.expanduser('~/.local/share/be.shell/fifo/twolame_mail'))
        except:
            pass

        with open(os.path.expanduser('~/.kde4/share/apps/be.shell/Themes/Hydrogen/twolame/mail.format')) as f:
            for line in f:
                if line.startswith('#'):
                    continue
                self.format_string += line

        self.format_string = re.sub(r'>\s<', '><', self.format_string)

    def run(self):
        while True:
            importlib.reload(mail)
            self.out()
            time.sleep(int(rc.MAIL_UPDATE_PERIOD))

    def out(self):
        self.info = mail.new_mail
        self.outstring = insert_data(self.format_string, self.info)

        with open(os.path.expanduser('~/.local/share/be.shell/fifo/twolame_mail'), 'w') as f:
            f.write(self.outstring)
            f.write('\n')

class UP(threading.Thread):

    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.outstring = ''
        self.format_string = ''

        try:
            os.mkfifo(os.path.expanduser('~/.local/share/be.shell/fifo/twolame_up'))
        except:
            pass

        with open(os.path.expanduser('~/.kde4/share/apps/be.shell/Themes/Hydrogen/twolame/up.format')) as f:
            for line in f:
                if line.startswith('#'):
                    continue
                self.format_string += line

        self.format_string = re.sub(r'>\s<', '><', self.format_string)

    def run(self):
        while True:
            importlib.reload(update)
            self.out()
            time.sleep(int(rc.UP_UPDATE_PERIOD))

    def out(self):
        self.info = update._update
        self.outstring = insert_data(self.format_string, self.info)

        with open(os.path.expanduser('~/.local/share/be.shell/fifo/twolame_up'), 'w') as f:
            f.write(self.outstring)
            f.write('\n')

def main():

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt="%H:%M:%S")

    rc_file = os.path.join(beshell.Theme.path(), 'twolamerc')

    rc.get_rc(rc_file)

    if rc.FILESYSTEM == '1':
        fit1 = FS(1)
        fit1.start()

    if rc.MAIL == '1':
        fit2 = MAIL(2)
        fit2.start()

    if rc.UP == '1':
        fit3 = UP(3)
        fit3.start()

if __name__ == '__main__':
    main()
