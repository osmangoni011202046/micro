#!/usr/bin/env python
# encoding: utf-8

def build(bld):
    vehicle = bld.path.name
    bld.ap_stlib(
        name=vehicle + '_libs',
        ap_vehicle=vehicle,
        ap_libraries=bld.ap_common_vehicle_libraries() + [
            'APM_Control',
            'AP_AdvancedFailsafe',
            'AP_Avoidance',
            'AP_Arming',
            'AP_Camera',
            'AP_L1_Control',
            'AP_Navigation',
            'AP_RCMapper',
            'AP_TECS',
            'AP_InertialNav',
            'AC_WPNav',
            'AC_AttitudeControl',
            'AP_Motors',
            'AP_Landing',
            'AP_Beacon',
            'PID',
            'AP_Soaring',
            'AP_LTM_Telem',
            'AP_Devo_Telem',
            'AP_OSD',
            'AC_AutoTune',
            'AP_Follow',
        ],
    )

    bld.ap_program(
        program_name='arduplane',
        program_groups=['bin', 'plane'],
        use=vehicle + '_libs',
    )
