#
Watchdog tool have three main module:
- Snapshot: 
	+ Input: Detection montioring folder from config.cnf file.
	+ Output: write hash file, time modify file to db.json.
- Ananysisd:
	+ Input: hash_old and hash_new
	+ Output: list all file change with domain
- Alert:
	+ Input: Input list all file change with domain from ananysisd module.
	+ Output: sms/msg send to list admin

[-] Tool writein python
[-] free for everyone
