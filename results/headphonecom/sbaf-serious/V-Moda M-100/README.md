# V-Moda M-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.5; 23 -2.8; 25 -3.0; 28 -3.3; 31 -3.4; 34 -3.5; 37 -3.6; 41 -3.8; 45 -3.9; 49 -4.0; 54 -4.1; 60 -4.2; 66 -4.3; 72 -4.2; 79 -4.2; 87 -5.2; 96 -4.9; 106 -4.6; 116 -5.3; 128 -5.5; 141 -5.5; 155 -5.1; 170 -4.3; 187 -4.1; 206 -3.2; 227 -2.1; 249 -1.0; 274 0.3; 302 0.4; 332 2.4; 365 3.4; 402 3.8; 442 3.7; 486 3.5; 535 3.2; 588 2.8; 647 2.1; 712 1.4; 783 0.8; 861 0.3; 947 -0.0; 1042 -0.2; 1146 0.0; 1261 0.3; 1387 0.4; 1526 0.5; 1678 0.5; 1846 0.7; 2031 0.4; 2234 0.2; 2457 0.6; 2703 0.7; 2973 1.4; 3270 2.0; 3597 1.6; 3957 1.5; 4353 2.6; 4788 5.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.6; 9330 -4.0; 10263 -3.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda M-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda M-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.37 | -3.4 dB |
| Peaking | 151 Hz  | 0.89 | -4.2 dB |
| Peaking | 415 Hz  | 1.28 | 5.1 dB  |
| Peaking | 5544 Hz | 1.89 | 6.8 dB  |
| Peaking | 9518 Hz | 3.91 | -5.5 dB |
| Peaking | 598 Hz  | 6.08 | 0.7 dB  |
| Peaking | 975 Hz  | 2.83 | -0.9 dB |
| Peaking | 1685 Hz | 0.56 | 0.1 dB  |
| Peaking | 3235 Hz | 6.68 | 1.0 dB  |
| Peaking | 3877 Hz | 6.72 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20M-100/V-Moda%20M-100.png)