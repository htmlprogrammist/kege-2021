// Автор: А.М. Кабанов

function bisect_left(a:List<integer>; x:real):integer;
begin
  var (lo, hi):=(0, a.Count-1);
  while lo<hi do begin
    var mid:= (lo+hi)div 2;
    if a[mid]<x then lo:=mid+1 else hi:=mid;
  end;
  Result:=lo;
end;

begin
 var f:= openRead('26-47.txt');
 var n:= f.ReadInteger;
 var a:= (1..n).Select(el->f.ReadInteger).Sorted.ToList;
 
 var (count, m):=(0, 0.0);
 for var i:=0 to a.Count - 2 do
   for var j:=i+1 to a.Count - 1 do begin
     var x:=(a[i]+a[j])/2;
     var pos:=bisect_left(a,x);
     if pos mod 100 = 0 then begin
       count:=count+1;
       m:=max(m, pos);
     end;
   end;
print(count,m);
end.