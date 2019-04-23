import sys
import traceback
import smtplib
import email
from email.mime.text import MIMEText
import re


# send_mail
# server_config is a dict, which should contains: from_addr, smtp_host, smtp_port
# body_type can be 'txt'/'html'
def send_mail(server_config, to_addrs, subject, body, body_type='html'):
    if not to_addrs:
        return
    to_list = [
        addr + ('@' not in addr and '@xxx.xxx' or '')
        for addr in filter(None, re.split(r'[,;]\s*', to_addrs))
    ]
    msg = MIMEText(body, body_type)
    msg['From'] = server_config['from_addr']
    msg['To'] = email.utils.COMMASPACE.join(to_list)
    msg['Date'] = email.utils.formatdate(localtime=True)
    msg['Subject'] = subject

    server = smtplib.SMTP(host=server_config['smtp_host'],
                          port=server_config['smtp_port'])
    server.sendmail(server_config['from_addr'], to_list, msg.as_string())
    server.quit()