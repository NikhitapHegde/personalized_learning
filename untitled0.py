# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 08:05:42 2023

@author: poorn
"""

ascii_text = "ದೈಹಿಕ ಶಿಕ್ಷಣ"
unicode_text = ascii_text.encode('utf-8')
print(unicode_text)
print(unicode_text.decode('utf-8'));
kannada_text = "ನಮಸ್ಕಾರ"  # Replace with your Kannada text
unicode_text = kannada_text.encode('utf-8')
print(unicode_text)

decoded_text = unicode_text.decode('utf-8')
print(decoded_text)
