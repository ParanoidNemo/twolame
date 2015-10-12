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

rc_file = os.path.join(beshell.Theme.path(), 'twolamerc')

rc.get_rc(rc_file)

if rc.SECURITY == 'imap':

    m = imaplib.IMAP4_SSL(rc.SERVER)

    if rc.PLAIN == 'True':
        password = rc.PASS
    else:
        password = keyring.get_password(rc.SERVICE, rc.USER)

    try:
        m.login(rc.USER, password)
    except imaplib.IMAP4.error:
        print("Error: Login Failed\nPlease check your username and password")

    rv, data = m.select("INBOX", readonly=True)
    if rv == 'OK':
        m_info = webmail.process_mailbox(m)
        m.close()
    m.logout()

else:
    pass

css = os.path.join(beshell.Theme.path(), 'style.css.d', rc.CSS)
new_mail = {}
tot = len(m_info)

if tot < 5:
    nl = 5 - tot
    for l in range(nl):
        m_info.append('')
else:
    pass

for index, item in enumerate(m_info[-5:]):
    i = '{' + str(index) + '}'
    new_mail[i] = item
new_mail['{x}'] = css
new_mail['{tot}'] = str(tot)
new_mail['{user}'] = rc.USER
