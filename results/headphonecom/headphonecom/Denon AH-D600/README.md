# Denon AH-D600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.9; 22 -5.2; 23 -5.4; 25 -5.7; 26 -5.8; 28 -6.1; 30 -6.3; 32 -6.5; 35 -6.6; 37 -6.7; 40 -6.8; 42 -6.8; 45 -6.7; 49 -6.4; 52 -6.1; 56 -5.8; 59 -5.8; 64 -6.0; 68 -6.3; 73 -6.9; 78 -7.0; 83 -6.9; 89 -6.9; 95 -6.9; 102 -6.9; 109 -6.9; 117 -6.9; 125 -6.8; 134 -6.6; 143 -6.6; 153 -6.6; 164 -5.8; 175 -5.6; 188 -5.6; 201 -5.1; 215 -4.4; 230 -3.2; 246 -2.1; 263 -1.3; 282 -1.1; 301 -1.4; 323 -1.7; 345 -1.7; 369 -1.4; 395 -1.4; 423 -1.1; 452 -0.2; 484 0.4; 518 0.1; 554 0.1; 593 0.2; 635 0.2; 679 0.1; 726 -0.1; 777 -0.1; 832 -0.0; 890 0.1; 952 -0.0; 1019 0.0; 1090 0.0; 1167 0.1; 1248 0.2; 1336 0.5; 1429 0.6; 1529 0.7; 1636 0.6; 1751 0.3; 1873 -0.1; 2004 0.1; 2145 1.1; 2295 2.3; 2455 2.2; 2627 1.9; 2811 1.9; 3008 2.3; 3219 2.8; 3444 3.8; 3685 5.2; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.0; 6331 2.3; 6775 2.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.5  | -6.0 dB |
| Peaking | 112 Hz  | 0.98 | -4.9 dB |
| Peaking | 185 Hz  | 2.47 | -2.5 dB |
| Peaking | 5523 Hz | 4.52 | 3.7 dB  |
| Peaking | 4137 Hz | 1.75 | 5.8 dB  |
| Peaking | 275 Hz  | 4.49 | 1.6 dB  |
| Peaking | 372 Hz  | 1.31 | -1.6 dB |
| Peaking | 488 Hz  | 1.91 | 1.5 dB  |
| Peaking | 7066 Hz | 5.62 | 1.2 dB  |
| Peaking | 7859 Hz | 2.54 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Denon%20AH-D600/Denon%20AH-D600.png)