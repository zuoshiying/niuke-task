import sys

code = sys.stdin.read()
result = []
i = 0
n = len(code)
in_string = False
in_comment = False
comment_start = 0

while i < n:
    if in_comment:
        if i + 1 < n and code[i] == '*' and code[i+1] == '/':
            in_comment = False
            i += 2
        else:
            i += 1
    elif in_string:
        if code[i] == '\\':
            result.append(code[i])
            if i + 1 < n:
                result.append(code[i+1])
                i += 2
            else:
                i += 1
        elif code[i] == '"':
            result.append(code[i])
            in_string = False
            i += 1
        else:
            result.append(code[i])
            i += 1
    else:
        if i + 1 < n and code[i] == '/' and code[i+1] == '*':
            in_comment = True
            comment_start = i
            i += 2
        elif code[i] == '"':
            in_string = True
            result.append(code[i])
            i += 1
        else:
            result.append(code[i])
            i += 1

if in_comment:
    result.append(code[comment_start:])

sys.stdout.write(''.join(result))


