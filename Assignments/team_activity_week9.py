
with open("Files/life-expectancy.csv") as life_expectancy:
    next(life_expectancy)
    year_interest = input("year: ")
    for line in life_expectancy:
        clean_line = line.strip()
        parts = clean_line.split(",")
        country = parts[0].strip()
        code = parts[1].strip()
        year = parts[2]
        life = float(parts[3])
        if year == year_interest:
            print(year,country,life)