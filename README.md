## 🔔 New Version Released – V1.4

- ✅ Spell Check Toggle (Group Only)
- ✅ Group Owners Can Manage Settings via Bot PM
- ✅ Reset All Group Settings (Owner Only)
- ✅ 3 Verification System

---

## 🌟 Features
- ✅ Double db support 
- ✅ Stream Mode Toggle  
- ✅ 3 User Verification  
- ✅ Multi FSub Admin & Group Support  
- ✅ Auto Movie Info Updates  
- ✅ PM Search Toggle  
- ✅ Verified User Counter  
- ✅ Trending Titles  
- ✅ Advanced AI Spelling Correction  
- ✅ Request to Join via FSub (Admins Only)  
- ✅ Verified User Database Save  
- ✅ Superfast User Broadcast  
- ✅ Refer & Earn Premium  
- ✅ Top Searching  
- ✅ Best Streaming Website Integration  
- ✅ Premium Membership Management  
- ✅ Online Streaming & Fast Download  
- ✅ File Indexing Above 2GB  
- ✅ PreDVD & CamRip Auto Deletion  
- ✅ Multiple File Deletion  
- ✅ Settings Menu  
- ✅ Welcome Message  
- ✅ Auto File Filtering    
- ✅ Single Filter Button  
- ✅ Bot PM File Send Mode  
- ✅ Auto File Send  
- ✅ Forward Restriction  
- ✅ File Protection  
- ✅ Admin Commands  
- ✅ Group Broadcast  
- ✅ Full File Indexing Support  
- ✅ ID & User Info  
- ✅ Stats & Analytics  
- ✅ User Ban/Unban  
- ✅ Chat Leave/Disable  
- ✅ Auto Delete Old Files  
- ✅ …and more!

---

## ⚙️ Commands

```bash
movie_update        – Toggle movie update notifications
pm_search           – Toggle private message search
verification        – View total verified users
top                 – Search top trending items
start               – Start the bot
settings            – Modify bot settings
plan                – View available premium plans
myplan              – Check your active plan
stats               – View database stats
info                – Get user info
id                  – Get Telegram ID
link                – Create single post link
batch               – Create bulk post link
deleteall           – Delete all files from DB
delete              – Delete a specific file
deletefiles         – Remove PreDVD and CamRip files
broadcast           – Broadcast to users
grp_broadcast       – Broadcast to groups
enable              – Enable group joining
disable             – Disable group
leave               – Leave group
ban                 – Ban user from bot
unban               – Unban user
add_premium         – Add premium access
remove_premium      – Remove premium access
premium_users       – List premium users
restart             – Restart the bot
```


## 🛠️ Reliability updates

- `/health` provides a lightweight health-check endpoint for Render.
- Render's health check now targets `/health`.
- Render supplies its own `PORT`; do not hard-code a port in the Render environment.
- Optional environment settings are documented in `render.yaml` for cache time, search mode, auto-delete, streaming, and secondary database support.

### Important deployment notes

1. Set all required environment variables in Render before deploying.
2. Keep `MULTIPLE_DB=False` unless you have configured a valid `DATABASE_URI2`.
3. Keep API keys and bot tokens in environment variables; do not commit real secrets to a public repository.
4. A successful `/health` response confirms that the web server is responding; it does not by itself verify Telegram or MongoDB connectivity.

---

<p align="center"><b>Jai Shree Krishna 🙏😉</b></p>
