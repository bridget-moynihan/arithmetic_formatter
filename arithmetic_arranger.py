def arithmetic_arranger(problems,answer=False):
  if len(problems) > 5:
    return("Error: Too many problems.")

  firstRow = []
  operands = []
  secondElems = []
  secondRow = []
  lastRow=[]
  answers = []
  for i in range(len(problems)):
    string= problems[i]
    prob = string.split()
    if prob[0].isdigit() and prob[2].isdigit():
      if len(prob[0]) <=4 and len(prob[2]) <= 4:
        if prob[1] == "+" or prob[1] == '-':
          correct = True
        else:
          return("Error: Operator must be '+' or '-'.")
      else:
        return("Error: Numbers cannot be more than four digits.")
    else:
        return("Error: Numbers must only contain digits.")
    # Max spaces to fill in the final print. We will find the longest operand and we add 
    # the operator's space and the space btw the operator and the second element
    max_spaces_to_fill = max(len(x) for x in prob)
    if i == len(problems) -1:
      firstRow.append(prob[0].rjust(max_spaces_to_fill+2))
      secondRow.append(prob[1] + " "+prob[2].rjust(max_spaces_to_fill))
      lastRow.append("-"*(max_spaces_to_fill+2))
      answers.append(str(eval(string)).rjust(max_spaces_to_fill+2))
    else:
      firstRow.append(prob[0].rjust(max_spaces_to_fill+2)+ " "*4)
      secondRow.append(prob[1] + " "+prob[2].rjust(max_spaces_to_fill)+" "*4)
      lastRow.append("-"*(max_spaces_to_fill+2) +" "*4)
      answers.append(str(eval(string)).rjust(max_spaces_to_fill+2)+" "*4)
    secondElems.append(prob[2])
    operands.append(prob[1])
  arranged_problems = "".join(firstRow) +"\n" + "".join(secondRow) + "\n" +"".join(lastRow)
  if answer==True:
    arranged_problems += "\n" +"".join(answers)
  return arranged_problems
