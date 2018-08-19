# Polk UltraFocus 8000 NC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -5.9; 22 -5.6; 23 -5.5; 25 -5.3; 26 -5.2; 28 -5.0; 30 -4.8; 32 -4.6; 35 -4.4; 37 -4.3; 40 -4.2; 42 -4.1; 45 -3.8; 49 -3.6; 52 -3.5; 56 -3.3; 59 -3.1; 64 -2.7; 68 -2.5; 73 -2.4; 78 -2.4; 83 -2.4; 89 -2.6; 95 -2.6; 102 -2.4; 109 -2.3; 117 -2.1; 125 -2.1; 134 -2.0; 143 -1.9; 153 -1.8; 164 -1.4; 175 -1.5; 188 -1.6; 201 -1.6; 215 -1.6; 230 -1.2; 246 -1.0; 263 -0.9; 282 -1.0; 301 -1.4; 323 -1.4; 345 -1.2; 369 -0.7; 395 -1.1; 423 -1.4; 452 -1.4; 484 -1.6; 518 -1.5; 554 -1.1; 593 -1.0; 635 -1.2; 679 -1.2; 726 -0.9; 777 -0.4; 832 -0.1; 890 -0.3; 952 0.0; 1019 0.0; 1090 0.2; 1167 0.9; 1248 1.5; 1336 1.3; 1429 0.9; 1529 0.6; 1636 0.4; 1751 0.1; 1873 0.1; 2004 -0.2; 2145 -0.0; 2295 0.6; 2455 1.5; 2627 2.5; 2811 3.4; 3008 4.0; 3219 4.7; 3444 5.9; 3685 5.7; 3943 4.8; 4219 5.5; 4514 0.4; 4830 0.0; 5168 1.4; 5530 1.6; 5917 2.6; 6331 4.4; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.7; 9502 -1.3; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999999643415945dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk UltraFocus 8000 NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.74 | -5.1 dB |
| Peaking | 31 Hz   | 0.58 | -2.2 dB |
| Peaking | 130 Hz  | 0.23 | -1.5 dB |
| Peaking | 3501 Hz | 2.49 | 6.1 dB  |
| Peaking | 6460 Hz | 6.86 | 4.5 dB  |
| Peaking | 543 Hz  | 2.53 | -0.6 dB |
| Peaking | 1129 Hz | 4.21 | -0.7 dB |
| Peaking | 1240 Hz | 3.29 | 2.0 dB  |
| Peaking | 2041 Hz | 6    | -1.0 dB |
| Peaking | 9352 Hz | 5.85 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20UltraFocus%208000%20NC/Polk%20UltraFocus%208000%20NC.png)