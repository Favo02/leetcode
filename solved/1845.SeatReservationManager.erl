-module('1845.SeatReservationManager').
-export([seat_manager_init_/1, seat_manager_reserve/0, seat_manager_unreserve/1]).

% funcions signatures REQUIRED by leetcode, cannot be modified
-spec seat_manager_init_(N :: integer()) -> any().
-spec seat_manager_reserve() -> integer().
-spec seat_manager_unreserve(SeatNumber :: integer()) -> any().

seat_manager_init_(N) ->
  % check if manager is already registered (leetcode calls this without restaring the BEAM)
  Registered = whereis(manager),
  if
    Registered =/= undefined -> unregister(manager);
    true -> none
  end,
  % register manager
  register(
    manager,
    spawn(fun() ->
      seat_manager(lists:seq(1, N))
    end)
  ).

seat_manager_reserve() ->
  % send message to manager to reserve a seat (self() is required for reply)
  manager ! {reserve, self()},
  % receive reserved seat
  receive
    {reserved, Seat} -> Seat
  end.

seat_manager_unreserve(SeatNumber) ->
  % send message to managet to unreserve a seat
  manager ! {unreserve, SeatNumber}.

% manager: manage reserve and unreserve operations, saving the current Seats state
seat_manager(Seats) ->
  receive
    % reserve operation:
    {reserve, Pid} ->
      % get min seat free from seats
      Min = lists:nth(1, Seats),
      % send selected seat to function that requested the seat
      Pid ! {reserved, Min},
      % restart manager with updated seats (seats without selected (index 0))
      seat_manager(lists:sublist(Seats, 2, length(Seats)));

    % unreserve operation:
    {unreserve, SeatNumber} ->
      % add new seat to seats list, sort list and
      % restart manager with updated seats
      seat_manager(lists:sort(Seats ++ [SeatNumber]))
  end.
