_base_ = 'trainshipv8.py'
model = dict(
    backbone=dict(
        plugins=[
            dict(
                cfg=dict(
                    type='CBAM',
                    kernel_size=7),
                stages=(False, False, False, True)),
            dict(
                cfg=dict(
                    type='NonLocal2d'),
                stages=(False, True, True, False)
                )
        ]))
