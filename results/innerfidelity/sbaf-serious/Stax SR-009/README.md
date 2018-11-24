# Stax SR-009

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.6; 66 4.5; 72 4.5; 79 4.7; 87 4.5; 96 4.3; 106 4.2; 116 4.0; 128 3.7; 141 3.6; 155 3.4; 170 3.1; 187 3.0; 206 2.9; 227 3.0; 249 2.8; 274 2.8; 302 2.7; 332 2.6; 365 2.5; 402 2.4; 442 2.3; 486 1.9; 535 1.8; 588 2.0; 647 1.7; 712 1.6; 783 1.9; 861 1.3; 947 0.6; 1042 -0.0; 1146 -0.6; 1261 -0.4; 1387 0.0; 1526 -0.1; 1678 -0.1; 1846 1.7; 2031 3.0; 2234 3.6; 2457 4.9; 2703 4.1; 2973 4.1; 3270 3.6; 3597 3.7; 3957 2.0; 4353 0.8; 4788 -1.2; 5267 0.5; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-009 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.13 | 6.1 dB  |
| Peaking | 381 Hz  | 0.85 | 1.8 dB  |
| Peaking | 2780 Hz | 1.74 | 4.7 dB  |
| Peaking | 4951 Hz | 5.44 | -4.0 dB |
| Peaking | 6011 Hz | 4.15 | 6.7 dB  |
| Peaking | 795 Hz  | 2.57 | 1.5 dB  |
| Peaking | 1293 Hz | 1.11 | -1.6 dB |
| Peaking | 2138 Hz | 3.36 | 1.5 dB  |
| Peaking | 6784 Hz | 7.94 | 1.5 dB  |
| Peaking | 7764 Hz | 2.9  | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-009/Stax%20SR-009.png)