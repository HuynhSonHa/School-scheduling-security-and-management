from faker import Faker
import random

MASV = ["SV4880", "SV9738", "SV7875", "SV3938", "SV8666", "SV3902", "SV5069", "SV3609", "SV7695", "SV1285", "SV5457", "SV2295", "SV7614", "SV917", "SV4322", "SV1970", "SV4064", "SV8922", "SV7732", "SV4232", "SV7630", "SV5013", "SV4537", "SV8258", "SV885", "SV6", "SV2192", "SV7288", "SV349", "SV8115", "SV1538", "SV7850", "SV5208", "SV5362", "SV7936", "SV4021", "SV4576", "SV3994", "SV8175", "SV8374", "SV1577", "SV2089", "SV3509", "SV6854", "SV5338", "SV3100", "SV5356", "SV5963", "SV5905", "SV8486", "SV2935", "SV7814", "SV7969", "SV3749", "SV9000", "SV4476", "SV5368", "SV7956", "SV9038", "SV9624", "SV9795", "SV227", "SV7457", "SV6246", "SV1693", "SV3170", "SV1406", "SV4225", "SV273", "SV9562", "SV1616", "SV2213", "SV1912", "SV7565", "SV6841", "SV1127", "SV4747", "SV5480", "SV2490", "SV2709", "SV8829", "SV9670", "SV3755", "SV300", "SV8818", "SV5666", "SV5765", "SV4180", "SV6018", "SV6380", "SV2082", "SV1239", "SV2279", "SV4873", "SV6001", "SV4490", "SV3006", "SV9246", "SV2381", "SV2575", "SV4695", "SV2981", "SV6445", "SV6151", "SV3349", "SV1838", "SV2836", "SV8102", "SV668", "SV8040", "SV892", "SV1233", "SV4496", "SV6591", "SV4520", "SV3226", "SV9635", "SV7227", "SV1674", "SV1381", "SV9611", "SV1257", "SV1715", "SV7741", "SV5760", "SV8160", "SV1422", "SV4012", "SV4925", "SV7594", "SV5683", "SV2351", "SV3181", "SV8780", "SV6516", "SV2826", "SV4884", "SV7277", "SV4158", "SV1989", "SV8546", "SV3682", "SV2046", "SV5242", "SV7704", "SV6421", "SV9992", "SV8579", "SV40", "SV5453", "SV6042", "SV52", "SV7343", "SV7710", "SV2784", "SV4035", "SV4842", "SV8901", "SV3566", "SV4662", "SV3148", "SV3461", "SV3333", "SV472", "SV3253", "SV4806", "SV394", "SV4127", "SV8469", "SV2109", "SV3336", "SV1697", "SV1885", "SV2135", "SV9073", "SV9796", "SV9053", "SV378", "SV8967", "SV1812", "SV3427", "SV9835", "SV327", "SV6465", "SV6850", "SV4184", "SV3768", "SV2405", "SV1202", "SV9921", "SV1423", "SV8753", "SV9534", "SV2659", "SV2464", "SV9408", "SV4250", "SV8665", "SV9896", "SV518"]

data = "GV2039 HP1369 1 2024 CLC GV2038 HP5236 2 2023 CLC GV2038 HP2374 3 2023 CTTT GV2037 HP5236 3 2022 CQ GV2036 HP1369 1 2023 CQ GV2035 HP1923 3 2023 CQ GV2032 HP1369 2 2023 CTTT GV2031 HP5236 2 2024 CTTT GV2030 HP5236 1 2023 VP GV2025 HP5236 3 2024 VP GV2025 HP3306 2 2023 CTTT GV2019 HP5454 1 2022 CQ GV2019 HP1923 3 2024 CLC GV2017 HP5236 1 2022 VP GV2017 HP1923 1 2024 VP GV2016 HP1923 3 2024 VP GV2013 HP2374 3 2022 CQ GV2009 HP3704 1 2023 CQ GV2009 HP1923 3 2024 CQ GV2004 HP1923 1 2022 VP GV2003 HP1923 1 2023 CLC GV2002 HP3306 1 2023 CLC GV2000 HP5236 3 2023 VP GV1038 HP3306 3 2024 CQ GV1037 HP1369 1 2022 CLC GV1036 HP3306 1 2022 CQ GV1035 HP2374 2 2022 VP GV1034 HP3704 2 2023 CLC GV1033 HP5236 1 2022 CQ GV1032 HP3704 1 2023 CLC GV1032 HP2374 2 2024 CQ GV1031 HP3704 3 2024 CQ GV1029 HP3704 2 2022 CQ GV1026 HP3704 2 2024 VP GV1024 HP2374 1 2023 VP GV1023 HP5236 1 2024 CQ GV1021 HP5236 2 2023 CQ GV1020 HP1369 2 2024 CTTT GV1017 HP1923 1 2022 CQ GV1015 HP2374 2 2023 VP GV1015 HP1369 3 2024 CQ GV1012 HP3306 2 2022 CLC GV1011 HP3306 1 2024 CLC GV1010 HP5236 3 2024 CLC GV1010 HP3306 1 2022 VP GV1010 HP2374 1 2023 CQ GV1009 HP5236 3 2023 CQ GV1005 HP1923 2 2024 CLC GV1005 HP1369 3 2023 CTTT GV1002 HP2374 1 2024 CTTT"
elements = data.split()

for i in range(0, len(elements), 5):
    masv=random.choice(MASV)
    MAGV, MAHP, HK, NAM, MACT = elements[i:i+5]
    DIEMTH = round(random.uniform(0, 10), 2)
    DIEMQT = round(random.uniform(0, 10), 2)
    DIEMCK = round(random.uniform(0, 10), 2)
    DIEMTK = round((DIEMTH + DIEMQT + DIEMCK) / 3, 2)

    print(f"INSERT INTO DANGKY (MASV,MAGV, MAHP, HK, NAM, MACT, DIEMTH, DIEMQT, DIEMCK, DIEMTK) VALUES ('{masv}','{MAGV}', '{MAHP}', '{HK}', {NAM}, '{MACT}', {DIEMTH}, {DIEMQT}, {DIEMCK}, {DIEMTK});")