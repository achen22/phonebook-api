from app import app, db
from database.models import Contact
from datetime import date

if __name__ == "__main__":
    db.create_all(app=app)

    with app.app_context():
        data = (
            ("Amy Norman", "daniel40@hotmail.com", "0492323972", "1958-05-21"),
            ("Michelle Clayton", "kimberlyjackson@gmail.com", "0402014907", "1999-11-09"),
            ("Michelle Rivera", "tamarabrooks@hotmail.com", "0413600973", "2009-01-02"),
            ("Rebecca Smith", "jessicafrederick@yahoo.com", "0456911617", "1935-12-09"),
            ("Douglas Jones", "dmccoy@hotmail.com", "0453064476", "1959-09-21"),
            ("Anne Mcintosh", "mcfarlandandrew@hotmail.com", "0406489208", "1974-04-14"),
            ("Erika Walker", "hmartin@gmail.com", "0443764605", "1986-07-16"),
            ("Morgan Wood", "patricia59@gmail.com", "0439689172", "1958-11-10"),
            ("John Chandler", "lbenson@gmail.com", "0426807804", "1982-01-06"),
            ("Travis Russell", "ashleymiller@yahoo.com", "0408744311", "2019-05-26"),
            ("Kimberly Porter", "harrisongeoffrey@gmail.com", "0422937083", "1970-06-29"),
            ("Brandi Glass", "brianfrank@hotmail.com", "0475480073", "1929-06-25"),
            ("Mikayla Weber", "yfarley@hotmail.com", "0405267001", "1914-09-26"),
            ("Amy Collins", "william26@yahoo.com", "0437692474", "1947-02-20"),
            ("Robin Cain", "melindasteele@gmail.com", "0498442314", "1930-05-09"),
            ("Krista Holmes", "connercheryl@gmail.com", "0492958716", "1949-02-07"),
            ("Barbara Gonzalez", "bbennett@gmail.com", "0408132618", "1990-12-16"),
            ("Jessica Tucker", "karenpage@hotmail.com", "0401460751", "1912-05-16"),
            ("Gary Weber", "tanyasmith@hotmail.com", "0439250899", "1998-04-11"),
            ("Amy Murray", "kennethwebb@hotmail.com", "0448069040", "1994-11-02"),
            ("Emily Frye", "davidgrant@gmail.com", "0464523178", "1907-09-05"),
            ("Peter Kramer", "carrie14@hotmail.com", "0442862693", "1986-05-11"),
            ("Jesse Martin", "jason91@yahoo.com", "0490512330", "1904-06-09"),
            ("Angela Lewis", "dawnmartinez@yahoo.com", "0447421347", "2002-01-03"),
            ("Laura Morris", "williamsongregory@gmail.com", "0468148637", "1948-09-09"),
            ("Brenda Lee", "kristen20@yahoo.com", "0422512398", "1959-01-13"),
            ("Dr. Tony Harris", "powens@yahoo.com", "0431113642", "2010-05-31"),
            ("Yesenia Davis", "rhowell@gmail.com", "0489011859", "1946-11-09"),
            ("Adam Watts", "jennifersnyder@hotmail.com", "0445580410", "1951-11-19"),
            ("John Wilkins", "evan57@yahoo.com", "0442324376", "1949-06-06")
        )

        for t in data:
            dob = date(*(int(i) for i in t[3].split("-")))
            db.session.add(Contact(name=t[0], email=t[1], phone=t[2], dob=dob))
        db.session.commit()
