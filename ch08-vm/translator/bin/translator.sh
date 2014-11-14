#!/usr/bin/env bash 

print_usage() { 
	echo "Usage: "
	echo "  $ bash bin/translator.sh [directory]"
	echo "where directory contains all vm files" 
}

if [ $# != 1 ]; then 
	print_usage >&2
	exit 1
fi

java -cp target/translator-0.1.0-standalone.jar translator.main $@
