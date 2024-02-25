import functools
import logging
import base64
import os
import sys
from datetime import datetime
from pathlib import Path

import bcrypt
from PySide6.QtCore import QIODevice, QBuffer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QTableWidget
from sqlalchemy import URL, create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from .db_init import User, Activity, Device

# Load environment variables from the .env file
if getattr(sys, 'frozen', False):
    # If opened from executable
    application_path = Path(sys.executable).parent
    env_path = application_path / '_internal' / '.env'
else:
    # If opened from terminal (for example. python app.py)
    application_path = Path(__file__).parent
    env_path = application_path / '.env'

load_dotenv(dotenv_path=env_path)

# Define the connection string
connection_string = URL.create(
    'postgresql',
    username=os.environ.get('NEON_USERNAME'),
    password=os.environ.get('NEON_PASSWORD'),
    host=os.environ.get('NEON_HOST'),
    database=os.environ.get('NEON_DATABASE')
)

# Create the database engine
engine = create_engine(connection_string)

# Create the session factory from the engine
Session = sessionmaker(bind=engine)


def provide_session(func):
    """
    A decorator function that provides a session for the wrapped function.
    Accepts a function as input and returns a wrapped function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        session = Session()
        try:
            result = func(*args, session=session, **kwargs)
        except IntegrityError as e:
            session.rollback()
            logging.exception(e)
            result = None
        except Exception as e:
            session.rollback()
            logging.exception(e)
            result = None
        finally:
            session.close()
        return result

    return wrapper


@provide_session
def is_login_available(login: str, session: Session) -> bool:
    """
    Check if login is available

    :param login: The login to check.
    :type login: str
    :param session: Session: An instance of the SQLAlchemy Session class
    :type session: Session

    :return: True if the login is available, False otherwise
    :rtype: bool
    """

    # Query the database for the user
    existing_user = session.query(User).filter_by(Login=login).first()

    return existing_user is None


def hash_password(password: str) -> str:
    """
    Generate a hashed password from the input password string.

    :param password: The input password string.
    :type password: str

    :return: The hashed password string.
    :rtype: str
    """
    # Generate a random salt
    salt = bcrypt.gensalt()

    # Hash the password using the salt
    hashed_password_bytes = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Convert the hashed password to a string
    hashed_password_str = base64.b64encode(hashed_password_bytes).decode('utf-8')

    return hashed_password_str


@provide_session
def add_user(login: str, password: str, session: Session) -> None:
    """
    Add a new user to the database.

    :param login: The user's login
    :type login: str
    :param password: The user's password
    :type password: str
    :param session: The database session
    :type session: Session

    :return: None
    """
    # Hash the user's password
    hashed_password = hash_password(password)

    # Create a new user object
    new_user = User(Login=login, PasswordHash=hashed_password)

    # Add the new user to the session and commit the changes
    session.add(new_user)
    session.commit()


@provide_session
def verify_user(login: str, password: str, session: Session) -> bool:
    """
    Verify the user's login and password.

    :param login: The user's login.
    :type login: str
    :param password: The user's password.
    :type password: str
    :param session: The database session.
    :type session: Session

    :return: True if the user is verified, False otherwise.
    :rtype: bool
    """
    # Query the database for the user
    user = session.query(User).filter_by(Login=login).first()

    # If the user does not exist, return False
    if user is None:
        return False

    # Decode the user's stored password hash and check if it matches the input password
    hashed_password_bytes = base64.b64decode(user.PasswordHash.encode('utf-8'))
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password_bytes):
        return True
    else:
        return False


@provide_session
def get_user_id(login: str, session: Session) -> int:
    """
    Retrieve the user ID for the given login from the database.

    :param login: The user's login name
    :type login: str
    :param session: The database session
    :type session: Session

    :return: The user ID
    :rtype: int
    """
    # Query the database to find the user with the given login
    user = session.query(User).filter_by(Login=login).first()

    # Return the user ID
    return user.UserID


@provide_session
def verify_current_password(login: str, new_password: str, session: Session) -> bool:
    """
    Verify if the provided current password is correct for the given user login.

    :param login: The user's login
    :type login: str
    :param new_password: The new password to be verified
    :type new_password: str
    :param session: The database session
    :type session: Session

    :return: True if the current password is correct, False otherwise
    :rtype: bool
    """
    # Query the user by login
    user = session.query(User).filter_by(Login=login).first()
    # Decode the hashed password
    hashed_password_bytes = base64.b64decode(user.PasswordHash.encode('utf-8'))
    # Check if the user exists and the password is correct
    if user and bcrypt.checkpw(new_password.encode('utf-8'), hashed_password_bytes):
        return True
    else:
        return False


@provide_session
def update_password(login: str, new_password: str, session: Session) -> bool:
    """
    Update the password for a user.

    :param login: The login of the user.
    :type login: str
    :param new_password: The new password to be set.
    :type new_password: str
    :param session: The SQLAlchemy session.
    :type session: Session

    :return: True if the password was updated, False otherwise.
    :rtype: bool
    """
    user = session.query(User).filter_by(Login=login).first()
    if user:
        # Hash the new password
        hashed_password_bytes = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        hashed_password_str = base64.b64encode(hashed_password_bytes).decode('utf-8')
        user.PasswordHash = hashed_password_str
        session.commit()
        return True
    return False


@provide_session
def get_user_devices(user_id: int, session: Session) -> list:
    """
    Retrieve all devices associated with a user.

    :param user_id: The ID of the user.
    :type user_id: int
    :param session: The database session.
    :type session: Session

    :return: A list of devices associated with the user.
    :rtype: list
    """
    return session.query(Device).filter(Device.UserID == user_id).all()


@provide_session
def get_device(device_id: int, session: Session) -> Device:
    """
    Retrieve a device by its ID.

    :param device_id: The ID of the device to retrieve.
    :type device_id: int
    :param session: The database session.
    :type session: Session

    :return: The device object.
    :rtype: Device
    """
    return session.query(Device).filter_by(DeviceID=device_id).first()


@provide_session
def get_activity_count_for_device(device_id: int, session: Session) -> str:
    """
    Get the count of activities for a given device ID.

    :param device_id: The ID of the device.
    :type device_id: int
    :param session: The SQLAlchemy session.
    :type session: Session

    :return: The count of activities as a string.
    :rtype: str
    """
    # Query the session for the count of activities for the given device ID
    activity_count = session.query(Activity).filter_by(DeviceID=device_id).count()

    # Convert the activity count to a string and return it
    return str(activity_count)


@provide_session
def add_device(user_id: int, icon_path: str | QIcon, brand: str, model: str, type: str, session: Session) -> None:
    """
    Add a new device to the database.

    :param user_id: The ID of the user adding the device.
    :type user_id: int
    :param icon_path: The file path or QIcon of the device icon.
    :type icon_path: str | QIcon
    :param brand: The brand of the device.
    :type brand: str
    :param model: The model of the device.
    :type model: str
    :param type: The type of the device.
    :type type: str
    :param session: The database session.
    :type session: Session

    :return: None
    """
    if isinstance(icon_path, str):
        # If icon_path is a string, it's treated as a file path
        with open(icon_path, 'rb') as file:
            icon = file.read()
    elif isinstance(icon_path, QIcon):
        # If icon_path is a QIcon, convert it to QImage and then to byte array
        pixmap = icon_path.pixmap(icon_path.availableSizes()[0])
        image = pixmap.toImage()
        buffer = QBuffer()
        buffer.open(QIODevice.WriteOnly)
        image.save(buffer, 'JPG')
        ba = buffer.data()
        icon = ba.data()
    else:
        raise ValueError('icon_path must be a file path or QIcon')

    new_device = Device(UserID=user_id, Icon=icon, Brand=brand, Model=model, Type=type)
    session.add(new_device)
    session.commit()


def save_changes_to_database(table_widget: QTableWidget) -> None:
    """
    Save changes made in the QTableWidget to the database.

    :param table_widget: The QTableWidget containing the data to be saved.
    :type table_widget: QTableWidget

    :return: None
    """
    # Iterate through each row in the QTableWidget
    for row in range(table_widget.rowCount()):
        # Extract data from the table_widget
        device_id = int(table_widget.item(row, 6).text())
        brand = table_widget.item(row, 1).text()
        model = table_widget.item(row, 2).text()
        device_type = table_widget.item(row, 3).text()

        # Retrieve the device from the database
        device = get_device(device_id)

        # Check if the brand, model, or device type has been modified
        if brand != device.Brand or model != device.Model or device_type != device.Type:
            # Update the device in the database
            update_device(device_id, brand, model, device_type)


@provide_session
def update_device(device_id: int, brand: str, model: str, device_type: str, session: Session) -> bool:
    """
    Update device information in the database.

    :param device_id: The ID of the device to be updated.
    :type device_id: int
    :param brand: The new brand of the device.
    :type brand: str
    :param model: The new model of the device.
    :type model: str
    :param device_type: The new type of the device.
    :type device_type: str
    :param session: The database session.
    :type session: Session

    :return: True if the device was updated successfully, False otherwise.
    :rtype: bool
    """
    # Get the device from the database
    device = session.query(Device).filter_by(DeviceID=device_id).first()

    # If the device exists, update its information and commit the changes
    if device:
        device.Brand = brand
        device.Model = model
        device.Type = device_type
        device.LastUpdate = datetime.now()
        session.commit()
        return True
    return False


@provide_session
def delete_device(selected_device_id: list, table_widget: QTableWidget, session: Session) -> None:
    """
    Delete the selected devices from the database and the table widget.

    :param selected_device_id: List of device IDs to be deleted.
    :type selected_device_id: list
    :param table_widget: The table widget displaying the devices.
    :type table_widget: QTableWidget
    :param session: The database session.
    :type session: Session

    :return: None
    """
    for device_id in selected_device_id:
        row = device_id.row()
        device_id = int(table_widget.item(row, 6).text())  # ID_COLUMN_INDEX is the index of the ID column
        # Retrieve the device from the database
        device = session.query(Device).filter_by(DeviceID=device_id).first()
        # If the device exists, remove it from the table and delete it from the database
        if device:
            table_widget.removeRow(device_id)
            session.delete(device)
            session.commit()


@provide_session
def add_activity_from_json(activity_data: str, data_type: str, device_id: int, session: Session) -> bool:
    """
    Adds activity to the database based on JSON data.

    :param activity_data: Activity data in JSON format.
    :type activity_data: str
    :param data_type: Type of the activity data.
    :type data_type: str
    :param device_id: ID of the device to which the activity is assigned.
    :type device_id: int
    :param session: Database session.
    :type session: Session

    :return: True if the addition is successful, False otherwise.
    :rtype: bool
    """
    try:
        # Create a new activity object
        new_activity = Activity(
            DeviceID=device_id,
            Data=activity_data,
            DataType=data_type
        )

        # Add the activity to the session and commit the changes
        session.add(new_activity)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Error adding activity: {e}")
        return False


@provide_session
def get_user_activities(device_id: int, session: Session) -> list:
    """
    Retrieve activities for a specific device.

    :param device_id: The ID of the device
    :type device_id: int
    :param session: The database session
    :type session: Session

    :return: A list of activities for the specified device
    :rtype: list
    """
    # Retrieve activities for the specified device
    activities = session.query(Activity).filter(Activity.DeviceID == device_id).all()
    return activities


@provide_session
def get_activity(activity_id: int, session: Session) -> Activity:
    """
    Retrieve the activity with the given activity_id from the database.

    :param activity_id: The ID of the activity to retrieve.
    :type activity_id: int
    :param session: The database session.
    :type session: Session

    :return: The activity with the given activity_id.
    :rtype: Activity
    """
    # Query the database for the activity with the given activity_id
    return session.query(Activity).filter(Activity.WorkoutID == activity_id).first()


@provide_session
def delete_activity(activity_id: int, session: Session) -> None:
    """
    Deletes the activity with the given ID.

    :param activity_id: The ID of the activity to be deleted.
    :type activity_id: int
    :param session: The SQLAlchemy session object.
    :type session: Session

    :return: None
    """
    # Delete the activity with the given ID
    session.query(Activity).filter(Activity.WorkoutID == activity_id).delete()
    # Commit the changes
    session.commit()
