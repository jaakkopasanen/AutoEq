# Fischer Audio Tandem

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.9; 52 5.7; 56 5.1; 59 4.7; 64 4.1; 68 3.7; 73 3.2; 78 2.7; 83 2.1; 89 1.7; 95 1.1; 102 0.7; 109 0.4; 117 0.1; 125 -0.4; 134 -0.7; 143 -0.9; 153 -1.2; 164 -1.4; 175 -1.5; 188 -1.7; 201 -1.8; 215 -1.8; 230 -1.9; 246 -2.0; 263 -1.9; 282 -1.9; 301 -1.8; 323 -1.7; 345 -1.7; 369 -1.5; 395 -1.4; 423 -1.2; 452 -1.0; 484 -1.0; 518 -0.9; 554 -0.6; 593 -0.2; 635 -0.0; 679 -0.1; 726 0.0; 777 0.1; 832 0.3; 890 0.2; 952 0.2; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.1; 1336 0.0; 1429 0.1; 1529 0.2; 1636 0.3; 1751 0.7; 1873 1.3; 2004 2.1; 2145 2.9; 2295 3.8; 2455 5.2; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.9; 4219 3.7; 4514 2.3; 4830 3.3; 5168 5.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Tandem ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.37 | 7.3 dB  |
| Peaking | 148 Hz  | 0.45 | -3.9 dB |
| Peaking | 3081 Hz | 1.61 | 6.6 dB  |
| Peaking | 5837 Hz | 3.56 | 5.6 dB  |
| Peaking | 821 Hz  | 1.65 | 1.1 dB  |
| Peaking | 1237 Hz | 0.91 | -1.0 dB |
| Peaking | 2458 Hz | 6.25 | 1.4 dB  |
| Peaking | 6596 Hz | 8.47 | 1.9 dB  |
| Peaking | 7850 Hz | 2.42 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20Tandem/Fischer%20Audio%20Tandem.png)