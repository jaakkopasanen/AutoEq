# V-Moda LP2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.5; 23 -2.9; 25 -3.3; 28 -3.7; 31 -4.0; 34 -4.3; 37 -4.4; 41 -4.6; 45 -4.8; 49 -4.9; 54 -5.0; 60 -5.1; 66 -5.3; 72 -5.2; 79 -4.8; 87 -4.9; 96 -6.2; 106 -6.8; 116 -6.9; 128 -6.8; 141 -7.0; 155 -6.9; 170 -6.4; 187 -6.5; 206 -5.8; 227 -4.9; 249 -3.5; 274 -2.7; 302 -0.9; 332 1.1; 365 2.6; 402 3.6; 442 4.4; 486 5.1; 535 5.3; 588 4.7; 647 3.4; 712 1.8; 783 0.6; 861 0.1; 947 -0.0; 1042 -0.0; 1146 0.0; 1261 0.1; 1387 -0.3; 1526 -0.2; 1678 0.0; 1846 0.7; 2031 1.2; 2234 0.6; 2457 -0.8; 2703 -1.2; 2973 -2.2; 3270 -0.8; 3597 1.4; 3957 3.4; 4353 4.7; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.1; 10263 -1.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda LP2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda LP2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.64 | -3.6 dB |
| Peaking | 158 Hz  | 0.65 | -7.0 dB |
| Peaking | 462 Hz  | 1.46 | 7.4 dB  |
| Peaking | 5314 Hz | 2.38 | 7.1 dB  |
| Peaking | 608 Hz  | 4.68 | 1.8 dB  |
| Peaking | 900 Hz  | 1.11 | -1.1 dB |
| Peaking | 2992 Hz | 2.91 | -5.7 dB |
| Peaking | 3208 Hz | 1.12 | 2.8 dB  |
| Peaking | 9464 Hz | 2.22 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20LP2/V-Moda%20LP2.png)