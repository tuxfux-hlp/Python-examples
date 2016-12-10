#!/usr/bin/python
import socket
import platform
import time
import sys
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Mail:
    def __init__(self,user_defined=None):
        self.user_defined = user_defined

    def sendMail(self, SUBJECT, BODY, TO, FROM, ATTACHMENT):
        """With this function we send out our html email"""

        # Create message container - the correct MIME type is multipart/alternative here!
        MESSAGE = MIMEMultipart('alternative')
        MESSAGE['subject'] = SUBJECT
        MESSAGE['To'] = ", ".join(TO)
        MESSAGE['From'] = FROM
        MESSAGE.preamble = ""
        ATTACHMENT_NAME = os.path.basename(ATTACHMENT)

        # Record the MIME type text/html...
        HTML_BODY = MIMEText(BODY, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        MESSAGE.attach(HTML_BODY)

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(ATTACHMENT,"rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % ATTACHMENT_NAME)
        MESSAGE.attach(part)

        # The actual sending of the e-mail
        server = smtplib.SMTP('outlook.td.teradata.com')

        # Print debugging output when testing
        if __name__ == "__main__":
            server.set_debuglevel(1)

        # Credentials (if needed) for sending the mail
        #password = "mypassword"

        #server.starttls() "TLS (transport layer security) encryption option is not working on soem machines"
        #server.login(FROM,password)
        server.sendmail(FROM, TO, MESSAGE.as_string())
        server.quit()




if __name__ == "__main__":
    """Executes if the script is run as main script (for testing purposes)"""

    hostname = socket.gethostname()
    os = platform.platform()
    localtime = time.asctime( time.localtime(time.time()) )
    email_content = """
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>html title</title>
  <style type="text/css" media="screen">
    table{
        empty-cells:hide;
    }
    td.cell{
        background-color: white;
    }
  </style>
</head>
<body>
    <STYLE>
    .boldtable, .boldtable TD, .boldtable TH
    {
        font-size:10pt;
        border: 1px solid #CCCCCC;
    }
    </STYLE>
  <table>
  <table width= "430" cellpadding="1" border="0" style="border-top:1px solid; border-left:1px solid; border-right:1px solid; border-bottom:1px solid">
    <TR bgcolor="#336699"><TD colspan="2"><B><FONT color = "white" size="3">Overall Summary</B></TD></tr>
    <tr valign="top">
        <td>
        <table style="border: black 1px solid;width:100%">
            <tr><td bgcolor="#f4e9d3"><B>Overall Status</B></td>
            <td bgcolor="#f4e9d3"><B><FONT COLOR="red">REJECTED</FONT></B></td></tr>
            <tr><td bgcolor="#f4e9d3"><B>Hostname</B></td><td bgcolor="#f4e9d3">""" + hostname + """</td></tr>
            <tr><td bgcolor="#f4e9d3"><B>OS</B></td><td bgcolor="#f4e9d3">""" + os + """</td></tr>
            <tr><td bgcolor="#f4e9d3"><B>Date and Time</B></td><td bgcolor="#f4e9d3">""" + localtime + """</td></tr>
        </table>
        </td>
    </tr>
  </table>
  <table width= "430" cellpadding="1" border="0" style="border-top:1px solid; border-left:1px solid; border-right:1px solid; border-bottom:1px solid">
    <tr bgcolor="#336699"><td><B><FONT color = "white" size="3">Test Case Status Summary</FONT></B></td></tr>
    <tr valign="top">
        <td>
        <table style="border: black 1px solid;width:100%">
            <TR bgcolor="#f4e9d3"><TD align="center"><B>Passed</B></TD><TD align="center"><B>Failed</B></TD>
            <TD align="center"><B>NonAttempted</B></TD>
            <TD align="center"><B>Total Test Cases</B></TD></TR>

