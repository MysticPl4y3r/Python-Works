import re

text_to_search='''The Lockheed Martin F-22 Raptor is an American single-seat, twin-engine, 
all-weather stealth tactical fighter aircraft developed for the United States Air Force (USAF). 
As the result of the USAF's Advanced Tactical Fighter (ATF) program, the aircraft was designed 
as an air superiority fighter, but also has ground attack, electronic warfare, and signals 
intelligence capabilities. The prime contractor, Lockheed Martin, built most of the F-22's 
airframe and weapons systems and conducted final assembly, while Boeing provided the wings, 
aft fuselage, avionics integration, and training systems. '''

sentence='Start a sentence and bring it to an end'

#pattern matching
pattern=re.compile(r'\d{3}-\d{3}-d{4}',re.I)
print(pattern)