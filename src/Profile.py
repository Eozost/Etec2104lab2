import tornado

accountDetails = {
"alice": {
    "realName": "Alice Smith",
    "dateofBirth": "Jan. 1",
    "email": "alice@example.com"
},
"bob": {
    "realName": "Bob Jones",
    "dateofBirth": "Dec. 31",
    "email": "bob@bob.xyz"
},
"carol": {
    "realName": "Carol Ling",
    "dateofBirth": "Jul. 17",
    "email": "carol@example.com"
},
"dave": {
    "realName": "Dave N. Port",
    "dateofBirth": "Mar. 14",
    "email": "dave@dave.dave"
}
}
class profileHandler(tornado.web.RequestHandler):
    def get(self):
            user = self.request.path.split("/")[2]
            rname = accountDetails[user]["realName"]
            dob = accountDetails[user]["dateofBirth"]
            email = accountDetails[user]["email"]

        
            self.render("TemplateTest.html",
                    Realname=rname,
                    dateofBirth=dob,
                    Adress = email,
                    uname = user
            )       
    
