// Автор: А.М. Кабанов

##
var F:= openRead('26-46.txt');
var n:= F.ReadInteger;
var a:= (1..n).Select(i->F.ReadInteger).Sorted.ToArray;
 
var (count, m):=(0, longInt.MaxValue);
for var i:=0 to a.High-2 do
  for var j:=i+1 to a.High-1 do
    for var k:=j+1 to a.High do begin
      var s:= a[i]+a[j]+a[k];
      if s mod 3 = 0 then begin
        var x:= s div 3;
        if a.BinarySearch(x)>=0 then begin
          count:=count+1;
          m:=min(m,x);
        end;
      end;
    end;
print(count,m);
