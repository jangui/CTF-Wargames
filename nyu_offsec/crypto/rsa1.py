from math import pow
from decimal import *
from gmpy2 import *

n = 158624820740690269480228010097824397074490987590828721424772590208400232205836339765166764192912139481260391551114525498192991409458296138199067549202160725274091648026491212957634263499635158066804483479197898923398422038764200509193145230559332198362412294433311788824138347438067995511476294521078765641773354481723588705207981967690662398784535505435523786822686233715102606431270884910535026499916693172602038035262176862294900434222490106930048422475480350847053510618561692705155716386615335665134090288770228630457820279473413632883795814379251877990065902116201157883301344989210937763777367943151210211207624006378657308960839919678847271813756786368074602384488876042579225994905910121055772200922553865613555352853204066855218806094027274031920486288290088126097424837015100700215939589527990983846051799811795191180827176952634406111221550214276907441086772864597193890609093946370430556945371517874880961284687377953183495106492261217833833852868326459310911919996162727836925163483031621490822735783914249358322955758400386506341998321699791373869406159882726079459148961495061419377505549767118071101184198430841567588260227323304519424110407841853385958976219537106103400877482945632432799160702151285922630305919049
e = 5
c = 805354919578674492707633177891704018257163257116088490707850440207599375589425431073370174283120082855262268711861045862124382401392774191092640977927795372636606554704690437194756452766421234525865873452463263951100507347033237163787580230598751413885035994611890859127560082180271327004298547019797294634977553433607605473099154881582850121296107620916338991972453402473575943009829513547894001906511788470580993277567422362475732352459796480512515972179144099023289213905806942154208674528390405124210561389093562808116669440348521675720513749372557


m = mpz(c)
rt = iroot(m, e)
m = hex(rt[0])

res = ''
for i in range(2, len(m), 2):
    res += chr(int(str(m[i:i+2]), 16))

print(res)


