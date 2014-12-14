#
Mo ta ve cac module. He thong gom 3 module chinh:
- Snapshot: 
	+ Input: Doc file configurations lay danh sach cac thu muc va file xe monitoring.
	+ Output: write file hash + time to db.json file
- Ananysisd:
	+ Input: old_hash and new_hash
	+ Output: Alert if new_hash  != old_hash
- Alert:
	+ Input: List all changed file, list admin
	+ Output: sms/msg send to list admin

---------------------------------
Langguage Python
