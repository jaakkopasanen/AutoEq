# Radius HP-TWF31

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.4; 22 -0.5; 23 -0.6; 25 -0.8; 26 -0.8; 28 -0.9; 30 -1.0; 32 -1.1; 35 -1.3; 37 -1.4; 40 -1.5; 42 -1.6; 45 -1.7; 49 -1.9; 52 -2.0; 56 -2.2; 59 -2.3; 64 -2.6; 68 -2.8; 73 -3.1; 78 -3.3; 83 -3.6; 89 -3.9; 95 -4.2; 102 -4.5; 109 -4.6; 117 -4.8; 125 -5.0; 134 -5.2; 143 -5.3; 153 -5.5; 164 -5.6; 175 -5.6; 188 -5.7; 201 -5.7; 215 -5.7; 230 -5.6; 246 -5.6; 263 -5.5; 282 -5.3; 301 -5.2; 323 -5.0; 345 -4.7; 369 -4.4; 395 -4.3; 423 -4.0; 452 -3.7; 484 -3.4; 518 -3.0; 554 -2.4; 593 -1.8; 635 -1.6; 679 -1.5; 726 -1.1; 777 -0.6; 832 -0.3; 890 -0.1; 952 0.0; 1019 0.1; 1090 0.2; 1167 0.2; 1248 0.3; 1336 0.2; 1429 -0.0; 1529 -0.2; 1636 -0.2; 1751 0.0; 1873 0.3; 2004 0.6; 2145 0.9; 2295 1.3; 2455 1.9; 2627 2.3; 2811 3.5; 3008 4.0; 3219 4.4; 3444 4.6; 3685 4.0; 3943 2.9; 4219 1.3; 4514 0.8; 4830 2.2; 5168 4.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.2; 9502 -2.8; 10167 -3.2; 10879 -1.5; 11640 -0.1; 12455 -0.2; 13327 -0.9; 14260 -1.4; 15258 -2.6; 16326 -4.0; 17469 -4.2; 18692 -2.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.088006189830303dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-TWF31 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 148 Hz   | 0.53 | -5.0 dB |
| Peaking | 338 Hz   | 1.11 | -2.5 dB |
| Peaking | 3189 Hz  | 2.42 | 4.7 dB  |
| Peaking | 5949 Hz  | 3.1  | 7.1 dB  |
| Peaking | 16201 Hz | 0.36 | -2.5 dB |
| Peaking | 987 Hz   | 2.78 | 0.8 dB  |
| Peaking | 8816 Hz  | 7.54 | 1.8 dB  |
| Peaking | 9848 Hz  | 3.1  | -4.3 dB |
| Peaking | 11787 Hz | 1.65 | 2.9 dB  |
| Peaking | 16932 Hz | 3.32 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-TWF31/Radius%20HP-TWF31.png)