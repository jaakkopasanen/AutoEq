# Grado GS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.6; 23 5.3; 25 4.7; 26 4.4; 28 3.7; 30 3.1; 32 2.5; 35 1.5; 37 0.8; 40 0.1; 42 -0.2; 45 -1.0; 49 -2.5; 52 -3.6; 56 -4.6; 59 -5.3; 64 -6.4; 68 -7.1; 73 -7.9; 78 -8.5; 83 -9.0; 89 -9.3; 95 -9.6; 102 -9.5; 109 -9.4; 117 -8.9; 125 -8.5; 134 -7.9; 143 -7.4; 153 -6.9; 164 -6.2; 175 -5.6; 188 -5.0; 201 -4.4; 215 -3.9; 230 -3.3; 246 -2.9; 263 -2.5; 282 -2.5; 301 -2.4; 323 -2.1; 345 -1.7; 369 -1.5; 395 -1.2; 423 -0.9; 452 -0.8; 484 -0.8; 518 -0.8; 554 -0.5; 593 -0.1; 635 0.1; 679 0.1; 726 0.2; 777 0.3; 832 0.3; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.1; 1248 -0.2; 1336 -0.5; 1429 -0.8; 1529 -1.2; 1636 -0.8; 1751 -0.7; 1873 -1.3; 2004 -1.2; 2145 -1.5; 2295 -1.2; 2455 -1.0; 2627 -1.2; 2811 -1.4; 3008 -1.2; 3219 -1.0; 3444 -1.4; 3685 -5.0; 3943 -5.1; 4219 -3.4; 4514 -3.9; 4830 -6.1; 5168 -6.8; 5530 -7.5; 5917 -8.3; 6331 -9.8; 6775 -10.3; 7249 -10.0; 7756 -9.4; 8299 -8.6; 8880 -7.7; 9502 -6.7; 10167 -4.9; 10879 -2.6; 11640 -0.9; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.3; 20000 -0.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.53 | 7.1 dB   |
| Peaking | 73 Hz    | 0.99 | -4.4 dB  |
| Peaking | 113 Hz   | 0.78 | -7.3 dB  |
| Peaking | 1944 Hz  | 3.57 | -0.6 dB  |
| Peaking | 6895 Hz  | 1.26 | -10.7 dB |
| Peaking | 768 Hz   | 2.41 | 0.7 dB   |
| Peaking | 3386 Hz  | 5.58 | 1.9 dB   |
| Peaking | 3746 Hz  | 8.76 | -3.8 dB  |
| Peaking | 9533 Hz  | 2.75 | -3.4 dB  |
| Peaking | 11522 Hz | 1.25 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GS1000/Grado%20GS1000.png)