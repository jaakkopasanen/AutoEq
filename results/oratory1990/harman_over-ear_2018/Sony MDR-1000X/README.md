# Sony MDR-1000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.1dB
GraphicEQ: 10 -84; 20 -6.6; 22 -6.9; 23 -7.1; 25 -7.4; 26 -7.5; 28 -7.6; 30 -7.7; 32 -7.8; 35 -7.8; 37 -7.7; 40 -7.7; 42 -7.6; 45 -7.5; 49 -7.4; 52 -7.4; 56 -7.3; 59 -7.4; 64 -7.5; 68 -7.6; 73 -7.8; 78 -8.0; 83 -8.3; 89 -8.6; 95 -8.8; 102 -9.1; 109 -9.3; 117 -9.5; 125 -9.7; 134 -9.7; 143 -9.8; 153 -9.7; 164 -9.6; 175 -9.5; 188 -9.2; 201 -8.9; 215 -8.6; 230 -8.3; 246 -8.2; 263 -8.2; 282 -8.1; 301 -7.7; 323 -7.0; 345 -6.2; 369 -5.5; 395 -5.3; 423 -5.6; 452 -5.9; 484 -6.0; 518 -5.9; 554 -5.4; 593 -4.3; 635 -4.4; 679 -5.6; 726 -5.6; 777 -2.8; 832 -0.9; 890 -1.4; 952 -0.4; 1019 -0.0; 1090 0.8; 1167 1.3; 1248 -0.3; 1336 -1.1; 1429 -3.7; 1529 -5.3; 1636 -6.6; 1751 -7.8; 1873 -8.3; 2004 -7.7; 2145 -7.0; 2295 -4.8; 2455 -5.0; 2627 -4.9; 2811 -5.1; 3008 -4.2; 3219 -4.2; 3444 -4.6; 3685 -5.3; 3943 -7.6; 4219 -8.4; 4514 -7.8; 4830 -6.5; 5168 -7.3; 5530 -11.6; 5917 -11.8; 6331 -6.2; 6775 -2.5; 7249 -2.7; 7756 -4.1; 8299 -4.4; 8880 -2.7; 9502 -0.7; 10167 0.0; 10879 -1.2; 11640 -3.8; 12455 -6.3; 13327 -6.6; 14260 -3.3; 15258 -0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.1dB` and instead set Global volume in the UI for both channels to **-21**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.14 | -6.9 dB |
| Peaking | 193 Hz   | 0.64 | -6.0 dB |
| Peaking | 543 Hz   | 2.09 | -3.1 dB |
| Peaking | 1885 Hz  | 3.07 | -7.5 dB |
| Peaking | 5147 Hz  | 1.1  | -8.8 dB |
| Peaking | 715 Hz   | 9.69 | -3.5 dB |
| Peaking | 1162 Hz  | 2.32 | 3.4 dB  |
| Peaking | 1520 Hz  | 4.24 | -2.7 dB |
| Peaking | 10007 Hz | 4.21 | 3.0 dB  |
| Peaking | 12834 Hz | 3.73 | -6.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20MDR-1000X/Sony%20MDR-1000X.png)