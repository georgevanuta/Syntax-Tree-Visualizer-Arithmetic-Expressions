def exit_if(cond, message):
    if cond:
        print(message)
        exit(2)


# split an arithmetic expression into elements (parenthesis, numbers, operands)
def split_arith_expr(arith_expr):
    arith_split = []
    arith_expr.replace(' ', '')

    i = 0
    while i < len(arith_expr):
        if arith_expr[i] in ['+', '-', '*', '/', '(', ')']:
            arith_split.append(arith_expr[i])
        elif arith_expr[i].isnumeric() or arith_expr[i] == '.':
            dot_count = 0
            if arith_expr[i] == '.':
                dot_count += 1

            current_number = arith_expr[i]
            i += 1
            while (arith_expr[i].isnumeric() or arith_expr[i] == '.') and i < len(arith_expr):
                if arith_expr[i] == '.':
                    dot_count += 1
                current_number += arith_expr[i]
                i += 1

            i -= 1

            exit_if(current_number[-1] == '.' or dot_count > 1, f'[ERROR]: invalid number format: {current_number}')

            arith_split.append(current_number)
        else:
            exit_if(True, f'[ERROR]: invalid character in arithmetic expression: {arith_expr[i]}')

        i += 1

    return arith_split


NODE_SIZE = 60
FONT_SIZE = int(NODE_SIZE / 3.8)
START_X = 740
START_Y = 50
DISP_Y = 200
DISP_X = 350
MINIMIZER_SIZE = 0.86
MINIMIZER_DISP = 0.77