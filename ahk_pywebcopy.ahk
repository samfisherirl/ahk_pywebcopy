

definitions := ["website", "http://nytimes.com", A_ScriptDir "\temp", "NameProj"]
				;website or webpage || url || pathlocal to save || name
definitions := ["webpage", "http://www.nysed.gov/college-transcripts", A_ScriptDir "\differentFolder", "DifferentName"]

obj := Web(definitions)
obj.run()


class Web
{
	__New(def) {
	;website or webpage || url || pathlocal to save || name
	this.config := A_ScriptDir "\command.txt"
	this.command := def[1]
	this.path_to_save := def[3]
	this.name := def[4]
	this.url := def[2]
	command_storage := this.command ",," this.url ",," this.path_to_save ",,", this.name ",,"
	FileAppend(command_storage, A_ScriptDir "\temp.txt")
	FileMove(A_ScriptDir "\temp.txt", this.config, 1)
	}

	run(){
		Run("ahk_webcopy.exe", A_ScriptDir)
	}

}





