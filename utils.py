import os
from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class RendezVousConfig:
    first_name: str
    last_name: str
    ramq: str
    ramq_seq: str
    dob_day: str
    dob_month: str
    dob_year: str
    genre: str
    perimeter: str
    reason: str


class PersonLoader:
    config_file_path = Path('.')
    config_file_name = 'config.yml'

    @property
    def config_file(self):
        return self.config_file_path / self.config_file_name

    def load_config_file(self):
        with open(self.config_file, 'r') as yml:
            value = yaml.load(yml, Loader=yaml.FullLoader)
            return RendezVousConfig(**value.get('patient'))

    def get_person(self) -> RendezVousConfig:
        person_config = self.load_config_file()
        return person_config

