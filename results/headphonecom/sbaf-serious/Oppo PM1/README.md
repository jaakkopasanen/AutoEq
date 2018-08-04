# Oppo PM1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.5; 22 -0.9; 23 -1.0; 25 -1.3; 26 -1.4; 28 -1.6; 30 -1.7; 32 -1.9; 35 -2.0; 37 -2.0; 40 -1.8; 42 -1.7; 45 -1.3; 49 -0.7; 52 -1.0; 56 -2.4; 59 -3.2; 64 -3.3; 68 -3.3; 73 -3.2; 78 -3.3; 83 -3.2; 89 -3.2; 95 -3.3; 102 -3.1; 109 -3.0; 117 -2.9; 125 -2.7; 134 -2.8; 143 -2.8; 153 -2.8; 164 -2.6; 175 -2.6; 188 -2.7; 201 -2.5; 215 -2.3; 230 -2.0; 246 -2.0; 263 -2.2; 282 -2.4; 301 -2.5; 323 -2.3; 345 -1.8; 369 -1.2; 395 -0.5; 423 0.0; 452 -0.5; 484 -1.1; 518 -1.3; 554 -1.2; 593 -0.9; 635 -0.8; 679 -1.1; 726 -1.2; 777 -1.2; 832 -1.4; 890 -1.4; 952 -0.5; 1019 0.2; 1090 0.8; 1167 0.9; 1248 1.1; 1336 0.2; 1429 -0.1; 1529 0.1; 1636 -0.0; 1751 0.3; 1873 0.8; 2004 1.1; 2145 1.4; 2295 2.0; 2455 2.7; 2627 2.8; 2811 2.7; 3008 3.2; 3219 3.1; 3444 3.0; 3685 3.0; 3943 3.4; 4219 3.1; 4514 3.4; 4830 4.6; 5168 5.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.5; 8880 -2.4; 9502 -1.8; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 2.1  | -1.3 dB |
| Peaking | 77 Hz   | 1.45 | -1.8 dB |
| Peaking | 178 Hz  | 0.43 | -2.4 dB |
| Peaking | 3078 Hz | 1.44 | 3.0 dB  |
| Peaking | 5645 Hz | 3.05 | 6.2 dB  |
| Peaking | 422 Hz  | 7    | 1.7 dB  |
| Peaking | 1026 Hz | 1.53 | -2.2 dB |
| Peaking | 1104 Hz | 3.12 | 3.1 dB  |
| Peaking | 6550 Hz | 8.2  | 1.7 dB  |
| Peaking | 8981 Hz | 4.99 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Oppo%20PM1/Oppo%20PM1.png)