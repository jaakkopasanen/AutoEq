# NAD RP18 Bass Light Version

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 6.0; 201 6.0; 215 6.0; 230 6.0; 246 5.6; 263 4.5; 282 4.0; 301 3.5; 323 2.5; 345 2.2; 369 2.1; 395 1.7; 423 1.4; 452 0.7; 484 0.4; 518 0.9; 554 0.9; 593 0.9; 635 0.4; 679 -0.2; 726 -0.1; 777 -0.1; 832 -0.6; 890 -0.3; 952 -0.1; 1019 0.1; 1090 0.4; 1167 0.5; 1248 0.3; 1336 0.0; 1429 0.1; 1529 -0.2; 1636 -0.7; 1751 -0.5; 1873 0.0; 2004 0.4; 2145 0.2; 2295 0.1; 2455 -0.7; 2627 -1.0; 2811 1.0; 3008 1.2; 3219 1.3; 3444 2.8; 3685 3.4; 3943 2.5; 4219 1.5; 4514 0.2; 4830 -0.2; 5168 3.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000003dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD RP18 Bass Light Version ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 46 Hz   |  0.13 | 6.1 dB  |
| Peaking | 217 Hz  |  1.33 | 2.8 dB  |
| Peaking | 415 Hz  |  0.52 | -1.8 dB |
| Peaking | 3619 Hz |  5.47 | 3.2 dB  |
| Peaking | 5940 Hz |  4.06 | 6.8 dB  |
| Peaking | 1154 Hz |  8.66 | 0.7 dB  |
| Peaking | 2548 Hz | 15.04 | -1.6 dB |
| Peaking | 4802 Hz |  9.38 | -2.8 dB |
| Peaking | 5315 Hz | 10.35 | 2.4 dB  |
| Peaking | 8237 Hz |  5.13 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NAD%20RP18%20Bass%20Light%20Version/NAD%20RP18%20Bass%20Light%20Version.png)