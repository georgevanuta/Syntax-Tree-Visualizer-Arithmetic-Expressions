from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QFont

from misc import NODE_SIZE, FONT_SIZE,\
                 START_X, START_Y, \
    DISP_Y,\
                 MINIMIZER_SIZE, MINIMIZER_DISP

from src.parse_tree import ArithParseTree


class GraphicInterface(QWidget):
    def __init__(self, arith_expr):
        self.parse_tree = ArithParseTree(arith_expr)
        print(self.parse_tree.get_expression())
        super().__init__()
        self.setWindowTitle(f'Parse Tree for {arith_expr}')
        self.initUI()


    def initUI(self):
        self.setMinimumSize(100, 100)
        self.setGeometry(500, 100, 600, 600)

        # start window
        self.showMaximized()


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        font = QFont('Arial', FONT_SIZE)
        font.setBold(True)
        qp.setFont(font)
        self.draw_graph(qp, START_Y, self.parse_tree.tree, 0, 2 * START_X, NODE_SIZE, FONT_SIZE, DISP_Y)
        qp.end()


    # ! coordinates are the center of the two nodes
    #   - the first are for the father node
    #   - the second are for the child node
    def draw_line_nodes(self, qp, from_x, from_y, to_x, to_y, node_size):
        qp.drawLine(from_x + int(node_size / 2), from_y + node_size, to_x + int(node_size / 2), to_y)


    def center_text_coordinates(self, x, y, data, node_size, font_size):
        nr = int(node_size / font_size) - len(data)
        if nr < 0:
            nr = 0
        x_cent = x + int(nr * font_size / 2)

        y_cent = y + int(font_size / 3)
        return x_cent, y_cent


    def draw_node(self, qp, x, y, data, node_size, font_size):
        qp.drawEllipse(x, y, node_size, node_size)
        x_cent, y_cent = self.center_text_coordinates(x, y, data, node_size, font_size)
        font = QFont('Arial', font_size)
        font.setBold(True)
        qp.setFont(font)
        qp.drawText(x_cent, y_cent + int(node_size / 2), data)


    def draw_graph(self, qp, current_y, node, limit_left, limit_right, node_size, font_size, displacement_y):
        current_x = int((limit_right + limit_left) / 2)
        self.draw_node(qp, current_x, current_y, node.data, node_size, font_size)

        if node.left != None:
            self.draw_line_nodes(qp, current_x, current_y, int((current_x + limit_left) / 2),\
                                 current_y + displacement_y, node_size)
            self.draw_graph(qp, current_y + displacement_y, node.left, limit_left, current_x, \
                            int(MINIMIZER_SIZE * node_size), int(MINIMIZER_SIZE * font_size), \
                            int(MINIMIZER_DISP * displacement_y))
        if node.right != None:
            self.draw_line_nodes(qp, current_x, current_y, int((current_x + limit_right) / 2),\
                                 current_y + displacement_y, node_size)
            self.draw_graph(qp, current_y + displacement_y, node.right, current_x, limit_right, \
                            int(MINIMIZER_SIZE * node_size), int(MINIMIZER_SIZE * font_size), \
                            int(MINIMIZER_DISP * displacement_y))