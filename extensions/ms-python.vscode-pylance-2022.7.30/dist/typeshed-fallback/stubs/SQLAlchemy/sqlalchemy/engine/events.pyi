from .. import event as event

class ConnectionEvents(event.Events):
    def before_execute(self, conn, clauseelement, multiparams, params, execution_options) -> None: ...
    def after_execute(self, conn, clauseelement, multiparams, params, execution_options, result) -> None: ...
    def before_cursor_execute(self, conn, cursor, statement, parameters, context, executemany) -> None: ...
    def after_cursor_execute(self, conn, cursor, statement, parameters, context, executemany) -> None: ...
    def handle_error(self, exception_context) -> None: ...
    def engine_connect(self, conn, branch) -> None: ...
    def set_connection_execution_options(self, conn, opts) -> None: ...
    def set_engine_execution_options(self, engine, opts) -> None: ...
    def engine_disposed(self, engine) -> None: ...
    def begin(self, conn) -> None: ...
    def rollback(self, conn) -> None: ...
    def commit(self, conn) -> None: ...
    def savepoint(self, conn, name) -> None: ...
    def rollback_savepoint(self, conn, name, context) -> None: ...
    def release_savepoint(self, conn, name, context) -> None: ...
    def begin_twophase(self, conn, xid) -> None: ...
    def prepare_twophase(self, conn, xid) -> None: ...
    def rollback_twophase(self, conn, xid, is_prepared) -> None: ...
    def commit_twophase(self, conn, xid, is_prepared) -> None: ...

class DialectEvents(event.Events):
    def do_connect(self, dialect, conn_rec, cargs, cparams) -> None: ...
    def do_executemany(self, cursor, statement, parameters, context) -> None: ...
    def do_execute_no_params(self, cursor, statement, context) -> None: ...
    def do_execute(self, cursor, statement, parameters, context) -> None: ...
    def do_setinputsizes(self, inputsizes, cursor, statement, parameters, context) -> None: ...
