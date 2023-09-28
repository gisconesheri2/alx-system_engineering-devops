awk '  
BEGIN { 
 printf("%-8s %12s %12s\n", "class", "total files", "total GiB") 
} 
{ 
 split($1, d, "/");  
 class = d[4];  
 counts[class]+= $3;  
 sizes[class]+= $2;  
} END { 
 for (k in counts) { 
   printf("%-8s %12d %12d\n", k, counts[k], sizes[k]/(1024*1024*1024)); 
 } 
}'
