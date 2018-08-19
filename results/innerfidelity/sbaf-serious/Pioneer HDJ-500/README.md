# Pioneer HDJ-500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.6; 49 4.7; 52 4.1; 56 3.4; 59 3.0; 64 2.7; 68 2.6; 73 2.5; 78 2.2; 83 1.8; 89 1.8; 95 1.8; 102 1.7; 109 1.5; 117 1.4; 125 1.2; 134 1.0; 143 0.8; 153 0.5; 164 0.6; 175 0.4; 188 0.3; 201 0.2; 215 0.1; 230 0.3; 246 0.4; 263 0.3; 282 0.4; 301 0.2; 323 0.0; 345 -0.1; 369 -0.6; 395 -0.4; 423 0.0; 452 -0.0; 484 -0.4; 518 -0.7; 554 -0.8; 593 -0.7; 635 -0.7; 679 -0.7; 726 -0.7; 777 -0.6; 832 -0.4; 890 -0.3; 952 -0.2; 1019 0.1; 1090 0.4; 1167 0.9; 1248 1.4; 1336 1.5; 1429 1.9; 1529 2.4; 1636 2.8; 1751 3.5; 1873 4.6; 2004 5.6; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.7; 4830 0.4; 5168 -2.1; 5530 -2.0; 5917 0.1; 6331 -0.1; 6775 -1.6; 7249 0.9; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.5; 16326 -1.6; 17469 -1.2; 18692 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.57 | 6.4 dB  |
| Peaking | 912 Hz   | 0.8  | -2.2 dB |
| Peaking | 3692 Hz  | 0.51 | 9.3 dB  |
| Peaking | 5280 Hz  | 5.38 | -6.3 dB |
| Peaking | 6791 Hz  | 0.74 | -5.0 dB |
| Peaking | 2102 Hz  | 4.71 | 1.5 dB  |
| Peaking | 4144 Hz  | 0.57 | -0.9 dB |
| Peaking | 4405 Hz  | 7.53 | 2.7 dB  |
| Peaking | 8773 Hz  | 1.6  | 0.7 dB  |
| Peaking | 16825 Hz | 3.37 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20HDJ-500/Pioneer%20HDJ-500.png)