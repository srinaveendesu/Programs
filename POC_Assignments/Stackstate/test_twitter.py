from datadog_checks.twitter import TwitterCheck

def test_check(aggregator, instance):
    instance = {}
    c = TwitterCheck('twitter', {}, [instance])
    c.check(instance)

    aggregator.assert_all_metrics_covered()

def test_message( instance):
    instance = {'test':'twitter_metrics','client_key': 'xxxxxxx',
                'client_secret': 'xxxxxxx',
                'access_key': "xxxxxx",
                'access_secret': "xxxxxx",
                'screen_name': '@gostackstate'}
    c = TwitterCheck('twitter', {}, [instance])
    c.check(instance)

def test_event( instance):
    instance = {'test':'twitter_events','client_key': 'xxxxxx',
                'client_secret': 'xxxxxx',
                'access_key': "xxxxxx",
                'access_secret': "xxxxx",
                'screen_name': 'srinaveen_desu'}
    c = TwitterCheck('twitter', {}, [instance])
    c.check(instance)