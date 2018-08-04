# Sonoma Model One

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 1.6; 22 1.5; 23 1.4; 25 1.4; 26 1.3; 28 1.3; 30 1.4; 32 1.4; 35 1.4; 37 1.5; 40 1.5; 42 1.6; 45 1.7; 49 1.9; 52 2.1; 56 2.3; 59 2.5; 64 2.4; 68 1.6; 73 0.6; 78 0.2; 83 0.4; 89 0.8; 95 0.9; 102 0.9; 109 0.8; 117 0.5; 125 0.4; 134 0.4; 143 0.4; 153 0.4; 164 0.4; 175 0.4; 188 0.3; 201 0.3; 215 0.4; 230 0.5; 246 0.5; 263 0.5; 282 0.6; 301 0.5; 323 0.5; 345 0.5; 369 0.5; 395 0.5; 423 0.7; 452 0.4; 484 -0.0; 518 -0.0; 554 0.2; 593 0.6; 635 -0.0; 679 -0.8; 726 -1.2; 777 -0.8; 832 -0.8; 890 -0.7; 952 -0.2; 1019 0.3; 1090 -0.3; 1167 -1.4; 1248 -2.4; 1336 -1.9; 1429 -3.0; 1529 -3.5; 1636 -2.3; 1751 -2.0; 1873 -1.1; 2004 -0.6; 2145 -1.5; 2295 -0.9; 2455 -0.3; 2627 -2.0; 2811 -1.0; 3008 -0.9; 3219 -1.6; 3444 -1.0; 3685 -0.6; 3943 0.1; 4219 0.1; 4514 0.1; 4830 0.0; 5168 -1.0; 5530 0.9; 5917 5.6; 6331 2.2; 6775 0.5; 7249 1.0; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.3dB` and instead set Global volume in the UI for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sonoma Model One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  0.17 | 1.3 dB  |
| Peaking | 58 Hz   |  4.29 | 1.5 dB  |
| Peaking | 1479 Hz |  2.84 | -3.2 dB |
| Peaking | 2946 Hz |  2.23 | -1.2 dB |
| Peaking | 5949 Hz | 11.1  | 6.3 dB  |
| Peaking | 79 Hz   |  5.5  | -0.7 dB |
| Peaking | 412 Hz  |  1.05 | 0.5 dB  |
| Peaking | 743 Hz  |  4.22 | -1.2 dB |
| Peaking | 1204 Hz |  9.02 | -0.8 dB |
| Peaking | 1041 Hz |  7.14 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sonoma%20Model%20One/Sonoma%20Model%20One.png)