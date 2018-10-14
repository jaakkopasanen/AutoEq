# Monster Beats by Dr

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 4.2; 31 1.3; 34 -0.9; 37 -1.7; 41 -2.3; 45 -2.7; 49 -2.7; 54 -2.4; 60 -2.6; 66 -3.0; 72 -3.4; 79 -3.7; 87 -3.9; 96 -4.1; 106 -4.3; 116 -4.5; 128 -4.5; 141 -4.7; 155 -4.9; 170 -4.6; 187 -4.7; 206 -4.0; 227 -3.8; 249 -3.7; 274 -3.6; 302 -3.3; 332 -2.9; 365 -2.4; 402 -2.2; 442 -1.6; 486 -0.9; 535 0.1; 588 1.3; 647 2.6; 712 3.2; 783 3.1; 861 2.3; 947 0.8; 1042 -0.5; 1146 -1.7; 1261 -3.0; 1387 -4.7; 1526 -6.5; 1678 -7.6; 1846 -7.9; 2031 -7.3; 2234 -5.5; 2457 -3.1; 2703 -0.4; 2973 1.5; 3270 3.4; 3597 3.3; 3957 5.4; 4353 1.3; 4788 -2.2; 5267 -3.3; 5793 0.1; 6373 4.2; 7010 2.5; 7711 -2.1; 8482 -6.7; 9330 -6.1; 10263 -0.9; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats by Dr ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 2.59 | 7.1 dB  |
| Peaking | 125 Hz  | 0.57 | -5.0 dB |
| Peaking | 1832 Hz | 2.35 | -9.1 dB |
| Peaking | 3604 Hz | 3.16 | 5.6 dB  |
| Peaking | 8857 Hz | 5.78 | -8.3 dB |
| Peaking | 16 Hz   | 2.65 | 1.5 dB  |
| Peaking | 747 Hz  | 2.69 | 4.6 dB  |
| Peaking | 1402 Hz | 4.42 | -1.9 dB |
| Peaking | 5163 Hz | 5.64 | -4.4 dB |
| Peaking | 6572 Hz | 6.74 | 5.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Beats%20by%20Dr/Monster%20Beats%20by%20Dr.png)