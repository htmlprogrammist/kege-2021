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
 var f:= openRead('26-48.txt');
 var n:= f.ReadInteger();
 var a:= (1..n).Select(i->f.ReadInteger).Sorted.ToArray;
 
 var (count, m):=(0, LongInt.MaxValue);
 for var i:=0 to a.High-1 do
   for var j:=i+1 to a.High do
     if (a[i]+a[j]) mod 2 = 0 then begin
       var x:=(a[i]+a[j]) div 2;
       var pos:=bisect_left(a,x);
       var raz:=min(abs(a[pos]-x), abs(x-a[pos-1]));
       if raz = 5 then begin
         count:=count+1;
         m:=min(m, x);
       end;
     end;
print(count,m);
end.