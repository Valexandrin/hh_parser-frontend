import httpx

from frontend.schemas import Vacancy
from frontend.config import config


class VacancyClient:
    def __init__(self, url: str) -> None:
        self.url = f'{url}/vacancies'

    def get_all(self, status) -> list[Vacancy]:
        res = httpx.get(f'{self.url}/{status}')

        res.raise_for_status()

        vacancies = res.json()

        return [Vacancy(**vacancy) for vacancy in vacancies]

    def get_by_id(self, vacancy_id: int) -> Vacancy:
        res = httpx.get(f'{self.url}/{vacancy_id}', follow_redirects=True)
        res.raise_for_status()

        vacancy = Vacancy(**res.json())

        return vacancy

    def change_status(self, vacancy_id: int, status: str='seen') -> None:
        params = {
            'status': status,
        }
        httpx.put(f'{self.url}/{vacancy_id}', json=params)


vacancies = VacancyClient(config.endpoint.url)
