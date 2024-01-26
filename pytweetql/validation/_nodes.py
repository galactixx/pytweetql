nodes_list_create = {
    'entry': {'list': {'type': 'dict'}},
    'objects': {
        'description': {'description': {'type': 'str'}},
        'is_following': {'following': {'type': 'bool'}},
        'list_id': {'id_str': {'type': 'str'}},
        'member_count': {'member_count': {'type': 'int'}},
        'mode': {'mode': {'type': 'str'}},
    }
}
nodes_user_tweets = {
    'entry': {'user': {'type': 'dict', 'children': {
        'result': {'type': 'dict', 'children': {
            'timeline_v2': {'type': 'dict', 'children': {
                'timeline': {'type': 'dict', 'children': {
                    'instructions': {'type': 'list', 'children': {
                        'entries': {'type': 'list', 'children': {
                            'content': {'type': 'dict', 'children': {
                                'itemContent': {'type': 'dict', 'children': {
                                    'tweet_results': {'type': 'dict', 'children': {
                                        'result': {'type': 'dict'}}}}}}}}}}}}}}}}}}}
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
nodes_tweet_result_by_id = {
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
nodes_user_by_screen_name = {
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
        'user_info': {'legacy': {'type': 'dict'}}
    }
}
nodes_list_members = {
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
        'user_info': {'legacy': {'type': 'dict'}}
    }
}
nodes_user_by_rest_id = {
    'entry': {'user': {'type': 'dict', 'children': {
        'result': {'type': 'dict'}}}
    },
    'objects': {
        'user': {'rest_id': {'type': 'str'}},
        'user_info': {'legacy': {'type': 'dict'}}
    }
}
nodes_users_by_rest_ids = {
    'entry': {'users': {'type': 'list', 'children': {
        'result': {'type': 'dict'}}}
    },
    'objects': {
        'user': {'rest_id': {'type': 'str'}},
        'user_info': {'legacy': {'type': 'dict'}}
    }
}