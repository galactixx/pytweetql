NODES_ERROR_API = {
    'entry': {'errors': {'type': 'list'}},
    'objects': {
        'code': {'code': {'type': 'int'}},
        'message': {'message': {'type': 'str'}}
    }
}
NODES_LIST_ADD_MEMBER = {
    'entry': {'list': {'type': 'dict', 'children': {
        'user_results': {'type': 'dict', 'children': {
            'result': {'type': 'dict'}}}}}
    },
    'objects': {
        'user': {'rest_id': {'type': 'str'}},
        'verified': {'is_blue_verified': {'type': 'bool'}},
        'user_info': {'legacy': {'type': 'dict'}}
    }
}
NODES_LIST_REMOVE_MEMBER = {
    'entry': {'list': {'type': 'dict', 'children': {
        'user_results': {'type': 'dict', 'children': {
            'result': {'type': 'dict'}}}}}
    },
    'objects': {
        'user': {'rest_id': {'type': 'str'}},
        'verified': {'is_blue_verified': {'type': 'bool'}},
        'user_info': {'legacy': {'type': 'dict'}}
    }
}
NODES_CREATE_TWEET = {
    'entry': {'create_tweet': {'type': 'dict', 'children': {
        'tweet_results': {'type': 'dict', 'children': {
            'result': {'type': 'dict'}}}}}
    },
    'objects': {
        'user': {'core': {'type': 'dict', 'children': {
            'user_results': {'type': 'dict', 'children': {
                'result': {'type': 'dict'}}}}}
        },
        'user_info': {'core': {'type': 'dict', 'children': {
            'user_results': {'type': 'dict', 'children': {
                'result': {'type': 'dict', 'children': {
                    'legacy': {'type': 'dict'}}}}}}}
        },
        'tweet': {'legacy': {'type': 'dict'}},
        'source': {'source': {'type': 'str'}}
    }
}
NODES_LIST_CREATE = {
    'entry': {'list': {'type': 'dict'}},
    'objects': {
        'name': {'name': {'type': 'str'}},
        'description': {'description': {'type': 'str'}},
        'is_following': {'following': {'type': 'bool'}},
        'list_id': {'id_str': {'type': 'str'}},
        'member_count': {'member_count': {'type': 'int'}},
        'mode': {'mode': {'type': 'str'}},
    }
}
NODES_LIST_LATEST_TWEETS = {
    'entry': {'list': {'type': 'dict', 'children': {
        'tweets_timeline': {'type': 'dict', 'children': {
            'timeline': {'type': 'dict', 'children': {
                'instructions': {'type': 'list', 'children': {
                    'entries': {'type': 'list', 'children': {
                        'content': {'type': 'dict', 'children': [
                            {'itemContent': {'type': 'dict', 'children': {
                                'tweet_results': {'type': 'dict', 'children': {
                                    'result': {'type': 'dict'}}}}}},
                            {'items': {'type': 'list', 'children': {
                                'item': {'type': 'dict', 'children': {
                                    'itemContent': {'type': 'dict', 'children': {
                                        'tweet_results': {'type': 'dict', 'children': {
                                            'result': {'type': 'dict'}}}}}}}}}}
                        ]}}}}}}}}}}}
    },
    'objects': {
        'user': {'core': {'type': 'dict', 'children': {
            'user_results': {'type': 'dict', 'children': {
                'result': {'type': 'dict'}}}}}
        },
        'user_info': {'core': {'type': 'dict', 'children': {
            'user_results': {'type': 'dict', 'children': {
                'result': {'type': 'dict', 'children': {
                    'legacy': {'type': 'dict'}}}}}}}
        },
        'tweet': {'legacy': {'type': 'dict'}},
        'source': {'source': {'type': 'str'}}
    }
}
NODES_USER_TWEETS = {
    'entry': {'user': {'type': 'dict', 'children': {
        'result': {'type': 'dict', 'children': {
            'timeline_v2': {'type': 'dict', 'children': {
                'timeline': {'type': 'dict', 'children': {
                    'instructions': {'type': 'list', 'children': {
                        'entries': {'type': 'list', 'children': {
                            'content': {'type': 'dict', 'children': [
                                {'itemContent': {'type': 'dict', 'children': {
                                    'tweet_results': {'type': 'dict', 'children': {
                                        'result': {'type': 'dict'}}}}}},
                                {'items': {'type': 'list', 'children': {
                                    'item': {'type': 'dict', 'children': {
                                        'itemContent': {'type': 'dict', 'children': {
                                            'tweet_results': {'type': 'dict', 'children': {
                                                'result': {'type': 'dict'}}}}}}}}}}
                            ]}}}}}}}}}}}}}
    },
    'objects': {
        'user': {'core': {'type': 'dict', 'children': {
            'user_results': {'type': 'dict', 'children': {
                'result': {'type': 'dict'}}}}}
        },
        'user_info': {'core': {'type': 'dict', 'children': {
            'user_results': {'type': 'dict', 'children': {
                'result': {'type': 'dict', 'children': {
                    'legacy': {'type': 'dict'}}}}}}}
        },
        'tweet': {'legacy': {'type': 'dict'}},
        'source': {'source': {'type': 'str'}}
    }
}
NODES_TWEET_RESULT_BY_ID = {
    'entry': {'tweetResult': {'type': 'dict', 'children': {
        'result': {'type': 'dict'}}}
    },
    'objects': {
        'user': {'core': {'type': 'dict', 'children': {
            'user_results': {'type': 'dict', 'children': {
                'result': {'type': 'dict'}}}}}
        },
        'user_info': {'core': {'type': 'dict', 'children': {
            'user_results': {'type': 'dict', 'children': {
                'result': {'type': 'dict', 'children': {
                    'legacy': {'type': 'dict'}}}}}}}
        },
        'tweet': {'legacy': {'type': 'dict'}},
        'source': {'source': {'type': 'str'}}
    }
}
NODES_FOLLOWING = {
    'entry': {'user': {'type': 'dict', 'children': {
        'result': {'type': 'dict', 'children': {
            'timeline': {'type': 'dict', 'children': {
                'timeline': {'type': 'dict', 'children': {
                    'instructions': {'type': 'list', 'children': {
                        'entries': {'type': 'list', 'children': {
                            'content': {'type': 'dict', 'children': {
                                'itemContent': {'type': 'dict', 'children': {
                                    'user_results': {'type': 'dict', 'children': {
                                        'result': {'type': 'dict'}}}}}}}}}}}}}}}}}}}
    },
    'objects': {
        'user': {'rest_id': {'type': 'str'}},
        'verified': {'is_blue_verified': {'type': 'bool'}},
        'user_info': {'legacy': {'type': 'dict'}}
    }
}
NODES_USER_BY_SCREEN_NAME = {
    'entry': {'user': {'type': 'dict', 'children': {
        'result': {'type': 'dict'}}}
    },
    'objects': {
        'user': {'rest_id': {'type': 'str'}},
        'verified': {'is_blue_verified': {'type': 'bool'}},
        'user_info': {'legacy': {'type': 'dict'}}
    }
}
NODES_LIST_MEMBERS = {
    'entry': {'list': {'type': 'dict', 'children': {
        'members_timeline': {'type': 'dict', 'children': {
            'timeline': {'type': 'dict', 'children': {
                'instructions': {'type': 'list', 'children': {
                    'entries': {'type': 'list', 'children': {
                        'content': {'type': 'dict', 'children': {
                            'itemContent': {'type': 'dict', 'children': {
                                'user_results': {'type': 'dict', 'children': {
                                    'result': {'type': 'dict'}}}}}}}}}}}}}}}}}
    },
    'objects': {
        'user': {'rest_id': {'type': 'str'}},
        'verified': {'is_blue_verified': {'type': 'bool'}},
        'user_info': {'legacy': {'type': 'dict'}}
    }
}
NODES_USER_BY_REST_ID = {
    'entry': {'user': {'type': 'dict', 'children': {
        'result': {'type': 'dict'}}}
    },
    'objects': {
        'user': {'rest_id': {'type': 'str'}},
        'verified': {'is_blue_verified': {'type': 'bool'}},
        'user_info': {'legacy': {'type': 'dict'}}
    }
}
NODES_USERS_BY_REST_IDS = {
    'entry': {'users': {'type': 'list', 'children': {
        'result': {'type': 'dict'}}}
    },
    'objects': {
        'user': {'rest_id': {'type': 'str'}},
        'verified': {'is_blue_verified': {'type': 'bool'}},
        'user_info': {'legacy': {'type': 'dict'}}
    }
}