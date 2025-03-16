from typing import TypedDict
from truck import Truck
from entrepot import Entrepot
from client import Client

class TeamCreds(TypedDict):
    teamName: str
    password: str


class SolutionApiModel(TypedDict):
    credentials: TeamCreds
    dayNumber: int
    steps: list[str]


class TruckDaily(TypedDict):
    Id: int
    AffiliatedWarehouseId: int
    Capacity: int


class LegosQty(TypedDict):
    LegoId: int
    Quantity: int


class CustomerDaily(TypedDict):
    Id: int
    Orders: list[LegosQty]


class LegoType(TypedDict):
    Id: int
    Weight: int


class Warehouse(TypedDict):
    Id: int
    Stock: list[LegosQty]


class Coords(TypedDict):
    X: int
    Y: int


class Daily(TypedDict):
    DayNumber: int
    Trucks: list[TruckDaily]
    Customers: list[CustomerDaily]
    Warehouses: list[Warehouse]
    Legos: list[LegoType]


class IdCoords(TypedDict):
    Id: int
    Coordinates: Coords


class MapData(TypedDict):
    Customers: list[IdCoords]
    Warehouses: list[IdCoords]


def load_step(truck: Truck, qty: int, lego: int) -> str:
    return f"load truck={truck.id} quantity={qty} lego={lego}"

def move_to_customer_step(truck: Truck, client: Client) -> str:
    return f"move_to_customer truck={truck.id} customer={client.id}"

def deliver_step(truck: Truck, qty: int, lego: int) -> str:
    return f"deliver truck={truck.id} quantity={qty} lego={lego}"

def move_to_warehouse_step(truck: Truck, entrepot: Entrepot) -> str:
    return f"move_to_warehouse truck={truck.id} warehouse={entrepot.id}"


