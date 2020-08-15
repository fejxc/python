def main():
    full_name = get_full_name()
    print()
    password = get_password()
    print()
    first_name = get_first_name(full_name)
    print()
    email = get_email()
    print()
    phone = get_phonenumber()
    print()
  #  if get_phonenumber() and get_email() and get_first_name() and get_full_name() and get_password():


    print("Hi " + first_name + ", thanks for creating an account.")
    print("We'll text your confirmation code to this number:"+phone[0:3] + '.' + phone[3:6] + '.' + phone[6:])
'''
2. 创建并使用一个函数以获取有效的电子邮件地址。地址要有效，必须包含@符号，最后以".com"结尾。
'''
def get_email():
    while True:
        email = input("Enter email address:       ")
        if email.find('@') and email.endswith('.com'):
            return email
        else:
            print('Please enter a valid email address.')
'''
3. 创建并使用函数获取有效电话号码。为此，请从数字中删除所有空格、短划线、小括号 和句号。
   然后，检查以确保电话号码由 10 个字符组成的，并且是数字。
'''

def get_phonenumber():
    while True:
        phoneid = input('Enter phone number:       ')
        result = phoneid.strip()
        x = [i for i in result if i.isdigit()]
        s2 = ''.join(x)
        if s2.isdigit() and len(s2) >= 10:

            return s2
        else:
            print('Please enter a 10-digit phone number.')



def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")


def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name


def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print("Password must be 8 characters or more \n" +
                  "with at least one digit and one uppercase letter.")
        else:
            return password


if __name__ == "__main__":
    main()
