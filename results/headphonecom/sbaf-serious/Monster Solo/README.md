# Monster Solo

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.0; 22 -4.3; 23 -4.5; 25 -4.7; 26 -4.8; 28 -5.1; 30 -5.2; 32 -5.4; 35 -5.7; 37 -5.8; 40 -6.1; 42 -6.2; 45 -6.3; 49 -6.5; 52 -6.6; 56 -6.8; 59 -7.0; 64 -7.4; 68 -7.6; 73 -7.8; 78 -7.9; 83 -7.9; 89 -7.9; 95 -7.8; 102 -7.6; 109 -7.5; 117 -8.3; 125 -9.4; 134 -10.4; 143 -10.9; 153 -10.8; 164 -10.1; 175 -9.8; 188 -9.7; 201 -9.1; 215 -8.2; 230 -7.2; 246 -6.2; 263 -5.1; 282 -4.4; 301 -3.9; 323 -3.3; 345 -2.7; 369 -2.0; 395 -1.3; 423 -0.4; 452 0.2; 484 0.5; 518 0.6; 554 0.8; 593 0.9; 635 0.7; 679 0.3; 726 0.0; 777 -0.1; 832 -0.2; 890 -0.4; 952 -0.2; 1019 0.1; 1090 0.5; 1167 1.0; 1248 1.5; 1336 1.8; 1429 1.9; 1529 2.0; 1636 2.0; 1751 2.1; 1873 2.3; 2004 2.4; 2145 2.4; 2295 2.7; 2455 2.9; 2627 2.8; 2811 3.3; 3008 3.6; 3219 3.5; 3444 3.2; 3685 2.6; 3943 1.9; 4219 0.6; 4514 -0.2; 4830 1.8; 5168 5.4; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Solo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 2 Hz    | 1.87 | -3.2 dB |
| Peaking | 13 Hz   | 1.41 | -6.3 dB |
| Peaking | 60 Hz   | 0.51 | -6.2 dB |
| Peaking | 169 Hz  | 1.21 | -8.3 dB |
| Peaking | 3417 Hz | 0.44 | 3.2 dB  |
| Peaking | 524 Hz  | 2.72 | 1.7 dB  |
| Peaking | 910 Hz  | 3.69 | -1.2 dB |
| Peaking | 4488 Hz | 4.09 | -5.9 dB |
| Peaking | 5845 Hz | 1.72 | 7.6 dB  |
| Peaking | 7590 Hz | 1.3  | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Solo/Monster%20Solo.png)