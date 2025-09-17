

# bms,dst,ptm,wkn

orders=["bms","bms","bms","ptm","ptm","ptm","wkn","wkn","wkn","bms","bms","ptm"]

bms_count = 0
ptm_count = 0
wkn_count = 0

for ord in orders:

    if ord == "bms":
        bms_count += 1
        
    elif ord == "ptm":
        ptm_count += 1

    elif ord == "wkn":
        wkn_count += 1

# total_tiket_sold
total_tickets_sold = bms_count + ptm_count + wkn_count
print("Total tickets sold:" , total_tickets_sold)


# highest
if bms_count >= ptm_count and bms_count >= wkn_count:

    print("Highest ticket orders are from - book my show:" ,bms_count)

elif ptm_count >= bms_count and ptm_count >= wkn_count: 

    print("Highest ticket orders are from - paytm:" ,ptm_count)

elif wkn_count >= bms_count and wkn_count >= ptm_count:
    
    print("Highest ticket orders are from - walk in booking:" ,wkn_count)


# lowest
if bms_count <= ptm_count and bms_count <= wkn_count:

    print("Lowest ticket orders are from - book my show:" ,bms_count)

elif ptm_count <= bms_count and ptm_count <= wkn_count: 

    print("Lowest ticket orders are from - paytm:" ,ptm_count)

elif wkn_count <= bms_count and wkn_count <= ptm_count:
    
    print("Lowest ticket orders are from - walk in booking:" ,wkn_count)

