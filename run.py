import os
import csv
import pendulum

# folder to store the files in same format as the .dat file, but split into different foles for each customer
divided_output_dir = "divided"
solar_output_dir = "solar_only"

os.system("mkdir "+divided_output_dir)
os.system("mkdir "+solar_output_dir)


with open('CD_INTERVAL_READING.csvHdr') as f:
    header = f.readline()
print(header)




customer_key = ""
idx = 0
indicator = 0
with open('CD_INTERVAL_READING.dat') as f:
    for line in f:
        idx += 1
        if idx % 4000000 == 0:
            print(indicator, idx)
            indicator += 1
        key = line.split(',')[0]

        # Check if key matches the previous line's key
        # If it doesn't match, make a new file.
        if key != customer_key:
            # print(key)
            # Set the customer key to the current line's key.
            customer_key = key
            # Create a new csv file
            file_path = os.path.join(divided_output_dir,key+".csv")
            if not os.path.isfile(file_path):
                outfile = open(file_path, "a")
                outfile.write(header)
            else:
                outfile = open(file_path, "a")
            
        outfile.write(line)

        

            
        




for filename in os.listdir(divided_output_dir):
    if filename.endswith(".csv"): 
        print(os.path.join(divided_output_dir, filename))
        file = open(os.path.join(divided_output_dir, filename))
        reader = csv.DictReader(file)
        outfile = open(os.path.join(solar_output_dir, filename), 'w+')
        outfile.write("HHE,solar\n")
        for line in reader:
            # print(line)
            write_line = pendulum.parse(line[' READING_DATETIME']).format('d/MM/YYYY h:mm')+","+line[' GROSS_GENERATION_KWH']
            outfile.write(write_line+"\n")
        continue
    else:
        continue