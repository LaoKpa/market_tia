import sys
import tables
from lib.db_curators import db_curator as db

anomalous = [1312118578000000,
1312118658000000,
1312118723000000,
1312118791000000,
1312118858000000,
1312118919000000,
1312119158000000,
1312119283000000,
1312119350000000,
1312119425000000,
1312119497000000,
1312119561000000,
1312119621000000,
1312119760000000,
1312119909000000,
1312120014000000,
1312120078000000,
1312120138000000,
1312120238000000,
1312120314000000,
1312120420000000,
1312120584000000,
1312120650000000,
1312120711000000,
1312758208000000,
1312760900000000,
1312861524000000,
1312886905000000,
1312903374000000,
1312903439000000,
1313074304000000,
1313079629000000,
1313081662000000,
1313081723000000,
1313082241000000,
1313082302000000,
1313082363000000,
1313082606000000,
1313082873000000,
1313099114000000,
1313126000000000,
1313175708000000,
1313175769000000,
1313189319000000,
1313189379000000,
1313189440000000,
1313189500000000,
1313189561000000,
1313267321000000,
1313267382000000,
1313270132000000,
1313280532000000,
1313280593000000,
1314311824000000,
1314332084000000,
1314332145000000,
1314333597000000,
1314336873000000,
1314337176000000,
1314340632000000,
1314340753000000,
1314341178000000,
1314341239000000,
1314341299000000,
1314341360000000,
1314366539000000,
1314366600000000,
1314388952000000,
1314431261000000,
1314431504000000,
1314513010000000,
1314513070000000,
1314830000000000,
1314830789000000,
1314835759000000,
1314835819000000,
1314845998000000,
1314924302000000,
1314924363000000,
1314925939000000,
1314950756000000,
1314950998000000,
1314951606000000,
1314957494000000,
1314958161000000,
1314960226000000,
1314960287000000,
1314960347000000,
1314960408000000,
1315588314000000,
1316120393000000,
1316174838000000,
1316301521000000,
1316301703000000,
1316301763000000,
1316301824000000,
1316379172000000,
1316397045000000,
1316638694000000,
1316638754000000,
1317029055000000,
1317029116000000,
1317029238000000,
1317029298000000,
1317044252000000,
1317048020000000,
1317049963000000,
1317050024000000,
1317050084000000,
1317054210000000,
1317094082000000,
1317094143000000,
1317110617000000,
1317147324000000,
1317147385000000,
1317147445000000,
1317147506000000,
1317147567000000,
1317147627000000,
1317147688000000,
1317147749000000,
1317147809000000,
1317147870000000,
1317186254000000,
1317194028000000,
1317209637000000,
1317217528000000,
1317310613000000,
1317310673000000,
1317332205000000,
1317389966000000,
1317416695000000,
1317416756000000,
1317421551000000,
1317423681000000,
1317423742000000,
1317423802000000,
1317423863000000,
1317423923000000,
1317425440000000,
1317425501000000,
1317428485000000,
1317428546000000,
1317430487000000,
1317434553000000,
1317434614000000,
1317440560000000,
1317440621000000,
1317440681000000,
1317440742000000,
1317440802000000,
1317449002000000,
1317613201000000,
1317771943000000,
1317772003000000,
1317783236000000,
1317866559000000,
1317866620000000,
1317866681000000,
1317957027000000,
1317972862000000,
1317972923000000,
1317972983000000,
1317973044000000,
1317973105000000,
1317973165000000,
1317973226000000,
1317973287000000,
1317973347000000,
1317973408000000,
1317973469000000,
1317973530000000,
1317973590000000,
1317973651000000,
1317973712000000,
1317973772000000,
1317973833000000,
1317973893000000,
1317973954000000,
1317974015000000,
1317974075000000,
1317974136000000,
1317974196000000,
1317974257000000,
1317974318000000,
1317974378000000,
1317974439000000,
1317974499000000,
1317974560000000,
1317974621000000,
1317993578000000,
1317993699000000,
1317993760000000,
1317993821000000,
1317993882000000,
1317993942000000,
1317994003000000,
1317994064000000,
1317994124000000,
1317994185000000,
1317994245000000,
1317994306000000,
1317994367000000,
1317994427000000,
1318003556000000,
1318032076000000,
1318118432000000,
1318194769000000,
1318199384000000,
1318390376000000,
1318390437000000,
1318390498000000,
1318390558000000,
1318390619000000,
1318390679000000,
1318390740000000,
1318390801000000,
1318390861000000,
1318390922000000,
1318423434000000,
1318423495000000,
1318499993000000,
1318550458000000,
1318558534000000,
1318558655000000,
1318558716000000,
1318558777000000,
1318558837000000,
1318558898000000,
1318558958000000,
1318559019000000,
1318559626000000,
1318559686000000,
1318620856000000,
1318888224000000,
1319017628000000,
1319027475000000,
1319057467000000,
1319149243000000,
1319149303000000,
1319159392000000,
1319168172000000,
1321242656000000,
1321372205000000,
1321380284000000,
1321414916000000,
1321493817000000,
1321518954000000,
1321543290000000,
1321682222000000,
1321817337000000,
1321817397000000,
1321817458000000,
1321837719000000,
1321837780000000,
1321837841000000,
1321848004000000,
1321914885000000,
1321914946000000,
1321915006000000,
1321915067000000,
1321915188000000,
1321915249000000,
1321915309000000,
1321915370000000,
1321915613000000,
1321916727000000,
1321941678000000,
1321941738000000,
1321941799000000,
1321941860000000,
1321941920000000,
1321941981000000,
1321942041000000,
1321942102000000,
1321942163000000,
1321942223000000,
1322077586000000,
1322091286000000,
1322091349000000,
1322095531000000,
1322095592000000,
1322095653000000,
1322095713000000,
1322095774000000,
1322095834000000,
1322095895000000,
1322095956000000,
1322096016000000,
1322127168000000,
1322127228000000,
1322300093000000,
1322509512000000,
1322511942000000,
1322512003000000,
1322512064000000,
1322514751000000,
1322524796000000,
1324386146328000,
1324387804000000,
1324387985000000,
1324388046000000,
1324388168000000,
1324388228000000,
1324832658000000,
1324845951000000,
1324846012000000,
1324854972000000,
1324867606000000,
1324881519000000,
1324886618000000,
1324948052000000,
1324948074265000,
1324948113000000,
1324948173000000,
1324948234000000,
1324948296000000,
1325018993000000,
1325082222000000,
1325082237375000,
1325235803000000,
1325236411000000,
1325249809218000,
1325249854000000,
1325249914000000,
1325249975000000,
1325319825000000,
1325441984000000,
1325545019000000,
1325595982000000,
1325597938000000,
1325625735000000,
1325645568000000,
1325660473000000,
1326656827000000,
1328089365000000,
1328089676000000,
1328089737000000]
dbFilters = tables.Filters(complevel=9, complib='blosc', shuffle=1)
mAF = tables.openFile("_misc/db/masks.h5", mode="r"); mAT = mAF.root.mtgoxUSD.asks
mBF = tables.openFile("_misc/db/mbids.h5", mode="r"); mBT = mBF.root.mtgoxUSD.bids
newAF = db.getMasterDB("_misc/db/mAsks.h5", dbFilters, "mtgoxUSD"); newAT = newAF.root.mtgoxUSD.asks 
newBF = db.getMasterDB("_misc/db/mBids.h5", dbFilters, "mtgoxUSD"); newBT = newBF.root.mtgoxUSD.bids

#copy masks.h5 to mAsks.h5
nrows = mAT.nrows
for index, row in enumerate(mAT):
    if row["eventDate"] not in anomalous:
        newAT.row["eventDate"] = row["eventDate"]
        newAT.row["price"] = row["price"]
        newAT.row["amount"] = row["amount"]
        newAT.row.append()
        if index%10000==0:
            sys.stderr.write("\ncopying masks: %.8f" % (float(index) / float(nrows)))
            newAT.flush()
newAT.flush(); newAF.close(); mAF.close()

#copy mbids.h5 to mBids.h5
nrows = mBT.nrows
for index, row in enumerate(mBT):
    if row["eventDate"] not in anomalous:
        newBT.row["eventDate"] = row["eventDate"]
        newBT.row["price"] = row["price"]
        newBT.row["amount"] = row["amount"]
        newBT.row.append()
        if index%10000==0:
            sys.stderr.write("\ncopying mbids: %.8f" % (float(index) / float(nrows)))
            newBT.flush()
newBT.flush(); newBF.close(), mBF.close()