# coding=utf-8

parts = ['词汇语法', '读解', '听解']
ispassed = True


def error(a):
    print(str(parts[a]) + '部分输入错误')
    quit()


def is_pass(score, is_total):
    global ispassed
    if not is_total and score >= 19:
        return '合格;'
    elif not is_total and score < 19:
        ispassed = False
        return '不合格;'
    elif is_total and score >= 100 and ispassed:
        return '合格;'
    else:
        return '不合格;'


for questions in range(1, 14):
    name = 'q' + str(questions)
    locals()['q' + str(questions)] = input('问题' + str(questions) + '错题数:')
    if locals()['q' + str(questions)] == '':
        locals()['q' + str(questions)] = 0
try:
    part1 = (6 - int(q1)) + (7 - int(q2)) + (6 - int(q3)) + (12 - 2 * int(q4)) + (10 - int(q5)) + (5 - int(q6)) + (
            10 - 2 * int(q7))
    part1_score = part1 / 56 * 60
except:
    error(0)
try:
    part2 = (8 - 2 * int(q8)) + (18 - 2 * int(q9)) + (12 - 3 * int(q10)) + (4 - 2 * int(q11)) + (12 - 3 * int(q12)) + (
            4 - 2 * int(q13))
    part2_score = part2 / 58 * 60
except:
    error(1)
print('词汇语法部分得分' + str(int(round(part1_score))) + '/60,' + str(is_pass(int(round(part1_score)), False)),
      '读解部分得分' + str(int(round(part2_score))) + '/60,' + str(
          is_pass(int(round(part2_score)), False)) + '\n总分（不含听力）: ' + str(
          int(round(part1_score)) + int(round(part2_score))) + ' 分')

if_listening = input('包含听力吗?(y/N):')
if if_listening.upper() == 'Y':
    pass
else:
    quit()

for questions_listening in range(1, 6):
    question_order_listening = 'ql' + str(questions_listening)
    locals()[str(question_order_listening)] = input('听解问题' + str(questions_listening) + '错题数:')
    if locals()[str(question_order_listening)] == '':
        locals()[str(question_order_listening)] = 0
try:
    part3 = (12 - 2 * int(ql1)) + (7 - int(ql2)) + (12 - 2 * int(ql3)) + (13 - int(ql4)) + (12 - 3 * int(ql5))
    part3_score = part3 / 56 * 60
except:
    error(2)
total = int(round(part1_score)) + int(round(part2_score)) + int(round(part3_score))
print('听解部分得分' + str(int(round(part3_score))) + '/60,' + str(is_pass(int(round(part3_score)), False)) + '\n总分' + str(
    total) + '分,' + str(is_pass(total, True)))
