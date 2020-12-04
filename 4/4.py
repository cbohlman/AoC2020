import re

def validate_byr(byr):
    if byr >= 1920 and byr <= 2002:
        return True
    else:
        return False

def validate_iyr(iyr):
    if iyr >= 2010 and iyr <= 2020:
        return True
    else:
        return False

def validate_eyr(eyr):
    if eyr >= 2020 and eyr <= 2030:
        return True
    else:
        return False

def validate_hgt(hgt):
    num = int(re.findall('\d+', hgt)[0])
    if (re.search('cm', hgt)):
        if num >= 150 and num <= 193:
            return True 
    elif (re.search('in', hgt)):
        if num >= 59 and num <= 76:
            return True
    
    return False    

def validate_hcl(hcl):
    if re.match('^#(?:[0-9a-fA-F]{6})$', hcl):
        return True
    return False

def validate_ecl(ecl):
    if re.match('amb|blu|brn|gry|grn|hzl|oth', ecl):
        return True
    return False

def validate_pid(pid):
    if re.match('^\d{9}$', pid):
        return True
    return False

def validate_passport(passport):
    byr = int(passport['byr'])
    iyr = int(passport['iyr'])
    eyr = int(passport['eyr'])
    hgt = passport['hgt']
    hcl = passport['hcl']
    ecl = passport['ecl']
    pid = passport['pid']
    
    # debugging
    print(validate_byr(byr))
    print(validate_eyr(eyr))
    print(validate_iyr(iyr))
    print(validate_hgt(hgt))
    print(validate_hcl(hcl))
    print(validate_ecl(ecl))
    print(validate_pid(pid))

    if (validate_byr(byr) and validate_eyr(eyr) and validate_iyr(iyr) and validate_hgt(hgt) and 
            validate_hcl(hcl) and validate_ecl(ecl) and validate_pid(pid)):
        return True
    else:
        return False


with open('4.txt', 'r') as f:
    input_lines = f.read()
    input_lines = re.split('\n\n',input_lines)
    passport_input = [re.split('\s+', line) for line in input_lines]
    passports = []
    for line in passport_input:
        passport = {}
        for field in line:
            data = field.split(':')
            passport[data[0]] = data[1]
        passports.append(passport)

    count1 = 0
    count2 = 0
    for passport in passports:
        if len(passport) == 8:
            count1 += 1
            if (validate_passport(passport)):
                count2 += 1
        elif len(passport) == 7 and 'cid' not in passport:
            count1 +=1
            if (validate_passport(passport)):
                count2 += 1

    print("Part 1:")
    print(count1)
    print("Part 2:")
    print(count2)

