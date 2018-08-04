# Denon AH-D600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.4; 22 -4.7; 23 -4.9; 25 -5.2; 26 -5.3; 28 -5.6; 30 -5.8; 32 -5.9; 35 -6.1; 37 -6.1; 40 -6.2; 42 -6.2; 45 -6.1; 49 -5.8; 52 -5.5; 56 -5.2; 59 -5.2; 64 -5.4; 68 -5.8; 73 -6.3; 78 -6.3; 83 -6.2; 89 -6.1; 95 -6.0; 102 -5.9; 109 -5.7; 117 -5.6; 125 -5.6; 134 -5.3; 143 -5.3; 153 -5.3; 164 -4.4; 175 -4.2; 188 -4.2; 201 -3.8; 215 -3.0; 230 -1.8; 246 -0.7; 263 0.1; 282 0.3; 301 0.0; 323 -0.3; 345 -0.3; 369 -0.0; 395 -0.1; 423 0.1; 452 0.9; 484 1.1; 518 0.6; 554 0.6; 593 0.6; 635 0.5; 679 0.1; 726 -0.1; 777 0.0; 832 0.1; 890 0.1; 952 -0.0; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.5; 1336 -0.9; 1429 -1.5; 1529 -2.0; 1636 -2.4; 1751 -2.8; 1873 -3.0; 2004 -2.9; 2145 -1.9; 2295 -0.8; 2455 -0.7; 2627 -1.1; 2811 -1.1; 3008 -0.3; 3219 0.4; 3444 1.7; 3685 3.2; 3943 4.4; 4219 4.9; 4514 5.7; 4830 6.0; 5168 5.2; 5530 3.3; 5917 1.5; 6331 0.0; 6775 1.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -0.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.1; 20000 -0.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 0.24 | -5.8 dB |
| Peaking | 172 Hz  | 0.84 | -4.7 dB |
| Peaking | 246 Hz  | 0.65 | 4.5 dB  |
| Peaking | 1865 Hz | 1.91 | -3.2 dB |
| Peaking | 4586 Hz | 2.59 | 6.6 dB  |
| Peaking | 133 Hz  | 4.85 | 0.3 dB  |
| Peaking | 269 Hz  | 7.1  | 1.1 dB  |
| Peaking | 348 Hz  | 4.89 | -0.7 dB |
| Peaking | 2851 Hz | 4.34 | -2.5 dB |
| Peaking | 2841 Hz | 2.08 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D600/Denon%20AH-D600.png)