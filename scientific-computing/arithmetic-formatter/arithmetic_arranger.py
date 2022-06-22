def arithmetic_arranger(problems, *args):
    def _arrange_space(first_operand, second_operand):
      spaces = ' ' * 2
      if len(first_operand) >= len(second_operand):
        return spaces
      else:
        return spaces + ' ' * (len(second_operand) -len(first_operand))
  
    if len(problems) > 5:
      return 'Error: Too many problems.'

    problems_in_partitions = []
    arranged_problems = ''
    show_result = args[0] if args else False
    for i, problem in enumerate(problems):
      first_operand, operator, second_operand = problem.split(' ')
      if operator not in ('+', '-'):
        return "Error: Operator must be '+' or '-'."
      elif not first_operand.isnumeric() or not second_operand.isnumeric():
        return 'Error: Numbers must only contain digits.'
      elif len(first_operand) > 4 or len(second_operand) > 4:
        return 'Error: Numbers cannot be more than four digits.'

      problems_in_partitions.append({
        'operands': [first_operand, second_operand],
        'operator': operator,
        'result': (
          str(int(first_operand) + int(second_operand))
          if operator == '+'
          else str(int(first_operand) - int(second_operand))
        ),
        'spaces': 2 + max(len(first_operand), len(second_operand))
      })
        
      # first line
      arranged_problems += _arrange_space(first_operand, second_operand)
      arranged_problems += first_operand
      if i + 1 != len(problems):
        arranged_problems += ' ' * 4
      else:
        arranged_problems += '\n'

      if i == len(problems) - 1:
        # second line
        for j, partition in enumerate(problems_in_partitions):
          arranged_problems += partition['operator'] + ' '
          arranged_problems += ' ' * (len(partition['operands'][0]) - len(partition['operands'][-1])) if len(partition['operands'][-1]) < len(partition['operands'][0]) else ''
          arranged_problems += partition['operands'][-1]

          if j + 1 != len(problems_in_partitions):
            arranged_problems += ' ' * 4
          else:
            arranged_problems += '\n'
        # third line
        for k, partition in enumerate(problems_in_partitions):
          arranged_problems += '-' * partition['spaces']
          if k + 1 != len(problems_in_partitions):
            arranged_problems += ' ' * 4
          elif show_result:
            arranged_problems += '\n'
        # last line
        if show_result:
          for l, partition in enumerate(problems_in_partitions):
            arranged_problems += ' ' * (partition['spaces'] - len(partition['result']))
            arranged_problems += partition['result']
            if l + 1 != len(problems_in_partitions):
              arranged_problems += ' ' * 4
  
    return arranged_problems