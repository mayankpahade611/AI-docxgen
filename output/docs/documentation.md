Project Documentation

## Code Overview
### `C:/flask\docs\conf.py`
**Funcitons:** github_link, setup

### `C:/flask\examples\celery\make_celery.py`
### `C:/flask\examples\celery\src\task_app\tasks.py`
**Funcitons:** add, block, process

### `C:/flask\examples\celery\src\task_app\views.py`
**Funcitons:** result, add, block, process

### `C:/flask\examples\celery\src\task_app\__init__.py`
**Classes:** FlaskTask

**Funcitons:** create_app, index, celery_init_app, __call__

### `C:/flask\examples\javascript\js_example\views.py`
**Funcitons:** index, add

### `C:/flask\examples\javascript\js_example\__init__.py`
### `C:/flask\examples\javascript\tests\conftest.py`
**Funcitons:** fixture_app, client

### `C:/flask\examples\javascript\tests\test_js_example.py`
**Funcitons:** test_index, check, test_add

### `C:/flask\examples\tutorial\flaskr\auth.py`
**Funcitons:** login_required, wrapped_view, load_logged_in_user, register, login, logout

### `C:/flask\examples\tutorial\flaskr\blog.py`
**Funcitons:** index, get_post, create, update, delete

### `C:/flask\examples\tutorial\flaskr\db.py`
**Funcitons:** get_db, close_db, init_db, init_db_command, init_app

### `C:/flask\examples\tutorial\flaskr\__init__.py`
**Funcitons:** create_app, hello

### `C:/flask\examples\tutorial\tests\conftest.py`
**Classes:** AuthActions

**Funcitons:** app, client, runner, __init__, login, logout, auth

### `C:/flask\examples\tutorial\tests\test_auth.py`
**Funcitons:** test_register, test_register_validate_input, test_login, test_login_validate_input, test_logout

### `C:/flask\examples\tutorial\tests\test_blog.py`
**Funcitons:** test_index, test_login_required, test_author_required, test_exists_required, test_create, test_update, test_create_update_validate, test_delete

### `C:/flask\examples\tutorial\tests\test_db.py`
**Classes:** Recorder

**Funcitons:** test_get_close_db, test_init_db_command, fake_init_db

### `C:/flask\examples\tutorial\tests\test_factory.py`
**Funcitons:** test_config, test_hello

### `C:/flask\src\flask\app.py`
**Classes:** Flask, CustomClient

**Funcitons:** _make_timedelta, __init__, get_send_file_max_age, send_static_file, open_resource, open_instance_resource, create_jinja_environment, create_url_adapter, raise_routing_exception, update_template_context, make_shell_context, run, test_client, __init__, test_cli_runner, handle_http_exception, handle_user_exception, handle_exception, log_exception, dispatch_request, full_dispatch_request, finalize_request, make_default_options_response, ensure_sync, async_to_sync, url_for, make_response, preprocess_request, process_response, do_teardown_request, do_teardown_appcontext, app_context, request_context, test_request_context, wsgi_app, __call__

### `C:/flask\src\flask\blueprints.py`
**Classes:** Blueprint

**Funcitons:** __init__, get_send_file_max_age, send_static_file, open_resource

### `C:/flask\src\flask\cli.py`
**Classes:** NoAppException, ScriptInfo, AppGroup, to, FlaskGroup, CertParamType, SeparatedPathType

**Funcitons:** find_best_app, _called_with_wrong_args, find_app_by_string, prepare_import, locate_app, locate_app, locate_app, get_version, __init__, load_app, with_appcontext, decorator, command, decorator, group, _set_app, _set_debug, _env_file_callback, __init__, _load_plugin_commands, get_command, list_commands, make_context, parse_args, _path_is_ancestor, load_dotenv, show_server_banner, __init__, convert, _validate_key, convert, run_command, app, shell_command, routes_command, main

### `C:/flask\src\flask\config.py`
**Classes:** ConfigAttribute, Config

**Funcitons:** __init__, __get__, __get__, __get__, __set__, __init__, from_envvar, from_prefixed_env, from_pyfile, from_object, from_file, from_mapping, get_namespace, __repr__

### `C:/flask\src\flask\ctx.py`
**Classes:** _AppCtxGlobals, AppContext

**Funcitons:** __getattr__, __setattr__, __delattr__, get, pop, setdefault, __contains__, __iter__, __repr__, after_this_request, index, add_header, copy_current_request_context, index, do_some_work, wrapper, has_request_context, has_app_context, __init__, from_environ, has_request, copy, request, session, match_request, push, pop, __enter__, __exit__, __repr__, __getattr__

### `C:/flask\src\flask\debughelpers.py`
**Classes:** UnexpectedUnicodeError, DebugFilesKeyError, FormDataRoutingRedirect, newcls

**Funcitons:** __init__, __str__, __init__, attach_enctype_error_multidict, __getitem__, _dump_loader_info, explain_template_loading_attempts

### `C:/flask\src\flask\globals.py`
**Classes:** ProxyMixin, FlaskProxy, AppContextProxy, _AppCtxGlobalsProxy, RequestProxy, SessionMixinProxy

**Funcitons:** _get_current_object, __getattr__

### `C:/flask\src\flask\helpers.py`
**Funcitons:** get_debug_flag, get_load_dotenv, stream_with_context, stream_with_context, stream_with_context, streamed_response, generate, streamed_response, generate, decorator, generator, make_response, index, index, url_for, redirect, abort, get_template_attribute, flash, get_flashed_messages, _prepare_send_file_kwargs, send_file, send_from_directory, download_file, get_root_path, _split_blueprint_path

### `C:/flask\src\flask\logging.py`
**Funcitons:** wsgi_errors_stream, has_level_handler, create_logger

### `C:/flask\src\flask\sessions.py`
**Classes:** SessionMixin, SecureCookieSession, NullSession, SessionInterface, Session, SecureCookieSessionInterface

**Funcitons:** permanent, permanent, __init__, on_update, __getitem__, get, setdefault, _fail, make_null_session, is_null_session, get_cookie_name, get_cookie_domain, get_cookie_path, get_cookie_httponly, get_cookie_secure, get_cookie_samesite, get_cookie_partitioned, get_expiration_time, should_set_cookie, open_session, save_session, _lazy_sha1, get_signing_serializer, open_session, save_session

### `C:/flask\src\flask\signals.py`
### `C:/flask\src\flask\templating.py`
**Classes:** Environment, DispatchingJinjaLoader

**Funcitons:** _default_template_ctx_processor, __init__, __init__, get_source, _get_source_explained, _get_source_fast, _iter_loaders, list_templates, _render, render_template, render_template_string, _stream, generate, stream_template, stream_template_string

### `C:/flask\src\flask\testing.py`
**Classes:** EnvironBuilder, FlaskClient, FlaskCliRunner

**Funcitons:** __init__, json_dumps, _get_werkzeug_version, __init__, session_transaction, _copy_environ, _request_from_builder_args, open, __enter__, __exit__, __init__, invoke

### `C:/flask\src\flask\typing.py`
### `C:/flask\src\flask\views.py`
**Classes:** View, Hello, sets, MethodView, CounterAPI

**Funcitons:** dispatch_request, dispatch_request, as_view, view, view, get, post, __init_subclass__, dispatch_request

### `C:/flask\src\flask\wrappers.py`
**Classes:** Request, Response

**Funcitons:** max_content_length, max_content_length, max_form_memory_size, max_form_memory_size, max_form_parts, max_form_parts, endpoint, blueprint, blueprints, _load_form_data, on_json_loading_failed, max_cookie_size

### `C:/flask\src\flask\__init__.py`
### `C:/flask\src\flask\__main__.py`
### `C:/flask\src\flask\json\provider.py`
**Classes:** JSONProvider, DefaultJSONProvider

**Funcitons:** __init__, dumps, dump, loads, load, _prepare_response_obj, response, _default, dumps, loads, response

### `C:/flask\src\flask\json\tag.py`
**Classes:** TagOrderedDict, JSONTag, TagDict, PassDict, TagTuple, PassList, TagBytes, TagMarkup, TagUUID, TagDateTime, TaggedJSONSerializer

**Funcitons:** check, to_json, to_python, __init__, check, to_json, to_python, tag, check, to_json, to_python, check, to_json, check, to_json, to_python, check, to_json, check, to_json, to_python, check, to_json, to_python, check, to_json, to_python, check, to_json, to_python, __init__, register, tag, untag, _untag_scan, dumps, loads

### `C:/flask\src\flask\json\__init__.py`
**Funcitons:** dumps, dump, loads, load, jsonify

### `C:/flask\src\flask\sansio\app.py`
**Classes:** App, of, ListConverter

**Funcitons:** _make_timedelta, __init__, to_python, to_url, _check_setup_finished, name, logger, jinja_env, create_jinja_environment, make_config, make_aborter, auto_find_instance_path, create_global_jinja_loader, select_jinja_autoescape, debug, debug, register_blueprint, iter_blueprints, add_url_rule, template_filter, template_filter, template_filter, reverse_filter, decorator, add_template_filter, template_test, template_test, template_test, is_prime_test, decorator, add_template_test, template_global, template_global, template_global, double, decorator, add_template_global, teardown_appcontext, shell_context_processor, _find_error_handler, trap_http_exception, should_ignore_error, redirect, inject_url_defaults, handle_url_build_error

### `C:/flask\src\flask\sansio\blueprints.py`
**Classes:** BlueprintSetupState, Blueprint

**Funcitons:** __init__, add_url_rule, __init__, _check_setup_finished, record, record_once, wrapper, make_setup_state, register_blueprint, register, _merge_blueprint_funcs, extend, add_url_rule, app_template_filter, app_template_filter, app_template_filter, decorator, add_app_template_filter, register_template_filter, app_template_test, app_template_test, app_template_test, decorator, add_app_template_test, register_template_test, app_template_global, app_template_global, app_template_global, decorator, add_app_template_global, register_template_global, before_app_request, after_app_request, teardown_app_request, app_context_processor, app_errorhandler, decorator, from_blueprint, app_url_value_preprocessor, app_url_defaults

### `C:/flask\src\flask\sansio\scaffold.py`
**Classes:** Scaffold

**Funcitons:** setupmethod, wrapper_func, __init__, __repr__, _check_setup_finished, static_folder, static_folder, has_static_folder, static_url_path, static_url_path, jinja_loader, _method_route, get, post, put, delete, patch, route, index, decorator, add_url_rule, index, index, index, endpoint, example, decorator, before_request, load_user, after_request, teardown_request, context_processor, url_value_preprocessor, url_defaults, errorhandler, page_not_found, special_exception_handler, decorator, register_error_handler, _get_exc_class_and_code, _endpoint_from_view_func, _find_package_path, find_package

### `C:/flask\tests\conftest.py`
**Funcitons:** _standard_os_environ, _reset_os_environ, app, app_ctx, req_ctx, client, test_apps, leak_detector, modules_tmp_path, modules_tmp_path_prefix, site_packages, purge_module, inner

### `C:/flask\tests\test_appctx.py`
**Classes:** CustomRequestGlobals

**Funcitons:** test_basic_url_generation, index, test_url_generation_requires_server_name, test_url_generation_without_context_fails, test_request_context_means_app_context, test_app_context_provides_current_app, test_app_tearing_down, cleanup, test_app_tearing_down_with_previous_exception, cleanup, test_app_tearing_down_with_handled_exception_by_except_block, cleanup, test_app_tearing_down_with_handled_exception_by_app_handler, cleanup, index, handler, test_app_tearing_down_with_unhandled_exception, cleanup, index, test_app_ctx_globals_methods, test_custom_app_ctx_globals_class, __init__, test_context_refcounts, teardown_req, teardown_app, index, test_clean_pop, teardown_req, teardown_app

### `C:/flask\tests\test_async.py`
**Classes:** AppError, BlueprintError, AsyncView, AsyncMethodView

**Funcitons:** dispatch_request, get, post, _async_app, index, handle, error, bp_index, bp_handle, bp_error, test_async_route, test_async_error_handler, test_async_before_after_request, index, before, after, bp_index, bp_before, bp_after

### `C:/flask\tests\test_basic.py`
**Classes:** PrefixPathMiddleware, MyException, ForbiddenSubclass, E1, E2, E3, View

**Funcitons:** test_options_work, index, test_options_on_multiple_rules, index, index_put, test_method_route, hello, test_method_route_no_methods, test_provide_automatic_options_attr, index, index2, test_provide_automatic_options_kwarg, index, more, test_request_dispatching, index, more, test_disallow_string_for_allowed_methods, test_url_mapping, index, more, options, test_werkzeug_routing, bar, index, test_endpoint_decorator, bar, index, test_session, set, get, test_session_path, index, test_session_using_application_root, __init__, __call__, index, test_session_using_session_settings, index, clear, test_session_using_samesite_attribute, index, test_missing_session, expect_exception, test_session_secret_key_fallbacks, set_session, get_session, test_session_expiration, index, test, test_session_stored_last, modify_session, dump_session_contents, test_session_special_types, dump_session_contents, test_session_cookie_setting, bump, read, run_test, test_session_vary_cookie, set_session, get, getitem, setdefault, clear, vary_cookie_header_set, vary_header_set, no_vary_header, expect, test_session_refresh_vary, login, ignored, test_flashes, test_extended_flashing, index, test, test_with_categories, test_filter, test_filters, test_filters2, test_request_processing, before_request, after_request, index, test_request_preprocessing_early_return, before_request1, before_request2, before_request3, index, test_after_request_processing, index, foo, test_teardown_request_handler, teardown_request, root, test_teardown_request_handler_debug_mode, teardown_request, root, test_teardown_request_handler_error, teardown_request1, teardown_request2, fails, test_before_after_request_order, before1, before2, after1, after2, finish1, finish2, index, test_error_handling, not_found, internal_server_error, forbidden, index, error, error2, test_error_handling_processing, internal_server_error, broken_func, after_request, test_baseexception_error_handling, broken_func, test_before_request_and_routing_errors, attach_something, return_something, test_user_error_handling, handle_my_exception, index, test_http_error_subclass_handling, handle_forbidden_subclass, handle_403, index1, index2, index3, test_errorhandler_precedence, handle_e2, handle_exception, raise_e1, raise_e3, test_trap_bad_request_key_error, fail, allow_abort, test_trapping_of_all_http_exceptions, fail, test_error_handler_after_processor_error, before_request, after_request, index, internal_server_error, test_enctype_debug_helper, index, test_response_types, from_text, from_bytes, from_full_tuple, from_text_headers, from_text_status, from_response_headers, from_response_status, from_wsgi, from_dict, from_list, test_response_type_errors, from_none, from_small_tuple, from_large_tuple, from_bad_type, from_bad_wsgi, test_make_response, test_make_response_with_response_instance, test_jsonify_no_prettyprint, test_jsonify_mimetype, test_json_dump_dataclass, test_jsonify_args_and_kwargs_check, test_url_generation, hello, test_build_error_handler, handler, test_build_error_handler_reraise, handler_raises_build_error, test_url_for_passes_special_values_to_build_error_handler, handler, test_static_files, test_static_url_path, test_static_url_path_with_ending_slash, test_static_url_empty_path, test_static_url_empty_path_default, test_static_folder_with_pathlib_path, test_static_folder_with_ending_slash, catch_all, test_static_route_with_host_matching, test_request_locals, test_server_name_matching, index, test_server_name_subdomain, index, subdomain, test_exception_propagation, index, test_werkzeug_passthrough_errors, run_simple_mock, test_url_processors, add_language_code, pull_lang_code, index, about, something_else, test_inject_blueprint_url_defaults, bp_defaults, view, test_nonascii_pathinfo, index, test_no_setup_after_first_request, index, test_routing_redirect_debugging, user, test_route_decorator_custom_endpoint, foo, for_bar, for_bar_foo, test_get_method_on_g, test_g_iteration_protocol, test_subdomain_basic_support, normal_index, test_index, test_subdomain_matching, index, test_subdomain_matching_with_ports, index, test_subdomain_matching_other_name, index, test_multi_route_rules, index, test_multi_route_class_views, __init__, index, test_run_defaults, run_simple_mock, test_run_server_port, run_simple_mock, test_run_from_config, run_simple_mock, test_max_cookie_size, index, test_app_freed_on_zero_refcount

### `C:/flask\tests\test_blueprints.py`
**Classes:** MyDecoratorException, MyFunctionException, MyBlueprint

**Funcitons:** test_blueprint_specific_error_handling, frontend_forbidden, frontend_no, backend_forbidden, backend_no, sideend_no, app_forbidden, test_blueprint_specific_user_error_handling, my_decorator_exception_handler, my_function_exception_handler, blue_deco_test, blue_func_test, test_blueprint_app_error_handling, forbidden_handler, app_forbidden, bp_forbidden, test_blueprint_prefix_slash, index, test_blueprint_url_defaults, foo, bar, test_blueprint_url_processors, add_language_code, pull_lang_code, index, about, test_templates_and_static, test_default_static_max_age, get_send_file_max_age, test_templates_list, test_dotted_name_not_allowed, test_empty_name_not_allowed, test_dotted_names_from_app, app_index, index, test_empty_url_defaults, something, test_route_decorator_custom_endpoint, foo, foo_bar, foo_bar_foo, bar_foo, index, test_route_decorator_custom_endpoint_with_dots, view, test_endpoint_decorator, foobar, test_template_filter, my_reverse, my_reverse_2, my_reverse_3, my_reverse_4, test_add_template_filter, my_reverse, test_template_filter_with_name, my_reverse, test_add_template_filter_with_name, my_reverse, test_template_filter_with_template, super_reverse, index, test_template_filter_after_route_with_template, index, super_reverse, test_add_template_filter_with_template, super_reverse, index, test_template_filter_with_name_and_template, my_reverse, index, test_add_template_filter_with_name_and_template, my_reverse, index, test_template_test, is_boolean, boolean_2, boolean_3, boolean_4, test_add_template_test, is_boolean, test_template_test_with_name, is_boolean, test_add_template_test_with_name, is_boolean, test_template_test_with_template, boolean, index, test_template_test_after_route_with_template, index, boolean, test_add_template_test_with_template, boolean, index, test_template_test_with_name_and_template, is_boolean, index, test_add_template_test_with_name_and_template, is_boolean, index, test_context_processing, template_string, not_answer_context_processor, answer_context_processor, bp_page, app_page, test_template_global, get_answer, get_stuff_1, get_stuff_2, get_stuff_3, test_request_processing, before_bp, after_bp, teardown_bp, bp_endpoint, test_app_request_processing, before_app, after_app, teardown_app, bp_endpoint, test_app_url_processors, add_language_code, pull_lang_code, index, about, test_nested_blueprint, forbidden, parent_index, parent_no, child_index, child_no, grandchild_forbidden, grandchild_index, grandchild_no, test_nested_callback_order, app_before1, app_teardown1, app_before2, app_teardown2, app_ctx, parent_before1, parent_teardown1, parent_before2, parent_teardown2, parent_ctx, child_before1, child_teardown1, child_before2, child_teardown2, child_ctx, a, b, test_nesting_url_prefixes, index, test_nesting_subdomains, index, test_child_and_parent_subdomain, index, test_unique_blueprint_names, test_self_registration, test_blueprint_renaming, index, error, forbidden, index2

### `C:/flask\tests\test_cli.py`
**Classes:** Module, Module, Module, Module, Module, Module, Module, Module, Module, Module, Module, Module, MockCtx, TestRoutes

**Funcitons:** runner, test_cli_name, test_find_best_app, create_app, create_app, make_app, create_app, create_app, create_app, create_app, test_prepare_import, reset_path, test_locate_app, test_locate_app_raises, test_locate_app_suppress_raise, test_get_version, exit, test_scriptinfo, create_app, test_app_cli_has_app_context, _param_cb, check, test_with_appcontext, testcmd, test_appgroup_app_context, cli, test, subgroup, test2, test_flaskgroup_app_context, create_app, cli, test, test_flaskgroup_debug, create_app, cli, test, test_flaskgroup_nested, show, test_no_command_echo_loading_error, test_help_echo_loading_error, test_help_echo_exception, create_app, app, invoke, expect_order, test_simple, test_sort, test_all_methods, test_no_routes, test_subdomain, test_host, dotenv_not_available, test_load_dotenv, test_dotenv_path, test_dotenv_optional, test_disable_dotenv_from_env, test_run_cert_path, test_run_cert_adhoc, test_run_cert_import, test_run_cert_no_ssl, test_cli_blueprints, custom_command, nested_command, merged_command, late_command, test_cli_empty, test_run_exclude_patterns

### `C:/flask\tests\test_config.py`
**Classes:** Base, Test, Config, Flask

**Funcitons:** common_object_test, test_config_from_pyfile, test_config_from_object, test_config_from_file_json, test_config_from_file_toml, test_from_prefixed_env, test_from_prefixed_env_custom_prefix, test_from_prefixed_env_nested, test_config_from_mapping, test_config_from_class, test_config_from_envvar, test_config_from_envvar_missing, test_config_missing, test_config_missing_file, test_custom_config_class, test_session_lifetime, test_get_namespace, test_from_pyfile_weird_encoding

### `C:/flask\tests\test_converters.py`
**Classes:** ListConverter, ContextConverter

**Funcitons:** test_custom_converters, to_python, to_url, index, test_context_available, to_python, index

### `C:/flask\tests\test_helpers.py`
**Classes:** FakePath, PyBytesIO, TestSendfile, StaticFileApp, TestUrlFor, MyView, MyAborter, MyFlask, My900Error, TestNoImports, TestStreaming, Wrapper, TestHelpers

**Funcitons:** __init__, __fspath__, __init__, __getattr__, test_send_file, test_static_file, get_send_file_max_age, test_send_from_directory, test_url_for_with_anchor, index, test_url_for_with_scheme, index, test_url_for_with_scheme_not_external, test_url_for_with_alternating_schemes, index, test_url_with_method, get, post, test_url_for_with_self, index, test_redirect_no_app, test_redirect_with_app, redirect, test_abort_no_app, test_app_aborter_class, test_abort_with_app, test_name_with_import_error, test_streaming_with_context, index, generate, test_streaming_with_context_as_decorator, index, generate, test_streaming_with_context_and_custom_close, __init__, __iter__, close, __next__, index, generate, test_stream_keeps_session, index, gen, test_async_view, index, gen, test_get_debug_flag, test_make_response, test_open_resource, test_open_resource_exceptions, test_open_resource_with_encoding

### `C:/flask\tests\test_instance_config.py`
**Funcitons:** test_explicit_instance_paths, test_uninstalled_module_paths, test_uninstalled_package_paths, test_uninstalled_namespace_paths, create_namespace, test_installed_module_paths, test_installed_package_paths, test_prefix_package_paths

### `C:/flask\tests\test_json.py`
**Classes:** FixedOffset, X, CustomProvider, ObjectWithHTML

**Funcitons:** test_bad_request_debug_message, post_json, test_json_bad_requests, return_json, test_json_custom_mimetypes, return_json, test_json_as_unicode, test_json_dump_to_file, test_jsonify_basic_types, test_jsonify_dicts, return_kwargs, return_dict, test_jsonify_arrays, return_args_unpack, return_array, test_jsonify_datetime, index, __init__, utcoffset, tzname, dst, test_jsonify_aware_datetimes, test_jsonify_uuid_types, test_json_decimal, test_json_attr, add, test_tojson_filter, test_json_customization, __init__, default, object_hook, loads, index, _has_encoding, test_json_key_sorting, index, test_html_method, __html__

### `C:/flask\tests\test_json_tag.py`
**Classes:** TagDict, Foo, TagFoo, Tag1, Tag2

**Funcitons:** test_dump_load_unchanged, test_duplicate_tag, test_custom_tag, __init__, check, to_json, to_python, test_tag_interface, test_tag_order

### `C:/flask\tests\test_logging.py`
**Funcitons:** reset_logging, test_logger, test_logger_debug, test_existing_handler, test_wsgi_errors_stream, index, test_has_level_handler, test_log_view_exception, index

### `C:/flask\tests\test_regression.py`
**Classes:** Foo

**Funcitons:** test_aborting, handle_foo, index, test

### `C:/flask\tests\test_reqctx.py`
**Classes:** TestGreenletContextCopying, SessionError, FailingSessionInterface, CustomFlask, PathAwareSessionInterface, CustomFlask

**Funcitons:** test_teardown_on_pop, end_of_request, test_teardown_with_previous_exception, end_of_request, test_teardown_with_handled_exception, end_of_request, test_proper_test_request_context, index, sub, test_context_binding, index, meh, test_context_test, test_manual_context_binding, index, test_greenlet_context_copying, index, g, test_greenlet_context_copying_api, index, g, test_session_error_pops_context, open_session, index, test_session_dynamic_cookie_name, get_cookie_name, set, get, set_dynamic_cookie, get_dynamic_cookie, test_bad_environ_raises_bad_request, test_environ_for_valid_idna_completes, index, test_normal_environ_completes, index

### `C:/flask\tests\test_request.py`
**Funcitons:** test_max_content_length, index, catcher, test_limit_config, test_trusted_hosts_config, index

### `C:/flask\tests\test_session_interface.py`
**Classes:** MySessionInterface

**Funcitons:** test_open_session_with_endpoint, save_session, open_session, index

### `C:/flask\tests\test_signals.py`
**Funcitons:** test_template_rendered, index, record, test_before_render_template, index, record, test_request_signals, before_request_signal, after_request_signal, before_request_handler, after_request_handler, index, test_request_exception_signal, index, record, test_appcontext_signals, record_push, record_pop, index, test_flash_signal, index, record, test_appcontext_tearing_down_signal, record_teardown, index

### `C:/flask\tests\test_subclassing.py`
**Classes:** SuppressedFlask

**Funcitons:** test_suppressed_exception_logging, log_exception, index

### `C:/flask\tests\test_templating.py`
**Classes:** MyFlask, _TestHandler, CustomEnvironment, CustomFlask

**Funcitons:** test_context_processing, context_processor, index, test_original_win, index, test_simple_stream, index, test_request_less_rendering, context_processor, test_standard_context, index, test_escaping, index, test_no_escaping, index, test_escaping_without_template_filename, test_macros, test_template_filter, my_reverse, my_reverse_2, my_reverse_3, my_reverse_4, test_add_template_filter, my_reverse, test_template_filter_with_name, my_reverse, test_add_template_filter_with_name, my_reverse, test_template_filter_with_template, super_reverse, index, test_add_template_filter_with_template, super_reverse, index, test_template_filter_with_name_and_template, my_reverse, index, test_add_template_filter_with_name_and_template, my_reverse, index, test_template_test, boolean, boolean_2, boolean_3, boolean_4, test_add_template_test, boolean, test_template_test_with_name, is_boolean, test_add_template_test_with_name, is_boolean, test_template_test_with_template, boolean, index, test_add_template_test_with_template, boolean, index, test_template_test_with_name_and_template, is_boolean, index, test_add_template_test_with_name_and_template, is_boolean, index, test_add_template_global, get_stuff, get_stuff_1, get_stuff_2, get_stuff_3, test_custom_template_loader, create_global_jinja_loader, index, test_iterable_loader, context_processor, index, test_templates_auto_reload, test_templates_auto_reload_debug_run, run_simple_mock, test_template_loader_debugging, handle, test_custom_jinja_env

### `C:/flask\tests\test_testing.py`
**Classes:** Namespace, SubRunner, NS

**Funcitons:** test_environ_defaults_from_config, index, test_environ_defaults, index, test_environ_base_default, index, test_environ_base_modified, index, test_client_open_environ, index, test_specify_url_scheme, index, test_path_is_url, test_environbuilder_json_dumps, test_blueprint_with_subdomain, index, test_redirect_session, index, get_session, test_session_transactions, index, test_session_transactions_no_null_sessions, test_session_transactions_keep_context, test_session_transaction_needs_cookies, test_test_client_context_binding, index, other, test_reuse_client, test_full_url_request, action, test_json_request_and_response, echo, test_client_json_no_app_context, hello, add, test_subdomain, view, test_nosubdomain, view, test_cli_runner_class, test_cli_invoke, hello_command, test_cli_custom_obj, create_app, hello_command, test_client_pop_all_preserved, index

### `C:/flask\tests\test_user_error_handler.py`
**Classes:** CustomException, ParentException, ChildExceptionUnregistered, ChildExceptionRegistered, ForbiddenSubclassRegistered, ForbiddenSubclassUnregistered, TestGenericHandlers, Custom

**Funcitons:** test_error_handler_no_match, custom_exception_handler, handle_500, custom_test, key_error, do_abort, test_error_handler_subclass, parent_exception_handler, child_exception_handler, parent_test, unregistered_test, registered_test, test_error_handler_http_subclass, code_exception_handler, subclass_exception_handler, forbidden_test, registered_test, unregistered_test, test_error_handler_blueprint, bp_exception_handler, bp_test, app_exception_handler, app_test, test_default_error_handler, bp_exception_handler, bp_forbidden_handler, bp_registered_test, bp_forbidden_test, catchall_exception_handler, catchall_forbidden_handler, forbidden, slash, app, do_custom, do_error, do_abort, do_raise, report_error, test_handle_class_or_code, handle_500, test_handle_generic_http, handle_http, test_handle_generic, handle_exception

### `C:/flask\tests\test_views.py`
**Classes:** Index, Index, Index, Other, Index, BetterIndex, Index, Index1, Index2, Index3, Index, Index, Index, BaseView, ChildView, GetView, DeleteView, GetDeleteView, GetView, OtherView, View, CountInit

**Funcitons:** common_test, test_basic_view, dispatch_request, test_method_based_view, get, post, test_view_patching, get, post, get, post, test_view_inheritance, get, post, delete, test_view_decorators, add_x_parachute, new_function, dispatch_request, test_view_provide_automatic_options_attr, dispatch_request, dispatch_request, dispatch_request, test_implicit_head, get, test_explicit_head, get, head, test_endpoint_override, dispatch_request, test_methods_var_inheritance, get, propfind, test_multiple_inheritance, get, delete, test_remove_method_from_parent, get, post, test_init_once, __init__, dispatch_request

### `C:/flask\tests\test_apps\blueprintapp\__init__.py`
### `C:/flask\tests\test_apps\blueprintapp\apps\__init__.py`
### `C:/flask\tests\test_apps\blueprintapp\apps\admin\__init__.py`
**Funcitons:** index, index2

### `C:/flask\tests\test_apps\blueprintapp\apps\frontend\__init__.py`
**Funcitons:** index, missing_template

### `C:/flask\tests\test_apps\cliapp\app.py`
### `C:/flask\tests\test_apps\cliapp\factory.py`
**Funcitons:** create_app, create_app2, no_app

### `C:/flask\tests\test_apps\cliapp\importerrorapp.py`
### `C:/flask\tests\test_apps\cliapp\multiapp.py`
### `C:/flask\tests\test_apps\cliapp\__init__.py`
### `C:/flask\tests\test_apps\cliapp\inner1\__init__.py`
### `C:/flask\tests\test_apps\cliapp\inner1\inner2\flask.py`
### `C:/flask\tests\test_apps\cliapp\inner1\inner2\__init__.py`
### `C:/flask\tests\test_apps\helloworld\hello.py`
**Funcitons:** hello

### `C:/flask\tests\test_apps\helloworld\wsgi.py`
### `C:/flask\tests\test_apps\subdomaintestmodule\__init__.py`
### `C:/flask\tests\type_check\typing_app_decorators.py`
**Funcitons:** after_sync, after_async, before_sync, before_async, teardown_sync, teardown_async

### `C:/flask\tests\type_check\typing_error_handler.py`
**Funcitons:** handle_400, handle_custom, handle_accept_base, handle_multiple

### `C:/flask\tests\type_check\typing_route.py`
**Classes:** StatusJSON, RenderTemplateView

**Funcitons:** hello_str, hello_bytes, hello_json, hello_json_dict, hello_json_list, typed_dict, hello_generator, show, hello_generator_expression, hello_iterator, tuple_status, tuple_status_enum, tuple_headers, return_template, return_template_stream, async_route, __init__, dispatch_request

## Git Commit History
Docs typo/markup fixes. Merge app and request context. Use Jinja name consistently. Refactor stream_with_context for async views. Security docs for TRUSTED_HOSTS.
