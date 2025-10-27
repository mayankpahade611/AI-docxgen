# Project Documentation

## Code Overview

### File: `C:/flask\docs\conf.py`

**Functions:** github_link, setup

**Classes:** None

**AI Summary:**  This code file defines functions: ['github_link', 'setup'], and classes: []. Here is the main code content: "Pallets_sphinx_themes"


## Git Commit History
### File: `C:/flask\examples\celery\make_celery.py`

**Functions:** None

**Classes:** None

**AI Summary:**  This code file defines functions: [], and classes: []. Here is the main code content: "flask_app = create_app()", "celery" and "task_app"


## Git Commit History
### File: `C:/flask\examples\celery\src\task_app\tasks.py`

**Functions:** add, block, process

**Classes:** None

**AI Summary:**  This code file defines functions: ['add', 'block', 'process', and classes: []. Here is the main code content: importing time, importing shared_task and importing Task@shared_task .


## Git Commit History
### File: `C:/flask\examples\celery\src\task_app\views.py`

**Functions:** result, add, block, process

**Classes:** None

**AI Summary:**  This code file defines functions: ['result', 'add', 'block', 'process', and classes: []. Here is the main code content: import Asyncresult from flask flask and import request from Blueprint from flask .


## Git Commit History
### File: `C:/flask\examples\celery\src\task_app\__init__.py`

**Functions:** create_app, index, celery_init_app, __call__

**Classes:** FlaskTask

**AI Summary:**  This code file defines functions: ['create_app', 'index', 'celery_init_app' and classes: ['FlaskTask'] Here is the main code content: import celery, Task, render_template, views, views and classes .


## Git Commit History
### File: `C:/flask\examples\javascript\js_example\views.py`

**Functions:** index, add

**Classes:** None

**AI Summary:**  This code file defines functions: ['index', 'add'], and classes: []. Here is the main code content: [], [], 'add', 'index' and 'fetch'


## Git Commit History
### File: `C:/flask\examples\javascript\js_example\__init__.py`

**Functions:** None

**Classes:** None

**AI Summary:**  This code file defines functions: [], and classes: []. Here is the main code content: "app = Flask(__name__) # noqa: E402, F401," "E402," "F401" "app" is a Flask application .


## Git Commit History
### File: `C:/flask\examples\javascript\tests\conftest.py`

**Functions:** fixture_app, client

**Classes:** None

**AI Summary:**  This code file defines functions: ['fixture_app', 'client'], and classes: []. Here is the main code content: 'fixture,' 'client', 'test' and 'test_client'


## Git Commit History
### File: `C:/flask\examples\javascript\tests\test_js_example.py`

**Functions:** test_index, check, test_add

**Classes:** None

**AI Summary:**  This code file defines functions: ['test_index', 'check', 'test_add', and classes: []. Here is the main code content: importing pytest, importing flask and importing template_rendered .


## Git Commit History
### File: `C:/flask\examples\tutorial\flaskr\auth.py`

**Functions:** login_required, wrapped_view, load_logged_in_user, register, login, logout

**Classes:** None

**AI Summary:**  This code file defines functions: ['login_required', 'wrapped_view', 'load_logged_in_user', 'register', 'login', 'logout'], and classes: [].


## Git Commit History
### File: `C:/flask\examples\tutorial\flaskr\blog.py`

**Functions:** index, get_post, create, update, delete

**Classes:** None

**AI Summary:**  This code file defines functions: ['index', 'get_post', 'create', 'update', 'delete'], and classes: []. Here is the main code content: import Blueprint and render_template .


## Git Commit History
### File: `C:/flask\examples\tutorial\flaskr\db.py`

**Functions:** get_db, close_db, init_db, init_db_command, init_app

**Classes:** None

**AI Summary:**  This code file defines functions: ['get_db', 'close_db' and 'init_app' [], and classes: []. Here is the main code content: [Get_db] and 'Close_DB' functions . The connection is unique for each request and will be reused .


## Git Commit History
### File: `C:/flask\examples\tutorial\flaskr\__init__.py`

**Functions:** create_app, hello

**Classes:** None

**AI Summary:**  This code file defines functions: ['create_app', 'hello'], and classes: []. Here is the main code content: create_app(test_config=None): # store the database in the instance folder: DATABASE=os.path.join(app.instance_path, "flaskr.sqlite") # register the database commands: "Hello, World!" # apply the blueprints to the app: app.register_blueprint(Auth.bp) # make url_for('index') == url_of('blog.index')


## Git Commit History
### File: `C:/flask\examples\tutorial\tests\conftest.py`

**Functions:** app, client, runner, __init__, login, logout, auth

**Classes:** AuthActions

**AI Summary:**  This code file defines functions: 'app', 'client', 'runner', 'login', 'logout', and classes: ['AuthActions'' It defines functions such as 'test' and 'run', 'test', 'save', 'reset', and 'save' 'Test' is created with a new app instance for each test .


## Git Commit History
### File: `C:/flask\examples\tutorial\tests\test_auth.py`

**Functions:** test_register, test_register_validate_input, test_login, test_login_validate_input, test_logout

**Classes:** None

**AI Summary:**  This code file defines functions: ['test_register', 'test register_validate_input' and 'test_logout', and classes: []. Here is the main code content: importing pytest, flask and flask .


## Git Commit History
### File: `C:/flask\examples\tutorial\tests\test_blog.py`

**Functions:** test_index, test_login_required, test_author_required, test_exists_required, test_create, test_update, test_create_update_validate, test_delete

**Classes:** None

**AI Summary:**  This code file defines functions: ['test_index', 'test_login_required', 'Test_exists_required' and 'test-delete' [], and classes: []. Here is the main code content: .


## Git Commit History
### File: `C:/flask\examples\tutorial\tests\test_db.py`

**Functions:** test_get_close_db, test_init_db_command, fake_init_db

**Classes:** Recorder

**AI Summary:**  This code file defines functions: ['test_get_close_db', 'test_init_db_command', and classes: ['Recorder'] Here is the main code content .


## Git Commit History
### File: `C:/flask\examples\tutorial\tests\test_factory.py`

**Functions:** test_config, test_hello

**Classes:** None

**AI Summary:**  This code file defines functions: ['test_config', 'test_hello', and classes: []. Here is the main code content: "Hello, World!" The code file contains a function that tests create_app without passing test config .


## Git Commit History
### File: `C:/flask\src\flask\app.py`

**Functions:** _make_timedelta, __init__, get_send_file_max_age, send_static_file, open_resource, open_instance_resource, create_jinja_environment, create_url_adapter, raise_routing_exception, update_template_context, make_shell_context, run, test_client, __init__, test_cli_runner, handle_http_exception, handle_user_exception, handle_exception, log_exception, dispatch_request, full_dispatch_request, finalize_request, make_default_options_response, ensure_sync, async_to_sync, url_for, make_response, preprocess_request, process_response, do_teardown_request, do_teardown_appcontext, app_context, request_context, test_request_context, wsgi_app, __call__

**Classes:** Flask, CustomClient

**AI Summary:**  This code file defines functions: ['_make_timedelta', 'get_send_file_max_age', 'send_static_file', 'open_resource', 'create_jinja_environment', 'raise_routing_exception' 'Update_template_context', 'make_shell_context' 'run', 'test_client', 'Test_clask', 'CustomClient', 'Flask', and classes: ['Flask'] 'T_teardown', 'customClient' and 'flask' are all classes .


## Git Commit History
### File: `C:/flask\src\flask\blueprints.py`

**Functions:** __init__, get_send_file_max_age, send_static_file, open_resource

**Classes:** Blueprint

**AI Summary:**  This code file defines functions: ['init__', 'get_send_file_max_age', 'send_static_file', 'open_resource', and classes: ['Blueprint' The commands are available from the 'flask' command .


## Git Commit History
### File: `C:/flask\src\flask\cli.py`

**Functions:** find_best_app, _called_with_wrong_args, find_app_by_string, prepare_import, locate_app, locate_app, locate_app, get_version, __init__, load_app, with_appcontext, decorator, command, decorator, group, _set_app, _set_debug, _env_file_callback, __init__, _load_plugin_commands, get_command, list_commands, make_context, parse_args, _path_is_ancestor, load_dotenv, show_server_banner, __init__, convert, _validate_key, convert, run_command, app, shell_command, routes_command, main

**Classes:** NoAppException, ScriptInfo, AppGroup, to, FlaskGroup, CertParamType, SeparatedPathType

**AI Summary:**  This code file defines functions: 'find_best_app', 'called_called_with_wrong_args', 'prepare_import', 'locate_app' 'get_version', 'load_dotenv', 'show_server_banner', 'convert', 'validate_key', 'run_command', 'shell_command' 'main', 'ScriptInfo', 'AppGroup', 'to', 'FlaskGroup' 'CertParamType', 'SeparatedPathType' and 'NoAppException' The code file contains a code file that tries to find the best possible application in the module .


## Git Commit History
### File: `C:/flask\src\flask\config.py`

**Functions:** __init__, __get__, __get__, __get__, __set__, __init__, from_envvar, from_prefixed_env, from_pyfile, from_object, from_file, from_mapping, get_namespace, __repr__

**Classes:** ConfigAttribute, Config

**AI Summary:**  This code file defines functions: ['init__', 'get,' 'get', 'set' and 'init', 'from_envvar' 'From_prefixed_env' 'Config' is the most interesting way to load configurations from Python . The code file includes classes: ['Config attribute', ['ConfigAttribute', 'Config') 'Config': 'Config('('Config)' '('Config')') '('App')')' 'App') 'App' is a Python module that loads from any Python file or module .


## Git Commit History
### File: `C:/flask\src\flask\ctx.py`

**Functions:** __getattr__, __setattr__, __delattr__, get, pop, setdefault, __contains__, __iter__, __repr__, after_this_request, index, add_header, copy_current_request_context, index, do_some_work, wrapper, has_request_context, has_app_context, __init__, from_environ, has_request, copy, request, session, match_request, push, pop, __enter__, __exit__, __repr__, __getattr__

**Classes:** _AppCtxGlobals, AppContext

**AI Summary:**  This code file defines functions: 'get', 'pop', 'setdefault' and 'set default' functions . It also defines classes: ['_AppCtxGlobals', 'AppContext' and classes: 'AppCteCte' It defines a singleton sentinel value for parameter defaults: 'sentinel' It is a simple object that is used as a namespace for storing data during an application context .


## Git Commit History
### File: `C:/flask\src\flask\debughelpers.py`

**Functions:** __init__, __str__, __init__, attach_enctype_error_multidict, __getitem__, _dump_loader_info, explain_template_loading_attempts

**Classes:** UnexpectedUnicodeError, DebugFilesKeyError, FormDataRoutingRedirect, newcls

**AI Summary:**  This code file defines functions: [' __init__', '__str__',  'attach_enctype_error_multidict', '_dump_loader_info', 'explain_template_loading_attempts', and classes: ['UnexpectedUnicodeError', 'DebugFilesKeyError' 'FormDataRoutingRedirect', 'Newcls' The idea is that it can provide a better error message than just a generic KeyError/BadRequest .


## Git Commit History
### File: `C:/flask\src\flask\globals.py`

**Functions:** _get_current_object, __getattr__

**Classes:** ProxyMixin, FlaskProxy, AppContextProxy, _AppCtxGlobalsProxy, RequestProxy, SessionMixinProxy

**AI Summary:**  This code file defines functions: ['_get_current_object', '__getattr__', and classes: ['ProxyMixin', 'FlaskProxy', 'AppContext proxy', '_AppCtxGlobals Proxy', 'Request proxy', and 'SessionMixin proxy' The code file is called Flask and contains a class called AppCteCteProxy .


## Git Commit History
### File: `C:/flask\src\flask\helpers.py`

**Functions:** get_debug_flag, get_load_dotenv, stream_with_context, stream_with_context, stream_with_context, streamed_response, generate, streamed_response, generate, decorator, generator, make_response, index, index, url_for, redirect, abort, get_template_attribute, flash, get_flashed_messages, _prepare_send_file_kwargs, send_file, send_from_directory, download_file, get_root_path, _split_blueprint_path

**Classes:** None

**AI Summary:**  This code file defines functions: ['get_debug_flag', 'get_load_dotenv', 'stream_with_context' 'streamed_response' and 'generate' 'Generate', 'decorator', 'make_response', 'url_for', 'redirect', 'abort', 'flash' 'flash', 'prepare_send_file_kwargs', 'Send_file', 'download_file' 'Stream_with-context' is a function that generates a response generator function .


## Git Commit History
### File: `C:/flask\src\flask\logging.py`

**Functions:** wsgi_errors_stream, has_level_handler, create_logger

**Classes:** None

**AI Summary:**  This code file defines functions: ['wsgi_errors_stream', 'has_level_handler', 'create_logger', and classes: []. Here is the main code content .


## Git Commit History
### File: `C:/flask\src\flask\sessions.py`

**Functions:** permanent, permanent, __init__, on_update, __getitem__, get, setdefault, _fail, make_null_session, is_null_session, get_cookie_name, get_cookie_domain, get_cookie_path, get_cookie_httponly, get_cookie_secure, get_cookie_samesite, get_cookie_partitioned, get_expiration_time, should_set_cookie, open_session, save_session, _lazy_sha1, get_signing_serializer, open_session, save_session

**Classes:** SessionMixin, SecureCookieSession, NullSession, SessionInterface, Session, SecureCookieSessionInterface

**AI Summary:**  This code file defines functions: 'permanent', 'on_update', 'get', 'setdefault', 'make_null_session', 'save_session' 'SecureCookieSession' is a class for sessions based on signed cookies .


## Git Commit History
### File: `C:/flask\src\flask\signals.py`

**Functions:** None

**Classes:** None

**AI Summary:**  The code file defines functions: [], and classes: []. Here is the main code content: # # # . The code is only for signals provided by Flask itself . # # This is a code file that defines functions and classes .


## Git Commit History
### File: `C:/flask\src\flask\templating.py`

**Functions:** _default_template_ctx_processor, __init__, __init__, get_source, _get_source_explained, _get_source_fast, _iter_loaders, list_templates, _render, render_template, render_template_string, _stream, generate, stream_template, stream_template_string

**Classes:** Environment, DispatchingJinjaLoader

**AI Summary:**  This code file defines functions: ['_default_template_ctx_processor', '__init__', 'get_source_explained', 'stream_template', and classes: ['Environment', 'DispatchingJinja loader']


## Git Commit History
### File: `C:/flask\src\flask\testing.py`

**Functions:** __init__, json_dumps, _get_werkzeug_version, __init__, session_transaction, _copy_environ, _request_from_builder_args, open, __enter__, __exit__, __init__, invoke

**Classes:** EnvironBuilder, FlaskClient, FlaskCliRunner

**AI Summary:**  This code file defines functions: ['init__', 'json_dumps', '_get_werkzeug_version', '__init__' and 'FlaskCliRunner' Here is the main code content .


## Git Commit History
### File: `C:/flask\src\flask\typing.py`

**Functions:** None

**Classes:** None

**AI Summary:**  The code file defines functions: [], and classes: []. Here is the main code content:import collections.abc as cabc.import typing as t.ype: # pragma: no cover.import WSGIApplication:    from werkzeug.sansio.response import Response . The possible types that are directly convertible or are a Response object .


## Git Commit History
### File: `C:/flask\src\flask\views.py`

**Functions:** dispatch_request, dispatch_request, as_view, view, view, get, post, __init_subclass__, dispatch_request

**Classes:** View, Hello, sets, MethodView, CounterAPI

**AI Summary:**  This code file defines functions: ['dispatch_request', 'as_view', 'view' 'Hello', 'sets', 'MethodView', 'CounterAPI', and classes: ['View' and 'Counter API' See :doc:`views` for a detailed guide to creating a generic class-based view .


## Git Commit History
### File: `C:/flask\src\flask\wrappers.py`

**Functions:** max_content_length, max_content_length, max_form_memory_size, max_form_memory_size, max_form_parts, max_form_parts, endpoint, blueprint, blueprints, _load_form_data, on_json_loading_failed, max_cookie_size

**Classes:** Request, Response

**AI Summary:**  The request object is a :class:`~flask.request` subclass and provides all of the attributes Werkzeug defines plus a few Flask attributes . It is what ends up as:class: `~Flask.Flaskrequest` If you want to replace the request object used you can subclass this and set it to your subclass .


## Git Commit History
### File: `C:/flask\src\flask\__init__.py`

**Functions:** None

**Classes:** None

**AI Summary:**  The code file defines functions: [], and classes: []. Here is the main code content: importing Flask as Flask and importing Flask . importing Flask is defined as a function, and importing a class . importing a function is defined by functions, classes and functions .


## Git Commit History
### File: `C:/flask\src\flask\__main__.py`

**Functions:** None

**Classes:** None

**AI Summary:**  This code file defines functions: [], and classes: []. Here is the main code content . The main code file contains a function, a class, a function and a function . The code file is called "main", and the main function is called main .


## Git Commit History
### File: `C:/flask\src\flask\json\provider.py`

**Functions:** __init__, dumps, dump, loads, load, _prepare_response_obj, response, _default, dumps, loads, response

**Classes:** JSONProvider, DefaultJSONProvider

**AI Summary:**  This code file defines functions: ['__init__', 'dumps', 'dump', 'loads', 'load', 'prepare_response_obj', 'response', '_default' and 'load' It also defines classes: ['JSON Provider', 'DefaultJSON Provider'] and 'Response' It defines functions and classes for a standard set of JSON operations .


## Git Commit History
### File: `C:/flask\src\flask\json\tag.py`

**Functions:** check, to_json, to_python, __init__, check, to_json, to_python, tag, check, to_json, to_python, check, to_json, check, to_json, to_python, check, to_json, check, to_json, to_python, check, to_json, to_python, check, to_json, to_python, check, to_json, to_python, __init__, register, tag, untag, _untag_scan, dumps, loads

**Classes:** TagOrderedDict, JSONTag, TagDict, PassDict, TagTuple, PassList, TagBytes, TagMarkup, TagUUID, TagDateTime, TaggedJSONSerializer

**AI Summary:**  A compact representation for lossless serialization of non-standard JSON types . The code file defines functions: 'check', 'to_json', 'To__Python', 'tag', 'unag', 'untag,' '_untag_scan', 'dumps', 'loads' and classes: ['TagOrderedDict', 'TaggedJSONSerializer'] The code is used to serialize the session data, but it may be useful in other places .


## Git Commit History
### File: `C:/flask\src\flask\json\__init__.py`

**Functions:** dumps, dump, loads, load, jsonify

**Classes:** None

**AI Summary:**  This code file defines functions: ['dumps', 'dump', 'loads', 'load', 'loading', 'jsonify', and classes: []. Here is the main code content .


## Git Commit History
### File: `C:/flask\src\flask\sansio\app.py`

**Functions:** _make_timedelta, __init__, to_python, to_url, _check_setup_finished, name, logger, jinja_env, create_jinja_environment, make_config, make_aborter, auto_find_instance_path, create_global_jinja_loader, select_jinja_autoescape, debug, debug, register_blueprint, iter_blueprints, add_url_rule, template_filter, template_filter, template_filter, reverse_filter, decorator, add_template_filter, template_test, template_test, template_test, is_prime_test, decorator, add_template_test, template_global, template_global, template_global, double, decorator, add_template_global, teardown_appcontext, shell_context_processor, _find_error_handler, trap_http_exception, should_ignore_error, redirect, inject_url_defaults, handle_url_build_error

**Classes:** App, of, ListConverter

**AI Summary:**  This code file defines functions: ['_make_timedelta', 'to_python', 'To_py', 'check_setup_finished', 'name', 'logger', 'jinja_env', 'jinja_environment', 'make_aborter', 'autoescape', 'bind_redirect', 'redirect' [App]], and classes: ['App', 'of', 'ListConverter'] The code file is created as a central registry for the application and acts as the central object . It is used to resolve resources from inside the WSGI package or folder .


## Git Commit History
### File: `C:/flask\src\flask\sansio\blueprints.py`

**Functions:** __init__, add_url_rule, __init__, _check_setup_finished, record, record_once, wrapper, make_setup_state, register_blueprint, register, _merge_blueprint_funcs, extend, add_url_rule, app_template_filter, app_template_filter, app_template_filter, decorator, add_app_template_filter, register_template_filter, app_template_test, app_template_test, app_template_test, decorator, add_app_template_test, register_template_test, app_template_global, app_template_global, app_template_global, decorator, add_app_template_global, register_template_global, before_app_request, after_app_request, teardown_app_request, app_context_processor, app_errorhandler, decorator, from_blueprint, app_url_value_preprocessor, app_url_defaults

**Classes:** BlueprintSetupState, Blueprint

**AI Summary:**  This code file defines functions: ['init__', 'add_url_rule', '_check_setup_finished', 'record' and 'record_once' It defines classes: ['Blueprint setupState', 'Blueprint'] and 'blueprint' The code file is created by an instance of the Blueprint setup method .


## Git Commit History
### File: `C:/flask\src\flask\sansio\scaffold.py`

**Functions:** setupmethod, wrapper_func, __init__, __repr__, _check_setup_finished, static_folder, static_folder, has_static_folder, static_url_path, static_url_path, jinja_loader, _method_route, get, post, put, delete, patch, route, index, decorator, add_url_rule, index, index, index, endpoint, example, decorator, before_request, load_user, after_request, teardown_request, context_processor, url_value_preprocessor, url_defaults, errorhandler, page_not_found, special_exception_handler, decorator, register_error_handler, _get_exc_class_and_code, _endpoint_from_view_func, _find_package_path, find_package

**Classes:** Scaffold

**AI Summary:**  This code file defines functions: 'setupmethod', 'wrapper_func', '_check_setup_finished', 'static_ folder', 'Static_folder', 'has_static_fold', 'jinja_loader', 'method_route', 'get', 'post', 'put', 'delete', 'patch', 'route' and 'decorator', 'endpoint', 'example', 'teardown_request', 'context_processor', 'url_defaults', 'errorhandler', 'page_not_found', 'special_exception_handler'


## Git Commit History
### File: `C:/flask\tests\conftest.py`

**Functions:** _standard_os_environ, _reset_os_environ, app, app_ctx, req_ctx, client, test_apps, leak_detector, modules_tmp_path, modules_tmp_path_prefix, site_packages, purge_module, inner

**Classes:** None

**AI Summary:**  This code file defines functions: ['_standard_os_environ', '_reset_os .environ' and 'leak_detector', 'test_apps' and classes: []. Here is the main code file .


## Git Commit History
### File: `C:/flask\tests\test_appctx.py`

**Functions:** test_basic_url_generation, index, test_url_generation_requires_server_name, test_url_generation_without_context_fails, test_request_context_means_app_context, test_app_context_provides_current_app, test_app_tearing_down, cleanup, test_app_tearing_down_with_previous_exception, cleanup, test_app_tearing_down_with_handled_exception_by_except_block, cleanup, test_app_tearing_down_with_handled_exception_by_app_handler, cleanup, index, handler, test_app_tearing_down_with_unhandled_exception, cleanup, index, test_app_ctx_globals_methods, test_custom_app_ctx_globals_class, __init__, test_context_refcounts, teardown_req, teardown_app, index, test_clean_pop, teardown_req, teardown_app

**Classes:** CustomRequestGlobals

**AI Summary:**  This code file defines functions: ['test_basic_url_generation', 'index', 'cleanup', 'test_app_tearing_down' and 'CustomRequestGlobals' It defines functions and classes: ['Test_request_context_means_app'], ['CustomRequestGolop', 'Cleanup'], 'Index', 'Credentialed_pop', 'Teardown_app', 'Tried_clean_pop' 'Test_app': 'Tired_App': 'CleanUp', 'Index' 'Clean_stuff': 'clean_stuff' 'Tied_down: 'Cleaned_down', 'Unhandled_exception', 'Untied


## Git Commit History
### File: `C:/flask\tests\test_async.py`

**Functions:** dispatch_request, get, post, _async_app, index, handle, error, bp_index, bp_handle, bp_error, test_async_route, test_async_error_handler, test_async_before_after_request, index, before, after, bp_index, bp_before, bp_after

**Classes:** AppError, BlueprintError, AsyncView, AsyncMethodView

**AI Summary:**  This code file defines functions: 'dispatch_request', 'get', 'post', 'async_app', 'AsyncView', and classes: ['AppError', 'BlueprintError'], 'MethodView' and 'AppError' The code file is created by Flask using the Flask API .


## Git Commit History
### File: `C:/flask\tests\test_basic.py`

**Functions:** test_options_work, index, test_options_on_multiple_rules, index, index_put, test_method_route, hello, test_method_route_no_methods, test_provide_automatic_options_attr, index, index2, test_provide_automatic_options_kwarg, index, more, test_request_dispatching, index, more, test_disallow_string_for_allowed_methods, test_url_mapping, index, more, options, test_werkzeug_routing, bar, index, test_endpoint_decorator, bar, index, test_session, set, get, test_session_path, index, test_session_using_application_root, __init__, __call__, index, test_session_using_session_settings, index, clear, test_session_using_samesite_attribute, index, test_missing_session, expect_exception, test_session_secret_key_fallbacks, set_session, get_session, test_session_expiration, index, test, test_session_stored_last, modify_session, dump_session_contents, test_session_special_types, dump_session_contents, test_session_cookie_setting, bump, read, run_test, test_session_vary_cookie, set_session, get, getitem, setdefault, clear, vary_cookie_header_set, vary_header_set, no_vary_header, expect, test_session_refresh_vary, login, ignored, test_flashes, test_extended_flashing, index, test, test_with_categories, test_filter, test_filters, test_filters2, test_request_processing, before_request, after_request, index, test_request_preprocessing_early_return, before_request1, before_request2, before_request3, index, test_after_request_processing, index, foo, test_teardown_request_handler, teardown_request, root, test_teardown_request_handler_debug_mode, teardown_request, root, test_teardown_request_handler_error, teardown_request1, teardown_request2, fails, test_before_after_request_order, before1, before2, after1, after2, finish1, finish2, index, test_error_handling, not_found, internal_server_error, forbidden, index, error, error2, test_error_handling_processing, internal_server_error, broken_func, after_request, test_baseexception_error_handling, broken_func, test_before_request_and_routing_errors, attach_something, return_something, test_user_error_handling, handle_my_exception, index, test_http_error_subclass_handling, handle_forbidden_subclass, handle_403, index1, index2, index3, test_errorhandler_precedence, handle_e2, handle_exception, raise_e1, raise_e3, test_trap_bad_request_key_error, fail, allow_abort, test_trapping_of_all_http_exceptions, fail, test_error_handler_after_processor_error, before_request, after_request, index, internal_server_error, test_enctype_debug_helper, index, test_response_types, from_text, from_bytes, from_full_tuple, from_text_headers, from_text_status, from_response_headers, from_response_status, from_wsgi, from_dict, from_list, test_response_type_errors, from_none, from_small_tuple, from_large_tuple, from_bad_type, from_bad_wsgi, test_make_response, test_make_response_with_response_instance, test_jsonify_no_prettyprint, test_jsonify_mimetype, test_json_dump_dataclass, test_jsonify_args_and_kwargs_check, test_url_generation, hello, test_build_error_handler, handler, test_build_error_handler_reraise, handler_raises_build_error, test_url_for_passes_special_values_to_build_error_handler, handler, test_static_files, test_static_url_path, test_static_url_path_with_ending_slash, test_static_url_empty_path, test_static_url_empty_path_default, test_static_folder_with_pathlib_path, test_static_folder_with_ending_slash, catch_all, test_static_route_with_host_matching, test_request_locals, test_server_name_matching, index, test_server_name_subdomain, index, subdomain, test_exception_propagation, index, test_werkzeug_passthrough_errors, run_simple_mock, test_url_processors, add_language_code, pull_lang_code, index, about, something_else, test_inject_blueprint_url_defaults, bp_defaults, view, test_nonascii_pathinfo, index, test_no_setup_after_first_request, index, test_routing_redirect_debugging, user, test_route_decorator_custom_endpoint, foo, for_bar, for_bar_foo, test_get_method_on_g, test_g_iteration_protocol, test_subdomain_basic_support, normal_index, test_index, test_subdomain_matching, index, test_subdomain_matching_with_ports, index, test_subdomain_matching_other_name, index, test_multi_route_rules, index, test_multi_route_class_views, __init__, index, test_run_defaults, run_simple_mock, test_run_server_port, run_simple_mock, test_run_from_config, run_simple_mock, test_max_cookie_size, index, test_app_freed_on_zero_refcount

**Classes:** PrefixPathMiddleware, MyException, ForbiddenSubclass, E1, E2, E3, View

**AI Summary:**  This code file defines functions: 'Test_options_work' and 'options', 'test_werkzeug_routing', 'bar', 'index', 'endpoint_decorator', 'Bar', 'Index', 'Session', 'set', 'get', 'session', 'event', 'sameite_attribute', 'exception', 'false', 'error', 'not_found', 'internal_server_error' is 'broken', 'broken_f', 'after_request', 'before_request1' 'after-request1', 'when-request2' 'before-request_order', 'if-request' is a code file .


## Git Commit History
### File: `C:/flask\tests\test_blueprints.py`

**Functions:** test_blueprint_specific_error_handling, frontend_forbidden, frontend_no, backend_forbidden, backend_no, sideend_no, app_forbidden, test_blueprint_specific_user_error_handling, my_decorator_exception_handler, my_function_exception_handler, blue_deco_test, blue_func_test, test_blueprint_app_error_handling, forbidden_handler, app_forbidden, bp_forbidden, test_blueprint_prefix_slash, index, test_blueprint_url_defaults, foo, bar, test_blueprint_url_processors, add_language_code, pull_lang_code, index, about, test_templates_and_static, test_default_static_max_age, get_send_file_max_age, test_templates_list, test_dotted_name_not_allowed, test_empty_name_not_allowed, test_dotted_names_from_app, app_index, index, test_empty_url_defaults, something, test_route_decorator_custom_endpoint, foo, foo_bar, foo_bar_foo, bar_foo, index, test_route_decorator_custom_endpoint_with_dots, view, test_endpoint_decorator, foobar, test_template_filter, my_reverse, my_reverse_2, my_reverse_3, my_reverse_4, test_add_template_filter, my_reverse, test_template_filter_with_name, my_reverse, test_add_template_filter_with_name, my_reverse, test_template_filter_with_template, super_reverse, index, test_template_filter_after_route_with_template, index, super_reverse, test_add_template_filter_with_template, super_reverse, index, test_template_filter_with_name_and_template, my_reverse, index, test_add_template_filter_with_name_and_template, my_reverse, index, test_template_test, is_boolean, boolean_2, boolean_3, boolean_4, test_add_template_test, is_boolean, test_template_test_with_name, is_boolean, test_add_template_test_with_name, is_boolean, test_template_test_with_template, boolean, index, test_template_test_after_route_with_template, index, boolean, test_add_template_test_with_template, boolean, index, test_template_test_with_name_and_template, is_boolean, index, test_add_template_test_with_name_and_template, is_boolean, index, test_context_processing, template_string, not_answer_context_processor, answer_context_processor, bp_page, app_page, test_template_global, get_answer, get_stuff_1, get_stuff_2, get_stuff_3, test_request_processing, before_bp, after_bp, teardown_bp, bp_endpoint, test_app_request_processing, before_app, after_app, teardown_app, bp_endpoint, test_app_url_processors, add_language_code, pull_lang_code, index, about, test_nested_blueprint, forbidden, parent_index, parent_no, child_index, child_no, grandchild_forbidden, grandchild_index, grandchild_no, test_nested_callback_order, app_before1, app_teardown1, app_before2, app_teardown2, app_ctx, parent_before1, parent_teardown1, parent_before2, parent_teardown2, parent_ctx, child_before1, child_teardown1, child_before2, child_teardown2, child_ctx, a, b, test_nesting_url_prefixes, index, test_nesting_subdomains, index, test_child_and_parent_subdomain, index, test_unique_blueprint_names, test_self_registration, test_blueprint_renaming, index, error, forbidden, index2

**Classes:** MyDecoratorException, MyFunctionException, MyBlueprint

**AI Summary:**  This code file defines functions: 'frontend_forbidden', 'front end end end', 'backend end end,' 'side end end' 'forbidden' and 'bp' 'Forbidden' are 'fronted end end ends' 'Front end_end end ends end endends end end points' 'foo', 'bar' 'bar_foo' is 'bar bar', 'foo_bar', 'Bar_foo,' 'bar's' 'passer', 'test_blueprint_specific_user_error_handling' is a code file .


## Git Commit History
### File: `C:/flask\tests\test_cli.py`

**Functions:** runner, test_cli_name, test_find_best_app, create_app, create_app, make_app, create_app, create_app, create_app, create_app, test_prepare_import, reset_path, test_locate_app, test_locate_app_raises, test_locate_app_suppress_raise, test_get_version, exit, test_scriptinfo, create_app, test_app_cli_has_app_context, _param_cb, check, test_with_appcontext, testcmd, test_appgroup_app_context, cli, test, subgroup, test2, test_flaskgroup_app_context, create_app, cli, test, test_flaskgroup_debug, create_app, cli, test, test_flaskgroup_nested, show, test_no_command_echo_loading_error, test_help_echo_loading_error, test_help_echo_exception, create_app, app, invoke, expect_order, test_simple, test_sort, test_all_methods, test_no_routes, test_subdomain, test_host, dotenv_not_available, test_load_dotenv, test_dotenv_path, test_dotenv_optional, test_disable_dotenv_from_env, test_run_cert_path, test_run_cert_adhoc, test_run_cert_import, test_run_cert_no_ssl, test_cli_blueprints, custom_command, nested_command, merged_command, late_command, test_cli_empty, test_run_exclude_patterns

**Classes:** Module, Module, Module, Module, Module, Module, Module, Module, Module, Module, Module, Module, MockCtx, TestRoutes

**AI Summary:**  This file was part of Flask-CLI and was modified under the terms of the Revised BSD License . Here is the main code content: The code file defines functions: ['runner', 'test_cli_name', 'find_best_app', 'create_app' 'Myapp' is the app's name and not the app itself .


## Git Commit History
### File: `C:/flask\tests\test_config.py`

**Functions:** common_object_test, test_config_from_pyfile, test_config_from_object, test_config_from_file_json, test_config_from_file_toml, test_from_prefixed_env, test_from_prefixed_env_custom_prefix, test_from_prefixed_env_nested, test_config_from_mapping, test_config_from_class, test_config_from_envvar, test_config_from_envvar_missing, test_config_missing, test_config_missing_file, test_custom_config_class, test_session_lifetime, test_get_namespace, test_from_pyfile_weird_encoding

**Classes:** Base, Test, Config, Flask

**AI Summary:**  This code file defines functions: ['common_object_test', 'test_config_from_pyfile', 'Test', 'Class', 'Base', 'Config', 'Flask'], and classes: ['Base'], 'Test' and 'Class' The code file is called 'TestConfig' and has been added to flask in 3.11 .


## Git Commit History
### File: `C:/flask\tests\test_converters.py`

**Functions:** test_custom_converters, to_python, to_url, index, test_context_available, to_python, index

**Classes:** ListConverter, ContextConverter

**AI Summary:**  This code file defines functions: 'test_custom_converters', 'to_py', 'test-context_available', 'To_url', 'index', and classes: ['ListConverter', 'ContextConverters'] Here is the main code content: 'Test_request_context' and 'index'


## Git Commit History
### File: `C:/flask\tests\test_helpers.py`

**Functions:** __init__, __fspath__, __init__, __getattr__, test_send_file, test_static_file, get_send_file_max_age, test_send_from_directory, test_url_for_with_anchor, index, test_url_for_with_scheme, index, test_url_for_with_scheme_not_external, test_url_for_with_alternating_schemes, index, test_url_with_method, get, post, test_url_for_with_self, index, test_redirect_no_app, test_redirect_with_app, redirect, test_abort_no_app, test_app_aborter_class, test_abort_with_app, test_name_with_import_error, test_streaming_with_context, index, generate, test_streaming_with_context_as_decorator, index, generate, test_streaming_with_context_and_custom_close, __init__, __iter__, close, __next__, index, generate, test_stream_keeps_session, index, gen, test_async_view, index, gen, test_get_debug_flag, test_make_response, test_open_resource, test_open_resource_exceptions, test_open_resource_with_encoding

**Classes:** FakePath, PyBytesIO, TestSendfile, StaticFileApp, TestUrlFor, MyView, MyAborter, MyFlask, My900Error, TestNoImports, TestStreaming, Wrapper, TestHelpers

**AI Summary:**  This code file defines functions: 'FakePath', 'TestSendfile', 'StaticFileApp' 'TestStreaming', 'MyView' 'MyAborter', 'Flask' and 'My900Error' are all classes and classes . The main code file contains a function that sends a static file with a static static file handler .


## Git Commit History
### File: `C:/flask\tests\test_instance_config.py`

**Functions:** test_explicit_instance_paths, test_uninstalled_module_paths, test_uninstalled_package_paths, test_uninstalled_namespace_paths, create_namespace, test_installed_module_paths, test_installed_package_paths, test_prefix_package_paths

**Classes:** None

**AI Summary:**  This code file defines functions: ['test_explicit_instance_paths', 'test_uninstalled_module_path's', 'create_namespace' and classes: []. Here is the main code content: importing os, importing flask, importing pytest and importing flask .


## Git Commit History
### File: `C:/flask\tests\test_json.py`

**Functions:** test_bad_request_debug_message, post_json, test_json_bad_requests, return_json, test_json_custom_mimetypes, return_json, test_json_as_unicode, test_json_dump_to_file, test_jsonify_basic_types, test_jsonify_dicts, return_kwargs, return_dict, test_jsonify_arrays, return_args_unpack, return_array, test_jsonify_datetime, index, __init__, utcoffset, tzname, dst, test_jsonify_aware_datetimes, test_jsonify_uuid_types, test_json_decimal, test_json_attr, add, test_tojson_filter, test_json_customization, __init__, default, object_hook, loads, index, _has_encoding, test_json_key_sorting, index, test_html_method, __html__

**Classes:** FixedOffset, X, CustomProvider, ObjectWithHTML

**AI Summary:**  This code file defines functions: 'return_json', 'test_bad_request_debug_message', 'post_jacket', 'Test_json_custom_mimetypes', and classes: ['FixedOffset', 'X', 'Custom Provider', 'ObjectWithHTML']


## Git Commit History
### File: `C:/flask\tests\test_json_tag.py`

**Functions:** test_dump_load_unchanged, test_duplicate_tag, test_custom_tag, __init__, check, to_json, to_python, test_tag_interface, test_tag_order

**Classes:** TagDict, Foo, TagFoo, Tag1, Tag2

**AI Summary:**  This code file defines functions: 'test_dump_load_unchanged', 'test test_duplicate_tag', 'Test_custom_tag' and 'tag_order' It defines functions and classes: ['TagDict', 'Foo', 'TagFoo' 'Tag1', 'tag2', 'to__tag_interface', and 'test tag_order', 'pytest.py' The code file also defines classes: TagFoo, TagDict, Tag1, Tag2 .


## Git Commit History
### File: `C:/flask\tests\test_logging.py`

**Functions:** reset_logging, test_logger, test_logger_debug, test_existing_handler, test_wsgi_errors_stream, index, test_has_level_handler, test_log_view_exception, index

**Classes:** None

**AI Summary:**  This code file defines functions: ['reset_logging', 'test_logger', 'Test_loggers', 'exception', and classes: []. Here is the main code content: 'reset' and 'test-logger' functions .


## Git Commit History
### File: `C:/flask\tests\test_regression.py`

**Functions:** test_aborting, handle_foo, index, test

**Classes:** Foo

**AI Summary:**  The code file defines functions: ['test_aborting', 'handle_foo', 'index', 'test'], and classes: ['Foo'] Here is the main code content: 'Test'() and 'Index()() .


## Git Commit History
### File: `C:/flask\tests\test_reqctx.py`

**Functions:** test_teardown_on_pop, end_of_request, test_teardown_with_previous_exception, end_of_request, test_teardown_with_handled_exception, end_of_request, test_proper_test_request_context, index, sub, test_context_binding, index, meh, test_context_test, test_manual_context_binding, index, test_greenlet_context_copying, index, g, test_greenlet_context_copying_api, index, g, test_session_error_pops_context, open_session, index, test_session_dynamic_cookie_name, get_cookie_name, set, get, set_dynamic_cookie, get_dynamic_cookie, test_bad_environ_raises_bad_request, test_environ_for_valid_idna_completes, index, test_normal_environ_completes, index

**Classes:** TestGreenletContextCopying, SessionError, FailingSessionInterface, CustomFlask, PathAwareSessionInterface, CustomFlask

**AI Summary:**  This code file defines functions: ['test_teardown_on_pop', 'end_of_request', 'test_proper_test_request_context', 'TestGreenletContextCopying', 'FailingSessionError', 'CustomFlask', 'PathAwareSession interface', 'CommonFlask'], and classes: ['TestGreenLetSessionError], 'FailedSessionError' and 'Bad_environ_raises_bad_request' [None]], 'Proper_Test_Request' is 'proper', 'sub' 'Test_Greenlet' 'Greenlet_context_copying_api', 'open_session', 'greenlet_error_p


## Git Commit History
### File: `C:/flask\tests\test_request.py`

**Functions:** test_max_content_length, index, catcher, test_limit_config, test_trusted_hosts_config, index

**Classes:** None

**AI Summary:**  This code file defines functions: ['test_max_content_length', 'index', 'catcher', 'test_trusted_hosts_config', and classes: [].


## Git Commit History
### File: `C:/flask\tests\test_session_interface.py`

**Functions:** test_open_session_with_endpoint, save_session, open_session, index

**Classes:** MySessionInterface

**AI Summary:**  This code file defines functions: 'test_open_session_with_endpoint', 'save_session', 'open_Session', 'index', and classes: ['MySessionInterface' Here is the main code .


## Git Commit History
### File: `C:/flask\tests\test_signals.py`

**Functions:** test_template_rendered, index, record, test_before_render_template, index, record, test_request_signals, before_request_signal, after_request_signal, before_request_handler, after_request_handler, index, test_request_exception_signal, index, record, test_appcontext_signals, record_push, record_pop, index, test_flash_signal, index, record, test_appcontext_tearing_down_signal, record_teardown, index

**Classes:** None

**AI Summary:**  This code file defines functions: ['test_template_rendered', 'index', 'record', 'test_request_signals', 'after_request#signal', 'before_request' and 'after-request_handler' It defines functions and classes: []. Here is the main code file .


## Git Commit History
### File: `C:/flask\tests\test_subclassing.py`

**Functions:** test_suppressed_exception_logging, log_exception, index

**Classes:** SuppressedFlask

**AI Summary:**  The code file defines functions: ['test_suppressed_exception_logging', 'log_Exception', 'index', and classes: ['SuppressedFlask'] Here is the main code content: 'Test' and 'Index' functions .


## Git Commit History
### File: `C:/flask\tests\test_templating.py`

**Functions:** test_context_processing, context_processor, index, test_original_win, index, test_simple_stream, index, test_request_less_rendering, context_processor, test_standard_context, index, test_escaping, index, test_no_escaping, index, test_escaping_without_template_filename, test_macros, test_template_filter, my_reverse, my_reverse_2, my_reverse_3, my_reverse_4, test_add_template_filter, my_reverse, test_template_filter_with_name, my_reverse, test_add_template_filter_with_name, my_reverse, test_template_filter_with_template, super_reverse, index, test_add_template_filter_with_template, super_reverse, index, test_template_filter_with_name_and_template, my_reverse, index, test_add_template_filter_with_name_and_template, my_reverse, index, test_template_test, boolean, boolean_2, boolean_3, boolean_4, test_add_template_test, boolean, test_template_test_with_name, is_boolean, test_add_template_test_with_name, is_boolean, test_template_test_with_template, boolean, index, test_add_template_test_with_template, boolean, index, test_template_test_with_name_and_template, is_boolean, index, test_add_template_test_with_name_and_template, is_boolean, index, test_add_template_global, get_stuff, get_stuff_1, get_stuff_2, get_stuff_3, test_custom_template_loader, create_global_jinja_loader, index, test_iterable_loader, context_processor, index, test_templates_auto_reload, test_templates_auto_reload_debug_run, run_simple_mock, test_template_loader_debugging, handle, test_custom_jinja_env

**Classes:** MyFlask, _TestHandler, CustomEnvironment, CustomFlask

**AI Summary:**  This code file defines functions: ['test_context_processing', 'context_processor', 'index', 'test_original_win', 'templates_auto_reload_run', 'run_simple_mock', 'handle', 'custom_jinja_env'], and classes: ['MyFlask', '_TestHandler', 'CustomEnvironment'], 'CustomFlask']. Here is the main code content: [Test_context]], 'Test_template_test_test', 'template_filter_with_name_and_template', 'my_reverse', 'super_reverse' and 'template'


## Git Commit History
### File: `C:/flask\tests\test_testing.py`

**Functions:** test_environ_defaults_from_config, index, test_environ_defaults, index, test_environ_base_default, index, test_environ_base_modified, index, test_client_open_environ, index, test_specify_url_scheme, index, test_path_is_url, test_environbuilder_json_dumps, test_blueprint_with_subdomain, index, test_redirect_session, index, get_session, test_session_transactions, index, test_session_transactions_no_null_sessions, test_session_transactions_keep_context, test_session_transaction_needs_cookies, test_test_client_context_binding, index, other, test_reuse_client, test_full_url_request, action, test_json_request_and_response, echo, test_client_json_no_app_context, hello, add, test_subdomain, view, test_nosubdomain, view, test_cli_runner_class, test_cli_invoke, hello_command, test_cli_custom_obj, create_app, hello_command, test_client_pop_all_preserved, index

**Classes:** Namespace, SubRunner, NS

**AI Summary:**  This code file defines functions: ['test_environ_defaults_from_config', 'index', 'test_test_client_context_binding', 'other', 'reuse_client', 'action', 'act', 'redirect_session', 'get_session' and 'subdomain', 'view' [Namespace], 'SubRunner', 'NS'], and classes: ['Namespace'], 'NS', 'Namespace', 'sub-runner', 'Hello', 'Sub-Runner' [NS]] is the main code file .


## Git Commit History
### File: `C:/flask\tests\test_user_error_handler.py`

**Functions:** test_error_handler_no_match, custom_exception_handler, handle_500, custom_test, key_error, do_abort, test_error_handler_subclass, parent_exception_handler, child_exception_handler, parent_test, unregistered_test, registered_test, test_error_handler_http_subclass, code_exception_handler, subclass_exception_handler, forbidden_test, registered_test, unregistered_test, test_error_handler_blueprint, bp_exception_handler, bp_test, app_exception_handler, app_test, test_default_error_handler, bp_exception_handler, bp_forbidden_handler, bp_registered_test, bp_forbidden_test, catchall_exception_handler, catchall_forbidden_handler, forbidden, slash, app, do_custom, do_error, do_abort, do_raise, report_error, test_handle_class_or_code, handle_500, test_handle_generic_http, handle_http, test_handle_generic, handle_exception

**Classes:** CustomException, ParentException, ChildExceptionUnregistered, ChildExceptionRegistered, ForbiddenSubclassRegistered, ForbiddenSubclassUnregistered, TestGenericHandlers, Custom

**AI Summary:**  This code file defines functions: ['test_error_handler_no_match', 'custom_exception_handler', 'handle_500', 'Custom_test', 'key_error', 'do_abort', 'report_error' and 'catchall_forbidden_handler' 'Forbidden' is 'forbidden', 'slash', 'app' 'CustomException() is an instance, not a class,' assert isinstance(e) with pytest.raises(ValueError) as exc_info: "Use a subclass of HTTPException"


## Git Commit History
### File: `C:/flask\tests\test_views.py`

**Functions:** common_test, test_basic_view, dispatch_request, test_method_based_view, get, post, test_view_patching, get, post, get, post, test_view_inheritance, get, post, delete, test_view_decorators, add_x_parachute, new_function, dispatch_request, test_view_provide_automatic_options_attr, dispatch_request, dispatch_request, dispatch_request, test_implicit_head, get, test_explicit_head, get, head, test_endpoint_override, dispatch_request, test_methods_var_inheritance, get, propfind, test_multiple_inheritance, get, delete, test_remove_method_from_parent, get, post, test_init_once, __init__, dispatch_request

**Classes:** Index, Index, Index, Other, Index, BetterIndex, Index, Index1, Index2, Index3, Index, Index, Index, BaseView, ChildView, GetView, DeleteView, GetDeleteView, GetView, OtherView, View, CountInit

**AI Summary:**  This code file defines functions: 'common_test', 'test_basic_view', 'dispatch_request', 'get', 'post', 'Test_view_inheritance', and classes: 'Index', 'Other', 'BetterIndex' 'Common_test' is the main code file . The code file is called common_test . It defines functions and classes, 'Common' and 'Index'


## Git Commit History
### File: `C:/flask\tests\test_apps\blueprintapp\__init__.py`

**Functions:** None

**Classes:** None

**AI Summary:**  This code file defines functions: [], and classes: []. Here is the main code content: "glyglygly" and "hysterical" The code file is called Flask . It defines functions, classes, functions and classes .


## Git Commit History
### File: `C:/flask\tests\test_apps\blueprintapp\apps\__init__.py`

**Functions:** None

**Classes:** None

**AI Summary:**  This code file defines functions: [], [], and classes: []. Here is the main code content: The code file is a code file that defines functions, classes, functions and classes .


## Git Commit History
### File: `C:/flask\tests\test_apps\blueprintapp\apps\admin\__init__.py`

**Functions:** index, index2

**Classes:** None

**AI Summary:**  This code file defines functions: ['index', 'index2'], and classes: []. Here is the main code content: "admin" and "index2" The code file contains a function called render_template .


## Git Commit History
### File: `C:/flask\tests\test_apps\blueprintapp\apps\frontend\__init__.py`

**Functions:** index, missing_template

**Classes:** None

**AI Summary:**  This code file defines functions: ['index', 'missing_template'], and classes: []. Here is the main code content: "frontend" and "missing_templates" Frontend = Blueprint("frontend", __name__, template_ folder="templates")


## Git Commit History
### File: `C:/flask\tests\test_apps\cliapp\app.py`

**Functions:** None

**Classes:** None

**AI Summary:**  This code file defines functions: [], and classes: []. Here is the main code content:testapp = Flask("testapp") Testapp is a Flask application that uses Flask functions and classes .


## Git Commit History
### File: `C:/flask\tests\test_apps\cliapp\factory.py`

**Functions:** create_app, create_app2, no_app

**Classes:** None

**AI Summary:**  This code file defines functions: ['create_app', 'create app2', 'no_app'], and classes: []. Here is the main code content: "No_app"


## Git Commit History
### File: `C:/flask\tests\test_apps\cliapp\importerrorapp.py`

**Functions:** None

**Classes:** None

**AI Summary:**  This code file defines functions: [], and classes: []. Here is the main code content: The main code file is called Flask . The code file contains a code file that defines functions and classes .


## Git Commit History
### File: `C:/flask\tests\test_apps\cliapp\multiapp.py`

**Functions:** None

**Classes:** None

**AI Summary:**  This code file defines functions: [], and classes: []. Here is the main code content: App1 = Flask("app1") and App2 = Flask() . App1 is Flask('app1') and Flask('App1') is Flask("App1") .


## Git Commit History
### File: `C:/flask\tests\test_apps\cliapp\__init__.py`

**Functions:** None

**Classes:** None

**AI Summary:**  This code file defines functions: [], [], and classes: []. Here is the main code content: The code file is a code file that defines functions, classes, functions and classes .


## Git Commit History
### File: `C:/flask\tests\test_apps\cliapp\inner1\__init__.py`

**Functions:** None

**Classes:** None

**AI Summary:**  This code file defines functions: [], and classes: []. Here is the main code content:application application = Flask(__name__)application = Flask() Application is called Application Application .


## Git Commit History
### File: `C:/flask\tests\test_apps\cliapp\inner1\inner2\flask.py`

**Functions:** None

**Classes:** None

**AI Summary:**  This code file defines functions: [], and classes: []. Here is the main code content:app = Flask(__name__) App is a Flask application that uses Flask functions and classes .


## Git Commit History
### File: `C:/flask\tests\test_apps\cliapp\inner1\inner2\__init__.py`

**Functions:** None

**Classes:** None

**AI Summary:**  This code file defines functions: [], [], and classes: []. Here is the main code content: The code file is a code file that defines functions, classes, functions and classes .


## Git Commit History
### File: `C:/flask\tests\test_apps\helloworld\hello.py`

**Functions:** hello

**Classes:** None

**AI Summary:**  This code file defines functions: ['hello'], and classes: []. Here is the main code content: "Hello World!" and "Hello Hello World" The code file contains functions: ["hello"] and ["Hello World"]


## Git Commit History
### File: `C:/flask\tests\test_apps\helloworld\wsgi.py`

**Functions:** None

**Classes:** None

**AI Summary:**  This code file defines functions: [], and classes: []. Here is the main code content:from hello import app  # noqa: F401 : F401 is F401 .


## Git Commit History
### File: `C:/flask\tests\test_apps\subdomaintestmodule\__init__.py`

**Functions:** None

**Classes:** None

**AI Summary:**  This code file defines functions: [], and classes: []. Here is the main code content:modmod = Module(__name__, "foo", subdomain="foo") Modmod is Module(modmod)


## Git Commit History
### File: `C:/flask\tests\type_check\typing_app_decorators.py`

**Functions:** after_sync, after_async, before_sync, before_async, teardown_sync, teardown_async

**Classes:** None

**AI Summary:**  This code file defines functions: ['after_sync', 'after_async', 'before_sync'', 'teardown_sync,' and classes: []. Here is the main code content: [], [].


## Git Commit History
### File: `C:/flask\tests\type_check\typing_error_handler.py`

**Functions:** handle_400, handle_custom, handle_accept_base, handle_multiple

**Classes:** None

**AI Summary:**  This code file defines functions: ['handle_400', 'handle_custom', 'handled_accept_base', 'Handle_multiple', and classes: []. Here is the main code file .


## Git Commit History
### File: `C:/flask\tests\type_check\typing_route.py`

**Functions:** hello_str, hello_bytes, hello_json, hello_json_dict, hello_json_list, typed_dict, hello_generator, show, hello_generator_expression, hello_iterator, tuple_status, tuple_status_enum, tuple_headers, return_template, return_template_stream, async_route, __init__, dispatch_request

**Classes:** StatusJSON, RenderTemplateView

**AI Summary:**  This code file defines functions: ['hello_str', 'hello_bytes', 'Hello_json', 'typed_dict', 'generator', 'show' and 'Hello' The code file also defines classes: ['StatusJSON', 'RenderTemplateView', 'Stream_template', 'render_template' 'Hello', 'status', 'return_template_stream', 'async_route', '__init__', 'dispatch_request', and 'render template'


## Git Commit History
- **Hynek Schlawack** (2025-10-14): Docs typo/markup fixes (#5829)
- **David Lord** (2025-09-19): merge app and request context (#5812)
- **David Lord** (2025-09-19): merge app and request context
- **David Lord** (2025-08-19): Merge branch 'stable'
- **David Lord** (2025-08-19): release version 3.1.2 (#5800)
- **David Lord** (2025-08-19): release version 3.1.2
- **David Lord** (2025-08-19): Update GitHub Actions workflow for artifact handling (#5795)
- **Grant Birkinbine** (2025-08-19): Update GitHub Actions workflow for artifact handling
- **David Lord** (2025-08-19): update dev dependencies
- **David Lord** (2025-08-19): support call template_filter without parens (#5736)
- **David Lord** (2025-08-19): rewrite docs, clean up typing for template decorators
- **kadai0308** (2025-08-19): use template_filter without parens
- **David Lord** (2025-08-19): use Jinja name consistently
- **David Lord** (2025-08-19): refactor stream_with_context for async views (#5799)
- **David Lord** (2025-08-19): refactor stream_with_context for async views
- **David Lord** (2025-08-18): security docs for TRUSTED_HOSTS (#5798)
- **David Lord** (2025-08-18): security docs for TRUSTED_HOSTS
- **David Lord** (2025-08-18): update flask-talisman link
- **David Lord** (2025-08-18): use IO[bytes] instead of BinaryIO for wider compatibility (#5777)
- **Tero Vuotila** (2025-08-18): relax type hint for bytes io
- **David Lord** (2025-08-18): Docs: Fix escaping in HTML escaping example (#5742)
- **Badhreesh** (2025-08-18): demonstrate escaping with query string

slash in value would be interpreted as a path separator in the URL
- **David Lord** (2025-08-18): Update macOS UI reference to “System Settings” (#5723)
- **David Lord** (2025-08-18): push preserved contexts in correct order (#5797)
- **David Lord** (2025-08-18): push preserved contexts in correct order
- **David Lord** (2025-08-18): start version 3.1.2
- **David Lord** (2025-06-12): Merge branch 'stable'
- **David Lord** (2025-06-12): svg logo
- **David Lord** (2025-06-10): Merge branch 'stable'
- **David Lord** (2025-06-10): cleanup svg
