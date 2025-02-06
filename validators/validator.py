# Validation schema for WCS command payload
wcs_command_payload_schema = {
    'clientType': {
        'type': 'integer',
        'required': True,
        'nullable': False,
        'min': 0,
        'max': 3,
    },
    'clientPriority': {
        'type': 'integer',
        'required': True,
        'nullable': False,
        'min': 0,
        'max': 3,
    },
    'contractType': {
        'type': 'integer',
        'required': True,
        'nullable': False,
        'min': 0,
        'max': 3,
    },
    'buildingType': {
        'type': 'integer',
        'required': True,
        'nullable': False,
        'min': 0,
        'max': 3,
    },
    'contractRateCode': {
        'type': 'integer',
        'required': True,
        'nullable': False,
        'min': 0,
        'max': 15,
    },
    'customerGroupNumberOne': {
        'type': 'integer',
        'required': True,
        'nullable': False,
        'min': 0,
        'max': 15,
    },
    'customerGroupNumberTwo': {
        'type': 'integer',
        'required': True,
        'nullable': False,
        'min': 0,
        'max': 7,
    },
    'useType': {
        'type': 'integer',
        'required': True,
        'nullable': False,
        'min': 0,
        'max': 31,
    },
    'countyCode': {
        'type': 'integer',
        'required': True,
        'nullable': False,
        'min': 0,
        'max': 99,
    },
    'townCode': {
        'type': 'integer',
        'required': True,
        'nullable': False,
        'min': 0,
        'max': 999,
    },
    'districtCode': {
        'type': 'integer',
        'required': True,
        'nullable': False,
        'min': 0,
        'max': 9999,
    },
    'command': {
        'type': 'dict',
        'required': True,
        'nullable': False,
        'schema': {
            'argument': {
                'type': 'integer',
                'required': True,
                'nullable': False,
                'min': 0,
                'max': 31,
            },
            'id': {
                'type': 'integer',
                'required': True,
                'nullable': False,
                'min': 0,
                'max': 7,
            },
        },
    },
}

# Validation schema for creating new WCS preconfigs
post_preconfig_validator = {
    'name': {
        'type': 'string',
        'required': True,
        'nullable': False,
        'maxlength': 100,
        'minlength': 1
    },
    'description': {
        'type': 'string',
        'required': False,
        'nullable': True
    },
    'insee_codes': {
        'type': 'list',
        'required': True,
        'nullable': False,
        'schema': {
            'type': 'integer',
            'min': 0,
            'max': 99999
        }
    },
    'command_payload': {
        'type': 'dict',
        'required': True,
        'nullable': False,
        'schema': wcs_command_payload_schema
    },
    'is_enabled': {
        'type': 'boolean',
        'required': True,
        'nullable': False,
    },
    'execution_time': {
        'type': 'string',  # Format "HH:MM"
        'required': True,
        'nullable': False,
        'regex': '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$'
    },
}
