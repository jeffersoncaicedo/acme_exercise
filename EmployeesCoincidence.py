from datetime import datetime
import sys


def open_file(src):
    with open(src) as file:
        data = file.readlines()
        file.close()
    organize_data(sets_of_data = data)


def organize_data(sets_of_data):
    companydata = []
    for i in range(len(sets_of_data)):
        nameemployes, days = sets_of_data[i].strip("\n").split("=")
        employeesdata = {}
        for workday in days.split(","):
            day = workday[0:2]
            if '-' in workday:
                employeesdata[day + '_entry'] = workday.split('-')[0][2:]
                employeesdata[day + '_departure'] = workday.split('-')[1]
        employeesdata['employee'] = nameemployes
        companydata.append(employeesdata)
    claculate_coincidence(companydata = companydata)
    

def claculate_coincidence(companydata):
    for i, employee1 in enumerate(companydata):
        for employee2 in companydata[i + 1:]:
            count = 0
            for key, value in employee1.items():
                for key2, value2 in employee2.items():
                    if key2 != 'employee':
                        if key == key2:
                            if "_entry" in key and "_entry" in key2:
                                entryemployee1 = value
                                entryemployee2 = value2
                            if "_departure" in key and "_departure" in key2:
                                departureemployee1 = value
                                departureemployee2 = value2
                                if (datetime.strptime(entryemployee1, '%H:%M') < datetime.strptime(departureemployee2, '%H:%M') and
                                    datetime.strptime(entryemployee2, '%H:%M') < datetime.strptime(departureemployee1, '%H:%M')):
                                    count += 1
            print_results(employee1 = employee1, employee2 = employee2, count = count)
            

def print_results(employee1, employee2, count):
    if count > 0:
        print(employee1['employee'] + "-" + employee2['employee'] + ":" + str(count))
        

if __name__ == "__main__":
    open_file(sys.argv[1]) 