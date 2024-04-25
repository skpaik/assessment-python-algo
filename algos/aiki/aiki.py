# Chat feature
collections_User = {
    "userId": "",
    "userEmail": "",
    "userRole": "Admin/Participant",
}

collections_Room = {
    "room_id": "",
    "name": "",
    "date_time": "",
    "members": [],
    "state": "received_unread"
}

collections_Message = {
    "message_id": "",
    "roomId": "",
    "sender": "",
    "last_message_detail": {

    },
    "date_time": "",
    #"gps_coordinates": [],
    #"state": "draft/sent/received/viewed/"
}

collections_Thread = {
    "thread_id": "",
    "message_id": "",
    "reply_parent_message_id": "",
    "sender": {""},
    "message": "",
    "message_type": "main/reply",
    "date_time": "",
    "gps_coordinates": [],
    "location": [],
    "state": "draft/sent/received_unread/received_seen/viewed/"
}

# const [roomList, setRoomList] = useState([])

# setRoomList(updated_list)

'''

handleView(roomId="abc"){
abcObj=roomList.filter(x=> x.roomId==roomId);

abcObj.state="received_seen";
}
'''
'''
        roomList.map(()=>{
        
        })
'''






