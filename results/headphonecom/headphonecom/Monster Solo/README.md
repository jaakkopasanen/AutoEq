# Monster Solo

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -8.6; 22 -8.9; 23 -9.0; 25 -9.3; 26 -9.4; 28 -9.6; 30 -9.8; 32 -10.0; 35 -10.3; 37 -10.4; 40 -10.6; 42 -10.8; 45 -10.9; 49 -11.0; 52 -11.1; 56 -11.3; 59 -11.5; 64 -11.8; 68 -12.0; 73 -12.2; 78 -12.2; 83 -12.1; 89 -11.9; 95 -11.5; 102 -11.0; 109 -10.7; 117 -11.1; 125 -11.9; 134 -12.5; 143 -12.8; 153 -12.5; 164 -11.7; 175 -11.3; 188 -11.2; 201 -10.5; 215 -9.7; 230 -8.6; 246 -7.6; 263 -6.5; 282 -5.8; 301 -5.2; 323 -4.7; 345 -4.1; 369 -3.3; 395 -2.5; 423 -1.6; 452 -0.8; 484 -0.2; 518 0.0; 554 0.3; 593 0.4; 635 0.4; 679 0.3; 726 0.1; 777 -0.2; 832 -0.3; 890 -0.4; 952 -0.2; 1019 0.1; 1090 0.6; 1167 1.3; 1248 2.1; 1336 3.1; 1429 4.0; 1529 4.7; 1636 5.0; 1751 5.1; 1873 5.2; 2004 5.3; 2145 5.5; 2295 5.7; 2455 5.8; 2627 5.8; 2811 6.0; 3008 6.0; 3219 5.8; 3444 5.3; 3685 4.6; 3943 4.2; 4219 4.2; 4514 4.6; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Solo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.58 | -6.6 dB |
| Peaking | 71 Hz   | 0.62 | -8.4 dB |
| Peaking | 174 Hz  | 1.03 | -8.4 dB |
| Peaking | 2399 Hz | 0.85 | 6.2 dB  |
| Peaking | 5569 Hz | 2.78 | 5.0 dB  |
| Peaking | 347 Hz  | 2.09 | -1.3 dB |
| Peaking | 536 Hz  | 1.27 | 2.1 dB  |
| Peaking | 932 Hz  | 1.37 | -1.9 dB |
| Peaking | 1467 Hz | 3.81 | 1.7 dB  |
| Peaking | 8439 Hz | 3.74 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Monster%20Solo/Monster%20Solo.png)