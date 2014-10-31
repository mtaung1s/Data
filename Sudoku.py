import sys

class Error(Exception):
    pass

def row(i,j): 
	return (i/9 == j/9)
def column(i,j): 
	return (i-j) % 9 == 0
def block(i,j): 
	return (i/27 == j/27 and i%9/3 == j%9/3)
	
def export(result):
    out_file = open(sys.argv[2], 'w')
    out_file.truncate()
    
    rowcount = 1
    colcount = 1

    for r in result:
        print r,
        out_file.write(r)
        if colcount % 9 != 0:
            print ",",
            out_file.write(",")
        if colcount % 9 == 0:
            print ""
            out_file.write("\n")
            rowcount += 1
			
	colcount += 1

    out_file.close()


def slove(sudoku):
 
  zero = sudoku.find('0')
  if zero == -1:
    raise Error(sudoku)

  numbers = set()
  for other in range(81):
    if row(zero,other) or column(zero,other) or block(zero,other):
      numbers.add(sudoku[other])

  for num in '123456789':
    if num not in numbers:
      slove(sudoku[:zero]+num+sudoku[zero+1:])
	  	  	   
			   
if __name__ == '__main__':
  if len(sys.argv) == 3:
    filename = sys.argv[1]
    import_file = open(filename)
    sudoku = "".join([line.strip("\n").strip() for line in import_file.readlines()]).replace(",","")
    import_file.close()

    if len(sudoku) != 81:
        sys.exit("file must contain 81 digits")

    try:
        slove(sudoku)
    except Error as e:
        print "The answer is.\n"
        export(str(e))
  else:
    print 'Please input three arguements(frist: python_file.py, second: import_file.csv, third: export_file.csv)'
  