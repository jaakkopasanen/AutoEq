# Read Heath Audio MA600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 10 -84; 20 -10.3; 22 -10.4; 23 -10.5; 25 -10.6; 26 -10.6; 28 -10.7; 30 -10.8; 32 -10.9; 35 -11.0; 37 -11.0; 40 -11.1; 42 -11.1; 45 -11.2; 49 -11.3; 52 -11.4; 56 -11.5; 59 -11.6; 64 -11.8; 68 -11.9; 73 -12.0; 78 -12.2; 83 -12.3; 89 -12.4; 95 -12.6; 102 -12.6; 109 -12.6; 117 -12.5; 125 -12.5; 134 -12.5; 143 -12.4; 153 -12.3; 164 -12.1; 175 -11.9; 188 -11.6; 201 -11.4; 215 -11.0; 230 -10.6; 246 -10.2; 263 -9.9; 282 -9.4; 301 -8.9; 323 -8.5; 345 -7.9; 369 -7.4; 395 -6.9; 423 -6.2; 452 -5.7; 484 -5.2; 518 -4.6; 554 -4.0; 593 -3.2; 635 -2.6; 679 -2.2; 726 -1.7; 777 -1.1; 832 -0.7; 890 -0.4; 952 -0.1; 1019 0.1; 1090 0.2; 1167 0.6; 1248 0.7; 1336 0.7; 1429 0.7; 1529 1.5; 1636 1.4; 1751 1.4; 1873 0.7; 2004 -0.2; 2145 -1.0; 2295 -1.2; 2455 -0.7; 2627 -0.5; 2811 -0.7; 3008 -1.0; 3219 -1.6; 3444 -2.5; 3685 -3.7; 3943 -5.0; 4219 -7.4; 4514 -9.9; 4830 -11.9; 5168 -10.5; 5530 -6.6; 5917 -2.4; 6331 0.4; 6775 2.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.4; 10167 -3.0; 10879 -4.0; 11640 -2.2; 12455 -0.7; 13327 -2.8; 14260 -7.2; 15258 -9.2; 16326 -7.7; 17469 -4.7; 18692 -1.8; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.3737138555321566dB` and instead set Global volume in the UI for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Read Heath Audio MA600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.22 | -10.3 dB |
| Peaking | 155 Hz   | 0.68 | -6.6 dB  |
| Peaking | 335 Hz   | 1.26 | -3.8 dB  |
| Peaking | 4795 Hz  | 4.03 | -12.8 dB |
| Peaking | 15577 Hz | 2.11 | -9.8 dB  |
| Peaking | 1426 Hz  | 1.8  | 1.8 dB   |
| Peaking | 3896 Hz  | 3.48 | -1.8 dB  |
| Peaking | 5438 Hz  | 6.67 | -3.8 dB  |
| Peaking | 6562 Hz  | 2.21 | 3.9 dB   |
| Peaking | 10644 Hz | 8    | -3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Read%20Heath%20Audio%20MA600/Read%20Heath%20Audio%20MA600.png)