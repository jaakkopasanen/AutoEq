# Spider Moonlight

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -2.1; 22 -2.6; 23 -2.9; 25 -3.3; 26 -3.5; 28 -3.8; 30 -4.1; 32 -4.4; 35 -4.8; 37 -5.0; 40 -5.2; 42 -5.3; 45 -5.5; 49 -5.8; 52 -5.9; 56 -6.0; 59 -6.0; 64 -6.1; 68 -6.2; 73 -6.2; 78 -6.2; 83 -6.5; 89 -6.6; 95 -6.4; 102 -6.4; 109 -6.5; 117 -6.8; 125 -7.0; 134 -7.1; 143 -7.2; 153 -7.3; 164 -6.8; 175 -6.5; 188 -6.8; 201 -6.6; 215 -6.1; 230 -5.4; 246 -4.7; 263 -3.8; 282 -2.4; 301 -1.1; 323 -0.3; 345 0.1; 369 0.1; 395 -0.2; 423 -0.5; 452 -0.8; 484 -1.0; 518 -1.0; 554 -1.0; 593 -0.9; 635 -0.7; 679 0.6; 726 0.6; 777 0.9; 832 0.5; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.1; 1248 0.1; 1336 0.1; 1429 0.1; 1529 -0.3; 1636 -0.9; 1751 -1.5; 1873 -2.1; 2004 -2.6; 2145 -3.1; 2295 -3.3; 2455 -3.0; 2627 -2.3; 2811 -2.0; 3008 -2.3; 3219 -2.8; 3444 -2.3; 3685 -2.0; 3943 -2.2; 4219 -1.3; 4514 0.9; 4830 4.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.2; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider Moonlight ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 61 Hz   | 0.5  | -6.0 dB |
| Peaking | 169 Hz  | 1.38 | -5.0 dB |
| Peaking | 3885 Hz | 1.68 | -4.4 dB |
| Peaking | 2220 Hz | 3.13 | -2.9 dB |
| Peaking | 5417 Hz | 2.36 | 8.8 dB  |
| Peaking | 239 Hz  | 4.17 | -1.5 dB |
| Peaking | 337 Hz  | 3.78 | 2.1 dB  |
| Peaking | 773 Hz  | 4.79 | 1.3 dB  |
| Peaking | 6522 Hz | 6.95 | 2.6 dB  |
| Peaking | 7708 Hz | 1.85 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Spider%20Moonlight/Spider%20Moonlight.png)