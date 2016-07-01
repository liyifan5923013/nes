from django.conf.urls import patterns, url

urlpatterns = patterns(
    'experiment.views',

    # keyword
    url(r'^keyword/search/$', 'keyword_search_ajax', name='keywords_search'),
    url(r'^keyword/new/(?P<research_project_id>\d+)/(?P<keyword_name>.+)/$', 'keyword_create_ajax', name='keyword_new'),
    url(r'^keyword/add/(?P<research_project_id>\d+)/(?P<keyword_id>\d+)/$', 'keyword_add_ajax', name='keyword_add'),
    url(r'^keyword/remove/(?P<research_project_id>\d+)/(?P<keyword_id>\d+)/$', 'keyword_remove_ajax',
        name='keyword_remove'),

    # research project
    url(r'^research_project/list/$', 'research_project_list', name='research_project_list'),
    url(r'^research_project/new/$', 'research_project_create', name='research_project_new'),
    url(r'^research_project/(?P<research_project_id>\d+)/$', 'research_project_view', name='research_project_view'),
    url(r'^research_project/edit/(?P<research_project_id>\d+)/$', 'research_project_update',
        name='research_project_edit'),

    # experiment
    url(r'^research_project/(?P<research_project_id>\d+)/new_experiment/$', 'experiment_create', name='experiment_new'),
    url(r'^(?P<experiment_id>\d+)/$', 'experiment_view', name='experiment_view'),
    url(r'^edit/(?P<experiment_id>\d+)/$', 'experiment_update', name='experiment_edit'),

    # group
    url(r'^(?P<experiment_id>\d+)/group/new/$', 'group_create', name='group_new'),
    url(r'^group/(?P<group_id>\d+)/$', 'group_view', name='group_view'),
    url(r'^group/edit/(?P<group_id>\d+)/$', 'group_update', name='group_edit'),

    # equipment
    # url(r'^equipment/list/$', 'equipment_list', name='equipment_list'),
    # url(r'^equipment/configuration/$', 'equipment_configuration', name='equipment_configuration'),

    # register manufacturer
    url(r'^manufacturer/list/$', 'manufacturer_list', name='manufacturer_list'),
    url(r'^manufacturer/new/$', 'manufacturer_create', name='manufacturer_new'),
    url(r'^manufacturer/(?P<manufacturer_id>\d+)/$', 'manufacturer_view', name='manufacturer_view'),
    url(r'^manufacturer/edit/(?P<manufacturer_id>\d+)/$', 'manufacturer_update', name='manufacturer_edit'),

    # register eeg machine
    url(r'^eegmachine/list/$', 'eegmachine_list', name='eegmachine_list'),
    url(r'^eegmachine/new/$', 'eegmachine_create', name='eegmachine_new'),
    url(r'^eegmachine/(?P<eegmachine_id>\d+)/$', 'eegmachine_view', name='eegmachine_view'),
    url(r'^eegmachine/edit/(?P<eegmachine_id>\d+)/$', 'eegmachine_update', name='eegmachine_edit'),

    # register eeg amplifier
    url(r'^eegamplifier/list/$', 'eegamplifier_list', name='eegamplifier_list'),
    url(r'^eegamplifier/new/$', 'eegamplifier_create', name='eegamplifier_new'),
    url(r'^eegamplifier/(?P<eegamplifier_id>\d+)/$', 'eegamplifier_view', name='eegamplifier_view'),
    url(r'^eegamplifier/edit/(?P<eegamplifier_id>\d+)/$', 'eegamplifier_update', name='eegamplifier_edit'),

    # register eeg solution
    url(r'^eegsolution/list/$', 'eegsolution_list', name='eegsolution_list'),
    url(r'^eegsolution/new/$', 'eegsolution_create', name='eegsolution_new'),
    url(r'^eegsolution/(?P<eegsolution_id>\d+)/$', 'eegsolution_view', name='eegsolution_view'),
    url(r'^eegsolution/edit/(?P<eegsolution_id>\d+)/$', 'eegsolution_update', name='eegsolution_edit'),

    # register eeg filter type
    url(r'^eegfiltertype/list/$', 'eegfiltertype_list', name='eegfiltertype_list'),
    url(r'^eegfiltertype/new/$', 'eegfiltertype_create', name='eegfiltertype_new'),
    url(r'^eegfiltertype/(?P<eegfiltertype_id>\d+)/$', 'eegfiltertype_view', name='eegfiltertype_view'),
    url(r'^eegfiltertype/edit/(?P<eegfiltertype_id>\d+)/$', 'eegfiltertype_update', name='eegfiltertype_edit'),

    # register eeg electrode model
    url(r'^eegelectrodemodel/list/$', 'eegelectrodemodel_list', name='eegelectrodemodel_list'),
    url(r'^eegelectrodemodel/new/$', 'eegelectrodemodel_create', name='eegelectrodemodel_new'),
    url(r'^eegelectrodemodel/(?P<eegelectrodemodel_id>\d+)/$', 'eegelectrodemodel_view', name='eegelectrodemodel_view'),
    url(r'^eegelectrodemodel/edit/(?P<eegelectrodemodel_id>\d+)/$', 'eegelectrodemodel_update', name='eegelectrodemodel_edit'),

    # register material
    url(r'^material/list/$', 'material_list', name='material_list'),
    url(r'^material/new/$', 'material_create', name='material_new'),
    url(r'^material/(?P<material_id>\d+)/$', 'material_view', name='material_view'),
    url(r'^material/edit/(?P<material_id>\d+)/$', 'material_update', name='material_edit'),

    # register eeg electrode net
    url(r'^eegelectrodenet/list/$', 'eegelectrodenet_list', name='eegelectrodenet_list'),
    url(r'^eegelectrodenet/new/$', 'eegelectrodenet_create', name='eegelectrodenet_new'),
    url(r'^eegelectrodenet/(?P<eegelectrodenet_id>\d+)/$', 'eegelectrodenet_view', name='eegelectrodenet_view'),
    url(r'^eegelectrodenet/edit/(?P<eegelectrodenet_id>\d+)/$', 'eegelectrodenet_update', name='eegelectrodenet_edit'),

    # register cap size
    url(r'^eeg_electrode_cap_size/(?P<eegelectrode_cap_id>\d+)/add_size/$',
        'eegelectrodenet_cap_size_create',name='eegelectrodenet_add_size'),
    # url(r'^eeg_electrode_cap_size/remove/(?P<eegelectrode_cap_size_id>\d+)/$',
    #     'eegelectrodenet_cap_size_remove', name='cap_size_remove'),
    url(r'^eeg_electrode_cap_size/(?P<eegelectrode_cap_size_id>\d+)/$',
        'eegelectrodenet_cap_size_view',name='eegelectrodenet_cap_size_view'),
    url(r'^eeg_electrode_cap_size/(?P<eegelectrode_cap_size_id>\d+)/edit/$',
        'eegelectrodenet_cap_size_update',name='eegelectrodenet_cap_size_edit'),

    # Localization system and position
    url(r'^eeg_electrode_localization_system/list/$',
        'eeg_electrode_localization_system_list', name='eeg_electrode_localization_system_list'),
    url(r'^eeg_electrode_localization_system/new/$',
        'eeg_electrode_localization_system_create', name='eeg_electrode_localization_system_new'),
    url(r'^eeg_electrode_localization_system/(?P<eeg_electrode_localization_system_id>\d+)/$',
        'eeg_electrode_localization_system_view', name='eeg_electrode_localization_system_view'),
    url(r'^eeg_electrode_localization_system/edit/(?P<eeg_electrode_localization_system_id>\d+)/$',
        'eeg_electrode_localization_system_update', name='eeg_electrode_localization_system_edit'),
    url(r'^eeg_electrode_localization_system/(?P<eeg_electrode_localization_system_id>\d+)/new_position/$',
        'eeg_electrode_position_create', name='eeg_electrode_position_create'),
    url(r'^eeg_electrode_position/(?P<eeg_electrode_position_id>\d+)/$',
        'eeg_electrode_position_view', name='eeg_electrode_position_view'),
    url(r'^eeg_electrode_position/edit/(?P<eeg_electrode_position_id>\d+)/$',
        'eeg_electrode_position_update', name='eeg_electrode_position_edit'),

    # eeg setting
    url(r'^(?P<experiment_id>\d+)/eeg_setting/new/$', 'eeg_setting_create', name='eeg_setting_new'),
    url(r'^eeg_setting/(?P<eeg_setting_id>\d+)/$', 'eeg_setting_view', name='eeg_setting_view'),
    url(r'^eeg_setting/edit/(?P<eeg_setting_id>\d+)/$', 'eeg_setting_update', name='eeg_setting_edit'),
    url(r'^eeg_setting/(?P<eeg_setting_id>\d+)/(?P<eeg_setting_type>\w+)/$',
        'view_eeg_setting_type', name='view_eeg_setting_type'),
    url(r'^eeg_setting/(?P<eeg_setting_id>\d+)/(?P<eeg_setting_type>\w+)/edit/$',
        'edit_eeg_setting_type', name='edit_eeg_setting_type'),
    url(r'^eeg_setting/(?P<eeg_setting_id>\d+)/equipment/(?P<equipment_id>\d+)/$',
        'equipment_view', name='equipment_view'),
    url(r'^eeg_setting/eeg_electrode_position_status/(?P<eeg_setting_id>\d+)/$',
        'eeg_electrode_position_setting', name='eeg_electrode_position_setting'),
    url(r'^eeg_setting/eeg_electrode_cap/(?P<eeg_setting_id>\d+)/$',
        'eeg_electrode_cap_setting', name='eeg_electrode_cap_setting'),
    url(r'^eeg_setting/eeg_electrode_position_status/edit/(?P<eeg_setting_id>\d+)/$',
        'edit_eeg_electrode_position_setting', name='edit_eeg_electrode_position_setting'),
    url(r'^eeg_setting/eeg_electrode_position_status_model/(?P<eeg_setting_id>\d+)/$',
        'eeg_electrode_position_setting_model', name='eeg_electrode_position_setting_model'),
    url(r'^eeg_setting/eeg_electrode_position_status_model/edit/(?P<eeg_setting_id>\d+)/$',
        'edit_eeg_electrode_position_setting_model', name='edit_eeg_electrode_position_setting_model'),


    # eeg setting (ajax)
    url(r'^equipment/get_equipment_by_manufacturer/(?P<equipment_type>\w+)/(?P<manufacturer_id>\d+)/$',
        'get_json_equipment_by_manufacturer'),
    url(r'^equipment/(?P<equipment_id>\d+)/attributes/$', 'get_json_equipment_attributes'),
    url(r'^solution/(?P<solution_id>\d+)/attributes/$', 'get_json_solution_attributes'),
    url(r'^filter/(?P<filter_id>\d+)/attributes/$', 'get_json_filter_attributes'),
    # url(r'^eeg_localization_system/(?P<eeg_localization_system_id>\d+)/attributes/$',
    #     'get_json_eeg_localization_system_attributes'),
    url(r'^equipment/get_localization_system_by_electrode_net/(?P<equipment_id>\d+)/$',
        'get_localization_system_by_electrode_net'),
    url(r'^equipment/get_equipment_by_manufacturer_and_localization_system/'
        r'(?P<manufacturer_id>\w+)/(?P<eeg_localization_system_id>\d+)/$',
        'get_equipment_by_manufacturer_and_localization_system'),

    # cid
    url(r'^group_diseases/cid-10/$', 'search_cid10_ajax', name='cid10_search'),

    # classification_of_diseases (add, remove)
    url(r'^group/(?P<group_id>\d+)/diagnosis/(?P<classification_of_diseases_id>\d+)/$',
        'classification_of_diseases_insert', name='classification_of_diseases_insert'),
    url(r'^diagnosis/delete/(?P<group_id>\d+)/(?P<classification_of_diseases_id>\d+)/$',
        'classification_of_diseases_remove', name='classification_of_diseases_remove'),

    # subject
    url(r'^group/(?P<group_id>\d+)/subjects/$', 'subjects', name='subjects'),
    url(r'^subject/search/$', 'search_patients_ajax', name='subject_search'),
    url(r'^group/(?P<group_id>\d+)/add_subject/(?P<patient_id>\d+)/$', 'subjects_insert', name='subject_insert'),
    url(r'^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/upload_file/$', 'upload_file', name='upload_file'),

    # subject + questionnaire
    url(r'^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/$',
        'subject_questionnaire_view', name='subject_questionnaire'),
    url(r'^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/questionnaire/'
        r'(?P<questionnaire_id>[0-9-]+)/add_response/$',
        'subject_questionnaire_response_create', name='subject_questionnaire_response'),
    url(r'^questionnaire_response/edit/(?P<questionnaire_response_id>\d+)/$',
        'questionnaire_response_edit', name='questionnaire_response_edit'),
    url(r'^questionnaire_response/(?P<questionnaire_response_id>\d+)/$',
        'questionnaire_response_view', name='questionnaire_response_view'),

    # subject + eeg data
    url(r'^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/eeg/$',
        'subject_eeg_view', name='subject_eeg_view'),
    url(r'^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/eeg/(?P<eeg_configuration_id>[0-9-]+)/add_eeg_data/$',
        'subject_eeg_data_create', name='subject_eeg_data_create'),
    url(r'^eeg_data/(?P<eeg_data_id>\d+)/(?P<tab>\d+)/$', 'eeg_data_view', name='eeg_data_view'),
    url(r'^eeg_data/edit/(?P<eeg_data_id>\d+)/(?P<tab>\d+)/$', 'eeg_data_edit', name='eeg_data_edit'),

    # eeg_data (ajax)
    url(r'^equipment/get_cap_size_list_from_eeg_setting/(?P<eeg_setting_id>\d+)/$',
        'get_cap_size_list_from_eeg_setting'),

    # subject + emg data
    url(r'^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/emg/$',
        'subject_emg_view', name='subject_emg_view'),
    url(r'^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/emg/(?P<emg_configuration_id>[0-9-]+)/add_emg_data/$',
        'subject_emg_data_create', name='subject_emg_data_create'),
    url(r'^emg_data/(?P<emg_data_id>\d+)/$', 'emg_data_view', name='emg_data_view'),
    url(r'^emg_data/edit/(?P<emg_data_id>\d+)/$', 'emg_data_edit', name='emg_data_edit'),

    # subject + additional data
    url(r'^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/additional_data/$',
        'subject_additional_data_view', name='subject_additional_data_view'),
    url(r'^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/additional_data/'
        r'(?P<path_of_configuration>[0-9-]+)/add/$',
        'subject_additional_data_create', name='subject_additional_data_create'),
    url(r'^additional_data/(?P<additional_data_id>\d+)/$', 'additional_data_view', name='additional_data_view'),
    url(r'^additional_data/edit/(?P<additional_data_id>\d+)/$', 'additional_data_edit', name='additional_data_edit'),

    # experimental protocol components
    url(r'^(?P<experiment_id>\d+)/components/$', 'component_list', name='component_list'),
    url(r'^(?P<experiment_id>\d+)/new_component/(?P<component_type>\w+)/$', 'component_create', name='component_new'),
    url(r'^component/(?P<path_of_the_components>[0-9-UG]+)/$', 'component_view', name='component_view'),
    url(r'^component/edit/(?P<path_of_the_components>[0-9-UG]+)/$', 'component_update', name='component_edit'),
    url(r'^component/(?P<path_of_the_components>[0-9-UG]+)/add_new/(?P<component_type>\w+)/$', 'component_add_new',
        name='component_add_new'),
    url(r'^component/(?P<path_of_the_components>[0-9-UG]+)/add/(?P<component_id>\d+)/$', 'component_reuse',
        name='component_reuse'),
    url(r'^component/change_the_order/(?P<path_of_the_components>[0-9-UG]+)/(?P<component_configuration_index>[0-9-]+)/'
        r'(?P<command>\w+)/$', 'component_change_the_order', name='component_change_the_order'),

    # Data collection
    url(r'^group/(?P<group_id>\d+)/questionnaire/(?P<component_configuration_id>\d+)/$', 'questionnaire_view',
        name='questionnaire_view'),
)
