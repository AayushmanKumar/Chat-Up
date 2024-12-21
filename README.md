# ⚡ChatUp⚡ : A Terminal based Chat Room Application
<img align = "center" src = "assets/working.png">

## ToDo
### 1. Add Colors to username inside the chat room using [Colorama](https://github.com/tartley/colorama):
```md
Dog: Hey Guys!
^         ^
GREEN    WHITE

(the username color can vary but should remain consisten throughout the chat)
```
* Error messages should be RED and LIGHT_RED
* Some commands like `Nick Joined the chat` can be YELLOW
* Try to indent my sent messages towards right while the messages recieved <br>
  would be at left side. (LIKE IN WHATSAPP)

### 2. Create simple Login Signup page for clients:
store the data permanently (maybe some sql?) for their future signons.

### 3. Create Admin privilege and Add chatroom commands for admins like:
* `\kick` : Kicks the exisiting user out of the room. <br>
* `\Info` : show basic info about the other user like their username so as to mute them if needed.<br>
* `\Mute` : Mutes a particular person (identified by their usernames). <br>
For Server(explicitly):
* `\Ban` : Bans the existing username-password set from the room disregarding any privilege.<br>

Admins should also have a (Adm) tag after their names so as to let others know.<br>
```md
Dog(Adm): Hey Guys!
^RED ^YELLOW???  ^WHITE
```

### 4. Add Joining Welcome Message:
* For zero privileged users, explain them to be civil and bla bla bla and the info and mute commands...
* For admins (privileged), also explain the kick command
* The first person in a live chat room by default will be the admin
* once the current admin leaves, the next person in the queue (that is the next person who joined after the first user gets the admin privileges) and so on.
* Changes in admins should be announced. If no one is admin you becoming the admin should be announced.
* can admins make other people admins ?

* SERVER WILL ALSO HAVE THE ADMIN PRIVILEGES

### 5. Add time and date of sent messages on the other side of the messages:
```md
Dog: Hey Guys!									12:46 AM | 20.12.24
                                                    					^GREYED
```

### 6. Convert server.py and client.py into a .exe file and update README after.

### 7. Configure the whole thing into a CLI inspired from [whatscli](https://github.com/normen/whatscli) :
* Potential to include contactbook and so as to begin one-to-one communication instead of exisiting communicaitons
* Host on a droplet on digitalocean finally ?!
* Finally share and ask for further suggestions on reddit!

<!--EOF-->



what the fuck is going on in the right terminal
cyan color should be for every messsage user sends only for his terminal windows
(currently for his nickname entry ?)