# Ortofon 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.9; 60 5.7; 66 6.0; 72 6.0; 79 5.9; 87 5.2; 96 5.2; 106 5.3; 116 5.5; 128 5.4; 141 5.2; 155 5.2; 170 5.5; 187 5.3; 206 4.8; 227 4.6; 249 3.2; 274 2.0; 302 0.3; 332 -1.1; 365 -1.8; 402 -1.5; 442 -1.1; 486 -0.8; 535 -0.6; 588 -0.3; 647 0.1; 712 0.2; 783 0.4; 861 0.3; 947 0.1; 1042 -0.1; 1146 0.0; 1261 0.6; 1387 0.5; 1526 0.4; 1678 -0.6; 1846 -1.1; 2031 -0.4; 2234 0.7; 2457 2.1; 2703 3.4; 2973 3.3; 3270 2.8; 3597 4.2; 3957 3.1; 4353 5.8; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -3.3; 10263 -4.0; 11289 -0.7; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.38 | 6.5 dB  |
| Peaking | 171 Hz  | 1.81 | 3.8 dB  |
| Peaking | 4457 Hz | 1.29 | 4.8 dB  |
| Peaking | 5962 Hz | 3.25 | 3.6 dB  |
| Peaking | 9842 Hz | 3.87 | -5.4 dB |
| Peaking | 19 Hz   | 2.62 | 1.0 dB  |
| Peaking | 241 Hz  | 3.22 | 2.0 dB  |
| Peaking | 365 Hz  | 2.01 | -3.0 dB |
| Peaking | 1863 Hz | 4.82 | -1.9 dB |
| Peaking | 2732 Hz | 6.36 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ortofon%202/Ortofon%202.png)