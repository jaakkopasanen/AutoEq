# Beats Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 10 -84; 20 -0.4; 22 -1.4; 23 -1.9; 25 -2.7; 26 -3.1; 28 -3.8; 30 -4.4; 32 -4.9; 35 -5.5; 37 -5.8; 40 -6.2; 42 -6.4; 45 -6.6; 49 -6.8; 52 -6.8; 56 -6.9; 59 -6.9; 64 -6.8; 68 -6.7; 73 -6.7; 78 -6.8; 83 -7.0; 89 -7.3; 95 -7.6; 102 -7.9; 109 -8.1; 117 -7.9; 125 -8.0; 134 -8.3; 143 -8.5; 153 -8.6; 164 -8.5; 175 -8.5; 188 -8.4; 201 -8.2; 215 -7.9; 230 -7.4; 246 -6.9; 263 -6.6; 282 -5.6; 301 -4.7; 323 -4.2; 345 -3.6; 369 -2.9; 395 -2.3; 423 -2.0; 452 -1.9; 484 -1.9; 518 -2.0; 554 -2.1; 593 -2.0; 635 -2.0; 679 -1.6; 726 -1.4; 777 -1.4; 832 -1.3; 890 -0.7; 952 0.0; 1019 -0.1; 1090 -0.2; 1167 0.2; 1248 0.5; 1336 0.8; 1429 0.8; 1529 0.4; 1636 -0.2; 1751 -1.0; 1873 -2.0; 2004 -3.2; 2145 -4.6; 2295 -6.1; 2455 -7.5; 2627 -8.9; 2811 -9.9; 3008 -9.7; 3219 -8.2; 3444 -5.9; 3685 -3.1; 3943 -0.4; 4219 -0.4; 4514 -2.6; 4830 -3.7; 5168 -1.9; 5530 -0.2; 5917 -0.7; 6331 -3.9; 6775 -5.0; 7249 -5.7; 7756 -5.5; 8299 -3.5; 8880 -0.7; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.9; 13327 -2.1; 14260 -2.6; 15258 -2.6; 16326 -1.9; 17469 -0.5; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.9371702658951439dB` and instead set Global volume in the UI for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 54 Hz    | 0.57 | -5.7 dB  |
| Peaking | 180 Hz   | 0.79 | -7.2 dB  |
| Peaking | 2819 Hz  | 2.69 | -10.7 dB |
| Peaking | 7320 Hz  | 3.78 | -6.0 dB  |
| Peaking | 24000 Hz | 2.1  | -1.1 dB  |
| Peaking | 1406 Hz  | 1.79 | 3.2 dB   |
| Peaking | 1788 Hz  | 0.55 | -1.4 dB  |
| Peaking | 3965 Hz  | 9.8  | 3.5 dB   |
| Peaking | 10352 Hz | 2.2  | 1.4 dB   |
| Peaking | 14694 Hz | 1.92 | -3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beats%20Pro/Beats%20Pro.png)