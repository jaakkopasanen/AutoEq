# Audeze SINE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 10 -84; 20 5.0; 22 4.2; 23 3.9; 25 3.3; 26 3.1; 28 2.6; 30 2.2; 32 1.9; 35 1.5; 37 1.3; 40 1.1; 42 1.0; 45 0.8; 49 0.5; 52 0.4; 56 0.3; 59 0.2; 64 0.0; 68 -0.1; 73 -0.3; 78 -0.5; 83 -0.7; 89 -0.9; 95 -1.3; 102 -1.5; 109 -1.5; 117 -1.7; 125 -2.0; 134 -2.1; 143 -2.2; 153 -2.3; 164 -2.3; 175 -2.4; 188 -2.5; 201 -2.6; 215 -2.5; 230 -2.4; 246 -2.2; 263 -2.1; 282 -2.1; 301 -2.1; 323 -2.1; 345 -2.0; 369 -1.9; 395 -1.8; 423 -1.7; 452 -1.5; 484 -1.4; 518 -1.2; 554 -0.8; 593 -0.5; 635 -0.1; 679 0.1; 726 0.4; 777 0.5; 832 0.4; 890 0.4; 952 0.2; 1019 -0.0; 1090 0.3; 1167 0.3; 1248 -0.2; 1336 -1.0; 1429 -1.3; 1529 -1.6; 1636 -2.2; 1751 -2.4; 1873 -2.4; 2004 -2.3; 2145 -2.3; 2295 -1.8; 2455 -1.0; 2627 -1.4; 2811 -1.6; 3008 -1.4; 3219 -0.9; 3444 -0.9; 3685 -0.9; 3943 0.4; 4219 0.9; 4514 1.2; 4830 2.3; 5168 3.3; 5530 3.7; 5917 4.1; 6331 3.5; 6775 3.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.4; 10167 -1.8; 10879 -1.1; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -1.7; 17469 -3.2; 18692 -2.7; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.058309070025588dB` and instead set Global volume in the UI for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze SINE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.84 | 5.8 dB  |
| Peaking | 197 Hz   | 0.67 | -2.7 dB |
| Peaking | 2083 Hz  | 1.59 | -2.5 dB |
| Peaking | 5785 Hz  | 2.85 | 4.6 dB  |
| Peaking | 17907 Hz | 2.14 | -3.6 dB |
| Peaking | 475 Hz   | 1.44 | -1.5 dB |
| Peaking | 705 Hz   | 0.83 | 1.5 dB  |
| Peaking | 1465 Hz  | 3    | -0.3 dB |
| Peaking | 1656 Hz  | 4.19 | -0.8 dB |
| Peaking | 10272 Hz | 6.66 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20SINE/Audeze%20SINE.png)