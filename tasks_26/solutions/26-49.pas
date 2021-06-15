// Автор: А.М. Кабанов

function bisect_left(a: array of integer; x:real):integer;
begin
  var (lo, hi):=(0, a.High);
  while lo<hi do begin
    var mid:= (lo+hi)div 2;
    if a[mid]<x then lo:=mid+1 else hi:=mid;
  end;
  Result:=lo;
end;

begin
 var f:= openRead('26-49.txt');
 var n:= f.ReadInteger();
 var a:= (1..n).Select(el->f.ReadInteger).Sorted.ToArray;
 
 var (count, m):=(0, 0);
 for var i:=0 to a.High-1 do
   for var j:=i+1 to a.High do
     if (a[i]+a[j]) mod 2 = 0 then begin
       var x:=(a[i]+a[j]) div 2;
       var pos:=bisect_left(a,x);
       if x < a[pos] then pos-=1;
       if pos < a.Count div 2 then begin
         count:=count+1;
         m:=max(m, x);
       end;
     end;
print(count,m);
end.