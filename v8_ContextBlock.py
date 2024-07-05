_base_ = 'trainshipv8.py'
model = dict(
    backbone=dict(
        plugins=[
            dict(
                cfg=dict(
                    type='ContextBlock',
                    ratio=0.5),
                stages=(False, False, False, True))
        ]))
