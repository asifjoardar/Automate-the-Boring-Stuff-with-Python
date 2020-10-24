import re

phone = re.compile(r'(\+?(88)?0?1[3456789][0-9]{8})') # bangladeshi phone format

email = re.compile(r'''(
[a-zA-Z0-9._%+-]+ # username
@                 # @ symbol
[a-zA-Z0-9.-]+    # domain name
(\.[a-zA-Z]{2,4}) # dot-something
)''', re.VERBOSE)

text = 'mahmud170052@diit.edu.bd diit ooj +8801902838603 mrsparrow04@gmail.com asif170088@diit.edu.bd'

phone_numbers = []
emails = []

for g in phone.findall(text):
    phone_numbers.append(g[0])
for g in email.findall(text):
    emails.append(g[0])

if(len(phone_numbers) or len(emails)):
    if(len(phone_numbers)):
        print('phone numbers:')
        for i in phone_numbers:
            print(i)
    if (len(emails)):
        print('Emails:')
        for i in emails:
            print(i)
else:
    print('There is no emails and phone number.')
