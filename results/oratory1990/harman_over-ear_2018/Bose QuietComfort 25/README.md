# Bose QuietComfort 25

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.5; 22 2.4; 23 1.9; 25 1.0; 26 0.6; 28 -0.1; 30 -0.6; 32 -1.1; 35 -1.5; 37 -1.7; 40 -1.8; 42 -1.9; 45 -1.8; 49 -1.7; 52 -1.6; 56 -1.5; 59 -1.4; 64 -1.3; 68 -1.3; 73 -1.3; 78 -1.3; 83 -1.4; 89 -1.5; 95 -1.5; 102 -1.6; 109 -1.7; 117 -1.8; 125 -1.9; 134 -2.0; 143 -2.1; 153 -2.1; 164 -2.0; 175 -1.9; 188 -1.9; 201 -1.8; 215 -1.6; 230 -1.4; 246 -1.2; 263 -1.0; 282 -0.7; 301 -0.5; 323 -0.1; 345 0.2; 369 0.4; 395 0.6; 423 0.7; 452 0.8; 484 0.9; 518 0.9; 554 1.0; 593 1.0; 635 1.1; 679 0.8; 726 0.5; 777 0.1; 832 -0.2; 890 -0.3; 952 -0.1; 1019 -0.1; 1090 -0.6; 1167 -1.2; 1248 -2.1; 1336 -2.3; 1429 -1.9; 1529 -1.5; 1636 -1.4; 1751 -1.5; 1873 -1.5; 2004 -1.6; 2145 -1.6; 2295 -1.7; 2455 -1.9; 2627 -1.2; 2811 1.0; 3008 4.8; 3219 6.0; 3444 4.6; 3685 -0.1; 3943 -2.0; 4219 -1.3; 4514 0.7; 4830 2.3; 5168 2.5; 5530 1.0; 5917 -3.3; 6331 -3.5; 6775 1.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 -1.0; 12455 -4.2; 13327 -5.2; 14260 -3.4; 15258 -1.0; 16326 -0.3; 17469 -1.1; 18692 -1.4; 20000 -0.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.7dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 2.69 | 3.9 dB  |
| Peaking | 81 Hz    | 0.44 | -1.9 dB |
| Peaking | 2216 Hz  | 1.11 | -2.3 dB |
| Peaking | 3187 Hz  | 5.94 | 8.3 dB  |
| Peaking | 13318 Hz | 3.94 | -5.8 dB |
| Peaking | 544 Hz   | 1.7  | 1.5 dB  |
| Peaking | 1303 Hz  | 5.88 | -1.8 dB |
| Peaking | 4014 Hz  | 5.53 | -4.3 dB |
| Peaking | 5449 Hz  | 1.7  | 4.4 dB  |
| Peaking | 6090 Hz  | 7.21 | -8.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Bose%20QuietComfort%2025/Bose%20QuietComfort%2025.png)