# AKG K702 65th Anv Ed 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 10 -84; 20 3.2; 22 2.6; 23 2.4; 25 1.9; 26 1.7; 28 1.3; 30 1.0; 32 0.7; 35 0.3; 37 0.1; 40 -0.2; 42 -0.4; 45 -0.6; 49 -0.9; 52 -1.1; 56 -1.3; 59 -1.5; 64 -1.7; 68 -2.0; 73 -2.3; 78 -2.4; 83 -2.7; 89 -3.0; 95 -3.3; 102 -3.5; 109 -3.6; 117 -3.7; 125 -3.8; 134 -3.9; 143 -4.0; 153 -4.4; 164 -4.6; 175 -4.2; 188 -4.2; 201 -4.5; 215 -4.5; 230 -4.7; 246 -4.7; 263 -4.7; 282 -4.7; 301 -4.7; 323 -4.5; 345 -4.4; 369 -4.3; 395 -4.2; 423 -3.9; 452 -3.7; 484 -3.5; 518 -3.2; 554 -2.9; 593 -2.4; 635 -2.2; 679 -1.9; 726 -1.3; 777 -0.7; 832 -0.6; 890 -0.3; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.4; 1248 0.6; 1336 0.2; 1429 -0.9; 1529 -2.1; 1636 -3.1; 1751 -3.7; 1873 -4.2; 2004 -4.3; 2145 -3.8; 2295 -2.4; 2455 -0.0; 2627 2.2; 2811 4.0; 3008 4.8; 3219 4.8; 3444 4.8; 3685 3.3; 3943 1.6; 4219 -0.6; 4514 -1.2; 4830 -0.8; 5168 -0.6; 5530 -1.5; 5917 -3.5; 6331 -4.0; 6775 -5.0; 7249 -5.4; 7756 -4.8; 8299 -4.5; 8880 -3.5; 9502 -1.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -1.3; 17469 -3.2; 18692 -3.4; 20000 -2.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.099654392931489dB` and instead set Global volume in the UI for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 65th Anv Ed 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.5dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 20 Hz    |  1.47 | 3.1 dB  |
| Peaking | 210 Hz   |  0.45 | -4.9 dB |
| Peaking | 2007 Hz  |  3.08 | -5.6 dB |
| Peaking | 3107 Hz  |  2.54 | 6.5 dB  |
| Peaking | 7146 Hz  |  2.04 | -5.8 dB |
| Peaking | 1206 Hz  |  2.12 | 1.7 dB  |
| Peaking | 1608 Hz  |  5.4  | -1.8 dB |
| Peaking | 4379 Hz  | 10.35 | -1.7 dB |
| Peaking | 15235 Hz |  0.88 | 2.4 dB  |
| Peaking | 18111 Hz |  1.04 | -4.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K702%2065th%20Anv%20Ed%202014/AKG%20K702%2065th%20Anv%20Ed%202014.png)