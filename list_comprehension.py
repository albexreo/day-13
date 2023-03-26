print([(i,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(10)])

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

countries = [{'country': country, 'capital': capital} for [(country, capital)] in countries]
print(countries)
lists = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

lists = [" ".join(lst[0]) for lst in lists]
print(lists)
function = lambda m,x,c : (m*x) + c 
print(function(2,3,4))