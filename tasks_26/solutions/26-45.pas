// Автор: А.М. Кабанов

##
var F:= openRead('26-45.txt');
var n:= F.ReadInteger;
var a:= (1..n).Select(i->F.ReadInteger).Sorted.ToArray;
 
var (k, m):=(0, 0);
for var i:=0 to a.High-1 do
  for var j:=i+1 to a.High do
    if (a[i]+a[j]) mod 2 = 0 then begin
      var s:=(a[i]+a[j]) div 2;
      if a.BinarySearch(s)>=0 then begin
        k:=k+1;
        m:=max(m,s);
      end;
    end;
print(k,m);
