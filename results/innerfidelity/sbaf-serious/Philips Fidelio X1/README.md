# Philips Fidelio X1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 10 -84; 20 4.6; 22 3.5; 23 3.0; 25 2.0; 26 1.5; 28 0.7; 30 -0.2; 32 -0.9; 35 -2.0; 37 -2.6; 40 -3.5; 42 -4.1; 45 -4.8; 49 -5.7; 52 -6.2; 56 -6.8; 59 -7.0; 64 -7.3; 68 -7.4; 73 -7.5; 78 -7.5; 83 -7.4; 89 -7.4; 95 -7.4; 102 -7.2; 109 -6.8; 117 -6.5; 125 -6.4; 134 -6.2; 143 -6.1; 153 -5.9; 164 -5.6; 175 -5.5; 188 -6.2; 201 -5.9; 215 -5.4; 230 -4.9; 246 -4.6; 263 -4.4; 282 -4.1; 301 -3.8; 323 -3.6; 345 -3.3; 369 -3.0; 395 -2.8; 423 -2.6; 452 -2.4; 484 -2.5; 518 -2.4; 554 -2.0; 593 -1.8; 635 -1.8; 679 -1.7; 726 -1.7; 777 -1.4; 832 -1.2; 890 -0.5; 952 -0.2; 1019 0.1; 1090 0.1; 1167 0.5; 1248 0.6; 1336 -0.6; 1429 -1.8; 1529 -2.7; 1636 -3.2; 1751 -3.2; 1873 -3.0; 2004 -3.2; 2145 -2.9; 2295 -2.8; 2455 -2.7; 2627 -1.8; 2811 0.7; 3008 0.9; 3219 -0.5; 3444 -1.4; 3685 -1.8; 3943 -1.8; 4219 -2.7; 4514 -3.3; 4830 -3.2; 5168 -2.8; 5530 -3.5; 5917 -3.7; 6331 -2.4; 6775 -1.3; 7249 -2.4; 7756 -3.8; 8299 -5.8; 8880 -6.8; 9502 -5.1; 10167 -1.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.656910701532395dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio X1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.99 | 6.1 dB  |
| Peaking | 65 Hz    | 0.65 | -6.9 dB |
| Peaking | 206 Hz   | 0.56 | -3.8 dB |
| Peaking | 1960 Hz  | 2.08 | -3.3 dB |
| Peaking | 8397 Hz  | 2    | -5.6 dB |
| Peaking | 1173 Hz  | 5.04 | 1.9 dB  |
| Peaking | 2929 Hz  | 6.83 | 3.4 dB  |
| Peaking | 7034 Hz  | 0.85 | -5.2 dB |
| Peaking | 7201 Hz  | 2.96 | 6.5 dB  |
| Peaking | 11083 Hz | 1.91 | 3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20X1/Philips%20Fidelio%20X1.png)