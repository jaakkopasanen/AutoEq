# Audeze LCD-3 Rev 2 sn2613375

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.0; 22 4.3; 23 4.3; 25 4.3; 26 4.2; 28 3.9; 30 3.4; 32 3.0; 35 2.7; 37 2.8; 40 3.0; 42 3.0; 45 3.0; 49 2.7; 52 2.2; 56 1.7; 59 1.6; 64 1.7; 68 1.6; 73 1.6; 78 1.4; 83 1.2; 89 1.0; 95 0.7; 102 0.7; 109 0.6; 117 0.4; 125 0.2; 134 0.0; 143 -0.1; 153 -0.3; 164 -0.4; 175 -0.5; 188 -0.7; 201 -0.8; 215 -0.8; 230 -0.7; 246 -0.8; 263 -0.9; 282 -0.8; 301 -0.9; 323 -0.9; 345 -0.8; 369 -0.7; 395 -0.6; 423 -0.5; 452 -0.6; 484 -1.0; 518 -1.2; 554 -1.1; 593 -0.8; 635 -0.7; 679 -0.7; 726 -0.5; 777 -0.3; 832 -0.3; 890 -0.3; 952 -0.2; 1019 0.2; 1090 0.5; 1167 0.4; 1248 -0.0; 1336 -0.6; 1429 -1.0; 1529 -1.4; 1636 -1.3; 1751 -0.7; 1873 -0.3; 2004 -0.5; 2145 -0.5; 2295 0.2; 2455 0.9; 2627 1.8; 2811 1.7; 3008 1.8; 3219 2.4; 3444 4.5; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.7; 5168 5.3; 5530 5.2; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.8; 16326 -3.5; 17469 -5.5; 18692 -5.3; 20000 -1.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999813384082dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 Rev 2 sn2613375 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.35 | 4.1 dB  |
| Peaking | 49 Hz    | 1.36 | 2.0 dB  |
| Peaking | 4786 Hz  | 1.42 | 6.9 dB  |
| Peaking | 14773 Hz | 1.67 | 4.9 dB  |
| Peaking | 17141 Hz | 0.82 | -7.2 dB |
| Peaking | 347 Hz   | 0.71 | -1.0 dB |
| Peaking | 1677 Hz  | 2.6  | -1.6 dB |
| Peaking | 3704 Hz  | 6.03 | 2.6 dB  |
| Peaking | 6141 Hz  | 1.56 | -2.9 dB |
| Peaking | 6281 Hz  | 4.28 | 5.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20Rev%202%20sn2613375/Audeze%20LCD-3%20Rev%202%20sn2613375.png)