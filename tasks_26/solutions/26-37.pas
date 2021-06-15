##
assign(input, '26-k6.txt');
var (N, K):= ReadInteger2;

var pairs := (1..N).Select(i->ReadString.ToIntegers)
                   .Skip(1).ToArray;
pairs.Sort( (x,y)-> x[1]/x[0]-y[1]/y[0] <> 0 ? 
                    sign(x[1]/x[0]-y[1]/y[0]) : y[1]-x[1] );

var selected := pairs[:K];

var weight := selected.Select( x->x[0] ).ToArray;
weight.Sum.Println;

var ind := weight.IndexOf( weight.Max );
selected[ind][1].Println;