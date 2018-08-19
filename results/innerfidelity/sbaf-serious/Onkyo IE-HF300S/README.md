# Onkyo IE-HF300S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.5; 22 -0.9; 23 -1.0; 25 -1.3; 26 -1.5; 28 -1.7; 30 -1.9; 32 -2.1; 35 -2.4; 37 -2.6; 40 -2.8; 42 -2.9; 45 -3.1; 49 -3.4; 52 -3.6; 56 -3.8; 59 -4.0; 64 -4.2; 68 -4.4; 73 -4.7; 78 -4.9; 83 -5.1; 89 -5.4; 95 -5.7; 102 -5.9; 109 -6.0; 117 -6.0; 125 -6.2; 134 -6.3; 143 -6.4; 153 -6.4; 164 -6.4; 175 -6.2; 188 -6.1; 201 -6.0; 215 -5.8; 230 -5.6; 246 -5.4; 263 -5.2; 282 -4.9; 301 -4.6; 323 -4.2; 345 -3.8; 369 -3.5; 395 -3.2; 423 -2.7; 452 -2.4; 484 -2.0; 518 -1.7; 554 -1.2; 593 -0.7; 635 -0.4; 679 -0.3; 726 -0.1; 777 0.3; 832 0.3; 890 0.3; 952 0.1; 1019 0.0; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.3; 1529 -1.6; 1636 -1.8; 1751 -1.6; 1873 -1.3; 2004 -0.7; 2145 0.0; 2295 0.7; 2455 1.8; 2627 2.8; 2811 3.7; 3008 4.8; 3219 5.6; 3444 6.0; 3685 5.3; 3943 4.1; 4219 1.8; 4514 -0.3; 4830 -1.3; 5168 -1.1; 5530 -0.3; 5917 1.2; 6331 2.7; 6775 3.4; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -1.7; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.073824304914448dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Onkyo IE-HF300S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 103 Hz   | 0.49 | -5.1 dB |
| Peaking | 235 Hz   | 0.95 | -3.0 dB |
| Peaking | 1698 Hz  | 3.35 | -2.2 dB |
| Peaking | 3296 Hz  | 2.74 | 6.5 dB  |
| Peaking | 24000 Hz | 2.25 | 0.7 dB  |
| Peaking | 797 Hz   | 3.01 | 1.1 dB  |
| Peaking | 3907 Hz  | 6.63 | 2.0 dB  |
| Peaking | 4865 Hz  | 3.29 | -2.9 dB |
| Peaking | 6590 Hz  | 5.05 | 3.7 dB  |
| Peaking | 8972 Hz  | 7.34 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Onkyo%20IE-HF300S/Onkyo%20IE-HF300S.png)