

# OOP Version: Take roughly 11 seconds to process
import sys

class H1BCounts:
    def __init__(self, input_file, output_top10_job, output_top10_state):
        self.total_certified = 0
        self.input_file = input_file
        self.output_top10_job = output_top10_job
        self.output_top10_state = output_top10_state
        self.job_dict = {}
        self.state_dict = {}
        self.sort_job = []
        self.sort_state = []

        # Create both two headers for writing files afterward
        self.job_header = "TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE"
        self.state_header = "TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE"

    def read_data(self, input_file, filter_column):
        with open(self.input_file, "r") as f:
            headers = f.readline().split(";")

            for line in f:
                values = line.split(";")
                raw_data = dict(zip(headers, values))

                if raw_data['CASE_STATUS'] != "CERTIFIED":
                    continue

                self.job_dict[raw_data['SOC_NAME']] = self.job_dict.get(raw_data['SOC_NAME'], 0) + 1
                self.state_dict[raw_data['WORKSITE_STATE']] = self.state_dict.get(raw_data['WORKSITE_STATE'], 0) + 1
                self.total_certified += 1


    # Sort top 10 job counts and state counts in a descending order
    def sort_top10(self):
        self.sort_job = sorted(self.job_dict.items(), key = lambda s: (s[1], s[0]), reverse = True)[:10]
        self.sort_job = [list(elem) for elem in self.sort_job]

        self.sort_state = sorted(self.state_dict.items(), key = lambda s: (s[1], s[0]), reverse = True)[:10]
        self.sort_state = [list(elem) for elem in self.sort_state]


    # Calculate the percentage rounding to 1st digit: (Numbers of specific counts / Total "CERTIFIED" case) * 100
    def percentage(self):
        for i in range(len(self.sort_job)):
            self.sort_job[i].append(round(self.sort_job[i][1] / self.total_certified * 100, 1))

        for i in range(len(self.sort_state)):
            self.sort_state[i].append(round(self.sort_state[i][1] / self.total_certified * 100, 1))


    # Output files
    def write_output_job(self):
        with open(self.output_top10_job, 'w') as f:
            f.write(self.job_header + '\n')
            for row in self.sort_job:
                output = row[0] + ';' + str(row[1]) + ';' + str(row[2]) + '%'
                f.write(output + '\n')

    def write_output_state(self):
        with open(self.output_top10_state, 'w') as f:
            f.write(self.state_header + '\n')
            for row in self.sort_state:
                output = row[0] + ';' + str(row[1]) + ';' + str(row[2]) + '%'
                f.write(output + '\n')

def H1BCount(input_file, output_top10_job, output_top10_state):
    print("Start processing the data!")

    result = H1BCounts(input_file, output_top10_job, output_top10_state)
    job = result.read_data(input_file, 'SOC_NAME')
    state = result.read_data(input_file, 'WORKSITE_STATE')

    print("Loading data - Finished!!")

    # Sort top 10 occupations and states based on the number of individual counts (descending order) and the names (alphabetical order)
    result.sort_top10()

    # Use "percentage" function to calculate: (Numbers of specific counts / Total "CERTIFIED" case) * 100
    result.percentage()

    # Output two txt files: top_10_occupations.txt and top_10_states.txt
    result.write_output_job()
    result.write_output_state()

    print("Output files successfully!")

if __name__ == '__main__':
    H1BCount(sys.argv[1], sys.argv[2], sys.argv[3])


# Non-OOP Version: Save raw data into a list, which takes 20 seconds to process
#import sys
#
#
## Our main function
#
#def H1BCount(input_file, output_top10_job, output_top10_state):
#
#    # open file first
#    with open(input_file, 'r') as f:
#        raw_data = []
#        for row in f:
#            rows = row.split(";")
#            raw_data.append(rows)
#
#    # Extract the header and convert the raw_data to a dictionary datatype to decrease the complexity
#    # Only save the "CERTIFIED" data
#    header = raw_data[0]
#    certified_data = [dict(zip(header, value)) for value in raw_data[1:] if 'CERTIFIED' in value]
#
#    # Use "count_freq" function to get job counts and state counts (all in dictionary datatype)
#    job = count_freq(certified_data, 'SOC_NAME') #If it's before year 2014, needs to change to 'LCA_CASE_SOC_NAME'
#    state = count_freq(certified_data, 'WORKSITE_STATE') #If it's before year 2014, needs to change to 'LCA_CASE_WORKLOC1_STATE'
#
#    # Use "sort_top10" function to sort top 10 job counts/state counts with descending order
#    sort_job = sort_top10(job)
#    sort_state = sort_top10(state)
#
#    # Get the total numbers of "CERTIFIED" case
#    total_certified = len(certified_data)
#
#    # Use "percentage" function to calculate: (Numbers of specific counts / Total "CERTIFIED" case) * 100
#    job_per = percentage(sort_job, total_certified)
#    state_per = percentage(sort_state, total_certified)
#
#    # Create both two headers for writing files afterward
#    top10_job_header = "TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE"
#    top10_state_header = "TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE"
#
#    # Output two txt files: top_10_occupations.txt and top_10_states.txt
#    write_output(output_top10_job, top10_job_header, job_per)
#    write_output(output_top10_state, top10_state_header, state_per)
#
#
## Get job counts and state counts in dictionary datatype
#def count_freq(file, filter_str):
#    temp_dict = {}
#    for row in file:
#        keys = row[filter_str]
#        if filter_str == 'SOC_NAME':
#            temp_dict[keys] = temp_dict.get(keys, 0) + 1
#        elif filter_str == 'WORKSITE_STATE':
#            temp_dict[keys] = temp_dict.get(keys, 0) + 1
#    return temp_dict
#
#
## Sort top 10 job counts and state counts in a descending order
#def sort_top10(file):
#    sort = sorted(file.items(), key = lambda s: s[1], reverse = True)[:10]
#    sort = [list(elem) for elem in sort]
#    return sort
#
#
## Calculate the percentage rounding to 1st digit: (Numbers of specific counts / Total "CERTIFIED" case) * 100
#def percentage(file, total_certified):
#    for i in range(len(file)):
#        file[i].append(round(file[i][1] / total_certified * 100, 1))
#    return file
#
#
## Output files
#def write_output(output_filename, file_header, input_list):
#    with open(output_filename, 'w') as f:
#        f.write(file_header + '\n')
#        for row in input_list:
#            output = row[0] + ';' + str(row[1]) + ';' + str(row[2]) + '%'
#            f.write(output + '\n')
#
#
#if __name__ == '__main__':
#    H1BCount(sys.argv[1], sys.argv[2], sys.argv[3])


