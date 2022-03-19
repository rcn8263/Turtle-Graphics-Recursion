"""
   Use turtle graphics and recursion to draw bowties

   assignment: Lab 2
   file: bowties.py
   author: Ryan Nowak
"""

# imports

import turtle as tt

# definitions


def draw_one_bowtie(size):
    """
    draw_one_bowtie draws a bowtie with filled-in circle in center

    pre-condition - pen is up, facing right
    post-condition - pen is up, facing right
    """
    tt.pencolor("blue")
    tt.fillcolor("red")
    tt.down()
    tt.left(30)
    tt.forward(size)
    tt.right(120)
    tt.forward(size)
    tt.right(120)
    tt.forward(size * 2)
    tt.left(120)
    tt.forward(size)
    tt.left(120)
    tt.forward(size)
    tt.right(120)
    tt.forward(size / 4)
    tt.left(90)
    tt.begin_fill()
    tt.circle(size / 4)
    tt.end_fill()
    tt.up()
    tt.left(90)
    tt.forward(size / 4)
    tt.right(90)


def draw_bowtie0():
    pass


def draw_bowtie1(size):
    """
    draw_bowtie1 calls the draw_one_bowtie function
    which then draws a single bowtie

    pre-condition - pen is up, facing east
    post-condition - pen is up, facing east
    """
    draw_one_bowtie(size)


def draw_bowtie2(size):
    """
    draw_bowtie2 calls the bowtie functions which then draw
    a bowtie with two more surrounding bowties

    pre-condition - pen is up, facing east
    post-condition - pen is up, facing east
    """
    draw_bowtie1(size)
    tt.left(30)
    tt.forward(size * 2)
    draw_bowtie1(size / 3)
    tt.back(size * 2)
    tt.left(120)
    tt.forward(size * 2)
    draw_bowtie1(size / 3)
    tt.back(size * 2)
    tt.right(150)


def draw_bowtie3(size):
    """
    draw_bowtie3 draws a bowtie with 2 surrounding bowties
    which each have 2 more surrounding bowties

    pre-condition - pen is up, facing east
    post-condition - pen is up, facing east
    """
    draw_one_bowtie(size)
    tt.left(30)
    tt.forward(size * 2)
    draw_bowtie2(size / 3)
    tt.back(size * 2)
    tt.left(120)
    tt.forward(size * 2)
    tt.right(180)
    draw_bowtie2(size / 3)
    tt.forward(size * 2)
    tt.left(30)


def draw_bowties(depth, size):
    """
    draw_bowties recursively calls itself to draw bowties with
    4 more surrounding bowties at each depth

    pre-condition - pen is up, facing east
    post-condition - pen is up, facing east
    """
    if depth == 0:
        pass
    elif depth == 1:
        draw_one_bowtie(size)
    else:
        draw_one_bowtie(size)
        tt.left(30)
        tt.forward(size * 2)
        draw_bowties(depth - 1, size / 3)
        tt.back(size * 2)
        tt.left(120)
        tt.forward(size * 2)
        tt.right(180)
        draw_bowties(depth - 1, size / 3)
        tt.forward(size * 2)
        tt.forward(size * 2)
        draw_bowties(depth - 1, size / 3)
        tt.back(size * 2)
        tt.right(120)
        tt.forward(size * 2)
        tt.right(180)
        draw_bowties(depth - 1, size / 3)
        tt.forward(size * 2)
        tt.right(30)


def main():
    tt.speed(0)
    tt.setup(600, 600)

    depth = int(input("Enter an integer for depth. "))
    draw_bowties(depth, 100)
    tt.done()


if __name__ == '__main__':
    main()
