# Noontec Zoro II Wireless Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 -2.0; 22 -2.2; 23 -2.2; 25 -2.3; 26 -2.4; 28 -2.5; 30 -2.6; 32 -2.6; 35 -2.7; 37 -2.7; 40 -2.7; 42 -2.7; 45 -2.8; 49 -2.8; 52 -2.9; 56 -2.9; 59 -3.0; 64 -3.1; 68 -3.1; 73 -3.2; 78 -3.4; 83 -3.7; 89 -4.1; 95 -4.5; 102 -4.9; 109 -5.1; 117 -5.3; 125 -5.5; 134 -5.7; 143 -5.9; 153 -6.0; 164 -5.8; 175 -5.9; 188 -6.0; 201 -5.9; 215 -5.8; 230 -5.5; 246 -5.4; 263 -5.1; 282 -4.7; 301 -4.5; 323 -4.1; 345 -3.8; 369 -3.6; 395 -3.5; 423 -3.3; 452 -3.1; 484 -2.8; 518 -2.7; 554 -2.2; 593 -1.6; 635 -1.2; 679 -0.9; 726 -0.6; 777 -0.1; 832 -0.2; 890 -0.0; 952 0.0; 1019 0.1; 1090 0.0; 1167 -0.1; 1248 -0.5; 1336 -0.9; 1429 -1.4; 1529 -1.7; 1636 -1.9; 1751 -1.8; 1873 -1.5; 2004 -0.9; 2145 -0.2; 2295 0.3; 2455 0.8; 2627 1.3; 2811 1.7; 3008 2.0; 3219 1.7; 3444 2.1; 3685 3.5; 3943 5.5; 4219 4.8; 4514 3.1; 4830 1.7; 5168 1.2; 5530 2.4; 5917 5.2; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.832821303285398dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro II Wireless Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.51 | -2.2 dB |
| Peaking | 121 Hz  | 1.06 | -2.1 dB |
| Peaking | 224 Hz  | 0.62 | -4.8 dB |
| Peaking | 3980 Hz | 3.85 | 5.3 dB  |
| Peaking | 6249 Hz | 5.45 | 5.9 dB  |
| Peaking | 504 Hz  | 2.56 | -1.0 dB |
| Peaking | 949 Hz  | 0.81 | 1.3 dB  |
| Peaking | 1646 Hz | 2.08 | -2.4 dB |
| Peaking | 2727 Hz | 3.27 | 1.6 dB  |
| Peaking | 3347 Hz | 0.22 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20II%20Wireless%20Passive/Noontec%20Zoro%20II%20Wireless%20Passive.png)