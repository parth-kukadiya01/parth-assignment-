from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.schemas import ProjectCreate, ProjectRead, ProjectNotFoundError
from app.models.models import User
from app.utils.dependencies import get_current_user, require_admin
from app.logics.project import (
    get_all_projects,
    create_new_project,
    get_project_by_id,
    update_project_by_id,
    delete_project_by_id,
)
from app.core.logger import logger

router = APIRouter()


@router.get("/", response_model=list[ProjectRead])
def get_projects(current_user: User = Depends(get_current_user)):
    return get_all_projects()


@router.post("/", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
def create_project(
    project_data: ProjectCreate,
    current_user: User = Depends(require_admin),
):
    return create_new_project(project_data, current_user)


@router.get("/{project_id}", response_model=ProjectRead)
def get_project(
    project_id: int,
    current_user: User = Depends(get_current_user),
):
    try:
        return get_project_by_id(project_id)
    except ProjectNotFoundError:
        logger.warning(f"Project not found: id={project_id}")
        raise HTTPException(status_code=404, detail="Project not found")


@router.put("/{project_id}", response_model=ProjectRead)
def update_project(
    project_id: int,
    project_data: ProjectCreate,
    current_user: User = Depends(require_admin),
):
    try:
        return update_project_by_id(project_id, project_data)
    except ProjectNotFoundError:
        logger.warning(f"Update failed, project not found: id={project_id}")
        raise HTTPException(status_code=404, detail="Project not found")


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(
    project_id: int,
    current_user: User = Depends(require_admin),
):
    try:
        delete_project_by_id(project_id)
    except ProjectNotFoundError:
        logger.warning(f"Delete failed, project not found: id={project_id}")
        raise HTTPException(status_code=404, detail="Project not found")