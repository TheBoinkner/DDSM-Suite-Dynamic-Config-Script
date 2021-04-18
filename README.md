# DDSM-Suite-Dynamic-Config-Script
This is a work in progress. The ultimate goal here is to
make a series of scripts that automate the DDSM and all
are fed their values from 1 global source. I have also
included a script manager that is a work in progress that
when finished will scan all scripts in that local 
directory and compile them into one script to be executed
instead of a bunch individually.
DDSMGlobal.py is the global config file that feeds all 
all of the scripts with variables.
func.py are functions used often so I just import them to
To make it easier on me.
Selection.py is the script manager that compiles the 
Scripts into one executable named Execute.py.
Everything here is mostly formated to run through 
Securecrt which is why there is a bunch of crt.Screen but
I am currently trying to change that and make it more 
versatile but I am currently stuck on trying to figure 
out how to do so.
