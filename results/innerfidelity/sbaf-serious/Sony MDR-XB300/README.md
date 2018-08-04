# Sony MDR-XB300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.9; 22 3.6; 23 3.0; 25 1.8; 26 1.3; 28 0.3; 30 -0.6; 32 -1.4; 35 -2.5; 37 -3.1; 40 -3.9; 42 -4.4; 45 -5.0; 49 -5.6; 52 -6.0; 56 -6.4; 59 -6.5; 64 -6.4; 68 -6.2; 73 -6.1; 78 -6.4; 83 -6.7; 89 -7.1; 95 -7.4; 102 -7.7; 109 -7.9; 117 -7.9; 125 -8.1; 134 -8.0; 143 -7.8; 153 -7.5; 164 -7.1; 175 -7.0; 188 -6.8; 201 -6.5; 215 -5.9; 230 -5.3; 246 -4.5; 263 -4.1; 282 -3.7; 301 -3.0; 323 -2.3; 345 -1.6; 369 -0.8; 395 -0.2; 423 0.7; 452 1.2; 484 1.8; 518 2.2; 554 2.8; 593 3.6; 635 3.9; 679 4.1; 726 4.2; 777 4.2; 832 3.3; 890 2.1; 952 0.8; 1019 -0.2; 1090 -1.0; 1167 -1.2; 1248 -1.8; 1336 -3.0; 1429 -3.6; 1529 -3.9; 1636 -4.0; 1751 -4.6; 1873 -5.1; 2004 -5.6; 2145 -6.1; 2295 -6.1; 2455 -5.4; 2627 -4.2; 2811 -2.9; 3008 -1.0; 3219 0.5; 3444 2.2; 3685 3.4; 3943 4.5; 4219 4.7; 4514 5.9; 4830 6.0; 5168 6.0; 5530 6.0; 5917 4.6; 6331 0.8; 6775 1.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.75 | 6.0 dB  |
| Peaking | 65 Hz   | 0.68 | -6.2 dB |
| Peaking | 157 Hz  | 1.27 | -6.0 dB |
| Peaking | 2173 Hz | 1.91 | -7.4 dB |
| Peaking | 4655 Hz | 1.77 | 7.2 dB  |
| Peaking | 73 Hz   | 6.2  | 0.7 dB  |
| Peaking | 271 Hz  | 2.02 | -1.9 dB |
| Peaking | 689 Hz  | 1.29 | 5.3 dB  |
| Peaking | 1304 Hz | 1.88 | -2.7 dB |
| Peaking | 8474 Hz | 2.9  | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB300/Sony%20MDR-XB300.png)