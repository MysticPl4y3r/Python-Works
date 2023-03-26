total_sec=0
retry='Y'

while True:
    time=str(input("Enter time (mm:ss) :"))
    minute=int(time[0:2])
    second=int(time[3:5])
    seconds=minute*60+second
    total_sec+=seconds
    
    retry=input("Do you want to add more? (y/n)")
    if retry.upper()=='N':
        break


full_minutes=int(total_sec/60)
full_seconds=int(total_sec%60)

full_hours=int(total_sec/(60*60))
full_hmin=int(total_sec%60)

if full_minutes>60:
    print("Total time= %2d Hour %2d Minutes %2d Seconds" %(full_hours,full_hmin,full_seconds))
else:
    print("Total time= %2d Minutes %2d Seconds" %(full_minutes,full_seconds))
