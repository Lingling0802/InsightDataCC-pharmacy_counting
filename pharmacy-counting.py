
drug_name = 'drug_name'
num_prescriber = 'num_prescriber'
total_cost = 'total_cost'
drug_cost = 'drug_cost'

def main():
    input_path = './input/itcont.txt'
    input_file = open(input_path)
    keys = [input_file.readline().strip()][0].strip().split(',')
    mapped_data_list =[]
    #mapping data to {'id': {}, 'prescriber_last_name': {}, 'prescriber_first_name': {}, 'drug_name': {}, 'drug_cost': {}} formattion
    for line in input_file:    
        mapped_data = {}
        entry = line.strip().split(',')
        length = 0
        for key in keys:
            mapped_data[key]= entry[length]
            length +=1
        mapped_data_list.append(mapped_data)
    #calculate drug drug's num of prescribers and total cost 
    processed_data_list = process_data(mapped_data_list)
    #sorting processed data
    sorted_data_list = sorted(processed_data_list, key = lambda x: (float(x[total_cost]), int(x[num_prescriber])), reverse = True)
    #write data to output file
    write_output(sorted_data_list)
    
#process raw data, calculate each drug's num of prescribers and total cost 
def process_data(data):
    processed_data_list = []
    drug_list = []
    i=0
    while i < len(data):
        #add drug_name to drug_list and its data to data_list if it is not in drug_list
        if data[i][drug_name] not in drug_list:
            processed_data = {}
            processed_data[drug_name]=data[i][drug_name]
            processed_data[num_prescriber]=1
            processed_data[total_cost]=data[i][drug_cost]
            processed_data_list.append(processed_data)
            drug_list.append(data[i][drug_name])
        #caluclate total_cost and increment num_prescriber if drug_name is in drug_list already
        else:
            processed_data_list[find_in_sublist(processed_data_list, data[i][drug_name], drug_name)][num_prescriber]+=1
            processed_data_list[find_in_sublist(processed_data_list, data[i][drug_name], drug_name)][total_cost]= float(processed_data_list[find_in_sublist(processed_data_list, data[i][drug_name], drug_name)][total_cost])+ float(data[i][drug_cost])            
        i+=1
    return processed_data_list

#find index of an item in a list of lists 
def find_in_sublist(lst, item, key):
    ind = [i for i, sublist in enumerate(lst) if item in sublist[key]]
    return ind[0]
  
#Write data into output file
def write_output(lst):
    output_path = './output/top_cost_drug.txt'
    output_file = open(output_path,'w')
    header = drug_name + ',' + num_prescriber + ',' + total_cost + '\n'
    output_file.write(header)
    i=0 
    while i < len(lst):
        output_file.write("{},{},{}\n".format(lst[i][drug_name],lst[i][num_prescriber],lst[i][total_cost]))
        i+=1
       
if __name__ == '__main__':
    main()
