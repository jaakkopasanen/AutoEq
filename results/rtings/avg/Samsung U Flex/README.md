# Samsung U Flex
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -0.7; 31 -0.8; 34 -0.9; 37 -1.0; 41 -1.1; 45 -1.2; 49 -1.3; 54 -1.4; 60 -1.8; 66 -2.2; 72 -2.5; 79 -2.9; 87 -3.4; 96 -3.9; 106 -4.6; 116 -5.2; 128 -5.8; 141 -6.2; 155 -6.5; 170 -6.6; 187 -6.6; 206 -6.8; 227 -6.9; 249 -6.7; 274 -6.4; 302 -6.0; 332 -5.8; 365 -5.4; 402 -5.2; 442 -4.8; 486 -4.5; 535 -4.0; 588 -3.5; 647 -3.1; 712 -2.7; 783 -2.4; 861 -2.4; 947 -2.7; 1042 -3.7; 1146 -4.8; 1261 -5.8; 1387 -6.4; 1526 -7.0; 1678 -7.5; 1846 -8.1; 2031 -8.6; 2234 -8.7; 2457 -8.9; 2703 -10.0; 2973 -10.9; 3270 -11.0; 3597 -10.8; 3957 -10.6; 4353 -10.6; 4788 -9.8; 5267 -9.4; 5793 -8.5; 6373 -6.8; 7010 -4.4; 7711 -6.2; 8482 -6.6; 9330 -11.2; 10263 -13.3; 11289 -12.3; 12418 -10.7; 13660 -9.2; 15026 -11.3; 16529 -15.3; 18182 -14.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung U Flex GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung U Flex ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.54 | 5.7 dB  |
| Peaking | 62 Hz    | 1.24 | 2.5 dB  |
| Peaking | 3458 Hz  | 1.65 | -5.0 dB |
| Peaking | 10449 Hz | 3.69 | -6.4 dB |
| Peaking | 17286 Hz | 1.2  | -9.7 dB |
| Peaking | 204 Hz   | 1.31 | -1.2 dB |
| Peaking | 841 Hz   | 0.9  | 4.9 dB  |
| Peaking | 1578 Hz  | 1.13 | -2.4 dB |
| Peaking | 5472 Hz  | 2.8  | -1.8 dB |
| Peaking | 7015 Hz  | 3.85 | 3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 3.9 dB   |
| Peaking | 125 Hz   | 1.41 | 0.1 dB   |
| Peaking | 250 Hz   | 1.41 | -1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -10.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20U%20Flex/Samsung%20U%20Flex.png)