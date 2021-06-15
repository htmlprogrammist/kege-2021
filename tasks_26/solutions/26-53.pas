##
var F:= openRead('26.txt');
var n:= F.ReadInteger;
var data:= (1..n).Select(i->F.ReadInteger)
           .Sorted.ToArray;

var averages := new List<integer>;
for var i:=0 to data.High-1 do
  for var j:=i+1 to data.High do
    if (data[i] mod 2 = 1) and (data[j] mod 2 = 1) then 
      averages.Add( (data[i]+data[j]) div 2 );
averages.Sort;

var selected := new List<integer>;
var i:= 0;
foreach var av in averages do begin
  while (i < N) and (data[i] < av) do
    i += 1;
  if (i < N) and (data[i] = av) then
    selected.Add(av);
end;

print( selected.Count, selected.Last )


