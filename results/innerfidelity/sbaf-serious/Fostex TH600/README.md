# Fostex TH600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.3; 23 -3.5; 25 -3.8; 28 -4.1; 31 -4.4; 34 -4.6; 37 -4.7; 41 -4.8; 45 -4.9; 49 -4.9; 54 -4.7; 60 -4.4; 66 -4.8; 72 -5.1; 79 -5.4; 87 -5.5; 96 -5.7; 106 -5.7; 116 -5.5; 128 -5.5; 141 -5.4; 155 -5.2; 170 -4.6; 187 -4.4; 206 -4.0; 227 -3.4; 249 -2.9; 274 -2.3; 302 -1.6; 332 -0.7; 365 0.3; 402 1.5; 442 3.0; 486 3.7; 535 3.6; 588 3.2; 647 2.1; 712 1.0; 783 1.2; 861 1.1; 947 0.1; 1042 0.1; 1146 0.3; 1261 0.6; 1387 0.6; 1526 0.6; 1678 0.5; 1846 0.7; 2031 1.1; 2234 2.2; 2457 5.1; 2703 3.7; 2973 5.7; 3270 5.6; 3597 4.9; 3957 4.5; 4353 0.9; 4788 -1.4; 5267 -1.0; 5793 -2.3; 6373 -2.1; 7010 -2.1; 7711 -0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.4; 20000 -6.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.75 | -3.1 dB |
| Peaking | 125 Hz  | 0.47 | -5.4 dB |
| Peaking | 496 Hz  | 1.69 | 5.2 dB  |
| Peaking | 3065 Hz | 2.4  | 6.3 dB  |
| Peaking | 2473 Hz | 7.76 | 3.7 dB  |
| Peaking | 2679 Hz | 4.67 | -1.8 dB |
| Peaking | 3861 Hz | 6.62 | 3.4 dB  |
| Peaking | 5664 Hz | 1.77 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH600/Fostex%20TH600.png)