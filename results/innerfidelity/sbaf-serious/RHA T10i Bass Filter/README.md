# RHA T10i Bass Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -9.9; 23 -10.0; 25 -10.2; 28 -10.4; 31 -10.6; 34 -10.8; 37 -10.9; 41 -10.9; 45 -10.9; 49 -11.1; 54 -11.1; 60 -11.1; 66 -11.2; 72 -11.2; 79 -11.4; 87 -11.4; 96 -11.5; 106 -11.2; 116 -11.0; 128 -10.9; 141 -10.7; 155 -10.4; 170 -10.1; 187 -9.6; 206 -9.1; 227 -8.5; 249 -8.0; 274 -7.3; 302 -6.7; 332 -6.0; 365 -5.4; 402 -4.7; 442 -3.9; 486 -3.4; 535 -2.8; 588 -1.9; 647 -1.3; 712 -1.2; 783 -0.5; 861 -0.1; 947 0.3; 1042 -0.1; 1146 -0.4; 1261 -0.8; 1387 -1.5; 1526 -2.4; 1678 -3.1; 1846 -3.5; 2031 -3.6; 2234 -3.4; 2457 -2.3; 2703 -0.9; 2973 0.7; 3270 1.4; 3597 1.2; 3957 2.4; 4353 4.3; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.6; 8482 -9.0; 9330 -11.5; 10263 -9.1; 11289 -1.0; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T10i Bass Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T10i Bass Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.23 | -10.5 dB |
| Peaking | 188 Hz   | 0.61 | -4.8 dB  |
| Peaking | 2062 Hz  | 2.02 | -4.6 dB  |
| Peaking | 5850 Hz  | 1.18 | 8.5 dB   |
| Peaking | 9162 Hz  | 2.95 | -16.1 dB |
| Peaking | 935 Hz   | 2.3  | 1.5 dB   |
| Peaking | 1774 Hz  | 1.85 | -1.2 dB  |
| Peaking | 1986 Hz  | 4.68 | 1.4 dB   |
| Peaking | 10390 Hz | 6.83 | -4.5 dB  |
| Peaking | 11502 Hz | 3.07 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T10i%20Bass%20Filter/RHA%20T10i%20Bass%20Filter.png)