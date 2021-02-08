# channel_surfer  
### a local media streaming application  


## concept  
re-create the vintage television watching experience  

# modules
## remote_receiver
1. contains Remote class
2. has properties for interpreting received remote signal  

## television  
### functions that share media content  
1. contains Television class  
2. change channels  
3. automatically shuts down (optional)  
4. manage channels, channels changing, timestamps, etc  

## vcr
### functions that manage media content
1. contains VCR class  
2. extracts video files from media folders  
3. create channels based on (undecided parameters)  

## cs_networking
### functions that allow the client/server to interact and share content
1. contains Broadcaster class  
2. communicate client to server  
