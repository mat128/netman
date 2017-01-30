from netman.core.objects.bond import Bond
from netman.core.objects.exceptions import UnknownVlan, BondAlreadyExist, BadBondNumber, \
    UnknownBond, VlanAlreadyExist, UnknownInterface
from netman.core.objects.interface import Interface
from netman.core.objects.port_modes import TRUNK
from netman.core.objects.switch_base import SwitchBase
from netman.core.objects.vlan import Vlan


def get_from_descriptor(switch_descriptor):
    return Memory(switch_descriptor=switch_descriptor)


class Memory(SwitchBase):
    def __init__(self, switch_descriptor):
        super(Memory, self).__init__(switch_descriptor)
        self.vlans = {}
        self.bonds = {}
        self.interfaces = [
            Interface(name='Port 1',
                      port_mode=TRUNK), # TODO(mmitchell): BUG: port_mode is mandatory otherwise interface can't get serialized.
            Interface(name='Port 2',
                      port_mode=TRUNK), # TODO(mmitchell): BUG: port_mode is mandatory otherwise interface can't get serialized.
            Interface(name='Port 3',
                      port_mode=TRUNK), # TODO(mmitchell): BUG: port_mode is mandatory otherwise interface can't get serialized.
            Interface(name='Port 4',
                      port_mode=TRUNK), # TODO(mmitchell): BUG: port_mode is mandatory otherwise interface can't get serialized.
        ]

    # NOTE(mmitchell): Boilerplate stuff

    def _connect(self):
        pass

    def _disconnect(self):
        pass

    def _start_transaction(self):
        pass

    def _end_transaction(self):
        pass

    def commit_transaction(self):
        pass

    def rollback_transaction(self):
        pass

    # NOTE(mmitchell): End boilerplate stuff


    # Create one
    def add_bond(self, number):
        number = int(number)
        if number == 1000:
            raise BadBondNumber()  # TODO(mmitchell): rules for this are obscure
        if number in self.bonds.keys():
            raise BondAlreadyExist()
        self.bonds[number] = Bond(number=number,
                                  port_mode=TRUNK) # TODO(mmitchell): BUG: port_mode is mandatory otherwise interface can't get serialized.

    def add_vlan(self, number, name=None):
        if number in self.vlans.keys():
            raise VlanAlreadyExist(number)
        self.vlans[number] = Vlan(number=number, name=name)

    # Get one
    def get_bond(self, number):
        try:
            return self.bonds[number]
        except KeyError:
            raise UnknownBond()

    def get_interface(self, interface_id):
        try:
            return next((i for i in self.interfaces if i.name == interface_id))
        except StopIteration:
            raise UnknownInterface(interface_id)

    def get_vlan(self, number):
        try:
            vlan = self.vlans[number]
        except KeyError:
            raise UnknownVlan(number)
        return vlan

    # Get many
    def get_bonds(self):
        return [bond for bond in self.bonds.values()]

    def get_interfaces(self):
        return self.interfaces

    def get_vlans(self):
        return [vlan for vlan in self.vlans.values()]

    # Remove one
    def remove_bond(self, number):
        if number == 999:
            raise UnknownBond()  # TODO(mmitchell): rules for this are obscure
        try:
            del self.bonds[number]
        except KeyError:
            raise UnknownBond()

    # Misc / non-standard
    def get_versions(self):
        return {'id': id(self)}



