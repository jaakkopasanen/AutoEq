# Blue MOFI Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.6; 22 1.5; 23 1.4; 25 1.3; 26 1.3; 28 1.2; 30 1.2; 32 1.1; 35 1.0; 37 1.0; 40 0.9; 42 0.9; 45 0.9; 49 0.8; 52 0.8; 56 0.7; 59 0.6; 64 0.4; 68 0.3; 73 0.1; 78 -0.0; 83 -0.2; 89 -0.4; 95 -0.7; 102 -0.9; 109 -0.9; 117 -0.8; 125 -0.9; 134 -1.2; 143 -1.7; 153 -2.0; 164 -1.5; 175 -1.1; 188 -1.7; 201 -1.8; 215 -1.5; 230 -1.0; 246 -0.6; 263 0.0; 282 0.9; 301 1.5; 323 1.9; 345 1.5; 369 1.4; 395 1.3; 423 2.3; 452 3.1; 484 3.3; 518 2.9; 554 2.6; 593 2.6; 635 2.5; 679 2.1; 726 1.6; 777 1.4; 832 1.2; 890 0.6; 952 0.2; 1019 -0.1; 1090 -0.2; 1167 -0.1; 1248 -0.1; 1336 -0.1; 1429 -0.4; 1529 -0.6; 1636 -0.6; 1751 -0.4; 1873 0.1; 2004 1.1; 2145 1.8; 2295 2.2; 2455 2.5; 2627 3.5; 2811 4.1; 3008 4.4; 3219 4.5; 3444 5.6; 3685 6.0; 3943 4.5; 4219 0.2; 4514 3.1; 4830 5.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999857591355dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue MOFI Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 189 Hz  | 1.16 | -2.1 dB |
| Peaking | 308 Hz  | 3.42 | 1.9 dB  |
| Peaking | 516 Hz  | 1.83 | 3.4 dB  |
| Peaking | 3265 Hz | 2.29 | 5.0 dB  |
| Peaking | 5670 Hz | 2.96 | 6.2 dB  |
| Peaking | 24 Hz   | 1.12 | 1.5 dB  |
| Peaking | 50 Hz   | 2.17 | 0.7 dB  |
| Peaking | 1716 Hz | 2.01 | -1.8 dB |
| Peaking | 2162 Hz | 2.63 | 1.6 dB  |
| Peaking | 8189 Hz | 4.67 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20MOFI%20Passive/Blue%20MOFI%20Passive.png)