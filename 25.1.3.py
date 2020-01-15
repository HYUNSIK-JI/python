y={1:'one',2:'two'};
y.update({1:'ONE',3:'THREE'});
y.update([[2,'TWO'],[4,'FOUR']]);
y.update(zip([1,2],['one','two']));
print(y);