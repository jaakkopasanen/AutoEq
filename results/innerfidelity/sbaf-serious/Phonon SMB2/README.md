# Phonon SMB2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.4; 22 5.4; 23 5.0; 25 4.2; 26 3.8; 28 3.1; 30 2.5; 32 2.0; 35 1.3; 37 0.9; 40 0.4; 42 0.2; 45 -0.2; 49 -0.5; 52 -0.7; 56 -0.9; 59 -1.1; 64 -1.3; 68 -1.4; 73 -1.4; 78 -1.5; 83 -1.6; 89 -1.6; 95 -1.7; 102 -1.8; 109 -1.7; 117 -1.6; 125 -1.6; 134 -1.9; 143 -2.0; 153 -2.1; 164 -1.9; 175 -1.8; 188 -1.8; 201 -1.8; 215 -1.8; 230 -1.7; 246 -1.9; 263 -2.0; 282 -1.7; 301 -1.4; 323 -1.1; 345 -0.7; 369 -0.2; 395 0.3; 423 1.2; 452 1.5; 484 1.6; 518 1.8; 554 2.3; 593 2.6; 635 2.3; 679 1.9; 726 1.5; 777 1.3; 832 0.9; 890 0.5; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 -0.1; 1336 -0.6; 1429 -1.2; 1529 -1.8; 1636 -2.3; 1751 -2.4; 1873 -2.2; 2004 -1.6; 2145 -0.6; 2295 0.6; 2455 2.3; 2627 3.3; 2811 4.3; 3008 5.7; 3219 5.9; 3444 5.8; 3685 4.6; 3943 5.8; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.529072408591196dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phonon SMB2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.15 | 6.7 dB  |
| Peaking | 200 Hz  | 0.21 | -2.3 dB |
| Peaking | 568 Hz  | 1.31 | 4.2 dB  |
| Peaking | 1814 Hz | 2.31 | -4.3 dB |
| Peaking | 4009 Hz | 0.93 | 6.9 dB  |
| Peaking | 2222 Hz | 7.57 | -0.7 dB |
| Peaking | 3209 Hz | 2.7  | 1.9 dB  |
| Peaking | 3670 Hz | 4.73 | -2.5 dB |
| Peaking | 6239 Hz | 2.8  | 4.8 dB  |
| Peaking | 7436 Hz | 1.49 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phonon%20SMB2/Phonon%20SMB2.png)