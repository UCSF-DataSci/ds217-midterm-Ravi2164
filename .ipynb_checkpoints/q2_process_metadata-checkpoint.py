#!/usr/bin/env python3 

def parse_config (filepath:str) -> dict:
    config = {}
    with open(filepath, 'r')as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'): 
                continue 

            if '=' in line:
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
    return config 



# TODO: Add shebang line: #!/usr/bin/env python3
# Assignment 5, Question 2: Python Data Processing
# Process configuration files for data generation.
    """
    Parse config file (key=value format) into dictionary.
    
    Args:
        filepath: Path to q2_config.txt

    Returns:
        dict: Configuration as key-value pairs

    Example:
        >>> config = parse_config('q2_config.txt')
        >>> config['sample_data_rows']
        '100'
    """
    # TODO: Read file, split on '=', create dict
    pass


def validate_config(config: dict) -> dict:
    results = {}
    #validate int> 0 
    if 'sample_data_rows' in config: 
        try: 
            value = int(config['sample_data_rows'])
            if value >0:
                 results['sample_data_rows'] = True
            else:
                results['sample_data_rows'] =False
        except (ValueError, AttributeError):
            results['sample_data_rows'] = False

# valiadate sample_data_min must be an int and >= 1
    if 'sample_data_min' in config:
        try:
            value = int(config['sample_data_min']) 
            if value >=1:
                results['sample_data_min'] = True
            else:
                results['sample_data_min']= False
        except (VlalueError,AttibuteError):
            results[ 'sample_datat_min'] = False
            
# validate sample_data_max must be an int and > sample_data_min
    if 'sample_data_max' in config:
        try:
            value = int(config['sample_data_max'])
            min_value = int(config.get('sample_data_min', 1))
            max_value = int(config.get('sample_data_max', 0))
            if max_value > min_value:
                results['sample_data_max'] =True
            else:
                 results['simple_data_max'] = False
        except (ValueError,AttributeError):
            results['sample_data_max'] = False
    return results 


    """
    Validate configuration values using if/elif/else logic.

    Rules:
    - sample_data_rows must be an int and > 0
    - sample_data_min must be an int and >= 1
    - sample_data_max must be an int and > sample_data_min

    Args:
        config: Configuration dictionary

    Returns:
        dict: Validation results {key: True/False}

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> results = validate_config(config)
        >>> results['sample_data_rows']
        True
    """
    # TODO: Implement with if/elif/else
    pass

import random 
def generate_sample_data(filename: str, config: dict) -> None:
    #random sample generation:
    
    if 'sample_data_rows' in config and 'sample_data_min' in config and 'sample_data_max' in config :
        try:
            rows = int(config.get('sample_data_rows', '100 '))
            min_value = int(config.get('sample_data_min', '18'))
            max_value = int(config.get('sample_data_max','75'))
              
# generate random nr.: 
            with open (filename, 'w') as f:
                for _ in range(rows):
                    number = random.randint(min_value, max_value) 
                    f.write (f"{number}\n") 
        
        except (ValueError,Keyerror) as e:
            print (f"invalid config values: {e}")
        
        except FilenotFoundError:
            print(f"Error:the path '{filename}' is invalid.")
    else: 
        print("file created, no errors found.")

#print(f"generated {rows} random numbers between {min_value} and {max_value} in {filename}") 

import csv  
def read_data(filename: str) -> list:
    data = []
    try:
        with open (filename, "r") as f: 
            for line in f: 
                line = line.strip ()
                if line:
                    data.append(int(line))
    except FilenotFoundError:
        print(f"file not found: {filename}") 
    except ValueError as e:
        print(f"Invalid nr. in file: {e}")
    return data 


def calculate_statistics(data: list) -> dict:
    """
    Calculate basic statistics.

    Args:
        data: List of numbers

    Returns:
        dict: {mean, median, sum, count}

    Example:
        >>> stats = calculate_statistics([10, 20, 30, 40, 50])
        >>> stats['mean']
        30.0
    """
    # TODO: Calculate stats
    pass
    n= len(data) 
    if n==0 :
        return{'count': 0 , 'sum':0 , 'mean':None, 'median':None, 'min': None, 'max':None}

    #sort the data 
    sorted_data = sorted(data)
    #cal mean
    total_sum = sum(sorted_data)
    mean = total_sum /n 
    #cal median
    if n %2 ==1: 
        median_value = sorted_data[n//2]
    else: 
        median_value = (sorted_data[n // 2-1] + sorted_data[n // 2]) / 2 
    return {
            "count": n,
            "sum": total_sum,
            "mean": mean,
            "median": median_value
    }


  
def main():
    config = parse_config('q2_config.txt')
    validation = validate_config(config)
    print ("validation reults:", validation)
    if not all (validation.values()): 
        print ("Invalid configuration.")
        return 
        # generate sample_data
        generate_sample_data("data/sample_data.csv", config) 
        data = read_data("data/sample_data.csv")
        print(f"first 10 data point: {data[:10]} (total {len(data)})")
        if not data: 
            print("no data to process.")
            return
        stats = calculate_statistics(data)
        print("statistics calculated:", stats)
        os.makedirs("output", exist_ok=True)
        with open ("output/statistics.txt", "w") as f:
            for key, value in stats.items():
                f.write(f"{key}: {value}\n")
        print("statistics saved to output/statistics.txt")

        save_statistics ( stats, 'output/statistics.txt')
  

if __name__ == '__main__':
    main()
    """ 
    # TODO: Test your functions with sample data
    # Example:
    # config = parse_config('q2_config.txt')
    # validation = validate_config(config)
    # generate_sample_data('data/sample_data.csv', config)
    # 
    # TODO: Read the generated file and calculate statistics
    # TODO: Save statistics to output/statistics.txt
    """
    
  
        
    
