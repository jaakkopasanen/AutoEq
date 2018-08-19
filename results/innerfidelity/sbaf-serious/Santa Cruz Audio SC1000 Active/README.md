# Santa Cruz Audio SC1000 Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.7; 22 5.6; 23 5.5; 25 5.3; 26 5.3; 28 5.2; 30 5.1; 32 5.0; 35 4.8; 37 4.7; 40 4.6; 42 4.5; 45 4.4; 49 4.2; 52 4.1; 56 3.9; 59 3.7; 64 3.4; 68 3.1; 73 2.9; 78 2.6; 83 2.5; 89 2.2; 95 1.9; 102 1.6; 109 1.5; 117 1.3; 125 1.0; 134 0.8; 143 0.7; 153 0.6; 164 0.4; 175 0.3; 188 0.3; 201 0.3; 215 0.3; 230 0.3; 246 0.3; 263 0.2; 282 0.2; 301 0.2; 323 0.2; 345 0.2; 369 0.3; 395 0.3; 423 0.6; 452 0.7; 484 0.6; 518 0.6; 554 0.9; 593 1.0; 635 1.1; 679 0.9; 726 0.8; 777 0.9; 832 0.6; 890 0.3; 952 0.1; 1019 0.0; 1090 0.0; 1167 0.0; 1248 -0.1; 1336 -0.5; 1429 -0.9; 1529 -1.3; 1636 -1.7; 1751 -1.8; 1873 -1.8; 2004 -1.8; 2145 -1.9; 2295 -1.9; 2455 -1.9; 2627 -2.1; 2811 -2.1; 3008 -1.3; 3219 0.0; 3444 1.6; 3685 2.3; 3943 1.9; 4219 0.1; 4514 -1.9; 4830 -2.5; 5168 0.8; 5530 5.1; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.9; 8880 -2.2; 9502 -1.9; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0638661943366365dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Santa Cruz Audio SC1000 Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.63 | 4.9 dB  |
| Peaking | 50 Hz   | 0.71 | 2.7 dB  |
| Peaking | 3746 Hz | 2.97 | 9.1 dB  |
| Peaking | 4572 Hz | 0.96 | -9.7 dB |
| Peaking | 5951 Hz | 2.68 | 13.0 dB |
| Peaking | 659 Hz  | 1.61 | 1.2 dB  |
| Peaking | 1266 Hz | 2.85 | 1.0 dB  |
| Peaking | 1553 Hz | 1.63 | -1.0 dB |
| Peaking | 9100 Hz | 4.11 | -3.3 dB |
| Peaking | 9676 Hz | 1.31 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Santa%20Cruz%20Audio%20SC1000%20Active/Santa%20Cruz%20Audio%20SC1000%20Active.png)