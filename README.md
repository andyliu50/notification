Notification

这个模块主要用于发送通知。

======
IFTTT
======

如果通过IFTTT的方式发送通知，请参考以下例子：

from notification import IFTTT
title = 'This is a title'
message = 'This is a test message.'
send_message = IFTTT(title, message)
send_message.send()

