-module('1921').
-export([eliminate_maximum/2]).

-spec eliminate_maximum(Dist :: [integer()], Speed :: [integer()]) -> integer().

round_up(N) ->
  if
    N > trunc(N) -> trunc(N) + 1;
    true -> trunc(N)
  end.

count_time_greather_than_index([]) -> 0;
count_time_greather_than_index([{Index, Time} | []]) ->
  if
    Time > Index -> Index;
    true -> Index-1
  end;
count_time_greather_than_index([{Index, Time} | TL]) ->
  if
    Time > Index -> count_time_greather_than_index(TL);
    true -> Index-1
  end.

eliminate_maximum(Dist, Speed) ->
  DS = lists:map(fun(D) -> round_up(element(2, D) / lists:nth(element(1, D), Speed)) end, lists:enumerate(Dist)),
  DSS = lists:sort(DS),
  count_time_greather_than_index(
    lists:enumerate(
      lists:sublist(DSS, 2, length(DSS))
    )
  ) + 1.

% c('1921').
% '1921':eliminate_maximum([1,3,4], [1,1,1]). % 3
% '1921':eliminate_maximum([1,1,2,3], [1,1,1,1]). % 1
% '1921':eliminate_maximum([3,2,4], [5,3,2]). % 1
% '1921':eliminate_maximum([4,2,8], [2,1,4]). % 2
% '1921':eliminate_maximum([3,5,7,4,5], [2,3,6,3,2]). % 2
