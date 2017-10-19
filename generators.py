import string
# Marks the first pokedex entry for each generation
generation = [1,152,252,367,494,650,722,803]

# Generates HTML for a specified range of generations 
def selector_generator(startgen, endgen):
	# Get to the correct pokedex entries from generation number
	script_generate_start = generation[startgen - 1]
	script_generate_end = generation[endgen]-1
	
	file = open('Pokemon List By Number - Sheet1.csv','r')
	output = ''
	
	# It makes sense to iterate over pokedex entries as is, (remember that generation[7] is the start of gen 8)
	for i in range(1, generation[7]) :
		if i < script_generate_start :
			file.readline()
			continue
		if i <= script_generate_end :
			input = file.readline().split(',')
			dex_number = input[0]
			name = input[1]
			type1 = input[2]
			if len(input) == 4 :
				type2 = input[3]
			output = output + 'option.species-selector(){} {}\n'.format(dex_number, name)
			continue
		print(i)
		file.close()
		break
	
	outfile = open('output', 'w')
	outfile.write(output)
	outfile.close()

	