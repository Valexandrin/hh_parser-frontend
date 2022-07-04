from flask import Blueprint, render_template

from frontend.client.vacancies import vacancies


view = Blueprint('vacancies', __name__)


@view.route('/')
def show_vacancies():
    all_vacancies = vacancies.get_all()


    return render_template(
        'vacancies.html',
        vacancies = [vacancy.dict() for vacancy in all_vacancies],
    )


@view.route('/<uid>')
def show_vacancy(uid):
    all_vacancies = vacancies.get_all()
    vacancy = vacancies.get_by_id(uid)

    return render_template(
        'vacancies.html',
        vacancies = [vacancy.dict() for vacancy in all_vacancies],
        vacancy_text = vacancy.description,
    )
