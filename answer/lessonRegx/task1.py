"""
課題 正規表現
"""

import re

content: str = 'abcdefg:-:12345678:ABCD:abc:efg:?:123efg456'
pattern: str = r'[0-9]+'

print(re.sub(pattern, '!', content))
