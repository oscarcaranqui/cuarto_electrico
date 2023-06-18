from typing import List
from dataclasses import dataclass, field


@dataclass
class Address:
    aplicacion: str
    ip: str = field(default=None, init=False)
    # port: int | str = field(default=None, init=False)
    method: str = field(default=None, init=False)
    baudrate: str = field(default=None, init=False)
    slave: int


@dataclass
class BreakerState:
    value: int
    status: str


@dataclass
class ComapStatus:
    mgcb_closed: int
    mcb_closed: int
    btb_appl: int
    intelimains: int


@dataclass
class Controlador:
    address: Address
    status: str

    ubat: int
    cpu_temp: int
    mains_v_l1_n: int
    mains_v_l2_n: int
    mains_v_l3_n: int
    mains_v_l1_l2: int
    mains_v_l2_l3: int
    mains_v_l3_l1: int
    mains_freq: int
    mains_curr_l1: int
    mains_curr_l2: int
    mains_curr_l3: int
    bus_v_l1_n: int
    bus_v_l2_n: int
    bus_v_l3_n: int
    bus_v_l1_l2: int
    bus_v_l2_l3: int
    bus_v_l3_l1: int

    breaker_state: BreakerState = field(default=None,init=False)
    comap_status: ComapStatus = field(default=None,init=False)

@dataclass
class Medidor:
    address: Address
    status: str
    date: str = field(default=None, init=False)

    # ACCUMULATED ENERGY - 32 BIT FLOATING POINT VALUES
    active_energy_delivered: float = field(init=False)
    active_energy_received: float = field(init=False)
    active_energy_delivered_more_received: float = field(init=False)
    active_energy_deliverd_less_received: float = field(init=False)
    reactive_energy_delivered: float = field(init=False)
    reactive_energy_received: float = field(init=False)
    reactive_energy_delivered_more_received: float = field(init=False)
    reactive_energy_delivered_less_received: float = field(init=False)
    apparent_energy_delivered: float = field(init=False)
    apparent_energy_received: float = field(init=False)
    apparent_energy_deliverd_more_received: float = field(init=False)
    apparent_energy_deliverd_less_received: float = field(init=False)

    # CURRENT
    current_a: float = field(init=False)
    current_b: float = field(init=False)
    current_c: float = field(init=False)
    current_n: float = field(init=False)
    current_g: float = field(init=False)
    current_avg: float = field(init=False)

    # CURRENT UNBALANCE
    current_unbalance_a: float = field(init=False)
    current_unbalance_b: float = field(init=False)
    current_unbalance_c: float = field(init=False)
    current_unbalance_worst: float = field(init=False)

    # VOLTAGE
    voltage_ab: float = field(init=False)
    voltage_bc: float = field(init=False)
    voltage_ca: float = field(init=False)
    voltage_ll_avg: float = field(init=False)
    voltage_an: float = field(init=False)
    voltage_bn: float = field(init=False)
    voltage_cn: float = field(init=False)
    voltage_ng: float = field(init=False)
    voltage_ln_avg: float = field(init=False)

    # VOLTAGE UNBALANCE
    voltage_unbalance_ab: float = field(init=False)
    voltage_unbalance_bc: float = field(init=False)
    voltage_unbalance_ca: float = field(init=False)
    voltage_unbalance_ll_worst: float = field(init=False)
    voltage_unbalance_an: float = field(init=False)
    voltage_unbalance_bn: float = field(init=False)
    voltage_unbalance_cn: float = field(init=False)
    voltage_unbalance_ln_worst: float = field(init=False)

    # POWER
    active_power_a: float = field(init=False)
    active_power_b: float = field(init=False)
    active_power_c: float = field(init=False)
    active_power_total: float = field(init=False)
    reactive_power_a: float = field(init=False)
    reactive_power_b: float = field(init=False)
    reactive_power_c: float = field(init=False)
    reactive_power_total: float = field(init=False)
    apparent_power_a: float = field(init=False)
    apparent_power_b: float = field(init=False)
    apparent_power_c: float = field(init=False)
    apparent_power_total: float = field(init=False)

    # POWER FACTOR
    power_factor_a: float = field(init=False)
    power_factor_b: float = field(init=False)
    power_factor_c: float = field(init=False)
    power_factor_total: float = field(init=False)
    displacement_power_factor_a: float = field(init=False)
    displacement_power_factor_b: float = field(init=False)
    displacement_power_factor_c: float = field(init=False)
    displacement_power_factor_total: float = field(init=False)

    # TOTAL HARMONIC DISTORTION, CURRENT
    thd_current_a: float = field(init=False)
    thd_current_b: float = field(init=False)
    thd_current_c: float = field(init=False)
    thd_current_n: float = field(init=False)
    thd_current_g: float = field(init=False)

    # TOTAL HARMONIC DISTORTION, VOLTAGE
    thd_voltage_ab: float = field(init=False)
    thd_voltage_bc: float = field(init=False)
    thd_voltage_ca: float = field(init=False)
    thd_voltage_ll: float = field(init=False)
    thd_voltage_an: float = field(init=False)
    thd_voltage_bn: float = field(init=False)
    thd_voltage_cn: float = field(init=False)
    thd_voltage_ng: float = field(init=False)
    thd_voltage_ln: float = field(init=False)

    # TOTAL DEMAND DISTORTION
    total_demand_distortion: float = field(init=False)

    # FRECUENCY
    frequency: float = field(init=False)




    v12_voltage: float = field(init=False)
    v23_voltage: float = field(init=False)
    v31_voltage: float = field(init=False)

    v1_v12_demand: float = field(init=False)
    v2_v23_demand: float = field(init=False)
    v3_v31_demand: float = field(init=False)

    i1_current: float = field(init=False)
    i2_current: float = field(init=False)
    i3_current: float = field(init=False)
    #
    power_factor_l1: float = field(init=False)
    power_factor_l2: float = field(init=False)
    power_factor_l3: float = field(init=False)
    total_pf: float = field(init=False)

    kw_l1: float = field(init=False)
    kw_l2: float = field(init=False)
    kw_l3: float = field(init=False)
    total_kw: float = field(init=False)

    kvar_l1: float = field(init=False)
    kvar_l2: float = field(init=False)
    kvar_l3: float = field(init=False)
    total_kvar: float = field(init=False)

    kva_l1: float = field(init=False)
    kva_l2: float = field(init=False)
    kva_l3: float = field(init=False)
    total_kva: float = field(init=False)

@dataclass
class Response:

    status: str
    tipo_de_red: str = field(default=None, init=False)
    controladores: List[dict] = field(default=None, init=False)
    medidores: List[dict] = field(default=None, init=False)
    date: str


