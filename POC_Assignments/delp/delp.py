import logging
import os
import platform
import requests
import traceback
import unittest

from abc import ABCMeta, abstractmethod
from datetime import datetime
from functools import wraps
from pytz import timezone


_LOGGER = logging.getLogger(__name__)

time_format = '%Y-%m-%dT%H:%M:%S%z'
# Get the key from Environment.
dev_api_key = 'e727d1f4199649bda474fefdb7d39b6e'
test_api_key = 'e727d1f4199649bda474fefdb7d39b6e'
tmz = 'Asia/Kolkata'
numer_of_trains = 10


def exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException:
            print(traceback.format_exc().split('\n'))
        except requests.exceptions.ConnectTimeout:
            print(traceback.format_exc().split('\n'))
        except ConnectionError:
            print(traceback.format_exc().split('\n'))
        except IndexError:
            print(traceback.format_exc().split('\n'))
        except KeyError:
            print(traceback.format_exc().split('\n'))
        except Exception:
            print(traceback.format_exc().split('\n'))
    return wrapper


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


###
# Helper methods
###

class Utilities:

    @staticmethod
    @exception
    def _get_current_time():
        dt_today = datetime.today().astimezone(timezone(tmz))
        return dt_today

    @staticmethod
    @exception
    def _convert_to_local_tmz(time_string):
        dt_global = datetime.strptime(time_string, time_format)
        dt_local = dt_global.astimezone(timezone(tmz))
        return dt_local

    @staticmethod
    def parameter_processor(filters, include, params):
        parameters = {}
        parameters.update(params)
        parameters['include'] = ','.join(include)
        filters = {f'filter[{k}]': v for k, v in filters.items()}
        parameters.update(filters)
        return parameters

    @exception
    def pretty_print(self, departure_map, station_map):
        print('=' * 32)
        print(self._get_current_time())
        print('=' * 32)
        print()
        for line, stations in departure_map.items():
            print('=' * 15, line, '=' * 15)
            for station in stations:
                print(station_map[station[0]], ':', f'{station[1]} minutes to departure')
            print()


class RequestHandler(metaclass=Singleton):
    _instance = None

    def __init__(self, api_key=None, api_key_env=None):
        key = api_key or api_key_env
        if not key:
            raise KeyError('API key must be given')
        self._api_key = self.authorize_api(api_key, api_key_env)

    @property
    def api_key(self):
        return self._api_key

    @staticmethod
    def authorize_api(api_key, api_key_env):
        if not api_key:
            valid_api_key = os.getenv(api_key_env)

            return valid_api_key

        valid_api_key = api_key
        return valid_api_key

    @exception
    def send_request(self, endpoint, parameters):
        parameters['api_key'] = self._api_key
        base_url = "https://api-v3.mbta.com"
        r = requests.get(base_url + endpoint, params=parameters)
        return r.json()


###
# json parser
###

class JsonParser(Utilities):

    @exception
    def get_departure_times(self, data, count):
        c = 1
        dt_now = self._get_current_time()
        data = data.get('data', None)
        departure_map = {}
        station_list = set()
        for predict_d in data:
            attr = predict_d.get('attributes', None)
            if attr and attr.get('departure_time', None) and c <= count:
                dt_local = self._convert_to_local_tmz(attr['departure_time'])
                departure_in_mins = (dt_local - dt_now).total_seconds()//60
                if departure_in_mins > 0:
                    relations = predict_d.get('relationships', None)
                    if relations:
                        route = relations.get('route', None)
                        stop = relations.get('stop', None)

                        temp = departure_map.get(route['data']['id'], None)
                        t = (stop['data']['id'], departure_in_mins)
                        if temp:
                            departure_map[route['data']['id']].append(t)
                        else:
                            departure_map[route['data']['id']] = [t]
                            station_list.add(stop['data']['id'])
                        c += 1
        return departure_map, station_list

    @exception
    def get_station_name(self, register, station_list):
        parameters = {}
        station_map = {}
        for station in station_list:
            data = Stops(register).get_api(id=station, parameters=parameters)
            attr = data.get('data', None)
            if attr and attr.get('attributes', None):
                name = attr.get('attributes', None)
                station_map[station] = name['platform_name'] if name.get('platform_name', None) else 'No name'
        return station_map

###
# Api methods
###


class API(metaclass=ABCMeta):

    def __init__(self, service):
        self.request_service = service

    @abstractmethod
    def get_api(self, parameters):
        pass


class Schedule(API):

    def get_api(self, parameters):

        data = self.request_service.send_request('/schedules', parameters)
        return data


class Prediction(API):

    def get_api(self, parameters):
        data = self.request_service.send_request('/predictions', parameters)
        return data


class Stops(API):

    def get_api(self, parameters, id):
        data = self.request_service.send_request(f'/stops/{id}', parameters)
        return data

@exception
def main(register):
    # TODO: Validate filters, Include parameters, Addtional params
    filters = {'direction_id': 0, 'stop': 'place-pktrm'}
    include = ['route', 'stop']
    params = {'sort': 'departure_time'}
    j = JsonParser()

    p = Prediction(register)
    parameters = j.parameter_processor(filters, include, params)
    predicted_data = p.get_api(parameters)
    departure_map, s_list = j.get_departure_times(predicted_data, numer_of_trains)
    station_map = j.get_station_name(r, s_list)

    # If prediction fails to get all stations we could use
    # schedule endpoint to get future departing trains list
    count = sum([len(v) for k, v in departure_map.items()])
    if count >= 10:
        j.pretty_print(departure_map, station_map)
    else:
        s = Schedule(r)
        schedule_data = s.get_api(parameters)
        departure_map, s_list = j.get_departure_times(schedule_data, numer_of_trains)
        station_map = j.get_station_name(register, s_list)
        j.pretty_print(departure_map, station_map)


class TestStations(unittest.TestCase):

    def setUp(self):
        self.register = RequestHandler(api_key=test_api_key)
        self.schedule = Schedule(self.register)
        self.prediction = Prediction(self.register)

    # Returns True if the string contains 4 a.
    def test_single_key(self):
        register = RequestHandler(api_key='Dummay_key')
        self.assertEqual(self.register.api_key, register.api_key)

    def test_validate_filters(self):
        filters = {'direction_id': 0, 'stop': 'place-pktrm'}
        include = ['route', 'stop']
        params = {'sort': 'departure_time'}
        response = Utilities.parameter_processor(filters,include, params)
        self.assertIn('filter[stop]', response)
        self.assertIn('filter[direction_id]', response)
        self.assertEqual(response['include'], 'route,stop')

    def test_validate_api(self):
        filters = {'direction_id': 0, 'stop': 'place-pktrm'}
        include = ['route', 'stop']
        params = {'sort': 'departure_time'}
        parameters = Utilities.parameter_processor(filters, include, params)
        response = self.schedule.get_api(parameters)
        self.assertIn('data', response)
        self.assertIn('attributes', response['data'][0])
        self.assertIn('departure_time', response['data'][0]['attributes'])
        self.assertIn('relationships', response['data'][0])
        self.assertIn('route', response['data'][0]['relationships'])
        self.assertIn('stop', response['data'][0]['relationships'])

    def test_validate_no_of_schedules(self):
        filters = {'direction_id': 0, 'stop': 'place-pktrm'}
        include = ['route', 'stop']
        params = {'sort': 'departure_time'}
        parameters = Utilities.parameter_processor(filters, include, params)
        data = self.schedule.get_api(parameters)
        self.assertIn('data', data)
        d_map, s_list = JsonParser().get_departure_times(data, 10)
        count = sum([len(v) for k, v in d_map.items()])
        self.assertEqual(count, 10)
        d_map, s_list = JsonParser().get_departure_times(data, 15)
        count = sum([len(v) for k, v in d_map.items()])
        self.assertEqual(count, 15)


if __name__ == '__main__':
    r = RequestHandler(api_key=dev_api_key)
    unittest.main()
    if platform.python_version() >= '3.8.5':
        main(r)
    else:
        print('The module can run on and above python version 3.8.5')


