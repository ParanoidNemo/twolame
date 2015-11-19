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

import os
import imaplib

import keyring

import rc
from spam import webmail
from spam import beshell
from spam import methods

rc_file = os.path.join(beshell.Theme.path(), 'twolamerc')

rc.get_rc(rc_file)
i = 0

m_info = []
m_count = []

for item in rc.USER.split(','):

    try:
        if len(rc.SECURITY.split(',')) == 1:
            sec = rc.SECURITY
        else:
            sec = rc.SECURITY.split(',')[i]

        if sec == 'imap':

            if len(rc.SERVER.split(',')) == 1:
                m = imaplib.IMAP4_SSL(rc.SERVER)
            else:
                m = imaplib.IMAP4_SSL(rc.SERVER.split(',')[i])

            if rc.PLAIN:
                password = rc.PASS.split(',')[i]
            else:
                if len(rc.SERVICE.split(',')) == 1:
                    password = keyring.get_password(rc.SERVICE, item)
                else:
                    password = keyring.get_password(rc.SERVICE.split(',')[i], item)

            try:
                m.login(item, password)
            except imaplib.IMAP4.error:
                print("Error: Login Failed\nPlease check your username and password")

            rv, data = m.select("INBOX", readonly=True)
            if rv == 'OK':

                m_count.append(webmail.new_message_count(m))

                for line in webmail.process_mailbox(m):
                    m_info.append(line)
                    m.close()
                m.logout()

            i += 1

        elif sec == 'pop':
            pass # need to add POP support service
        else:
            pass

    except Exception:
        pass

css = os.path.join(beshell.Theme.path(), 'style.css.d', rc.CSS)
tot = len(m_info)

if tot < 5:
    for l in range(5 - tot):
        m_info.append('')
else:
    pass

new_mail = methods.create_dict(m_info[-5:])
new_mail['{x}'] = css
new_mail['{tot}'] = str(tot)

if len(rc.USER.split(',')) == 1:
    new_mail['{user}'] = rc.USER
else:
    i = 0
    for item in rc.USER.split(','):
        new_mail['{user%d}' %i] = item
        i += 1

i = 0
for item in m_count:
    new_mail['{new_message%d}' %i] = item
    i += 1
