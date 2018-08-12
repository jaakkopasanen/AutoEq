# Bose QuietComfort 20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 -0.2; 22 -1.6; 23 -2.1; 25 -3.0; 26 -3.4; 28 -4.0; 30 -4.3; 32 -4.5; 35 -4.6; 37 -4.6; 40 -4.6; 42 -4.5; 45 -4.4; 49 -4.3; 52 -4.2; 56 -4.2; 59 -4.2; 64 -4.3; 68 -4.4; 73 -4.6; 78 -4.8; 83 -5.1; 89 -5.4; 95 -5.7; 102 -5.9; 109 -6.0; 117 -6.0; 125 -5.9; 134 -5.7; 143 -5.5; 153 -5.3; 164 -5.1; 175 -5.0; 188 -5.0; 201 -5.0; 215 -5.0; 230 -5.0; 246 -5.0; 263 -5.0; 282 -5.0; 301 -5.0; 323 -4.8; 345 -4.7; 369 -4.7; 395 -4.8; 423 -4.9; 452 -4.9; 484 -4.7; 518 -4.1; 554 -3.3; 593 -2.3; 635 -1.5; 679 -1.0; 726 -0.6; 777 -0.0; 832 0.6; 890 0.8; 952 0.5; 1019 -0.2; 1090 -1.0; 1167 -1.7; 1248 -2.3; 1336 -2.6; 1429 -3.3; 1529 -5.3; 1636 -6.8; 1751 -7.5; 1873 -7.0; 2004 -5.8; 2145 -4.4; 2295 -3.5; 2455 -3.0; 2627 -2.4; 2811 -2.0; 3008 -1.7; 3219 -1.7; 3444 -2.1; 3685 -2.9; 3943 -3.9; 4219 -4.4; 4514 -3.4; 4830 -1.3; 5168 1.5; 5530 3.7; 5917 4.7; 6331 4.2; 6775 1.1; 7249 -3.5; 7756 -4.1; 8299 -2.1; 8880 -0.3; 9502 -1.0; 10167 -2.2; 10879 -0.4; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -2.1; 15258 -7.9; 16326 -10.9; 17469 -11.1; 18692 -9.9; 20000 -8.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 1.35 | -3.4 dB  |
| Peaking | 126 Hz   | 0.53 | -5.6 dB  |
| Peaking | 402 Hz   | 1.75 | -3.4 dB  |
| Peaking | 1819 Hz  | 2.26 | -7.4 dB  |
| Peaking | 17820 Hz | 1.35 | -12.5 dB |
| Peaking | 880 Hz   | 3.99 | 2.4 dB   |
| Peaking | 4268 Hz  | 2.95 | -5.5 dB  |
| Peaking | 6012 Hz  | 2.43 | 7.6 dB   |
| Peaking | 7431 Hz  | 4.6  | -6.8 dB  |
| Peaking | 13087 Hz | 4.58 | 3.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)