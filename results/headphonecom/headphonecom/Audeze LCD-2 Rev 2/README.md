# Audeze LCD-2 Rev 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.0; 22 -4.0; 23 -4.0; 25 -4.0; 26 -4.0; 28 -4.0; 30 -3.9; 32 -3.8; 35 -3.9; 37 -3.9; 40 -4.0; 42 -3.9; 45 -3.9; 49 -3.7; 52 -3.5; 56 -3.9; 59 -4.4; 64 -4.7; 68 -4.6; 73 -4.6; 78 -4.6; 83 -4.4; 89 -4.4; 95 -4.5; 102 -4.6; 109 -4.6; 117 -4.6; 125 -4.6; 134 -4.6; 143 -4.6; 153 -4.7; 164 -4.7; 175 -4.8; 188 -4.9; 201 -4.9; 215 -4.8; 230 -4.8; 246 -4.5; 263 -4.5; 282 -4.6; 301 -4.5; 323 -4.1; 345 -3.7; 369 -3.5; 395 -3.5; 423 -3.5; 452 -3.3; 484 -3.2; 518 -3.1; 554 -2.8; 593 -2.8; 635 -2.6; 679 -2.6; 726 -2.3; 777 -2.3; 832 -2.3; 890 -1.8; 952 -0.7; 1019 0.1; 1090 0.7; 1167 1.7; 1248 1.4; 1336 1.3; 1429 1.1; 1529 0.8; 1636 0.7; 1751 0.5; 1873 1.8; 2004 2.6; 2145 2.9; 2295 1.7; 2455 2.5; 2627 4.0; 2811 3.8; 3008 3.2; 3219 2.9; 3444 4.1; 3685 5.0; 3943 5.9; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.6; 5530 4.7; 5917 3.3; 6331 2.5; 6775 2.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.11 | -3.5 dB |
| Peaking | 344 Hz  | 0.27 | -3.7 dB |
| Peaking | 122 Hz  | 1.85 | 0.3 dB  |
| Peaking | 1756 Hz | 0.57 | 2.9 dB  |
| Peaking | 4502 Hz | 1.76 | 5.7 dB  |
| Peaking | 829 Hz  | 4.52 | -1.2 dB |
| Peaking | 1151 Hz | 5.41 | 1.2 dB  |
| Peaking | 1675 Hz | 4.49 | -2.0 dB |
| Peaking | 1769 Hz | 0.89 | 0.6 dB  |
| Peaking | 8698 Hz | 2.78 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Audeze%20LCD-2%20Rev%202/Audeze%20LCD-2%20Rev%202.png)