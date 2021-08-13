import attr
from typing import NamedTuple

from ai.backend.agent.resources import AbstractComputeDevice
from ai.backend.common.types import DeviceId


@attr.define()
class CUDADevice(AbstractComputeDevice):
    model_name: str
    mother_uuid: DeviceId
    is_mig_device: bool


class DeviceStat(NamedTuple):
    device_id: DeviceId
    mem_total: int
    mem_used: int
    mem_free: int
    gpu_util: int
    mem_util: int
    power_usage: int  # milli-watts
    power_max: int    # milli-watts
    core_temperature: int


class ProcessStat(NamedTuple):
    # absolute value (bytes)
    used_gpu_memory: int
    # percent-based samples
    sm_util: int
    mem_util: int
    enc_util: int
    dec_util: int
