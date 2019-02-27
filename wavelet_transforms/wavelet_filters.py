import pywt
import numpy as np
import gplot as gp
import matplotlib.pyplot as plt


data = [3.3529,3.3543,3.3557,3.357,3.359,3.3611,3.3642,3.3655,3.3661,3.3664,3.3665,3.3658,3.365,3.364,3.3621,3.362,3.361,3.3605,3.3615,3.3611,3.3624,3.3595,3.3571,3.3527,3.3489,3.346,3.3432,3.3402,3.3383,3.3376,3.3362,3.3346,3.3335,3.331,3.3284,3.3269,3.3244,3.3216,3.3202,3.3172,3.3153,3.3134,3.3132,3.31,3.3113,3.3107,3.3077,3.3051,3.3015,3.2986,3.2953,3.2928,3.2903,3.2891,3.2891,3.2872,3.2865,3.2854,3.2831,3.2822,3.2817,3.2803,3.2797,3.2789,3.2776,3.2777,3.2772,3.2769,3.2767,3.2774,3.2785,3.279,3.2756,3.2737,3.2718,3.2696,3.2682,3.2675,3.2678,3.2685,3.2685,3.2681,3.2682,3.2673,3.268,3.2673,3.2667,3.2667,3.2664,3.266,3.2673,3.2675,3.2674,3.2693,3.2707,3.2714,3.2702,3.2671,3.2663,3.2646,3.2638,3.2632,3.2642,3.2645,3.2662,3.2668,3.2678,3.2691,3.2694,3.2719,3.2732,3.275,3.2776,3.2799,3.2823,3.2854,3.2898,3.294,3.298,3.3036,3.3061,3.309,3.31,3.3106,3.3137,3.3153,3.3184,3.3218,3.3263,3.3303,3.3336,3.3377,3.3408,3.3437,3.3473,3.3507,3.3539,3.3573,3.3598,3.3642,3.3676,3.3715,3.3769,3.3813,3.3864,3.3875,3.3891,3.3895,3.3894,3.3929,3.3942,3.3937,3.3969,3.3974,3.3995,3.4038,3.4039,3.4067,3.4089,3.4075,3.411,3.4101,3.4129,3.4154,3.4142,3.4182,3.4175,3.4183,3.4203,3.4178,3.4133,3.4113,3.4094,3.4095,3.4056,3.4052,3.4024,3.4019,3.4029,3.3988,3.3967,3.396,3.3916,3.3909,3.3884,3.386,3.383,3.3803,3.3799,3.3784,3.3753,3.3765,3.3729,3.3704,3.3659,3.3618,3.3573,3.3548,3.3505,3.3473,3.3467,3.3452,3.3444,3.3431,3.34,3.3381,3.3358,3.3331,3.3315,3.3292,3.3274,3.3254,3.3235,3.3227,3.3205,3.3198,3.32,3.3188,3.3172,3.3138,3.3096,3.3063,3.3032,3.3008,3.3002,3.3007,3.2999,3.2995,3.3,3.2977,3.2981,3.2948,3.2944,3.2944,3.2925,3.2918,3.2921,3.2898,3.2909,3.2904,3.2903,3.2931,3.2929,3.2948,3.2934,3.2893,3.289,3.2859,3.2861,3.2849,3.2856,3.2865,3.2882,3.2874,3.2879,3.2877,3.2873,3.2873,3.285,3.2865,3.2849,3.2856,3.2847,3.2842,3.2841,3.2845,3.2844,3.285,3.2871,3.287,3.2854,3.2818,3.2788,3.277,3.2744,3.2729,3.2725,3.2724,3.2744,3.274,3.2737,3.2743,3.2737,3.274,3.2735,3.2738,3.2746,3.2751,3.2752,3.2755,3.277,3.2793,3.281,3.2826,3.2866,3.2906,3.2918,3.293,3.2933,3.2941,3.2964,3.2977,3.3009,3.3028,3.3083,3.3113,3.3141,3.3178,3.3216,3.3247,3.329,3.3317,3.3349,3.3386,3.3414,3.3446,3.3476,3.3526,3.3572,3.3611,3.3677,3.3709,3.3717,3.3718,3.3731,3.3734,3.3776,3.3779,3.3815,3.3833,3.3863,3.3912,3.3911,3.3955,3.396,3.397,3.3992,3.4013,3.4053,3.4056,3.4071,3.4105,3.4125,3.4146,3.418,3.4176,3.4152,3.4119,3.41,3.4089,3.4072,3.4062,3.4051,3.4059,3.4065,3.4059,3.4056,3.4041,3.4031,3.4018,3.402,3.399,3.3991,3.397,3.3953,3.3951,3.3946,3.3948,3.3943,3.3902,3.3858,3.3814,3.3797,3.3745,3.3731,3.3699,3.3707,3.37,3.3668,3.3676,3.3639,3.3632,3.3612,3.3596,3.357,3.3539,3.3536,3.3522,3.3508,3.3492,3.349,3.3481,3.3467,3.3427,3.3397,3.3353,3.3307,3.3279,3.3261,3.3253,3.3243,3.3236,3.3222,3.3199,3.3185,3.3163,3.3151,3.313,3.3114,3.3104,3.3088,3.3075,3.3082,3.3055,3.3064,3.3053,3.3048,3.3018,3.2988,3.2955,3.2923,3.2891,3.2885,3.2881,3.2877,3.2877,3.2867,3.2863,3.2852,3.2845,3.2841,3.2832,3.2826,3.2826,3.2821,3.282,3.2818,3.2818,3.2825,3.2842,3.2845,3.2826,3.2801,3.2779,3.2761,3.275,3.2743,3.2751,3.2761,3.277,3.278,3.2778,3.2789,3.2785,3.28,3.2801,3.2795,3.2802,3.2806,3.2809,3.2807,3.2822,3.2835,3.2848,3.2879,3.2897,3.2906,3.2894,3.2894,3.2889,3.2893,3.2904,3.2917,3.2954,3.2983,3.3,3.3039,3.3053,3.3082,3.311,3.3141,3.3169,3.3201,3.3226,3.3262,3.3286,3.3329,3.3377,3.3423,3.3479,3.3531,3.3563,3.3566,3.3581,3.3594,3.3621,3.3646,3.3663,3.3695,3.3725,3.377,3.38,3.3823,3.3832,3.3874,3.388,3.3923,3.3929,3.3963,3.3983,3.403,3.4045,3.4081,3.4123,3.4162,3.4179,3.4141,3.4153,3.415,3.4149,3.4147,3.4149,3.4156,3.4176,3.4181,3.4184,3.4173,3.4163,3.4159,3.4159,3.413,3.4141,3.4115,3.4124,3.4104,3.4109,3.4101,3.4084,3.404,3.3982,3.3958,3.3901,3.3884,3.3829,3.3826,3.3817,3.3796,3.3772,3.3767,3.3745,3.372,3.3695,3.3668,3.3645,3.362,3.3602,3.359,3.3567,3.3563,3.3547,3.3549,3.352,3.3479,3.3439,3.3397,3.3367,3.3331,3.332,3.3306,3.3306,3.3287,3.3279,3.3259,3.3236,3.3222,3.32,3.3182,3.3166,3.3154,3.3144,3.3138,3.3117,3.3115,3.3112,3.3098,3.3069,3.3028,3.2999,3.2986,3.2938,3.2946,3.292,3.2932,3.2912,3.291,3.2886,3.2893,3.2878,3.2872,3.2858,3.2845,3.2835,3.2817,3.2827,3.2828,3.281,3.2821,3.2833,3.2833,3.2802,3.2782,3.2746,3.2734,3.2714,3.2708,3.2706,3.2713,3.2726,3.2721,3.2723,3.2714,3.2717,3.2712,3.2716,3.2715,3.2722,3.2722,3.2727,3.2726,3.2747,3.2756,3.2771,3.2792,3.2831,3.2854,3.2849,3.2861,3.2867,3.288,3.2896,3.2896,3.2937,3.2961,3.3019,3.3034,3.3068,3.3103,3.3136,3.3178,3.3212,3.3251,3.3279,3.3322,3.3345,3.3388,3.3423,3.3467,3.3512,3.3565,3.3614,3.3672,3.3684,3.3687,3.3701,3.3718,3.3744,3.3754,3.3763,3.3809,3.3853,3.3887,3.39,3.3944,3.3944,3.3991,3.3992,3.4036,3.4033,3.4073,3.4072,3.4117,3.412,3.417,3.4172,3.4206,3.4221,3.422,3.4181,3.4193,3.4177,3.4182,3.4158,3.4161,3.4145,3.4155,3.4137,3.4142,3.4114,3.4109,3.4098,3.4077,3.4058,3.4032,3.4009,3.3999,3.3972,3.3942,3.3942,3.3918,3.3924,3.3884,3.3823,3.3777,3.3737,3.3693,3.3655,3.3624,3.3613,3.3596,3.3581,3.3562,3.3542,3.3518,3.3491,3.3476,3.3444,3.3433,3.3404,3.3383,3.3359,3.3343,3.3327,3.3305,3.3296,3.3289,3.3272,3.3243,3.32,3.3162,3.312,3.3087,3.3065,3.3044,3.304,3.3021,3.3014,3.2992,3.2983,3.2954,3.2942,3.2922,3.291,3.2913,3.2895,3.2883,3.2864,3.2865,3.2855,3.2855,3.2846,3.285,3.2854,3.2841,3.2812,3.2772,3.2756,3.2726,3.2707,3.2695,3.269,3.2695,3.2693,3.2691,3.2693,3.2686,3.2682,3.2684,3.268,3.2682,3.2678,3.2678,3.2671,3.2674,3.2676,3.2677,3.2682,3.2676,3.2699,3.2715,3.2724,3.2701,3.2681,3.2662,3.2657,3.2685,3.2648,3.2643,3.2661,3.2669,3.2675,3.2682,3.2691,3.2703,3.2701,3.2723,3.2732,3.2758,3.2764,3.2784,3.2793,3.2829,3.2847,3.2891,3.2921,3.2968,3.3015,3.3045,3.3066,3.3055,3.3073,3.3091,3.3114,3.313,3.3169,3.3209,3.3255,3.3293,3.3328,3.3363,3.3399,3.3438,3.3475,3.3512,3.3549,3.3582,3.3614,3.3652,3.369,3.3743,3.3781,3.3817,3.3889,3.3892,3.3912,3.3884,3.3926,3.3919,3.3956,3.3952,3.3994,3.3998,3.405,3.4062,3.4087,3.4106,3.4126,3.4146,3.4162,3.4179,3.4199,3.421,3.4243,3.4258,3.429,3.4312,3.4337,3.4341,3.4313,3.4297,3.4287,3.4281,3.4262,3.4243,3.423,3.422,3.4205,3.4191,3.4159,3.4145,3.4134,3.4089,3.4083,3.4034,3.4029,3.3984,3.3985,3.3971,3.3949,3.3944,3.3913,3.389,3.3819,3.379,3.3747,3.3711,3.367,3.3648,3.363,3.3621,3.3615,3.3592,3.3563,3.3552,3.3523,3.3504,3.3483,3.3463,3.345,3.3437,3.3424,3.3413,3.3403,3.3394,3.3396,3.3371,3.3343,3.3304,3.3266,3.3235,3.3204,3.3184,3.3178,3.318,3.3171,3.3153,3.3137,3.312,3.3106,3.3093,3.3075,3.307,3.3056,3.3047,3.3037,3.3026,3.302,3.3009,3.302,3.3017,3.3019,3.2989,3.2959,3.2944,3.2903,3.2901,3.2877,3.2862,3.2884,3.2863,3.2873,3.2851,3.2862,3.2835,3.2848,3.2828,3.2834,3.2832,3.2817,3.2816,3.2813,3.2807,3.2817,3.2806,3.2817,3.283,3.2832,3.2808,3.2783,3.2759,3.2778,3.2724,3.2704,3.2712,3.2716,3.2721,3.272,3.2725,3.2724,3.2719,3.2717,3.2717,3.2731,3.2725,3.2735,3.2735,3.2749,3.2755,3.278,3.2806,3.2828,3.2874,3.2917,3.2954,3.2963,3.2971,3.2994,3.3013,3.3025,3.3051,3.3103,3.314,3.3186,3.3232,3.327,3.3305,3.3339,3.338,3.3412,3.3452,3.3482,3.3513,3.3549,3.3585,3.3624,3.3676,3.3734,3.3781,3.3836,3.3868,3.3865,3.3878,3.3894,3.3914,3.3945,3.3945,3.3992,3.4007,3.4076,3.4078,3.4128,3.4149,3.416,3.4202,3.4207,3.4248,3.4244,3.4289,3.4283,3.4302,3.4321,3.4336,3.4353,3.4328,3.4286,3.4239,3.4204,3.4191,3.4145,3.414,3.4087,3.4099,3.4072,3.4074,3.405,3.4012,3.4005,3.3978,3.3962,3.3928,3.3911,3.3887,3.3875,3.3858,3.3828,3.3828,3.3825,3.3806,3.376,3.3714,3.3664,3.3619,3.3575,3.3538,3.3518,3.3498,3.3496,3.3473,3.3454,3.3432,3.3405,3.3389,3.3359,3.3332,3.3318,3.3303,3.3285,3.3272,3.3253,3.3246,3.3235,3.3227,3.3193,3.3152,3.3116,3.308,3.3053,3.3025,3.3014,3.3015,3.301,3.3008,3.2985,3.2977,3.296,3.2957,3.2938,3.2925,3.2919,3.2912,3.2915,3.2916,3.2907,3.2915,3.2933,3.2942,3.2923,3.291,3.2903,3.2881,3.2868,3.2873,3.2877,3.2881,3.2888,3.2892,3.2892,3.2895,3.2892,3.2887,3.2899,3.2891,3.2892,3.2894,3.29,3.2907,3.2918,3.2935,3.2933,3.291,3.2892,3.2853,3.2828,3.2806,3.2797,3.2795,3.2852,3.2791,3.2792,3.2768,3.2752,3.2752,3.2731,3.2726,3.2713,3.27,3.2738,3.2682,3.269,3.2699,3.2699,3.2717,3.2654,3.2682,3.2619,3.2616,3.266,3.2635,3.2653,3.2667,3.2685,3.2695,3.2707,3.2733,3.2738,3.2777,3.2785,3.2819,3.2846,3.2881,3.2914,3.2965,3.3003,3.3021,3.3024,3.3038,3.3062,3.3088,3.3109,3.315,3.3201,3.3241,3.3276,3.3305,3.3338,3.3379,3.341,3.3445,3.348,3.3514,3.3564,3.3621,3.366,3.3723,3.3763,3.3778,3.3771,3.3789,3.3809,3.3832,3.3857,3.3878,3.3924,3.3948,3.3987,3.4009,3.4031,3.4054,3.4077,3.41,3.413,3.4159,3.4192,3.4225,3.4261,3.4302,3.4318,3.4304,3.4289,3.4298,3.4297,3.4294,3.4296,3.4299,3.431,3.432,3.4315,3.4301,3.4301,3.4287,3.4276,3.4265,3.4251,3.4254,3.4259,3.426,3.4266,3.4264,3.4232,3.417,3.4132,3.4102,3.4059,3.4027,3.3994,3.3988,3.3984,3.3968,3.3955,3.3925,3.3906,3.3882,3.3855,3.3832,3.3813,3.3795,3.3775,3.3758,3.3749,3.3743,3.3729,3.3701,3.3655,3.3607,3.3568,3.3527,3.3498,3.3484,3.3473,3.346,3.345,3.343,3.3411,3.3391,3.3367,3.3344,3.3325,3.3303,3.329,3.3267,3.3263,3.3236,3.3227,3.3215,3.3209,3.3188,3.3151,3.3112,3.3069,3.3045,3.3036,3.3032,3.3024,3.3013,3.3004,3.2993,3.2983,3.297,3.2962,3.2944,3.2936,3.2927,3.2919,3.2917,3.2904,3.2908,3.2911,3.2899,3.2909,3.292,3.294,3.2913,3.288,3.287,3.2834,3.284,3.2835,3.2824,3.2848,3.2836,3.2832,3.2851,3.2833,3.2858,3.2848,3.2837,3.2854,3.2837,3.2849,3.2851,3.2835,3.2858,3.286,3.2852,3.2875,3.2886,3.2908,3.2905,3.2882,3.288,3.2861,3.2839,3.2845,3.2857,3.2864,3.2879,3.2873,3.29,3.2917,3.2916,3.2942,3.2949,3.2968,3.3001,3.3017,3.3032,3.3052,3.3084,3.3108,3.314,3.3185,3.3217,3.3272,3.3312,3.3338,3.3346,3.3356,3.337,3.3395,3.3418,3.3445,3.3484,3.352,3.3562,3.3601,3.3638,3.3677,3.371,3.3743,3.3773,3.3809,3.3844,3.3875,3.3902,3.3945,3.3979,3.4028,3.4073,3.4124,3.4133,3.4164,3.4147,3.4132,3.4173,3.4185,3.4186,3.4224,3.4234,3.4282,3.4305,3.4305,3.4351,3.4332,3.4348,3.4376,3.4348,3.4377,3.4374,3.4354,3.4378,3.4375,3.4366,3.4388,3.4363,3.433,3.4291,3.4223,3.4212,3.4167,3.4111,3.4106,3.4091,3.4073,3.4077,3.4059,3.4036,3.4008,3.3982,3.3963,3.394,3.3923,3.3895,3.3879,3.3862,3.3838,3.3819,3.3811,3.3798,3.3781,3.3755,3.3698,3.3657,3.3616,3.3579,3.3549,3.3534,3.3528,3.3527,3.3511,3.3493,3.3482,3.3457,3.3445,3.3424,3.3401,3.3391,3.3373,3.3354,3.3344,3.333,3.3314,3.3312,3.3305,3.329,3.3258,3.3222,3.3182,3.3153,3.3129,3.3117,3.312,3.3115,3.3107,3.3105,3.3094,3.3081,3.307,3.3062,3.3058,3.3045,3.3034,3.3029,3.3029,3.3024,3.3023,3.3026,3.3043,3.3035,3.302,3.3049,3.2954,3.2934,3.2974,3.2883,3.2896,3.2953,3.2889,3.2911,3.2902,3.2886,3.2896,3.2897,3.2875,3.288,3.2886,3.2861,3.2869,3.286,3.2867,3.2867,3.2866,3.2882,3.2894,3.2899,3.2879,3.2899,3.2832,3.2816,3.285,3.2805,3.2813,3.2876,3.2841,3.2871,3.2877,3.2888,3.2931,3.2948,3.2967,3.3012,3.3017,3.3048,3.3079,3.3109,3.3151,3.3197,3.3239,3.3294,3.3346,3.3367,3.3372,3.3387,3.3408,3.3436,3.3458,3.3483,3.352,3.3561,3.3594,3.3631,3.3663,3.3689,3.3723,3.3756,3.3785,3.3816,3.3846,3.3871,3.3899,3.3937,3.3978,3.4022,3.4072,3.4094,3.4083,3.4072,3.4077,3.4081,3.4066,3.4099,3.4105,3.4103,3.4143,3.4152,3.4141,3.4158,3.4153,3.4137,3.4154,3.4145,3.413,3.4157,3.4162,3.415,3.418,3.4193,3.4179,3.4179,3.4129,3.4078,3.4043,3.3997,3.3958,3.3931,3.3912,3.3903,3.3897,3.3873,3.385,3.3821,3.3795,3.3777,3.3757,3.3734,3.371,3.3694,3.3667,3.3651,3.3637,3.3623,3.3619,3.3615,3.3577,3.3527,3.3482,3.3453,3.3411,3.3374,3.3363,3.3344,3.3333,3.3323,3.33,3.3281,3.3259,3.3242,3.3219,3.3207,3.319,3.3171,3.315,3.3139,3.3126,3.3112,3.3104,3.3103,3.3104,3.3087,3.3061,3.3037,3.2984,3.2959,3.2943,3.292,3.2899,3.2896,3.2902,3.2886,3.2885,3.289,3.2882,3.2871,3.2883,3.2876,3.2863,3.2882,3.2871,3.2872,3.2868,3.2884,3.2897,3.2886,3.2922,3.2941,3.2951,3.2943,3.2956,3.294,3.2954,3.2975,3.2978,3.3009,3.3044,3.3085,3.312,3.3153,3.3188,3.3225,3.3262,3.3297,3.333,3.3369,3.3401,3.3435,3.3462,3.35,3.3537,3.3584,3.3628,3.3673,3.372,3.3757,3.3761,3.3763,3.3776,3.3804,3.3815,3.3825,3.3848,3.3873,3.3909,3.3928,3.3957,3.3972,3.3988,3.4008,3.4022,3.4022,3.4023,3.4026,3.4017,3.4016,3.4019,3.4023,3.4019,3.403,3.4047,3.402,3.3975,3.3935,3.3898,3.387,3.3839,3.381,3.379,3.3785,3.3774,3.376,3.3739,3.3716,3.3697,3.3672,3.3652,3.3636,3.3616,3.3594,3.3574,3.3556,3.354,3.3533,3.3512,3.3512,3.3498,3.3478,3.3442,3.3389,3.3353,3.3321,3.3289,3.3263,3.3257,3.3256,3.3251,3.3228,3.3217,3.3206,3.3183,3.3173,3.3158,3.3144,3.3125,3.3112,3.3098,3.309,3.3086,3.3071,3.3066,3.3069,3.3068,3.3051,3.3021,3.3036,3.2961,3.293,3.2917,3.2952,3.2903,3.2907,3.2895,3.2892,3.2889,3.2891,3.2869,3.2859,3.2853,3.2855,3.2842,3.283]


# Variables you can tweek
N = len(data)
wavelet = 'db3'
levels = 4

print('Length (N): ',N)
coefs = pywt.wavedec(data,wavelet,mode='symmetric', level=levels)

print("wavelet Coefficients")
print(coefs)
dwt_coef_1D, slices3 = pywt.coeffs_to_array(coefs, padding=0, axes=None)

# Remove the highest scale vector A4, and reconstuct
rm_level = 0
zeros = np.zeros(len(coefs[rm_level]))
coefs[rm_level] = zeros

rm_level = 1
zeros = np.zeros(len(coefs[rm_level]))
coefs[rm_level] = zeros

# reconstruct the array
data_filt = pywt.waverec(coefs,wavelet,mode='symmetric')

plt.subplot(311)
plt.title('MLDWT Filter on Raw Data\nwith Breath and Cardiac Signals')
plt.ylabel('Original Data')
plt.grid(True)
plt.plot(data)
plt.subplot(312)
plt.ylabel('Multi-Level DWT')
plt.grid(True)
plt.plot(dwt_coef_1D)
plt.subplot(313)
plt.ylabel('Filterd Data')
plt.grid(True)
plt.plot(data_filt)
plt.xlabel('Sample #')
plt.savefig('mldwt_filter_HRandBR.png',dpi=300)
plt.show()