# Piaton PS 210

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.9; 56 5.6; 59 5.4; 64 5.0; 68 4.8; 73 4.4; 78 4.1; 83 3.8; 89 3.3; 95 2.8; 102 2.1; 109 1.5; 117 0.9; 125 0.1; 134 -0.4; 143 -1.0; 153 -1.2; 164 -1.4; 175 -1.7; 188 -1.8; 201 -2.0; 215 -2.0; 230 -2.0; 246 -2.2; 263 -2.1; 282 -2.0; 301 -2.0; 323 -2.0; 345 -1.9; 369 -2.0; 395 -2.0; 423 -2.1; 452 -2.2; 484 -2.0; 518 -1.9; 554 -1.7; 593 -1.6; 635 -1.7; 679 -1.9; 726 -1.8; 777 -1.4; 832 -1.1; 890 -0.8; 952 -0.4; 1019 0.0; 1090 0.5; 1167 1.0; 1248 1.3; 1336 1.5; 1429 1.5; 1529 1.2; 1636 0.8; 1751 0.2; 1873 -0.7; 2004 -1.8; 2145 -3.0; 2295 -4.1; 2455 -4.0; 2627 -2.2; 2811 0.4; 3008 3.5; 3219 5.6; 3444 6.0; 3685 6.0; 3943 5.0; 4219 2.1; 4514 0.3; 4830 1.9; 5168 5.0; 5530 5.9; 5917 3.7; 6331 0.8; 6775 0.1; 7249 -2.8; 7756 -6.2; 8299 -7.3; 8880 -3.9; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Piaton PS 210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.78 | 7.1 dB  |
| Peaking | 2408 Hz | 4.05 | -5.9 dB |
| Peaking | 3443 Hz | 3.1  | 7.2 dB  |
| Peaking | 5483 Hz | 6.04 | 6.3 dB  |
| Peaking | 8056 Hz | 5.32 | -8.5 dB |
| Peaking | 84 Hz   | 1.08 | 4.2 dB  |
| Peaking | 136 Hz  | 0.44 | -3.3 dB |
| Peaking | 837 Hz  | 0.62 | -2.1 dB |
| Peaking | 1318 Hz | 1.25 | 3.3 dB  |
| Peaking | 2006 Hz | 5.24 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Piaton%20PS%20210/Piaton%20PS%20210.png)