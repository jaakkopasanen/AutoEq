# Sleek SA1- Normal Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.3; 23 -5.4; 25 -5.5; 28 -5.6; 31 -5.6; 34 -5.7; 37 -5.7; 41 -5.8; 45 -5.9; 49 -6.1; 54 -6.3; 60 -6.6; 66 -6.9; 72 -7.2; 79 -7.5; 87 -7.8; 96 -7.9; 106 -8.2; 116 -8.2; 128 -8.5; 141 -8.5; 155 -8.6; 170 -8.5; 187 -8.5; 206 -8.2; 227 -8.0; 249 -7.7; 274 -7.3; 302 -6.8; 332 -6.2; 365 -5.6; 402 -4.9; 442 -4.4; 486 -3.9; 535 -3.2; 588 -2.5; 647 -1.8; 712 -1.1; 783 -0.6; 861 -0.2; 947 -0.1; 1042 0.1; 1146 0.2; 1261 0.2; 1387 0.3; 1526 0.3; 1678 0.5; 1846 1.2; 2031 1.9; 2234 2.7; 2457 3.5; 2703 4.4; 2973 6.0; 3270 6.0; 3597 6.0; 3957 4.6; 4353 1.6; 4788 -0.9; 5267 -3.1; 5793 -2.2; 6373 2.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sleek SA1- Normal Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sleek SA1- Normal Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.19 | -5.0 dB |
| Peaking | 136 Hz  | 0.64 | -4.4 dB |
| Peaking | 291 Hz  | 0.82 | -4.1 dB |
| Peaking | 3388 Hz | 1.26 | 6.6 dB  |
| Peaking | 5170 Hz | 4.2  | -6.2 dB |
| Peaking | 512 Hz  | 2.96 | -0.7 dB |
| Peaking | 854 Hz  | 1.57 | 0.7 dB  |
| Peaking | 1627 Hz | 3.89 | -0.7 dB |
| Peaking | 6532 Hz | 2.08 | -2.1 dB |
| Peaking | 6706 Hz | 6.01 | 5.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sleek%20SA1-%20Normal%20Filter/Sleek%20SA1-%20Normal%20Filter.png)