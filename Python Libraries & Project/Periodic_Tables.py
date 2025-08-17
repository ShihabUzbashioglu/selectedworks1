import PeriodicTables

#get details of an elements by atomic number

atomic_no = int(input("enter element atomic no :"))

element = PeriodicTables.elements[atomic_no]

print('atomic number :',element.number )
print('symbol :',element.symbol )
print('name :',element.name )
print('atomic mass :',element.mass )
print('density :',element.density )