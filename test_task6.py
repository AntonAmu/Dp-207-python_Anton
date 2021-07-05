from task6 import *
import pytest



@pytest.fixture()
def json_file(tmpdir):
    a_file = tmpdir.join('tickets.json')
    data = [{"id": 1, "number": "113123"}, {"id": 2, "number": "465645"}, {"id": 3, "number": "123456"}]
    with open(a_file, 'w') as f:
        json.dump(data, f)
    return str(Path(a_file))

@pytest.fixture()
def create_three_tickets_valid_six_sign():
    ticket1 = Ticket('161103')
    ticket2 = Ticket('888888')
    ticket3 = Ticket('456789')
    return ticket1, ticket2, ticket3
        
@pytest.fixture()
def reset_ticket():
    return Ticket.reset()

@pytest.fixture()
def create_serie_with_four_tickets_valid_six_sign(create_three_tickets_valid_six_sign):
    ticket1, ticket2, ticket3 = create_three_tickets_valid_six_sign
    ticket4 = Ticket('123123')
    serie = SerieOfTickets(num_len = 6)
    serie.add(ticket1)
    serie.add(ticket2)
    serie.add(ticket3)
    serie.add(ticket4)
    return serie

def test_create_valid_ticket_str(reset_ticket):
    ticket = Ticket('161103')
    assert ticket.number == '161103'
    assert ticket.id == 1

def test_create_invalid_ticket_str(reset_ticket):
    with pytest.raises(ValidationException):
        ticket = Ticket('161.103')

def test_create_valid_ticket_int_four_sign(reset_ticket):
    ticket = Ticket(111, num_len = 4)
    assert ticket.number == '0111'
    assert ticket.id == 1

def test_create_valid_ticket_int_six_sign(reset_ticket):
    ticket = Ticket(111)
    assert ticket.number == '000111'
    assert ticket.id == 1

def test_create_valid_ticket_from_class_serieOfTickets(reset_ticket):
    ticket = SerieOfTickets.ticket('888888')
    assert ticket.number == '888888'
    assert ticket.id == 1

def test_add_valid_tickets_toserie(reset_ticket, create_serie_with_four_tickets_valid_six_sign):
    serie = create_serie_with_four_tickets_valid_six_sign
    assert serie.tickets == {1: '161103', 2: '888888', 3: '456789', 4: '123123'}
    
def test_valid_set_approach_to_serie():
    serie = SerieOfTickets()
    serie.set_approach('Moskow')
    assert serie._SerieOfTickets__approach in Approach.list_of_approach.values()

def test_set_invalid_approach_to_serie():
    serie = SerieOfTickets()
    with pytest.raises(CanNotFindApproachException):
        serie.set_approach('Kiev')

def test_count_lucky_tickets_moskow(create_serie_with_four_tickets_valid_six_sign):
    serie = create_serie_with_four_tickets_valid_six_sign
    serie.set_approach('Moskow')
    assert serie.count_lucky_tickets() == 2

def test_count_lucky_tickets_piter(create_serie_with_four_tickets_valid_six_sign):
    serie = create_serie_with_four_tickets_valid_six_sign
    serie.set_approach('Piter')
    assert serie.count_lucky_tickets() == 1

def test_total_amount_of_lucky_tickets_moskow():
    serie = SerieOfTickets(num_len = 6)
    serie.set_approach('Moskow')
    assert serie._SerieOfTickets__approach.total_amount_of_lucky_tickets(serie) == 55252

@pytest.mark.skip(reason="too long calculation")
def test_total_amount_of_lucky_tickets__piter():
    serie = SerieOfTickets(num_len = 6)
    serie.set_approach('Piter')
    assert serie._SerieOfTickets__approach.total_amount_of_lucky_tickets(serie) == 25081

def test_create_serie_from_file(json_file):
    serie = SerieOfTickets(num_len = 6)
    serie.create_serie_from_file('tickets.json')
    assert serie.tickets == {1: '113123', 2: '465645', 3: '123456'}