#the grade calculator for different modules
#CTI-110
# P2HW2 - List
# Mikayla Blakey
# 10/27/22
#
#
#--------------------------Pseudocode--------------------------
#Display 'Enter grade for module 1 here:'
#Input module 1
##Display 'Enter grade for module 2 here:'
#Input module 2
##Display 'Enter grade for module 3 here:'
#Input module 3
##Display 'Enter grade for module 4 here:'
#Input module 4
##Display 'Enter grade for module 5 here:'
#Input module 5
##Display 'Enter grade for module 6 here:'
#Input module 6
#Display '---------------------Results-----------------------'
#Display 'Lowest Grade'
#Display 'Highest Grade'
#Display 'Sum of Grades:'
#Display 'Average'



module_1 = float(input('Enter grade for module 1 here:'))
module_2 = float(input('Enter grade for module 2 here:'))
module_3 = float(input('Enter grade for module 3 here:'))
module_4 = float(input('Enter grade for module 4 here:'))
module_5 = float(input('Enter grade for module 5 here:'))
module_6 = float(input('Enter grade for module 6 here:'))

module_list = [module_1 , module_2 , module_3, module_4, module_5, module_6]

print('---------------------Results------------------------')
print('Lowest Grade:', min(module_list))
print('Highest Grade:', max(module_list))
print('Sum of Grades:', sum(module_list))
print('Average:', sum(module_list) / len(module_list))
print('---------------------------------------------------')
