from typing import TypedDict

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


class Warehouse:
    Id: int
    Stock: list[LegosQty]


class Daily(TypedDict):
    DayNumber: int
    Trucks: list[TruckDaily]
    Customers: list[CustomerDaily]
    Warehouses: list[Warehouse]
    Legos: list[LegoType]
