# Sony XBA-Z5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -3.7; 23 -3.9; 25 -4.0; 28 -4.2; 31 -4.4; 34 -4.5; 37 -4.6; 41 -4.7; 45 -4.9; 49 -5.0; 54 -5.2; 60 -5.5; 66 -5.8; 72 -6.0; 79 -6.3; 87 -6.6; 96 -6.9; 106 -7.1; 116 -7.1; 128 -7.2; 141 -7.3; 155 -7.2; 170 -7.0; 187 -6.8; 206 -6.5; 227 -6.1; 249 -5.7; 274 -5.1; 302 -4.6; 332 -4.1; 365 -3.4; 402 -3.0; 442 -2.5; 486 -2.2; 535 -1.7; 588 -1.0; 647 -0.5; 712 0.2; 783 0.5; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.3; 1261 -0.4; 1387 -0.7; 1526 -0.8; 1678 -0.6; 1846 -0.0; 2031 0.9; 2234 1.6; 2457 2.3; 2703 3.3; 2973 3.9; 3270 5.1; 3597 4.8; 3957 2.2; 4353 -0.3; 4788 -0.8; 5267 1.5; 5793 5.3; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.5; 10263 -4.6; 11289 -4.6; 12418 -2.3; 13660 -2.2; 15026 -1.1; 16529 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-Z5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 51 Hz    | 0.27 | -4.3 dB |
| Peaking | 174 Hz   | 0.63 | -4.7 dB |
| Peaking | 3183 Hz  | 2.82 | 5.3 dB  |
| Peaking | 6210 Hz  | 4.96 | 6.5 dB  |
| Peaking | 11010 Hz | 2.78 | -5.3 dB |
| Peaking | 777 Hz   | 3.39 | 1.4 dB  |
| Peaking | 1540 Hz  | 4.09 | -1.1 dB |
| Peaking | 4483 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4630 Hz  | 4.26 | -4.3 dB |
| Peaking | 22704 Hz | 0.45 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20XBA-Z5/Sony%20XBA-Z5.png)