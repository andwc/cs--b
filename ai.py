def is_valid_email(email):
    at_count = email.count('@')
    if at_count != 1:
        return False
    username, domain = email.split('@')
    if username.startswith('.') or username.endswith('.') or domain.startswith('.') or domain.endswith('.'):
        return False
    if '.' not in domain:
        return False
    if '..' in domain:
        return False
    return True
import sys
for line in sys.stdin:
    email = line.strip()  # 去除两端空白字符
    if is_valid_email(email):
        print("YES")
    else:
        print("NO")