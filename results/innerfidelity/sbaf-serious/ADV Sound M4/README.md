# ADV Sound M4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.8; 23 -6.1; 25 -6.3; 28 -6.6; 31 -6.8; 34 -6.9; 37 -7.1; 41 -7.3; 45 -7.5; 49 -7.7; 54 -7.9; 60 -8.1; 66 -8.4; 72 -8.7; 79 -8.9; 87 -9.2; 96 -9.5; 106 -9.6; 116 -9.6; 128 -9.7; 141 -9.7; 155 -9.6; 170 -9.4; 187 -9.2; 206 -8.9; 227 -8.4; 249 -8.0; 274 -7.5; 302 -6.9; 332 -6.4; 365 -5.7; 402 -5.1; 442 -4.3; 486 -3.8; 535 -3.1; 588 -2.1; 647 -1.6; 712 -1.1; 783 -0.5; 861 -0.3; 947 -0.2; 1042 0.2; 1146 0.4; 1261 0.2; 1387 -0.1; 1526 -0.4; 1678 -0.4; 1846 0.1; 2031 0.6; 2234 1.0; 2457 0.6; 2703 0.5; 2973 3.0; 3270 5.1; 3597 6.0; 3957 5.7; 4353 3.8; 4788 3.2; 5267 3.4; 5793 2.2; 6373 -1.6; 7010 -5.9; 7711 -5.2; 8482 -1.8; 9330 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ADV Sound M4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ADV Sound M4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.27 | -6.4 dB |
| Peaking | 147 Hz  | 0.66 | -5.5 dB |
| Peaking | 309 Hz  | 1.06 | -3.2 dB |
| Peaking | 3899 Hz | 1.71 | 6.1 dB  |
| Peaking | 7282 Hz | 4.62 | -7.7 dB |
| Peaking | 997 Hz  | 2.5  | 0.9 dB  |
| Peaking | 2692 Hz | 5.57 | -1.8 dB |
| Peaking | 3414 Hz | 2.67 | 3.0 dB  |
| Peaking | 4133 Hz | 1.28 | -2.4 dB |
| Peaking | 5450 Hz | 4.59 | 2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ADV%20Sound%20M4/ADV%20Sound%20M4.png)