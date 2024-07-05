_base_ = 'trainshipv8.py'
model = dict(
    backbone=dict(
        plugins=[
            dict(
                cfg=dict(
                    type='NonLocal2d'),
                stages=(False, True, True, True))
        ]))
