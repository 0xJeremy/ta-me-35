with open('raise_processed.csv', 'w') as outfile:
    with open('raise.csv', 'r') as infile:
        for line in infile:
            if line != "\n":
                outfile.write(line.strip() + '\n')
