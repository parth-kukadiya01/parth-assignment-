from app.utils.sessioin_decorator import with_session
from sqlmodel import select
from app.models.models import Project
from app.schemas.schemas import ProjectNotFoundError

@with_session
def get_all_projects(*, session=None):
    return session.exec(select(Project)).all()

@with_session
def create_new_project(project_data, current_user, *, session=None):
    try:
        project = Project(**project_data.model_dump(), created_by=current_user.id)
        session.add(project)
        session.commit()
        session.refresh(project)
        return project
    except Exception as exc:
        session.rollback()
        raise exc

@with_session
def get_project_by_id(project_id, *, session=None):
    project = session.get(Project, project_id)
    if not project:
        raise ProjectNotFoundError()
    return project

@with_session
def update_project_by_id(project_id, project_data, *, session=None):
    project = session.get(Project, project_id)
    if not project:
        raise ProjectNotFoundError()
    try:
        for key, value in project_data.model_dump().items():
            setattr(project, key, value)
        session.add(project)
        session.commit()
        session.refresh(project)
        return project
    except Exception as exc:
        session.rollback()
        raise exc

@with_session
def delete_project_by_id(project_id, *, session=None):
    project = session.exec(select(Project).where(Project.id == project_id)).first()
    if not project:
        raise ProjectNotFoundError()
    try:
        session.delete(project)
        session.commit()
        return True
    except Exception as exc:
        session.rollback()
        raise exc