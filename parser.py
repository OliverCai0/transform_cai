from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    yes = open(fname,'r')
    yesr = yes.read().split('\n')
    index = 0
    o_matrix = new_matrix()
    t_matrix = transform
    while (index < len(yesr)):
      if yesr[index] == 'line':
            a = yesr[index + 1].split(' ')
            add_edge(o_matrix,int(a[0]),int(a[1]),int(a[2]),int(a[3]),int(a[4]),int(a[5]))
            index += 2
      elif yesr[index] == 'ident':
            ident(t_matrix)
            index += 1
      elif yesr[index] == 'scale':
            a = yesr[index + 1].split(' ')
            print(a)
            m = make_scale(int(a[0]),int(a[1]),int(a[2]))
            matrix_mult(m,t_matrix)
            index += 2
      elif yesr[index] == 'rotate':
            a = yesr[index + 1].split(' ')
            if a[0] == 'x':
                  r = make_rotX(int(a[1]))
            elif a[0] == 'y':
                  r = make_rotY(int(a[1]))
            elif a[0] == 'z':
                  r = make_rotZ(int(a[1]))
            matrix_mult(r,t_matrix)
            index += 2
      elif yesr[index] == 'apply':
            matrix_mult(t_matrix,o_matrix)
            index += 1
      elif yesr[index] == 'display':
            clear_screen(screen)
            draw_lines(o_matrix,screen,color)
            display(screen)
            index += 1
      elif yesr[index] == 'save':
            clear_screen(screen)
            draw_lines(o_matrix)
            save_extension(screen,fname)
            index += 1
      else:
            index = len(yesr)



      
