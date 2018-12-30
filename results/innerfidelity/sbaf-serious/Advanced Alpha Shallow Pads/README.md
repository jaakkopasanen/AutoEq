# Advanced Alpha Shallow Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 21 0.0; 23 1.1; 25 1.1; 28 1.1; 31 1.2; 34 1.2; 37 1.3; 41 1.2; 45 1.2; 49 1.2; 54 1.2; 60 1.0; 66 0.9; 72 0.8; 79 0.8; 87 0.3; 96 -0.2; 106 -0.5; 116 -0.8; 128 -1.3; 141 -1.6; 155 -2.0; 170 -2.1; 187 -2.4; 206 -2.5; 227 -2.6; 249 -2.7; 274 -2.8; 302 -2.5; 332 -2.5; 365 -2.3; 402 -1.9; 442 -1.4; 486 -1.2; 535 -1.2; 588 -0.3; 647 -0.0; 712 0.1; 783 0.2; 861 -0.0; 947 -0.2; 1042 -0.0; 1146 -0.2; 1261 -0.5; 1387 0.3; 1526 0.2; 1678 0.0; 1846 1.2; 2031 -0.9; 2234 -3.0; 2457 -4.8; 2703 -6.4; 2973 -7.0; 3270 -5.6; 3597 -4.3; 3957 -1.1; 4353 3.7; 4788 -1.9; 5267 -2.4; 5793 -0.1; 6373 -0.2; 7010 0.2; 7711 -0.7; 8482 -2.6; 9330 -2.9; 10263 -0.4; 11289 0.0; 12418 0.0; 13660 -2.5; 15026 -3.7; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced Alpha Shallow Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-39**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced Alpha Shallow Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 251 Hz   | 1.03 | -3.0 dB |
| Peaking | 2907 Hz  | 2.99 | -7.7 dB |
| Peaking | 14312 Hz | 3.53 | -1.8 dB |
| Peaking | 14630 Hz | 4.42 | -3.0 dB |
| Peaking | 22050 Hz | 2.06 | -0.4 dB |
| Peaking | 40 Hz    | 0.86 | 1.5 dB  |
| Peaking | 1978 Hz  | 2.59 | 2.5 dB  |
| Peaking | 2258 Hz  | 4.13 | -2.8 dB |
| Peaking | 9019 Hz  | 3.36 | -4.7 dB |
| Peaking | 9603 Hz  | 1.16 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Advanced%20Alpha%20Shallow%20Pads/Advanced%20Alpha%20Shallow%20Pads.png)