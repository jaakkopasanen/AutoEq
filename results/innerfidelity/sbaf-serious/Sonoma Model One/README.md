# Sonoma Model One

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 1.6; 22 1.4; 23 1.4; 25 1.3; 26 1.3; 28 1.3; 30 1.3; 32 1.3; 35 1.4; 37 1.4; 40 1.4; 42 1.5; 45 1.6; 49 1.7; 52 1.8; 56 2.0; 59 2.1; 64 1.9; 68 1.0; 73 -0.1; 78 -0.5; 83 -0.4; 89 -0.0; 95 0.2; 102 0.3; 109 0.4; 117 0.3; 125 0.4; 134 0.5; 143 0.6; 153 0.6; 164 0.6; 175 0.6; 188 0.5; 201 0.5; 215 0.6; 230 0.7; 246 0.6; 263 0.6; 282 0.6; 301 0.6; 323 0.5; 345 0.5; 369 0.5; 395 0.5; 423 0.7; 452 0.4; 484 -0.0; 518 -0.0; 554 0.2; 593 0.6; 635 -0.0; 679 -0.8; 726 -1.2; 777 -0.8; 832 -0.8; 890 -0.7; 952 -0.2; 1019 0.3; 1090 -0.3; 1167 -1.4; 1248 -2.4; 1336 -1.9; 1429 -3.0; 1529 -3.5; 1636 -2.3; 1751 -2.0; 1873 -1.1; 2004 -0.6; 2145 -1.5; 2295 -0.9; 2455 -0.3; 2627 -2.0; 2811 -1.0; 3008 -0.9; 3219 -1.6; 3444 -1.0; 3685 -0.6; 3943 0.1; 4219 0.1; 4514 0.1; 4830 0.0; 5168 -1.0; 5530 0.9; 5917 5.6; 6331 2.2; 6775 0.5; 7249 1.0; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.801150388429385dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sonoma Model One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 35 Hz   |  0.57 | 1.6 dB  |
| Peaking | 1433 Hz |  2.55 | -1.9 dB |
| Peaking | 1539 Hz |  4.3  | -1.4 dB |
| Peaking | 2920 Hz |  2.11 | -1.2 dB |
| Peaking | 5983 Hz | 10.93 | 6.3 dB  |
| Peaking | 63 Hz   |  3.47 | 1.9 dB  |
| Peaking | 75 Hz   |  2.54 | -2.0 dB |
| Peaking | 363 Hz  |  0.33 | 0.6 dB  |
| Peaking | 741 Hz  |  4.59 | -1.5 dB |
| Peaking | 1306 Hz |  2.54 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sonoma%20Model%20One/Sonoma%20Model%20One.png)