''' Type your code here. '''
gas_mileage = float(input()) 
cost_of_gas = float(input())


gas_20_mil = 20.0 / gas_mileage
gas_75_mil = 75.0 / gas_mileage
gas_500_mil = 500.0 / gas_mileage

print(f'{(gas_20_mil * cost_of_gas):.2f} {(gas_75_mil * cost_of_gas):.2f} {(gas_500_mil * cost_of_gas):.2f}')