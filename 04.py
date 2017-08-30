finance_employees=20
accounting_employees=30
marketing_employees=50
total_employees=finance_employees+accounting_employees+marketing_employees

finance_salary=100
accounting_salary=150
marketing_salary=200

total_fin_cost=finance_employees*finance_salary
total_acc_cost=accounting_employees*accounting_salary
total_mar_cost=marketing_employees*marketing_salary
total_cost=total_fin_cost+total_acc_cost+total_mar_cost

print('There are '+ str(total_employees) +' employees in this company')

print('The hourly salary for finance background is: '+str(finance_salary)+' TWD')
print('The hourly salary for accounting background is: '+str(accounting_salary)+' TWD')
print('The hourly salary for marketing background is: '+str(marketing_salary)+' TWD')

print('The total employees cost is '+str(total_cost)+' TWD')