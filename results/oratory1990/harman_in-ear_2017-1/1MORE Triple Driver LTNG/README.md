# 1MORE Triple Driver LTNG

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.9; 22 -1.3; 23 -1.4; 25 -1.8; 26 -1.9; 28 -2.2; 30 -2.4; 32 -2.6; 35 -2.9; 37 -3.0; 40 -3.2; 42 -3.3; 45 -3.5; 49 -3.7; 52 -3.9; 56 -4.1; 59 -4.3; 64 -4.5; 68 -4.7; 73 -4.9; 78 -5.1; 83 -5.3; 89 -5.5; 95 -5.7; 102 -5.9; 109 -6.0; 117 -6.1; 125 -6.2; 134 -6.3; 143 -6.3; 153 -6.2; 164 -6.2; 175 -6.0; 188 -5.9; 201 -5.7; 215 -5.5; 230 -5.3; 246 -5.1; 263 -4.8; 282 -4.5; 301 -4.2; 323 -3.8; 345 -3.3; 369 -3.0; 395 -2.8; 423 -2.5; 452 -2.1; 484 -1.8; 518 -1.5; 554 -1.1; 593 -0.8; 635 -0.5; 679 -0.3; 726 0.0; 777 0.2; 832 0.3; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -0.7; 1336 -0.7; 1429 -0.7; 1529 -0.8; 1636 -0.9; 1751 -1.0; 1873 -1.2; 2004 -1.4; 2145 -1.5; 2295 -1.7; 2455 -1.7; 2627 -1.4; 2811 -0.7; 3008 -0.2; 3219 0.1; 3444 -0.2; 3685 -1.0; 3943 -2.5; 4219 -3.9; 4514 -3.7; 4830 -1.0; 5168 3.2; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 -0.2; 10879 -1.6; 11640 -3.5; 12455 -7.1; 13327 -13.1; 14260 -20.4; 15258 -26.6; 16326 -29.7; 17469 -26.8; 18692 -12.9; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver LTNG ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 78 Hz    | 0.42 | -3.7 dB  |
| Peaking | 190 Hz   | 0.66 | -3.9 dB  |
| Peaking | 4255 Hz  | 4.35 | -6.7 dB  |
| Peaking | 7483 Hz  | 0.79 | 9.3 dB   |
| Peaking | 16190 Hz | 1.46 | -34.1 dB |
| Peaking | 2263 Hz  | 2.02 | -2.2 dB  |
| Peaking | 5842 Hz  | 4.43 | 4.1 dB   |
| Peaking | 7857 Hz  | 2.96 | -4.3 dB  |
| Peaking | 11663 Hz | 1.69 | 5.2 dB   |
| Peaking | 14445 Hz | 2.64 | -6.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/1MORE%20Triple%20Driver%20LTNG/1MORE%20Triple%20Driver%20LTNG.png)