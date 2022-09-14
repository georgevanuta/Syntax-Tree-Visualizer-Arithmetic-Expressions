from sys import argv, exit

from PyQt6.QtWidgets import QApplication

from misc import exit_if

from src.graphics import GraphicInterface


def main():
    exit_if(len(argv) != 2, '[USAGE]: python3 main.py <ARITHMETIC_EXPRESSION>')
    arith_expr = argv[1]

    app = QApplication([])
    gi = GraphicInterface(arith_expr)
    exit(app.exec())


if __name__ == '__main__':
    main()