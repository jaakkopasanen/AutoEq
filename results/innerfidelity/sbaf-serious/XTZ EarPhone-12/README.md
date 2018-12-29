# XTZ EarPhone-12
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 -0.1; 23 -0.6; 25 -1.0; 28 -1.6; 31 -2.1; 34 -2.5; 37 -2.9; 41 -3.3; 45 -3.7; 49 -4.0; 54 -4.4; 60 -4.9; 66 -5.3; 72 -5.6; 79 -6.0; 87 -6.4; 96 -6.8; 106 -7.0; 116 -7.1; 128 -7.2; 141 -7.3; 155 -7.3; 170 -7.1; 187 -7.0; 206 -6.7; 227 -6.3; 249 -6.0; 274 -5.5; 302 -5.0; 332 -4.5; 365 -4.0; 402 -3.4; 442 -2.7; 486 -2.2; 535 -1.6; 588 -0.8; 647 -0.3; 712 0.0; 783 0.6; 861 0.6; 947 0.3; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.2; 1526 -1.8; 1678 -2.5; 1846 -2.9; 2031 -3.4; 2234 -3.3; 2457 -2.6; 2703 -1.5; 2973 0.6; 3270 2.5; 3597 3.6; 3957 2.9; 4353 0.9; 4788 0.5; 5267 1.3; 5793 2.5; 6373 3.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`XTZ EarPhone-12 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `XTZ EarPhone-12 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 103 Hz  | 0.54 | -6.3 dB |
| Peaking | 240 Hz  | 1.04 | -3.3 dB |
| Peaking | 2138 Hz | 2.05 | -3.9 dB |
| Peaking | 3557 Hz | 3.57 | 4.5 dB  |
| Peaking | 6407 Hz | 4.57 | 3.9 dB  |
| Peaking | 16 Hz   | 0.36 | 1.1 dB  |
| Peaking | 38 Hz   | 1.32 | -1.2 dB |
| Peaking | 404 Hz  | 2.56 | -0.7 dB |
| Peaking | 803 Hz  | 1.99 | 1.5 dB  |
| Peaking | 1572 Hz | 4.04 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/XTZ%20EarPhone-12/XTZ%20EarPhone-12.png)