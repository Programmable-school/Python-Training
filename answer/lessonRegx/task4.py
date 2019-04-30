"""
課題 正規表現
"""

import re

content1: str = 'test@test.com'
content2: str = 'dummy'
content3: str = 'https://google.com'

pattern: str = r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'

print('%s -> %s' % (content1, True if re.match(pattern, content1) else False))
print('%s -> %s' % (content2, True if re.match(pattern, content2) else False))
print('%s -> %s' % (content3, True if re.match(pattern, content3) else False))
