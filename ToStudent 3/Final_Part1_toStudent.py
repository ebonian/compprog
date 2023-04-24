def get_consensus(ss):
    # write your code here.




    return consensus # DO NOT MODIFY THIS LINE

def get_consensus_generic(ss):
    # write your code here.





    return consensus # DO NOT MODIFY THIS LINE

#---------------------------------------
# DO NOTE MODIFY CODE AFTER THIS SECTION
#---------------------------------------

ss = ("ATCGATGC\n" +  
      "GTACaCGC\n" +
      "ACTACAGC\n" +
      "CtCAATTC\n" + 
      "CTGgATTC")
print(get_consensus(ss))

ss = ("ATCGATGC\n" +
      "GTACaCCC\n" +
      "ACTACATC\n" + 
      "CtCAATAC")
print(get_consensus(ss))

ss = ("YCXBATGZ\n" +
      "YCVBaCGZ\n" +
      "ACXBCTGZ\n" +
      "CtCAATTZ\n" +
      "CTXAATTM")
print(get_consensus_generic(ss))

ss = ("YCXBATGZ\n" +      
     "YCVBaCGZHQ\n" +
     "ACXBCTGZHQ\n" + 
     "CtCAATTZHD\n" + 
     "CTXAATTMFD")
print(get_consensus_generic(ss))

ss = ("YCXBATGZ\n" +      
      "YCVCaCGZHQ\n" +
      "ACXDCTGZHQ\n" + 
      "CtCTATTZHD\n" + 
      "CTXAATTMFD")
print(get_consensus_generic(ss))
