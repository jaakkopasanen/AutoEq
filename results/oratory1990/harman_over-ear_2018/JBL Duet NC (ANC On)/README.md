# JBL Duet NC (ANC On)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -7.6; 22 -7.2; 23 -6.9; 25 -6.4; 26 -6.2; 28 -5.7; 30 -5.3; 32 -4.9; 35 -4.4; 37 -4.1; 40 -3.7; 42 -3.5; 45 -3.2; 49 -3.0; 52 -2.9; 56 -2.8; 59 -2.7; 64 -2.5; 68 -2.3; 73 -2.3; 78 -2.1; 83 -1.9; 89 -1.9; 95 -2.2; 102 -2.4; 109 -2.4; 117 -2.4; 125 -2.3; 134 -2.0; 143 -1.6; 153 -1.2; 164 -0.7; 175 -0.1; 188 0.5; 201 0.9; 215 1.4; 230 1.9; 246 2.5; 263 3.1; 282 3.8; 301 4.4; 323 4.8; 345 5.0; 369 5.1; 395 5.2; 423 5.2; 452 5.5; 484 6.0; 518 5.8; 554 5.5; 593 5.4; 635 5.2; 679 4.8; 726 4.2; 777 3.5; 832 2.8; 890 1.8; 952 0.7; 1019 -0.3; 1090 -1.2; 1167 -1.7; 1248 -1.6; 1336 -1.3; 1429 -2.2; 1529 -2.3; 1636 -1.1; 1751 0.2; 1873 1.2; 2004 2.1; 2145 2.9; 2295 3.3; 2455 3.0; 2627 2.2; 2811 2.2; 3008 3.1; 3219 5.5; 3444 6.0; 3685 3.2; 3943 -0.1; 4219 -0.3; 4514 0.2; 4830 1.2; 5168 5.5; 5530 3.5; 5917 -0.8; 6331 2.6; 6775 3.6; 7249 0.1; 7756 -2.1; 8299 -2.4; 8880 -0.4; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Duet NC (ANC On) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 437 Hz   | 1.06 | 6.5 dB  |
| Peaking | 2308 Hz  | 5.66 | 3.1 dB  |
| Peaking | 3342 Hz  | 5.4  | 6.2 dB  |
| Peaking | 23996 Hz | 2.27 | 1.1 dB  |
| Peaking | 13 Hz    | 0.41 | -8.4 dB |
| Peaking | 122 Hz   | 1.83 | -2.4 dB |
| Peaking | 1335 Hz  | 2.8  | -3.2 dB |
| Peaking | 6958 Hz  | 2.18 | 4.6 dB  |
| Peaking | 7807 Hz  | 3.96 | -5.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/JBL%20Duet%20NC%20(ANC%20On)/JBL%20Duet%20NC%20(ANC%20On).png)