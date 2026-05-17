# File I/O and Data Workflows - Starter Code

# Task 1: Read and Display File Contents
def read_file(filename):
    """
    Read a file and return its contents.
    
    Args:
        filename (str): Path to the file to read
        
    Returns:
        str: The contents of the file
    """
    # TODO: Open the file using a with statement and read its contents
    pass


# Task 2: Process Data Line-by-Line
def process_data(filename):
    """
    Read a file and process each line.
    
    Args:
        filename (str): Path to the file to read
        
    Returns:
        list: A list of processed data
    """
    processed_data = []
    
    # TODO: Open the file and read it line-by-line
    # TODO: For each line, extract/transform the data
    # TODO: Store results in processed_data list
    
    return processed_data


# Task 3: Write Results to a New File
def write_results(output_filename, data, headers=None):
    """
    Write processed data to a new file.
    
    Args:
        output_filename (str): Path to the output file
        data (list): List of data to write
        headers (list, optional): Column headers to write first
    """
    # TODO: Open a new file for writing
    # TODO: If headers are provided, write them as the first line
    # TODO: Write each data item to the file
    pass


# Example usage
if __name__ == "__main__":
    # Task 1: Read a sample file
    input_file = "sample_data.txt"
    content = read_file(input_file)
    print("File Contents:")
    print(content)
    
    # Task 2: Process the data
    processed = process_data(input_file)
    print("\nProcessed Data:")
    print(processed)
    
    # Task 3: Write results to a new file
    output_file = "results.txt"
    write_results(output_file, processed)
    print(f"\nResults written to {output_file}")
