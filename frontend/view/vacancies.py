from flask import Blueprint, render_template

from frontend.client.vacancies import vacancies


view = Blueprint('vacancies', __name__)


@view.route('/')
@view.route('/<path:status>')
def show_vacancies(status: str=''):
    all_vacancies = vacancies.get_all(status)

    return render_template(
        'vacancies.html',
        vacancies = [vacancy.dict() for vacancy in all_vacancies],
        quantity = len(all_vacancies),
        vacancies_status = status,
    )


@view.route('/<int:uid>')
@view.route('/<path:status>/<int:uid>')
def show_vacancy(uid: int, status: str=''):
    vacancy = vacancies.get_by_id(uid)
    vacancies.change_status(uid)
    all_vacancies = vacancies.get_all(status)

    return render_template(
        'vacancies.html',
        vacancies = [vacancy.dict() for vacancy in all_vacancies],
        vacancies_status = status,
        uid = vacancy.uid,
        description = vacancy.description,
        employer = vacancy.employer,
        url = vacancy.url,
        vacancy = vacancy.name,
        area = vacancy.area,
        date = vacancy.published_at.strftime('%d %B %Y'),
        salary_from = vacancy.salary_from if vacancy.salary_from else '',
        salary_to = vacancy.salary_to if vacancy.salary_to else '',
        schedule = vacancy.schedule,
    )
