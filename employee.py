employee = [
    ['male', 20, 8000000, 'Kendaraan pribadi'],
    ['male', 35, 14000000, 'Kendaraan umum'],
    ['female', 26, 10000000, 'Kendaraan umum'],
    ['female', 27, 12000000, 'Kendaraan pribadi'],
    ['male', 21, 9000000, 'Kendaraan pribadi'],
    ['male', 22, 11000000, 'Kendaraan pribadi'],
    ['female', 32, 15000000, 'Kendaraan umum'],
    ['female', 26, 8000000, 'Kendaraan umum'],
    ['male', 25, 9000000, 'Kendaraan umum'],
    ['female', 20, 10000000, 'Kendaraan pribadi'],
]

greatest_salary = employee[0][2]
smallest_salary = employee[0][2]

for item in employee:
	position = "not officer"
	salary = item[2]

	if salary >= 8000000 and salary <= 9000000:
		position = "officer"
	elif salary >= 10000000 and salary <= 11000000:
		position = "supervisor"
	elif salary >= 12000000 and salary <= 14000000:
		position = "asisten manajer"
	elif salary >= 15000000:
		position = "manager"

	print("Gaji: Rp{}, posisi: {}".format(salary, position))

	if salary > greatest_salary:
		greatest_salary = salary
	

	if salary < smallest_salary:
		smallest_salary = salary
	
print("\n")
print("Gaji terbesar adalah: Rp{}".format(greatest_salary))
print("Gaji terkecil adalah: Rp{}".format(smallest_salary))