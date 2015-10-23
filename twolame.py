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
import filesystem, rc, mail, update, mpc
from spam import beshell
from spam import methods

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
        self.outstring = methods.insert_data(self.format_string, self.info)

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

        with open(os.path.join(beshell.Theme.path(), 'twolame', 'mail.format')) as f:
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
        self.outstring = methods.insert_data(self.format_string, self.info)

        self.outstring = re.sub(r'<br><br>', '', self.outstring)
        self.outstring = re.sub(r'\n', '', self.outstring)
        self.outstring = re.sub(r'<br></table>', '</table>', self.outstring)
        self.outstring = re.sub(r'\n', '', self.outstring)

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

        with open(os.path.join(beshell.Theme.path(), 'twolame', 'up.format')) as f:
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
        self.outstring = methods.insert_data(self.format_string, self.info)

        self.outstring = re.sub(r'<tr><td></td></tr>', '', self.outstring)
        self.outstring = re.sub(r'\n', '', self.outstring)
        self.outstring = re.sub(r'<br></table>', '</table>', self.outstring)
        self.outstring = re.sub(r'\n', '', self.outstring)

        with open(os.path.expanduser('~/.local/share/be.shell/fifo/twolame_up'), 'w') as f:
            f.write(self.outstring)
            f.write('\n')

class MPD(threading.Thread):

    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.outstring = ''
        self.outstring2 = ''
        self.outstring3 = ''
        self.format_string = ''
        self.format_string2 = ''
        self.format_string3 = ''

        try:
            os.mkfifo(os.path.expanduser('~/.local/share/be.shell/fifo/twolame_music'))
        except:
            pass

        try:
            os.mkfifo(os.path.expanduser('~/.local/share/be.shell/fifo/twolame_cover'))
        except:
            pass

        try:
            os.mkfifo(os.path.expanduser('~/.local/share/be.shell/fifo/twolame_playlist'))
        except:
            pass

        with open(os.path.join(beshell.Theme.path(), 'twolame', 'music.format')) as f:
            for line in f:
                if line.startswith('#'):
                    continue
                self.format_string += line

        self.format_string = re.sub(r'>\s<', '><', self.format_string)

        with open(os.path.join(beshell.Theme.path(), 'twolame', 'cover.format')) as v:
            for line in v:
                if line.startswith('#'):
                    continue
                self.format_string2 += line

        self.format_string2 = re.sub(r'>\s<', '><', self.format_string2)

        with open(os.path.join(beshell.Theme.path(), 'twolame', 'pl.format')) as p:
            for line in p:
                if line.startswith('#'):
                    continue
                self.format_string3 += line

        self.format_string3 = re.sub(r'>\s<', '><', self.format_string3)
        self.format_string3 = re.sub(r'\n', '', self.format_string3)

    def run(self):
        while True:
            importlib.reload(mpc)
            self.out()
            time.sleep(int(rc.MPD_UPDATE_PERIOD))

    def out(self):
        self.info = mpc.info
        self.outstring = methods.insert_data(self.format_string, self.info)

        with open(os.path.expanduser('~/.local/share/be.shell/fifo/twolame_music'), 'w') as f:
            f.write(self.outstring)
            f.write('\n')

        self.cover = mpc.info_cv
        self.outstring2 = methods.insert_data(self.format_string2, self.cover)

        with open(os.path.expanduser('~/.local/share/be.shell/fifo/twolame_cover'), 'w') as v:
            v.write(self.outstring2)

        self.pl = mpc.info_pl
        self.outstring3 = methods.insert_data(self.format_string3, self.pl)

        with open(os.path.expanduser('~/.local/share/be.shell/fifo/twolame_playlist'), 'w') as p:
            p.write(self.outstring3)
            p.write('\n')

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

    if rc.MUSIC == '1':
        fit4 = MPD(4)
        fit4.start()

if __name__ == '__main__':
    main()
