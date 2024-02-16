import json
import math
from datetime import datetime

from PySide6.QtWidgets import QWidget
from app.ui.ui_activity_item_widget import Ui_ActivityWidget


class ActivityWidget(QWidget, Ui_ActivityWidget):
    def __init__(self, activity):
        """
        Initialize the class with the given activity.

        :param activity: The activity object containing data and type information.
        """
        super().__init__()
        self.setupUi(self)
        self.activity = activity
        self.activity_data = json.loads(activity.Data)

        # Initialize variables for activity details
        self.duration_time = None
        self.avg_heart_rate = None
        self.average_speed = None
        self.distance_km = None
        self.avg_pace = None
        self.max_heart_rate = None
        self.max_speed = None

        # Initialize variables for charts and route
        self.points_for_heart_rate_chart = None
        self.route = None

        # Dynamically call the loading function based on the DataType
        load_function = getattr(self, f'load_data_from{activity.DataType.replace(".", "_")}', None)
        if load_function:
            # Load data from the activity and set activity details
            activity_details = load_function()
            if activity_details:
                self.set_activity_details(*activity_details)

    def set_activity_details(self, name, day_month_year, start_time, duration, avg_speed, distance) -> None:
        """
        Set activity details for the given activity.

        :param name: The name of the activity.
        :type name: str
        :param day_month_year: The date of the activity in the format 'DD/MM/YYYY'.
        :type day_month_year: str
        :param start_time: The start time of the activity.
        :type start_time: str
        :param duration: The duration of the activity.
        :type duration: str
        :param avg_speed: The average speed during the activity in km/h.
        :type avg_speed: float
        :param distance: The distance covered during the activity in kilometers.
        :type distance: float

        :return: None
        """
        # Set activity name label
        self.activity_name_label.setText(name.capitalize())

        # Set activity date label
        self.activity_date_label.setText(day_month_year)

        # Set activity start time label
        self.activity_start_time_label.setText(start_time)

        # Set activity duration label
        self.duration.setText(duration)

        # Set average speed label
        self.avg_speed.setText(f'{avg_speed:.2f} km/h')

        # Set distance label
        self.distance.setText(f'{distance:.2f} km')

        # Update class attributes
        self.duration_time = duration
        self.average_speed = f'{avg_speed:.2f} km/h'
        self.distance_km = f'{distance:.2f} km'

    def load_data_from_fit(self):
        """
        Extracts and formats relevant data from the activity_data and returns it.

        :return: A tuple containing the name, date, start time, duration, average speed, and distance of the activity.
        """
        # Extract name
        name = self.activity_data['session_mesgs'][0]['sport']

        # Extract activity date and format it
        activity_date = self.activity_data['session_mesgs'][0]['start_time']
        date_obj = datetime.strptime(activity_date, '%Y-%m-%d %H:%M:%S%z')
        day_month_year = date_obj.strftime('%d.%m.%Y')
        start_time = date_obj.strftime('%H:%M')

        # Extract duration and format it
        duration_in_seconds = int(self.activity_data['session_mesgs'][0]['total_elapsed_time'])
        hours = duration_in_seconds // 3600
        remaining_seconds = duration_in_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        duration = f'{hours:02d}:{minutes:02d}:{seconds:02d}'

        # Extract and format average speed
        avg_speed = self.activity_data['session_mesgs'][0].get('enhanced_avg_speed')
        if avg_speed is None:
            avg_speed = self.activity_data['session_mesgs'][0].get('avg_speed', 0)
        avg_speed *= 3.6

        # Extract distance
        distance = self.activity_data['session_mesgs'][0]['total_distance'] / 1000

        # Fields for summary
        avg_heart_rate = str(self.activity_data['session_mesgs'][0].get('avg_heart_rate'))
        if avg_heart_rate is None:
            avg_heart_rate = '0'
        self.avg_heart_rate = avg_heart_rate
        self.avg_pace = self.calculate_avg_pace(duration_in_seconds, distance)
        max_speed = self.activity_data['session_mesgs'][0]['enhanced_max_speed'] * 3.6
        self.max_speed = f'{max_speed:.2f} km/h'
        max_heart_rate = str(self.activity_data['session_mesgs'][0].get('max_heart_rate'))
        if max_heart_rate is None:
            max_heart_rate = '0'
        self.max_heart_rate = max_heart_rate

        # Points for heart rate chart
        heard_rate_points = []
        route = []
        for point in self.activity_data['record_mesgs']:
            iso_format_time = point['timestamp'].split("+")[0]
            iso_format_time = iso_format_time.replace(" ", "T")
            heart_rate = point.get('heart_rate')
            if heart_rate is not None:
                heart_rate_point = {
                    'time': iso_format_time,
                    'heart_rate': float(heart_rate),
                }
                heard_rate_points.append(heart_rate_point)

            lat = point.get('position_lat')
            lon = point.get('position_long')
            if lat is not None or lon is not None:
                coordinates = [self.semicircles_to_degrees(lat),
                               self.semicircles_to_degrees(lon)]
                route.append(coordinates)

        self.points_for_heart_rate_chart = heard_rate_points
        self.route = route

        return name, day_month_year, start_time, duration, avg_speed, distance

    @staticmethod
    def semicircles_to_degrees(semicircles: float) -> float:
        """
        Convert semicircles to degrees.

        :param semicircles: The value in semicircles to be converted to degrees.
        :type semicircles: float

        :return: The value converted to degrees.
        :rtype: float
        """
        return semicircles * (180.0 / 2 ** 31)

    @staticmethod
    def calculate_avg_pace(time_in_seconds: int, distance: float) -> str:
        """
        Calculate the average pace in minutes and seconds per kilometer.

        :param time_in_seconds: The time taken to cover the given distance in seconds.
        :type time_in_seconds: int
        :param distance: The distance covered in kilometers.
        :type distance: float

        :return: The average pace in the format MM'SS" / km.
        :rtype: str
        """
        avg_pace_in_seconds = time_in_seconds / distance  # Calculate average pace in seconds per kilometer
        avg_pace_minutes = int(avg_pace_in_seconds // 60)  # Calculate minutes in the average pace
        avg_pace_seconds = int(avg_pace_in_seconds % 60)  # Calculate seconds in the average pace
        return f'{avg_pace_minutes:02d}\'{avg_pace_seconds:02d}\" / km'

    def load_data_from_gpx(self):
        name = self.activity_data['tracks'][0]['name']

        activity_date = self.activity_data['tracks'][0]['segments'][0]['points'][0]['time']
        date_obj = datetime.fromisoformat(activity_date)

        day_month_year = date_obj.strftime('%d.%m.%Y')

        start_time = date_obj.strftime('%H:%M')

        start = self.activity_data['tracks'][0]['segments'][0]['points'][0]['time']
        last_index = len(self.activity_data['tracks'][0]['segments'][0]['points']) - 1
        end = self.activity_data['tracks'][0]['segments'][0]['points'][last_index]['time']

        # Parse the strings to datetime objects
        datetime_obj1 = datetime.fromisoformat(start)
        datetime_obj2 = datetime.fromisoformat(end)

        # Calculate the difference between the two datetime objects
        time_difference = datetime_obj2 - datetime_obj1
        total_seconds = time_difference.total_seconds()

        # Calculate hours, minutes, and seconds from total seconds
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Format the time difference with two digits for hours, minutes, and seconds
        duration = f'{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}'

        total_speed = 0
        max_speed = 0
        total_heart_rate = 0
        max_heart_rate = 0
        heart_rate_points = []
        route = []
        point_count = len(self.activity_data['tracks'][0]['segments'][0]['points'])
        for point in self.activity_data['tracks'][0]['segments'][0]['points']:
            speed = point['extensions'].get('speed')
            if speed is not None:
                speed = float(speed)
                total_speed += speed
                if speed > max_speed:
                    max_speed = speed

            heart_rate = point['extensions'].get('hr')
            if heart_rate is not None:
                total_heart_rate += heart_rate
                if heart_rate > max_heart_rate:
                    max_heart_rate = heart_rate

                iso_format_time = point['time']
                iso_format_time = iso_format_time.split("+")[0]
                heart_rate_point = {
                    'time': iso_format_time,
                    'heart_rate': float(heart_rate)
                }
                heart_rate_points.append(heart_rate_point)

            coordinates = [point['latitude'], point['longitude']]
            route.append(coordinates)
        self.points_for_heart_rate_chart = heart_rate_points
        self.route = route

        self.max_speed = f'{(max_speed * 3.6):.2f} km/h'
        self.avg_heart_rate = str(int(total_heart_rate / point_count))
        self.max_heart_rate = str(max_heart_rate)

        avg_speed = (total_speed / point_count) * 3.6

        distance = self.calculate_distance(self.activity_data['tracks'][0]['segments'][0]['points'])

        self.avg_pace = self.calculate_avg_pace(int(total_seconds), distance)

        return name, day_month_year, start_time, duration, avg_speed, distance

    @staticmethod
    def time_to_seconds(iso_format_time: str) -> float:
        """Converts ISO time to seconds from midnight.

        :param iso_format_time: The ISO format time string.
        :type iso_format_time: str

        :return: The number of seconds since midnight.
        :rtype: float
        """
        # Remove time zone
        iso_format_time = iso_format_time.split("+")[0]

        # Convert ISO time to datetime object
        datetime_obj = datetime.strptime(iso_format_time, "%Y-%m-%dT%H:%M:%S")

        # Calculate seconds since midnight
        seconds_since_midnight = (
                datetime_obj - datetime_obj.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

        return seconds_since_midnight

    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        """
        Calculate the great-circle distance between two points on the Earth given their latitude and longitude in decimal degrees.

        :param lat1: Latitude of the first point
        :type lat1: float
        :param lon1: Longitude of the first point
        :type lon1: float
        :param lat2: Latitude of the second point
        :type lat2: float
        :param lon2: Longitude of the second point
        :type lon2: float

        :return: The distance between the two points in kilometers
        :rtype: float
        """
        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        r = 6371  # Radius of Earth in kilometers
        return c * r

    def calculate_distance(self, points):
        """
        Calculate the total distance between a series of points using Haversine formula.

        :param points: A list of dictionaries containing latitude and longitude for each point
        :type points: list

        :return: The total distance between all the points
        :rtype: float
        """

        total_distance = 0  # initialize total distance
        for i in range(len(points) - 1):
            lat1, lon1 = points[i]['latitude'], points[i]['longitude']  # get latitude and longitude for point 1
            lat2, lon2 = points[i + 1]['latitude'], points[i + 1]['longitude']  # get latitude and longitude for point 2
            total_distance += self.haversine(lat1, lon1, lat2,
                                             lon2)  # calculate distance between two points and add to total
        return total_distance  # return the total distance

    def load_data_from_tcx(self):
        name = self.activity_data[0]['Sport']

        activity_date = self.activity_data[0]['Lap'][0]['StartTime']
        date_obj = datetime.strptime(activity_date, '%Y-%m-%dT%H:%M:%SZ')

        day_month_year = date_obj.strftime('%d.%m.%Y')

        start_time = date_obj.strftime('%H:%M')

        duration_in_seconds = int(self.activity_data[0]['Lap'][0]['TotalTimeSeconds'])
        hours = duration_in_seconds // 3600
        remaining_seconds = duration_in_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        duration = f'{hours:02d}:{minutes:02d}:{seconds:02d}'

        total_speed = 0
        max_speed = 0
        heart_rate_points = []
        route = []
        point_count = len(self.activity_data[0]['Lap'][0]['Track'])
        for point in self.activity_data[0]['Lap'][0]['Track']:
            speed = float(point['Speed'])
            total_speed += speed
            if speed > max_speed:
                max_speed = speed
            iso_format_time = point['Time'].split("Z")[0]
            heart_rate = point['HeartRateBpm']
            heart_rate_point = {
                'time': iso_format_time,
                'heart_rate': float(heart_rate) if heart_rate is not None else 0
            }
            heart_rate_points.append(heart_rate_point)

            coordinates = [float(point['Position']['LatitudeDegrees']), float(point['Position']['LongitudeDegrees'])]
            route.append(coordinates)
        self.points_for_heart_rate_chart = heart_rate_points
        self.route = route

        avg_speed = (total_speed / point_count) * 3.6

        distance = int(self.activity_data[0]['Lap'][0]['DistanceMeters']) / 1000

        # Summary fields
        self.avg_heart_rate = str(self.activity_data[0]['Lap'][0]['AverageHeartRateBpm'])
        self.avg_pace = self.calculate_avg_pace(duration_in_seconds, distance)
        self.max_speed = f'{(max_speed * 3.6):.2f} km/h'
        self.max_heart_rate = str(self.activity_data[0]['Lap'][0]['MaximumHeartRateBpm'])

        return name, day_month_year, start_time, duration, avg_speed, distance
