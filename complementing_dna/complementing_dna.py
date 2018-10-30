import time

complement_dict = {
    "A":"T",
    "T":"A",
    "C":"G",
    "G":"C"
}

def reverse_complement(s):
    return "".join([complement_dict[base] for base in s[::-1]])

def read_file(filename):
    with open(filename, 'r') as myfile:
        data = myfile.read().replace('\n', '')
        return data

def write_result(result):
    file = "result_{}.txt".format(int(time.time()))
    f = open(file, 'w')
    f.write(str(result))
    print("Written")
    f.close()

write_result(reverse_complement(read_file("rosalind_revc.txt")))