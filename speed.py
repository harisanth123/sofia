import speedtest

#test = speedtest.Speedtest()

print("loading server list")
#test.get_servers()

print("choosing best server")
#best = test.get_best_server()
#print(f"Found:{best['host']} located in{best['country']}")

print("performing a download test")
#download_result = test.download()

print("performing a upload test")
#upload_result = test.upload()

print("ping results")
#ping_result = test.results.ping

#print(download_result)
#print(upload_result)
#print(ping_result)

class network():
    def __init__(net):    
        net.test = speedtest.Speedtest()
        net.test.get_servers()

    def get_info(net):
        best = network()
