# ahk_pywebcopy
Copy full websites or a single webpage with AHK and PY

```autohotkey
definitions := ["website", "http://nytimes.com", A_ScriptDir "\temp", "NameProj"]
				;website or webpage || url || pathlocal to save || name
definitions := ["webpage", "http://www.nysed.gov/college-transcripts", A_ScriptDir "\differentFolder", "DifferentName"]

obj := Web(definitions)
obj.run()
```

