import re
import pandas as pd

data = []
with open('Dataset.txt', 'r', encoding="utf8") as file:
    while True:
        # Get next line from file
        line = file.readline()
        # if line is empty
        # end of file is reached
        if not line:
            break
        result = re.search(r"\[(.*?)].*\[(.*?)]: (.*$)", line)
        if not result.group(3):
            continue
        depp = 0
        amber = 0
        if any(re.findall(r'Depp|Johnny|John|jhonny|Captain|Jack|Sparrow| JD | He | Him |Monster|Drunk|Addict|Actor|Abuser',
                          result.group(3),
                          re.IGNORECASE)):
            depp = 1
        if any(re.findall(
                r'Amber|Heard|Survivor|Victim|Brave|Courageous|Actress|Liar|Accuser|Gold|Digger|Turd|Narcissist| She | Her |Bitch| AH',
                result.group(3),
                re.IGNORECASE)):
            amber = 1

        data.append({"time": result.group(1), "user": result.group(2), "comment": result.group(3), "depp": depp , "amber": amber})

df = pd.DataFrame(data)

df.to_csv('day1.csv', sep=',', escapechar='%', encoding='utf-8', index=False, header=True)
