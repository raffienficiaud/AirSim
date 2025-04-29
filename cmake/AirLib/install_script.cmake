message(STATUS "coucou ${CMAKE_INSTALL_PREFIX}")

find_program(PYTHON_EXE python3)

execute_process(
    COMMAND
        ${PYTHON_EXE} ${CMAKE_CURRENT_LIST_DIR}/configure_unreal_project.py ${CMAKE_INSTALL_PREFIX}
)
