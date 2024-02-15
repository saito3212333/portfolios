import re
import string
import urllib.request


class ReEngine2:
    def do_ex1(self):
        """
        r'[a-zA-Z0-9]+' :: Searching for any number of alphanumeric characters excluding _.
        r'\d' :: Searching for ONE numeric digit.
        r'\d\d' :: Searching for TWO numeric digits.
        r'\d*.\d{3}' :: Searching zero or more digits followed by any charadcter and THREE digits. 45h134 / y783 / 73824$342 / *342
        r'\d{11}' :: Searching for 11 numeric digits.  83746372817 / 48287390243 / 00000000000 / 11111111111
        r'[a-z0-9\.@#$%&]+' :: Searching for ONE or MORE lowercase alphas, digits,
                            or the following special characters: . @ # $ % &.
        r'[a-zA-Z0-9\s]{6,20}'  :: Searching for any alphanumeric or whitespace characters, excluding _, 6 to 20 times.
        r'https:/{2}[\w.]+[.]com' ::  'https://happyday.com', 'https://apple.picking.com'
        r'</?[\w\s]*>|<.+[\W]>' :: tags in an html context <div> </div> <span>
        r'(.+)/([^/]+)' :: k/ha   D:/tsom/da
        r'[\w,\s-]+\.[A-Za-z]{3}' :: hads.com     people.net
        """

        str2 = "hey you, how are you? ba ba black sheep had a lot of whool. \\you are good.\\ &^%, fly a k&$#!"
        print()
        result1 = re.findall(r'[a-z0-9.@#$%&]+', str2, re.I)
        print(result1)

        print()
        result1 = re.findall(r'[a-z0-9\\.@#$%&]+', str2, re.I)
        print(result1)

        str2 = "hey you, how are you? https://happyday.com https://apple.picking.com https://big.bang.ca"
        print()
        result1 = re.findall(r'https:/{2}[\w.]+[.]com', str2, re.I)
        print(result1)

    def do_ex2(self):
        with open("email.txt") as f:
            email = f.read()
        """ 
        List all the email addresses
        List all the phone numbers
        Extract the subject
        Extract the summary of reasons
        """
        print("EX 2")
        print(email)

        print()
        email_addresses = set(re.findall(r"\b\S+[@][\w.]+\b", email, re.I))
        print(email_addresses)

        print()
        phone_numbers = set(re.findall(r"[+]?[0-9 ]+\d", email, re.I))
        print(phone_numbers)

        # Extract
        # the subject
        print('Look for the subject?')
        subject = re.findall(r'Subject: .+[!]', email, re.I)
        print(subject)

        # Extract the summary of reasons
        print("Look for the summary of reasons?")
        parts = re.split(r'reasons:', email, re.I)
        print(parts)
        reasons = re.findall(r'[^:\n]+:\s', parts[1], re.I)
        print(reasons)

    def demonstrateRE(self):
        txt = "An arbitrary number of REs can be separated by the '|' in this way."
        x = re.search("\w*(ar)\w*", txt)
        print(x)
        print(x.span())
        print(x.string)
        print(x.group())

        print()
        txt = "An arbitrary number of REs can be separated by the '|' in this way."
        x = re.split(f"\s[{string.punctuation}]*\|[{string.punctuation}]*\s", txt)
        print(x)

        print()
        # Replace all white-space characters with the digit ";":
        txt = "There is a a key to solve every porblem."
        x = re.sub("\s", ";", txt)
        print(x)

        print()
        with open("tsom.html") as f:
            str3 = f.read()

        print(str3)
        result1 = set(re.findall(r"https:/{2}[\w./\\\-$%]+", str3, re.I))
        print(result1)
        print()
        print("\n".join(result1))

