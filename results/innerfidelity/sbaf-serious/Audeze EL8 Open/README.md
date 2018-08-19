# Audeze EL8 Open

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.9; 23 5.9; 25 5.8; 26 5.7; 28 5.7; 30 5.6; 32 5.5; 35 5.5; 37 5.5; 40 5.4; 42 5.3; 45 5.1; 49 5.0; 52 5.0; 56 5.0; 59 4.7; 64 4.0; 68 3.7; 73 3.6; 78 3.5; 83 3.3; 89 3.1; 95 2.8; 102 2.5; 109 2.5; 117 2.4; 125 2.2; 134 2.0; 143 1.8; 153 1.7; 164 1.5; 175 1.4; 188 1.4; 201 1.2; 215 1.1; 230 1.2; 246 1.0; 263 0.9; 282 0.9; 301 0.9; 323 0.9; 345 1.1; 369 1.2; 395 1.2; 423 1.2; 452 1.1; 484 1.1; 518 1.1; 554 1.0; 593 1.2; 635 1.1; 679 0.8; 726 0.7; 777 0.6; 832 0.3; 890 0.2; 952 -0.0; 1019 0.1; 1090 -0.0; 1167 -0.5; 1248 -0.4; 1336 -0.3; 1429 -0.1; 1529 0.1; 1636 0.2; 1751 0.3; 1873 -0.4; 2004 -0.9; 2145 -1.3; 2295 -1.2; 2455 -0.4; 2627 1.3; 2811 2.5; 3008 2.3; 3219 2.3; 3444 3.6; 3685 4.2; 3943 5.0; 4219 4.1; 4514 3.5; 4830 1.3; 5168 1.4; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.127950789963807dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze EL8 Open ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.41 | 4.9 dB  |
| Peaking | 46 Hz   | 0.08 | 1.0 dB  |
| Peaking | 3817 Hz | 3.25 | 4.7 dB  |
| Peaking | 6113 Hz | 3.7  | 6.7 dB  |
| Peaking | 7696 Hz | 1.68 | -1.0 dB |
| Peaking | 568 Hz  | 2.33 | 0.6 dB  |
| Peaking | 1187 Hz | 4.48 | -0.8 dB |
| Peaking | 2247 Hz | 3.93 | -2.1 dB |
| Peaking | 2800 Hz | 6.42 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20EL8%20Open/Audeze%20EL8%20Open.png)