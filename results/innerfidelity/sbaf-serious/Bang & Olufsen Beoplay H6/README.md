# Bang & Olufsen Beoplay H6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.9; 25 1.7; 28 1.4; 31 1.3; 34 1.2; 37 1.2; 41 1.2; 45 1.3; 49 1.5; 54 1.9; 60 2.4; 66 2.8; 72 3.0; 79 3.2; 87 3.6; 96 4.2; 106 4.4; 116 3.4; 128 1.9; 141 2.9; 155 4.7; 170 6.0; 187 3.8; 206 3.5; 227 4.3; 249 4.9; 274 5.5; 302 5.8; 332 5.8; 365 5.7; 402 5.5; 442 5.2; 486 4.5; 535 4.0; 588 3.7; 647 3.0; 712 2.2; 783 1.7; 861 0.8; 947 0.3; 1042 -0.1; 1146 -0.2; 1261 -0.3; 1387 -0.5; 1526 -0.7; 1678 -0.8; 1846 -0.4; 2031 0.2; 2234 1.7; 2457 4.2; 2703 4.5; 2973 4.8; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.5; 9330 -0.8; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.9  | 2.1 dB  |
| Peaking | 85 Hz   | 1.4  | 2.9 dB  |
| Peaking | 188 Hz  | 1.02 | 2.9 dB  |
| Peaking | 385 Hz  | 1.23 | 5.1 dB  |
| Peaking | 4269 Hz | 1.21 | 7.0 dB  |
| Peaking | 1856 Hz | 1.41 | -2.9 dB |
| Peaking | 2601 Hz | 2.09 | 3.6 dB  |
| Peaking | 6211 Hz | 2.71 | 6.9 dB  |
| Peaking | 6691 Hz | 1.17 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bang%20&%20Olufsen%20Beoplay%20H6/Bang%20&%20Olufsen%20Beoplay%20H6.png)