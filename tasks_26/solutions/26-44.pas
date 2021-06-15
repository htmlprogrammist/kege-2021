##
assign(input, '26-44_.txt');
var N := ReadInteger;
var data := ReadArrInteger(N);

data.Sort;

var last := 500;
var discount := 0.0;
var costMax := 0.0;
while data.Count > 0 do begin
  var chunk := data.Where(x->x<=last).ToArray;
  if chunk.Count > 0 then begin
    var mid := chunk.Count div 2;
    if mid > 0 then begin
      discount += 0.5*chunk[:mid].Sum;
      costMax := 0.5*chunk[mid-1];
    end;  
    data := data.Where(x->x>last).ToArray;   
  end;
  last += 500;
end; 

Println( trunc(discount), trunc(costMax) );