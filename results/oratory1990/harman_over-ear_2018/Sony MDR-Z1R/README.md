# Sony MDR-Z1R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -2.7; 22 -2.9; 23 -2.9; 25 -3.1; 26 -3.1; 28 -3.2; 30 -3.2; 32 -3.3; 35 -3.4; 37 -3.4; 40 -3.4; 42 -3.3; 45 -3.2; 49 -3.0; 52 -3.0; 56 -3.0; 59 -3.1; 64 -3.2; 68 -3.4; 73 -3.4; 78 -3.5; 83 -3.9; 89 -4.4; 95 -4.9; 102 -5.1; 109 -5.1; 117 -5.2; 125 -5.5; 134 -5.6; 143 -5.5; 153 -5.3; 164 -4.8; 175 -4.3; 188 -4.0; 201 -3.7; 215 -3.3; 230 -2.9; 246 -2.6; 263 -2.3; 282 -2.0; 301 -1.7; 323 -1.4; 345 -1.2; 369 -1.0; 395 -0.9; 423 -0.8; 452 -0.7; 484 -0.5; 518 -0.2; 554 0.2; 593 0.1; 635 -0.1; 679 -0.1; 726 -0.2; 777 -0.3; 832 -0.4; 890 -0.3; 952 -0.1; 1019 0.1; 1090 0.6; 1167 1.0; 1248 1.2; 1336 1.3; 1429 1.3; 1529 1.1; 1636 0.7; 1751 0.1; 1873 -0.6; 2004 -1.2; 2145 -1.4; 2295 -1.2; 2455 -1.4; 2627 -0.6; 2811 1.6; 3008 0.7; 3219 -4.7; 3444 -3.2; 3685 2.6; 3943 5.9; 4219 6.0; 4514 6.0; 4830 5.1; 5168 3.5; 5530 4.4; 5917 5.5; 6331 3.3; 6775 -0.6; 7249 -0.1; 7756 0.2; 8299 0.0; 8880 -0.1; 9502 -2.5; 10167 -4.7; 10879 -4.6; 11640 -3.5; 12455 -3.0; 13327 -3.7; 14260 -4.8; 15258 -4.8; 16326 -2.5; 17469 -0.0; 18692 -1.1; 20000 -9.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z1R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 29 Hz    |  0.61 | -2.9 dB |
| Peaking | 132 Hz   |  0.85 | -5.3 dB |
| Peaking | 3312 Hz  |  7.95 | -8.8 dB |
| Peaking | 4564 Hz  |  1.53 | 7.2 dB  |
| Peaking | 13084 Hz |  0.74 | -4.6 dB |
| Peaking | 1390 Hz  |  2.65 | 1.6 dB  |
| Peaking | 2282 Hz  |  2.42 | -2.7 dB |
| Peaking | 2876 Hz  | 10.16 | 2.7 dB  |
| Peaking | 10051 Hz |  1.91 | 2.7 dB  |
| Peaking | 10276 Hz |  4.64 | -4.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20MDR-Z1R/Sony%20MDR-Z1R.png)