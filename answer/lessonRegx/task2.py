"""
課題 正規表現
"""

import re

content: str = 'abcdefg:-:12345678:ABCD:abc:efg:?:123efg456'
pattern1: str = r'[0-9]+'
pattern2: str = r'[A-Z]+'

print(re.sub(pattern1 + '|' + pattern2, '!', content))
