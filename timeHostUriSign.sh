#!/bin/bash

logFile=waf_audit.log

echo "Generate Timestamp now..."
cat $logFile | sed -n '/---A--/{N;p}' | grep '0800' | awk '{print $1,$2}' > txtFile/timestamp.txt
echo "Timestamp is OK now."

echo "Generate uri now..."
awk '/---B--/{n=3}--n>=0' $logFile | grep 'GET \|POST \| DELETE \|HEAD \|PUT \|OPTIONS \|CONNECT \|TRACE' | awk '{print $2}' > txtFile/uri.txt
echo "uri is OK now."

echo "Generate Host now..."
cat $logFile | grep 'host: \|Host: ' | awk '{print $2}' > txtFile/host.txt
echo "Host is OK now."

keyWordFile=keyWordAll.txt
echo "Generate keyword BFH now..."
cat $keyWordFile  | grep '\-\-\-B' > txtFile/keyWordB.txt
cat $keyWordFile  | grep '\-\-\-F' > txtFile/keyWordF.txt
cat $keyWordFile  | grep '\-\-\-H' > txtFile/keyWordH.txt
echo "Keyword BFH is OK now."
cat keyWordAll.txt | grep '\-\-\-B\|\-\-\-F\|\-\-\-H' > keyWordButton.txt
