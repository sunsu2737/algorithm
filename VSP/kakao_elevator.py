import requests


url = 'http://litmuss.iptime.org:80'


def start(user, problem, count):
    uri = url + '/start' + '/' + user + '/' + str(problem) + '/' + str(count)
    return requests.post(uri).json()


def oncalls(token):
    uri = url + '/oncalls'
    return requests.get(uri, headers={'X-Auth-Token': token}).json()


def action(token, cmds):
    uri = url + '/action'
    return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': cmds}).json()


class Elevator:

    def __init__(self, id, floor, passengers, status):
        self.id = id
        self.floor = floor
        self.passengers = passengers
        self.status = status

    def update(self, id, floor, passengers, status):
        self.id = id
        self.floor = floor
        self.passengers = passengers
        self.status = status

    def up(self):
        if self.status == 'STOPPED':
            return 'UP'
        elif self.status == 'OPENED':
            return 'CLOSE'
        elif self.status == 'UPWARD':
            return 'UP'
        elif self.status == 'DOWNWARD':
            return 'STOP'

    def down(self):
        if self.status == 'STOPPED':
            return 'DOWN'
        elif self.status == 'OPENED':
            return 'CLOSE'
        elif self.status == 'UPWARD':
            return 'STOP'
        elif self.status == 'DOWNWARD':
            return 'DOWN'

    def stop(self):
        if self.status == 'STOPPED':
            return 'STOP'
        elif self.status == 'OPENED':
            return 'CLOSE'
        elif self.status == 'UPWARD':
            return 'STOP'
        elif self.status == 'DOWNWARD':
            return 'STOP'

    def open(self):
        if self.status == 'STOPPED':
            return 'OPEN'
        elif self.status == 'OPENED':
            return 'OPEN'
        elif self.status == 'UPWARD':
            return 'STOP'
        elif self.status == 'DOWNWARD':
            return 'STOP'

    def enter(self):
        if self.status == 'STOPPED':
            return 'OPEN'
        elif self.status == 'OPENED':
            return 'ENTER'
        elif self.status == 'UPWARD':
            return 'STOP'
        elif self.status == 'DOWNWARD':
            return 'STOP'

    def exit(self):
        if self.status == 'STOPPED':
            return 'OPEN'
        elif self.status == 'OPENED':
            return 'EXIT'
        elif self.status == 'UPWARD':
            return 'STOP'
        elif self.status == 'DOWNWARD':
            return 'STOP'

    def close(self):
        if self.status == 'STOPPED':
            return 'STOP'
        elif self.status == 'OPENED':
            return 'CLOSE'
        elif self.status == 'UPWARD':
            return 'UP'
        elif self.status == 'DOWNWARD':
            return 'DOWN'


def p0_simulator():
    user = 'yong'
    problem = 1
    count = 4

    ret = start(user, problem, count)
    token = ret['token']
    print('Token for %s is %s' % (user, token))
    elevator_list = [Elevator(i, 1, [], 'STOPPED') for i in range(count)]
    command_list = []
    complete = 0
    while True:
        _, _, elevators, calls, is_end = oncalls(token).values()

        # print(calls)
        # print()
        # print(calls)
        if is_end:

            break

        for elevator in elevators:
            id, floor, passengers, status = elevator.values()
            elevator_list[id].update(id, floor, passengers, status)
        for elevator in elevator_list:
            call_list = []

            command = {"elevator_id": elevator.id, "command": ''}
            for passenger in elevator.passengers:

                if elevator.floor == passenger['end']:
                    command['command'] = elevator.exit()
                    call_list.append(passenger['id'])
            if command['command'] == '':
                if (elevator.status == 'OPENED' or elevator.status == 'STOPPED') and len(elevator.passengers) < 8:

                    if calls:

                        i = 0
                        while True:
                            call = calls[i]

                            if elevator.floor == call['start'] and len(call_list)+len(elevator.passengers) < 8:
                                calls.pop(i)
                                command['command'] = elevator.enter()
                                call_list.append(call["id"])
                            else:
                                i += 1
                            if i >= len(calls):
                                break

            if command['command'] == '':
                if elevator.passengers:

                    if elevator.status == 'DOWNWARD':
                        i = 0
                        if calls:
                            while True:
                                call = calls[i]

                                if elevator.floor == call['start'] and len(call_list)+len(elevator.passengers) < 8 and call['start'] > call['end']:
                                    calls.pop(i)
                                    command['command'] = elevator.enter()
                                    call_list.append(call["id"])
                                else:
                                    i += 1
                                if i >= len(calls):
                                    break

                    if elevator.status == 'UOWARD':
                        i = 0
                        if calls:
                            while True:
                                call = calls[i]

                                if elevator.floor == call['start'] and len(call_list)+len(elevator.passengers) < 8 and call['start'] < call['end']:
                                    calls.pop(i)
                                    command['command'] = elevator.enter()
                                    call_list.append(call["id"])
                                else:
                                    i += 1
                                if i >= len(calls):
                                    break
                    if command['command'] == '':
                        if elevator.passengers[0]['end'] < elevator.floor:

                            command['command'] = elevator.down()
                        elif elevator.passengers[0]['end'] > elevator.floor:

                            command['command'] = elevator.up()

            if command['command'] == '':
                i = 0
                if calls:
                    while True:
                        call = calls[i]

                        if elevator.floor == call['start'] and len(call_list)+len(elevator.passengers) < 8:
                            calls.pop(i)
                            command['command'] = elevator.enter()
                            call_list.append(call["id"])
                        else:
                            i += 1
                        if i >= len(calls):
                            break
                if command['command'] == '':
                    if elevator.passengers:

                        if elevator.passengers[0]['end'] < elevator.floor:

                            command['command'] = elevator.down()
                        elif elevator.passengers[0]['end'] > elevator.floor:

                            command['command'] = elevator.up()
                    else:
                        if calls:
                            if elevator.id == 0 or elevator.id == 2:
                                if elevator.floor < calls[0]['start']:
                                    command['command'] = elevator.up()
                                else:
                                    command['command'] = elevator.down()
                            else:
                                if elevator.floor < calls[-1]['start']:
                                    command['command'] = elevator.up()
                                else:
                                    command['command'] = elevator.down()
                        else:
                            command['command'] = elevator.stop()

            if command['command'] == 'ENTER' or command['command'] == 'EXIT':
                if command['command'] == 'EXIT':
                    complete += len(call_list)
                    print(complete)
                command['call_ids'] = call_list
            command_list.append(command)

        print(command_list, elevator_list[0].floor)
        action(token, command_list)
        command_list = []


if __name__ == '__main__':
    p0_simulator()
