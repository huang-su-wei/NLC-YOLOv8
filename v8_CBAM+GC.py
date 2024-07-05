_base_ = 'trainshipv8.py'
model = dict(
    backbone=dict(
        plugins=[
            dict(
                cfg=dict(
                    type='CBAM'),
                stages=(False, False, False, True)),
            dict(
                cfg=dict(
                    type='ContextBlock',
                    ratio=1),
                stages=(False, False, False, True)
                )
        ]))
