# Samsung U Flex
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -0.9; 31 -1.0; 34 -1.1; 37 -1.2; 41 -1.3; 45 -1.4; 49 -1.5; 54 -1.6; 60 -2.0; 66 -2.4; 72 -2.7; 79 -3.1; 87 -3.6; 96 -4.1; 106 -4.9; 116 -5.4; 128 -6.0; 141 -6.4; 155 -6.7; 170 -6.8; 187 -6.8; 206 -7.0; 227 -7.1; 249 -6.9; 274 -6.6; 302 -6.3; 332 -6.0; 365 -5.7; 402 -5.4; 442 -5.0; 486 -4.7; 535 -4.2; 588 -3.7; 647 -3.3; 712 -2.9; 783 -2.6; 861 -2.6; 947 -3.0; 1042 -3.9; 1146 -5.0; 1261 -6.0; 1387 -6.6; 1526 -7.2; 1678 -7.7; 1846 -8.3; 2031 -8.8; 2234 -8.9; 2457 -9.1; 2703 -10.2; 2973 -11.1; 3270 -11.2; 3597 -11.0; 3957 -10.8; 4353 -10.8; 4788 -10.0; 5267 -9.7; 5793 -8.7; 6373 -7.0; 7010 -3.5; 7711 -3.1; 8482 -5.4; 9330 -11.4; 10263 -13.5; 11289 -12.5; 12418 -10.9; 13660 -9.4; 15026 -11.6; 16529 -15.5; 18182 -14.3; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung U Flex GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung U Flex ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.38 | 2.8 dB   |
| Peaking | 186 Hz   | 0.82 | -4.2 dB  |
| Peaking | 3233 Hz  | 0.89 | -8.0 dB  |
| Peaking | 10570 Hz | 3.45 | -8.0 dB  |
| Peaking | 17303 Hz | 0.88 | -12.8 dB |
| Peaking | 844 Hz   | 2.32 | 2.3 dB   |
| Peaking | 1496 Hz  | 2.35 | -1.6 dB  |
| Peaking | 5623 Hz  | 2.6  | -2.7 dB  |
| Peaking | 7556 Hz  | 2.74 | 5.4 dB   |
| Peaking | 9362 Hz  | 6.02 | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB   |
| Peaking | 62 Hz    | 1.41 | 1.5 dB   |
| Peaking | 125 Hz   | 1.41 | -2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -15.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20U%20Flex/Samsung%20U%20Flex.png)