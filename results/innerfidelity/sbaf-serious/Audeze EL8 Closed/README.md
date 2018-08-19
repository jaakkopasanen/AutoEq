# Audeze EL8 Closed

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.3; 22 2.2; 23 2.2; 25 2.1; 26 2.1; 28 2.1; 30 2.1; 32 2.1; 35 2.2; 37 2.3; 40 2.3; 42 2.2; 45 2.3; 49 2.8; 52 3.1; 56 2.8; 59 2.1; 64 1.0; 68 0.6; 73 0.4; 78 0.1; 83 -0.1; 89 -0.4; 95 -0.7; 102 -0.9; 109 -0.9; 117 -0.8; 125 -0.6; 134 -0.1; 143 0.3; 153 0.8; 164 1.7; 175 1.4; 188 2.0; 201 2.5; 215 2.8; 230 3.2; 246 3.3; 263 3.5; 282 3.6; 301 3.4; 323 3.3; 345 3.3; 369 3.2; 395 3.0; 423 2.8; 452 2.6; 484 2.4; 518 2.2; 554 2.2; 593 2.2; 635 1.9; 679 1.5; 726 1.1; 777 1.0; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 0.1; 1167 -0.1; 1248 -0.5; 1336 -0.9; 1429 -1.3; 1529 -1.9; 1636 -2.4; 1751 -2.5; 1873 -2.5; 2004 -2.0; 2145 -1.5; 2295 -0.9; 2455 -0.2; 2627 0.2; 2811 -0.3; 3008 -0.7; 3219 -1.1; 3444 -1.5; 3685 -1.5; 3943 -1.4; 4219 -2.0; 4514 -3.7; 4830 -4.4; 5168 0.2; 5530 5.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.5; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -1.2; 15258 -2.9; 16326 -1.8; 17469 -0.2; 18692 -0.4; 20000 -3.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.052587415132024dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze EL8 Closed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 1.01 | 4.0 dB  |
| Peaking | 351 Hz   | 0.58 | 5.7 dB  |
| Peaking | 927 Hz   | 0.03 | -2.2 dB |
| Peaking | 4811 Hz  | 4.04 | -9.6 dB |
| Peaking | 5694 Hz  | 2.06 | 11.1 dB |
| Peaking | 54 Hz    | 5.14 | 1.6 dB  |
| Peaking | 110 Hz   | 3.71 | -1.2 dB |
| Peaking | 1782 Hz  | 4.63 | -1.5 dB |
| Peaking | 2609 Hz  | 5.48 | 1.7 dB  |
| Peaking | 12078 Hz | 3.91 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20EL8%20Closed/Audeze%20EL8%20Closed.png)