import tornado

accountDetails = {
"alice": {
    "realName": "Alice Smith",
    "dateofBirth": "Jan. 1",
    "email": "alice@example.com",
    "profpic": "/static/aliceprof.png"
},
"bob": {
    "realName": "Bob Jones",
    "dateofBirth": "Dec. 31",
    "email": "bob@bob.xyz",
    "profpic": "/static/bobprof.png"
},
"carol": {
    "realName": "Carol Ling",
    "dateofBirth": "Jul. 17",
    "email": "carol@example.com",
    "profpic": "/static/carol.png"
},
"dave": {
    "realName": "Dave N. Port",
    "dateofBirth": "Mar. 14",
    "email": "dave@dave.dave",
    "profpic": "/static/simplesketch.png"
}
}
class profileHandler(tornado.web.RequestHandler):
    def get(self):
            user = self.request.path.split("/")[2]
            rname = accountDetails[user]["realName"]
            dob = accountDetails[user]["dateofBirth"]
            email = accountDetails[user]["email"]
            profilepic = accountDetails[user]["profpic"]

        
            self.render("TemplateTest.html",
                    Realname=rname,
                    dateofBirth=dob,
                    Adress = email,
                    uname = user,
                    image = profilepic
            )       
    
