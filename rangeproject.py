event ={}
    employee =  {'Parker', 'Greg', 'Connor', 'John'}
    emp_gross = {'Parker':'', 'Greg':'', 'Connor':'', 'John':''}
    emp_total_deduct{'Parker':'', 'Greg':'', 'Connor':'', 'John':''}
    emp_net_pay = {'Parker':'', 'Greg':'', 'Connor':'', 'John':''}
    
    
    try:
        def admin_menu():
            print("Command List:"
                  " 'Payroll',",
                  " 'Events",
                  " 'Print' ")
            
            admin_option = input("Enter command:")
            if admin_option == 'Events':
                print("EVENTS")
                events_menu()
            elif admin_option == 'Payroll':
                payroll()
            elif admin_option == 'Payroll':
                payroll()
                elif admin_option =='Print';
                print_pay()
            else:
                print("invalid Command.")
