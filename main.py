from Board import Board
from Player import Player
from StratTester import StratTester, simpleTest, steppedTest
from Strategy import DefaultStrategy, SimpleStrategyV1, SimpleStrategyV2, SimpleStrategyV3, SimpleStrategyV4, Strategy
import time


#simpleTest(DefaultStrategy(), SimpleStrategy())
strats = [SimpleStrategyV1(), SimpleStrategyV2(), SimpleStrategyV3(), SimpleStrategyV4()]
for s1 in strats:
    for s2 in strats:
        print(str(s1)+" vs " + str(s2))
        avgs = []
        total = 0
        count = 0
        for i in range(5) :
            start_time = time.time()
            results = steppedTest(10000, 500, s1, s2, False)
            avgs.append(sum(results) / len(results))
            total+=sum(results)
            count+=len(results)

            #print("--- %s seconds ---" % str((time.time() - start_time)).replace(".", ","))
            #print(results)

        print(avgs)
        print(total/count)
        print(total/(count*5))

#2,46 123,49 200-100-False
#2.47 123,81 200-20-False
#2,93 146,83 200-20-True
#2.87 143.64 200-100-True
#2.48 124,39 200-Sequential