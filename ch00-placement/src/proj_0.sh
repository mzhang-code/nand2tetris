#!/usr/bin/env bash 

print_usage() { 
	echo "Usage: executable file_path [no-comments]" 
}

argument_check() { 
	if [ $# -lt 1 ]; then 
		print_usage 
		exit 1 
	fi 

	if [ $# -ge 1 ] && [ ! -f $1 ]; then 
		echo "$1 is not a valid file path." 
		exit 1
	fi 

	if [ $# -eq 2 ] && [ "$2" != "no-comments" ]; then 
		echo "invalid option $2" 
		exit 1 
	fi
}

strip_whitespace() { 
	local in=$1
	perl -lape 's/\s+//sg' $in | perl -pe 's/^\n//g' 
}

strip_comments() { 
	local in=$1
	perl -pe "s/\/\/(.)*\n/\n/g" $in 
}

main() { 
	argument_check $@ 

	local in=$1 
	local out=${in/.in/.out}

	if [ $# -ge 1 ]; then 
		echo "`strip_whitespace $in`" > $out
	fi 

	if [ $# -gt 1 ]; then 
		echo "`strip_comments $out`" > $out
	fi 
}

main $@

