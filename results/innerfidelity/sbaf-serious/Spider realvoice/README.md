# Spider realvoice

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.7; 23 -4.7; 25 -4.6; 28 -4.5; 31 -4.4; 34 -4.4; 37 -4.3; 41 -4.2; 45 -4.1; 49 -4.0; 54 -4.0; 60 -3.9; 66 -3.8; 72 -3.9; 79 -3.9; 87 -3.9; 96 -3.9; 106 -3.8; 116 -3.6; 128 -3.5; 141 -3.4; 155 -3.2; 170 -2.9; 187 -2.7; 206 -2.4; 227 -2.0; 249 -1.9; 274 -1.6; 302 -1.3; 332 -1.0; 365 -0.7; 402 -0.5; 442 -0.2; 486 -0.1; 535 0.1; 588 0.5; 647 0.6; 712 1.1; 783 0.7; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.3; 1526 -1.9; 1678 -2.1; 1846 -1.8; 2031 -1.0; 2234 0.2; 2457 2.3; 2703 4.4; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.3; 4788 4.5; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider realvoice ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.19 | -4.5 dB |
| Peaking | 140 Hz  | 0.84 | -2.1 dB |
| Peaking | 1838 Hz | 1.95 | -4.1 dB |
| Peaking | 3298 Hz | 1.3  | 6.8 dB  |
| Peaking | 5794 Hz | 3.43 | 4.8 dB  |
| Peaking | 709 Hz  | 2.56 | 1.2 dB  |
| Peaking | 1395 Hz | 5.04 | -0.5 dB |
| Peaking | 8381 Hz | 3.82 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Spider%20realvoice/Spider%20realvoice.png)