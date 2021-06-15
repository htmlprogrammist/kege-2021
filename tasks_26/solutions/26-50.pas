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
 var f:= openRead('26-50.txt');
 var n:= f.ReadInteger();
 var a:= (1..n).Select(i->f.ReadInteger).Sorted.ToArray;
 
 var (count, m):=(0, Longint.MaxValue);
 for var i:=0 to a.High-1 do
   for var j:=i+1 to a.High do
     if (a[i]+a[j]) mod 2 = 0 then begin
       var x:=(a[i]+a[j]) div 2;
       var pos1:=bisect_left(a,x);
       var pos2:=pos1;
       if x < a[pos2] then pos2 -= 1;
       if (pos1 > a.Count div 2 - 1) and (pos2 < a.Count div 4 *3) then begin
         count:=count+1;
         m:=min(m, x);
       end;
     end;
print(count,m);
end.