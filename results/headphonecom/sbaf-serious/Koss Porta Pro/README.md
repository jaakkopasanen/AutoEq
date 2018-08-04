# Koss Porta Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.8; 30 5.3; 32 4.7; 35 3.8; 37 3.2; 40 2.5; 42 2.0; 45 1.3; 49 0.5; 52 -0.1; 56 -0.8; 59 -1.2; 64 -1.9; 68 -2.4; 73 -2.9; 78 -3.4; 83 -3.8; 89 -4.3; 95 -4.7; 102 -5.1; 109 -5.5; 117 -5.7; 125 -6.0; 134 -6.1; 143 -6.1; 153 -6.2; 164 -6.1; 175 -5.9; 188 -5.7; 201 -5.3; 215 -4.9; 230 -4.5; 246 -4.1; 263 -3.8; 282 -3.4; 301 -3.1; 323 -2.7; 345 -2.3; 369 -2.1; 395 -1.8; 423 -1.5; 452 -1.2; 484 -0.9; 518 -0.8; 554 -0.5; 593 -0.1; 635 0.1; 679 0.0; 726 -0.0; 777 0.3; 832 0.1; 890 0.1; 952 -0.0; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -1.1; 1429 -1.7; 1529 -2.4; 1636 -3.1; 1751 -3.8; 1873 -4.2; 2004 -4.6; 2145 -4.6; 2295 -3.9; 2455 -2.5; 2627 -1.1; 2811 1.0; 3008 2.9; 3219 4.0; 3444 4.6; 3685 4.5; 3943 2.0; 4219 0.5; 4514 0.6; 4830 -0.1; 5168 1.8; 5530 4.2; 5917 5.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.5; 8880 -2.7; 9502 -1.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.0; 14260 -0.3; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -3.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.86 | 6.9 dB  |
| Peaking | 139 Hz   | 0.57 | -6.6 dB |
| Peaking | 2042 Hz  | 1.13 | -9.8 dB |
| Peaking | 3257 Hz  | 3.81 | 4.5 dB  |
| Peaking | 2336 Hz  | 0.41 | 5.0 dB  |
| Peaking | 4755 Hz  | 4.23 | -3.3 dB |
| Peaking | 6056 Hz  | 3.44 | 5.3 dB  |
| Peaking | 8843 Hz  | 3.48 | -3.7 dB |
| Peaking | 30287 Hz | 3    | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)