import re
import ipaddress
import pandas as pd
def is_valid_ipv4_address (address):
    try:
        ipaddress.IPv4Address(address)
        return True
    except ipaddress.AddressValueError:
        return False
fileDataHuawei=[]
with open("D:/install/Programming/Python/disp_cur_vvo.txt") as file:
    # fileData = file.readlines()
    for data in file:
        fileDataHuawei.append(data.strip())
# print (fileDataHuawei)
# print (len(fileDataHuawei))

fileDataCisco=[]
with open("D:/install/Programming/Python/show_run_khb.txt") as file:
    # fileData = file.readlines()
    for data in file:
        fileDataCisco.append(data.strip())
# print (fileDataCisco)
# print (len(fileDataCisco))

fileDataHuaweiSwitch=[]
with open("D:/install/Programming/Python/disp_cur_switch.txt") as file:
    # fileData = file.readlines()
    for data in file:
        fileDataHuaweiSwitch.append(data.strip())
# print (fileDataHuaweiSwitch)
# print (len(fileDataHuaweiSwitch))
def int_list_cisco_router(fileData):
    exclamList = [i for i, item in enumerate(fileData) if item.find("!") == 0]
    print(exclamList)
    intListMain = []
    # intDict = {"intNum": [], "intSub":[] , "intDesc":[]}
    intDict = {key: [] for key in ["intNum",
                                   "intSub",
                                   "intStatus",
                                   "intDesc",
                                   "intType",
                                   "intL3IpAddress",
                                   # "intL3IpMask",
                                   "intVRF",
                                   "intSpeed",
                                   "intL2vcIpPeer",
                                   "intL2vcId",
                                   "intNetwork",
                                   "intRouteStaticNetwork",
                                   "intRouteHexthop"]}
    routeDict={key: [] for key in["routeVRF",
                                  "routeStaticNetwork",
                                  "routeStaticNextHop"]}
    bgpDict = {key: [] for key in ["bgprIpv4Family",
                                   "bgpVRF",
                                   "bgpPeerIp",
                                   "bgpPeerAs",
                                   "bgpRouteLimit,"
                                   "bgpOtherParam"]}
    # for key in intDict:
    #     print("Begin:", intDict[key], len(intDict[key]))

    for i in range(len(exclamList)-1):
        # print (sharpList[i])
        for k in fileData[exclamList[i] + 1:exclamList[i+1]]:
            # print (k)
            # if ("interface" in k and "loop-detect" not in k):
            # find any interface and generate list of attributes
            if (k.find("interface ")==0):
                # print ("range is:", fileData.index(k), sharpList[i+1])
                for key in intDict:
                    intDict[key].append(False)
                temp1 = re.split(' ', k)
                if ("." in temp1[1]):
                    temp1.append(temp1[1].split(".")[1])
                    # print ("temp1: ", temp1, len(temp1))
                else:
                    temp1.append("")
                    intListMain.append(temp1[1])
                # intDict["intNum"].append(temp1[1].split(".")[0])
                intDict["intNum"][len(intDict["intNum"])-1]=temp1[1].split(".")[0]
                # intDict["intSub"].append(temp1[2])
                if len(temp1)>3:
                    intDict["intSub"][len(intDict["intSub"]) - 1] = temp1[3]
                else:
                    intDict["intSub"][len(intDict["intSub"]) - 1] = temp1[2]
                for k in fileData[fileData.index(k):exclamList[i + 1]]:
                    if "description" in k:
                        temp2 = k.split(' ', 1)
                        intDict["intDesc"][len(intDict["intDesc"])-1]=temp2[1]
                        # print(intDict["intSub"][len(intDict["intSub"])-1], intDict["intDesc"][len(intDict["intDesc"])-1])
                    if "ipv4 address" in k:
                        if "secondary" not in k:
                            temp3 = k.split()
                            intDict["intType"][len(intDict["intType"]) - 1] = "L3"
                            # intDict["intL3IpAddress"][len(intDict["intL3IpAddress"]) - 1] = temp3[2]
                            intDict["intL3IpAddress"][len(intDict["intL3IpAddress"]) - 1] = ipaddress.IPv4Interface((temp3[2], temp3[3])).with_prefixlen
                            # intDict["intL3IpMask"][len(intDict["intL3IpMask"]) - 1] = temp3[3]
                            intDict["intNetwork"][len(intDict["intNetwork"]) - 1] = ipaddress.IPv4Interface((temp3[2], temp3[3])).network
                        else:
                            temp3 = k.split()
                            intDict["intL3IpAddress"][len(intDict["intL3IpAddress"]) - 1] = [intDict["intL3IpAddress"][len(intDict["intL3IpAddress"]) - 1]]
                            intDict["intL3IpAddress"][len(intDict["intL3IpAddress"]) - 1].append(ipaddress.IPv4Interface((temp3[2], temp3[3])).with_prefixlen)
                            # intDict["intL3IpMask"][len(intDict["intL3IpMask"]) - 1] = [intDict["intL3IpMask"][len(intDict["intL3IpMask"]) - 1]]
                            # intDict["intL3IpMask"][len(intDict["intL3IpMask"]) - 1].append(temp3[3])
                    if "shutdown" in k and "undo shutdown" not in k:
                        intDict["intStatus"][len(intDict["intStatus"]) - 1] = "shutdown"
                    if "vrf" in k:
                        temp4 = k.split()
                        intDict["intVRF"][len(intDict["intVRF"]) - 1] = temp4[1]
                    if "service-policy" in k:
                        temp5 = k.split()
                        intDict["intSpeed"][len(intDict["intSpeed"]) - 1] = temp5[2]
                    if "mpls l2vc" in k:
                        temp6 = k.split()
                        intDict["intType"][len(intDict["intType"]) - 1] = "xconnect"
                        intDict["intL2vcIpPeer"][len(intDict["intL2vcIpPeer"]) - 1] = temp6[2]
                        intDict["intL2vcId"][len(intDict["intL2vcId"]) - 1] = temp6[3]
                        # if "sub" in k:
                # intDict["intSub"].append(temp1[2])
                # print ("lenght:", len(intDict["intNum"]), len(intDict["intSub"]), len(intDict["intDesc"]))
            if k.find("ip route-static")==0 and "NULL" not in k:
                for key in routeDict:
                    routeDict[key].append(False)
                temp11=k.split()
                if "vpn-instance" in k:
                    routeDict["routeVRF"][len(routeDict["routeVRF"])-1] = temp11[3]
                    routeDict["routeStaticNetwork"][len(routeDict["routeStaticNetwork"])-1] = ipaddress.IPv4Interface(
                        (temp11[4], temp11[5])).with_prefixlen
                    if is_valid_ipv4_address(temp11[6]):
                        routeDict["routeStaticNextHop"][len(routeDict["routeStaticNextHop"])-1] = ipaddress.IPv4Address(
                            temp11[6]).compressed
                    else:
                        routeDict["routeStaticNextHop"][len(routeDict["routeStaticNextHop"]) - 1] = ipaddress.IPv4Address(
                            temp11[7]).compressed
                else:
                    routeDict["routeStaticNetwork"][len(routeDict["routeStaticNetwork"]) - 1] = ipaddress.IPv4Interface(
                        (temp11[2], temp11[3])).with_prefixlen
                    # print (temp11[4])
                    routeDict["routeStaticNextHop"][len(routeDict["routeStaticNextHop"]) - 1] = ipaddress.IPv4Address(
                        temp11[4]).compressed
            if k.find("bgp")==0:
                for key in bgpDict:
                    bgpDict[key].append(False)

    for i in range(len(routeDict["routeStaticNextHop"])):
        for j in range(len(intDict["intNetwork"])):
            if intDict["intType"][j] == "L3" and ipaddress.IPv4Address(routeDict["routeStaticNextHop"][i]) in ipaddress.IPv4Network(intDict["intNetwork"][j]) \
                    and routeDict["routeVRF"][i]==intDict["intVRF"][j]:
                # print (routeDict["routeStaticNextHop"][i],  intDict["intNetwork"][j])
                intDict["intRouteStaticNetwork"][j]=routeDict["routeStaticNetwork"][i]
                intDict["intRouteHexthop"][j]=routeDict["routeStaticNextHop"][i]

    # print (intDict["intNum"][100], intDict["intSub"][100], intDict["intDesc"][100])
    # for key in intDict:
    #     print(key, intDict[key][371])
    # print ("IP:", intDict["intL3IpAddress"][371])
    #
    # for key in routeDict:
    #     print (key, routeDict[key])
    #
    # df = pd.DataFrame(intDict)
    # print (df)
    # export data to excel:
    # df.to_excel(r'test.xlsx', index = False, header = True)
    # print (intListMain)
    return intDict
def int_list_huawei_router(fileData):

    sharpList = [i for i, item in enumerate(fileData) if item.find("#")==0]
    # print (sharpList)

    intListMain = []
    # intDict = {"intNum": [], "intSub":[] , "intDesc":[]}
    intDict = {key: [] for key in ["intNum",
                                   "intSub",
                                   "intStatus",
                                   "intDesc",
                                   "intType",
                                   "intL3IpAddress",
                                   # "intL3IpMask",
                                   "intVRF",
                                   "intSpeed",
                                   "intL2vcIpPeer",
                                   "intL2vcId",
                                   "intNetwork",
                                   "intRouteStaticNetwork",
                                   "intRouteHexthop"]}
    routeDict={key: [] for key in["routeVRF",
                                  "routeStaticNetwork",
                                  "routeStaticNextHop"]}
    bgpDict = {key: [] for key in ["bgprIpv4Family",
                                   "bgpVRF",
                                   "bgpPeerIp",
                                   "bgpPeerAs",
                                   "bgpRouteLimit,"
                                   "bgpOtherParam"]}
    # for key in intDict:
    #     print("Begin:", intDict[key], len(intDict[key]))

    for i in range(len(sharpList)-1):
        # print (sharpList[i])
        for k in fileData[sharpList[i] + 1:sharpList[i+1]]:
            # print (k)
            # if ("interface" in k and "loop-detect" not in k):
            # find any interface and generate list of attributes
            if (k.find("interface ")==0):
                # print ("range is:", fileData.index(k), sharpList[i+1])
                for key in intDict:
                    intDict[key].append(False)
                temp1 = re.split(' ', k)
                if ("." in temp1[1]):
                    temp1.append(temp1[1].split(".")[1])
                else:
                    temp1.append("")
                    intListMain.append(temp1[1])
                # intDict["intNum"].append(temp1[1].split(".")[0])
                intDict["intNum"][len(intDict["intNum"])-1]=temp1[1].split(".")[0]
                # intDict["intSub"].append(temp1[2])
                intDict["intSub"][len(intDict["intSub"]) - 1] = temp1[2]
                for k in fileData[fileData.index(k):sharpList[i + 1]]:
                    if "description" in k:
                        temp2 = k.split(' ', 1)
                        intDict["intDesc"][len(intDict["intDesc"])-1]=temp2[1]
                        # print(intDict["intSub"][len(intDict["intSub"])-1], intDict["intDesc"][len(intDict["intDesc"])-1])
                    if "ip address" in k and not "unnumbered" in k:
                        if "sub" not in k:
                            temp3 = k.split()
                            intDict["intType"][len(intDict["intType"]) - 1] = "L3"
                            # intDict["intL3IpAddress"][len(intDict["intL3IpAddress"]) - 1] = temp3[2]
                            intDict["intL3IpAddress"][len(intDict["intL3IpAddress"]) - 1] = [ipaddress.IPv4Interface((temp3[2], temp3[3])).with_prefixlen]
                            # intDict["intL3IpAddress"][len(intDict["intL3IpAddress"]) - 1] = [
                            #     intDict["intL3IpAddress"][len(intDict["intL3IpAddress"]) - 1]]
                            # intDict["intL3IpMask"][len(intDict["intL3IpMask"]) - 1] = temp3[3]
                            intDict["intNetwork"][len(intDict["intNetwork"]) - 1] = [ipaddress.IPv4Interface((temp3[2], temp3[3])).network.with_prefixlen]
                            # intDict["intNetwork"][len(intDict["intNetwork"]) - 1] = [
                            #     intDict["intNetwork"][len(intDict["intNetwork"]) - 1]]
                        else:
                            temp3 = k.split()
                            # intDict["intL3IpAddress"][len(intDict["intL3IpAddress"]) - 1] = [intDict["intL3IpAddress"][len(intDict["intL3IpAddress"]) - 1]]
                            intDict["intL3IpAddress"][len(intDict["intL3IpAddress"]) - 1].append(ipaddress.IPv4Interface((temp3[2], temp3[3])).with_prefixlen)
                            intDict["intNetwork"][len(intDict["intNetwork"]) - 1].append(ipaddress.IPv4Interface((temp3[2], temp3[3])).network.with_prefixlen)
                            # intDict["intL3IpMask"][len(intDict["intL3IpMask"]) - 1] = [intDict["intL3IpMask"][len(intDict["intL3IpMask"]) - 1]]
                            # intDict["intL3IpMask"][len(intDict["intL3IpMask"]) - 1].append(temp3[3])
                    if "shutdown" in k and "undo shutdown" not in k:
                        intDict["intStatus"][len(intDict["intStatus"]) - 1] = "shutdown"
                    if "ip binding vpn-instance" in k:
                        temp4 = k.split()
                        intDict["intVRF"][len(intDict["intVRF"]) - 1] = temp4[3]
                    if "qos car cir" in k:
                        temp5 = k.split()
                        intDict["intSpeed"][len(intDict["intSpeed"]) - 1] = temp5[3]
                    if "mpls l2vc" in k:
                        temp6 = k.split()
                        intDict["intType"][len(intDict["intType"]) - 1] = "xconnect"
                        intDict["intL2vcIpPeer"][len(intDict["intL2vcIpPeer"]) - 1] = temp6[2]
                        intDict["intL2vcId"][len(intDict["intL2vcId"]) - 1] = temp6[3]
                    if "l2 binding vsi" in k:
                        temp7 = k.split()
                        intDict["intType"][len(intDict["intType"]) - 1] = "vsi"
                        # if "sub" in k:
                # intDict["intSub"].append(temp1[2])
                # print ("lenght:", len(intDict["intNum"]), len(intDict["intSub"]), len(intDict["intDesc"]))
            if k.find("ip route-static")==0 and "NULL" not in k:
                for key in routeDict:
                    routeDict[key].append(False)
                temp11=k.split()
                if "vpn-instance" in k:
                    routeDict["routeVRF"][len(routeDict["routeVRF"])-1] = temp11[3]
                    routeDict["routeStaticNetwork"][len(routeDict["routeStaticNetwork"])-1] = ipaddress.IPv4Interface(
                        (temp11[4], temp11[5])).with_prefixlen
                    if is_valid_ipv4_address(temp11[6]):
                        routeDict["routeStaticNextHop"][len(routeDict["routeStaticNextHop"])-1] = ipaddress.IPv4Address(
                            temp11[6]).compressed
                    else:
                        routeDict["routeStaticNextHop"][len(routeDict["routeStaticNextHop"]) - 1] = ipaddress.IPv4Address(
                            temp11[7]).compressed
                else:
                    routeDict["routeStaticNetwork"][len(routeDict["routeStaticNetwork"]) - 1] = ipaddress.IPv4Interface(
                        (temp11[2], temp11[3])).with_prefixlen
                    # print (temp11[4])
                    routeDict["routeStaticNextHop"][len(routeDict["routeStaticNextHop"]) - 1] = ipaddress.IPv4Address(
                        temp11[4]).compressed
            if k.find("bgp")==0:
                for key in bgpDict:
                    bgpDict[key].append(False)

    for i in range(len(routeDict["routeStaticNextHop"])):
        for j in range(len(intDict["intNetwork"])):
            # for k in range(len(routeDict["routeStaticNextHop"][i])):
            if intDict["intNetwork"][j] != False:
                # print (intDict["intNetwork"][j])
                # print (len(intDict["intNetwork"][j]))
                for l in range (len(intDict["intNetwork"][j])):
                    # print ((routeDict["routeStaticNextHop"][i], intDict["intNetwork"][j][l]))
                    if intDict["intType"][j] == "L3" and ipaddress.IPv4Address(routeDict["routeStaticNextHop"][i]) in ipaddress.IPv4Network(intDict["intNetwork"][j][l]) \
                        and routeDict["routeVRF"][i]==intDict["intVRF"][j]:
                        # print ("find: ", routeDict["routeStaticNextHop"][i],  intDict["intNetwork"][j][l], routeDict["routeStaticNetwork"][i])
                        if intDict["intRouteStaticNetwork"][j]==False:
                            intDict["intRouteStaticNetwork"][j]=[routeDict["routeStaticNetwork"][i]]
                            # intDict["intRouteStaticNetwork"][j] = [intDict["intRouteStaticNetwork"][j]]
                            intDict["intRouteHexthop"][j]=[routeDict["routeStaticNextHop"][i]]
                            # intDict["intRouteHexthop"][j] = [intDict["intRouteHexthop"][j]]
                        else:
                            # print ("noFalse: ")
                            # print (intDict["intRouteStaticNetwork"][j])
                            intDict["intRouteStaticNetwork"][j].append(routeDict["routeStaticNetwork"][i])
                            intDict["intRouteHexthop"][j].append(routeDict["routeStaticNextHop"][i])

    # print (intDict["intNum"][100], intDict["intSub"][100], intDict["intDesc"][100])
    # for key in intDict:
    #     print(key, intDict[key][85])
    # print ("IP:", intDict["intL3IpAddress"][85])
    # print ("IP:", intDict["intL3IpAddress"][85][1])
    # print ("net:", intDict["intNetwork"][85])
    # print ("net:", intDict["intNetwork"][85][1])

    # for key in routeDict:
    #     print (key, routeDict[key])

    # df = pd.DataFrame(intDict)
    # print (df)
    # export data to excel:
    # df.to_excel(r'test.xlsx', index = False, header = True)
    # print (intListMain)
    # ipv4 = ipaddress.ip_address(intDict["intL3IpAddress"][100])
    # subnet1 = ipaddress.IPv4Network((0, intDict["intL3IpMask"][100]))
    # print (ipaddress.ip_address(intDict["intL3IpAddress"][100]), ipv4.is_global)
    #
    # print (ipv4,"/",subnet1.prefixlen)
    # # print (str(ipv4)+'/'+subnet1.prefixlen)
    # # int1 = ipaddress.ip_interface(ipv4+"/"+subnet1)
    #
    # print (subnet1.prefixlen)
    return intDict
def vlan_list_huawei_switch(fileData):
    sharpList = [i for i, item in enumerate(fileData) if item.find("#")==0]
    # print (sharpList)

    intListMain = []
    # intDict = {"intNum": [], "intSub":[] , "intDesc":[]}
    vlanDict = {key: [] for key in ["vlanNum",
                                    "vlanName",
                                    "vlanInInt",
                                    "vlanIntType"]}
    intDict = {key: [] for key in ["intNum",
                                   "intDesc",
                                   "intPortType",
                                   "intVlanInclude"]}
    for i in range(len(sharpList)-1):
        for k in fileData[sharpList[i] + 1:sharpList[i+1]]:
            if k.find("interface ")==0:
                # print ("range is:", fileData.index(k), sharpList[i+1])
                for key in intDict:
                    intDict[key].append([])
                temp1 = k.split()
                intDict["intNum"][len(intDict["intNum"]) - 1] = temp1[1]
                intDict["intVlanInclude"][len(intDict["intVlanInclude"]) - 1] = []
                for k in fileData[fileData.index(k):sharpList[i + 1]]:
                    if "description" in k:
                        temp2 = k.split(' ', 1)
                        intDict["intDesc"][len(intDict["intDesc"])-1]=temp2[1]
                    if "port link-type" in k:
                        temp3 = k.split()
                        intDict["intPortType"][len(intDict["intPortType"])-1]=temp3[2]
                    if "port trunk allow-pass vlan" in k and "undo" not in k:
                        temp4 = k.split()
                        del temp4[:4]
                        for i in temp4:
                            if i == "to":
                                # print (temp4 [temp4.index(i)-1], temp4 [temp4.index(i)+1])
                                temp5 = list(range(int(temp4 [temp4.index(i)-1])+1, int(temp4 [temp4.index(i)+1])))
                                # print (temp5, "Len:", len(temp5))
                                if len(temp5)!=0:
                                    for j in temp5:
                                        temp4.append(j)
                                # print (list(range(1,1)))
                                del temp4 [temp4.index(i)]
                        temp4 = [int(item) for item in temp4]
                        temp4.sort()
                        for item in temp4:
                            intDict["intVlanInclude"][len(intDict["intVlanInclude"]) - 1].append(item)
                    if "port default vlan" in k:
                        temp6 = k.split()
                        del temp6[:3]
                        intDict["intVlanInclude"][len(intDict["intVlanInclude"]) - 1].append(int(temp6[0]))
            if k.find("vlan") ==0 and "vlan batch" not in k:
                for key in vlanDict:
                    vlanDict[key].append([])
                temp7 = k.split()
                vlanDict["vlanNum"][len(vlanDict["vlanNum"]) - 1] = int(temp7[1])
                # print ("test", fileData[fileData.index(k)])
                if fileData[fileData.index(k)+1].find("description")==0 or fileData[fileData.index(k)+1].find("name")==0:
                    temp8 = fileData[fileData.index(k)+1].split(' ', 1)
                    vlanDict["vlanName"][len(vlanDict["vlanName"]) - 1] = temp8[1]
    for data1 in vlanDict["vlanNum"]:
        # vlanDict["vlanInInt"][vlanDict["vlanNum"].index(data1)]=[]
        for num1 in range(len(intDict["intVlanInclude"])):
            for num2 in range(len(intDict["intVlanInclude"][num1])):
                if data1 ==intDict["intVlanInclude"][num1][num2]:
                    # print(data1, "in", intDict["intVlanInclude"][num1][num2], intDict["intNum"][num1])
                    vlanDict["vlanInInt"][vlanDict["vlanNum"].index(data1)].append(intDict["intNum"][num1])
                    vlanDict["vlanIntType"][vlanDict["vlanNum"].index(data1)].append(intDict["intPortType"][num1])
        #     for data2 in range (len(intDict["intVlanInclude"][num1])):
        #         print ("proTest", intDict["intVlanInclude"][num1])
        # print("vlanNum", data1, vlanDict["intNum"][vlanDict["vlanNum"].index(data1)])
    # print (intDict["intVlanInclude"][190])
    # df = pd.DataFrame(intDict)
    # df1 = pd.DataFrame(vlanDict)
    # print (df.loc[190])
    # print (df1)
    # print (vlanDict)
    return vlanDict
# print (int_list_huawei_router(fileDataHuawei))

# int_list_huawei_router(fileDataHuawei)
# vlan_list_huawei_switch(fileDataHuaweiSwitch)
dictOfRouter = int_list_huawei_router(fileDataHuawei)
dictOfRouterCisco = int_list_cisco_router(fileDataCisco)
dictOfSwitch = vlan_list_huawei_switch(fileDataHuaweiSwitch)
dictOfAll={}
# print (dictOfRouter.keys())
# dictOfAll = dict.fromkeys(list(dictOfRouter.keys())+list(dictOfSwitch.keys()))
dictOfAll = {key: [] for key in (list(dictOfRouter.keys())+list(dictOfSwitch.keys()))}
# dictOfAll.update(dictOfSwitch.keys())
# print (dictOfAll)
# dataOutRouter = pd.DataFrame(int_list_huawei_router(fileDataHuawei))
# dataOutSwitch = pd.DataFrame(vlan_list_huawei_switch(fileDataHuaweiSwitch))
#
# print(dataOutRouter)
# print(dataOutSwitch)

for num1 in range(len(dictOfRouter["intNum"])):
    for num2 in range(len(dictOfSwitch["vlanNum"])):
        if dictOfRouter["intNum"][num1] == "GigabitEthernet3/0/1" and dictOfRouter["intSub"][num1]==str(dictOfSwitch["vlanNum"][num2]):
            # print (dictOfRouter["intNum"][num1], dictOfRouter["intSub"][num1], dictOfSwitch["vlanNum"][num2])
            dictOfAll["intNum"].append(dictOfRouter["intNum"][num1])
            dictOfAll["intSub"].append(dictOfRouter["intSub"][num1])
            dictOfAll["intStatus"].append(dictOfRouter["intStatus"][num1])
            dictOfAll["intDesc"].append(dictOfRouter["intDesc"][num1])
            dictOfAll["intType"].append(dictOfRouter["intType"][num1])
            dictOfAll["intL3IpAddress"].append(dictOfRouter["intL3IpAddress"][num1])
            dictOfAll["intVRF"].append(dictOfRouter["intVRF"][num1])
            dictOfAll["intSpeed"].append(dictOfRouter["intSpeed"][num1])
            dictOfAll["intL2vcIpPeer"].append(dictOfRouter["intL2vcIpPeer"][num1])
            dictOfAll["intL2vcId"].append(dictOfRouter["intL2vcId"][num1])
            dictOfAll["intNetwork"].append(dictOfRouter["intNetwork"][num1])
            dictOfAll["intRouteStaticNetwork"].append(dictOfRouter["intRouteStaticNetwork"][num1])
            dictOfAll["intRouteHexthop"].append(dictOfRouter["intRouteHexthop"][num1])
            dictOfAll["vlanNum"].append(dictOfSwitch["vlanNum"][num2])
            dictOfAll["vlanName"].append(dictOfSwitch["vlanName"][num2])
            dictOfAll["vlanInInt"].append(dictOfSwitch["vlanInInt"][num2])
            dictOfAll["vlanIntType"].append(dictOfSwitch["vlanIntType"][num2])

            # for key in dictOfRouter:
            #     dictOfAll.append(key[num1])
        # for keyR in DictOfRouter["intSub"]:
        #     for keyS in DictOfSwitch["vlanNum"]:
        #         # print("find", keyR, "in", keyS)
        #         if keyR==str(keyS):
        #             print ("Find!", keyR, "in", keyS)
# def int_list_router_and_switch(listRouter, listSwitch):
# print (dictOfAll)
# df2 = pd.DataFrame(dictOfAll)
# print (df2)
# df2.to_excel(r'test.xlsx', index = False, header = True)
df3 = pd.DataFrame(dictOfRouterCisco)
print (df3)
print (df3.loc[190])
df3.to_excel(r'test_cisco.xlsx', index=False, header=True)
