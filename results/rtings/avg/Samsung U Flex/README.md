# Samsung U Flex
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -0.7; 34 -0.8; 37 -0.8; 41 -0.9; 45 -1.0; 49 -1.1; 54 -1.3; 60 -1.7; 66 -2.0; 72 -2.3; 79 -2.7; 87 -3.2; 96 -3.8; 106 -4.4; 116 -5.0; 128 -5.6; 141 -6.0; 155 -6.3; 170 -6.4; 187 -6.4; 206 -6.6; 227 -6.8; 249 -6.6; 274 -6.3; 302 -6.0; 332 -5.7; 365 -5.4; 402 -5.1; 442 -4.8; 486 -4.5; 535 -4.0; 588 -3.6; 647 -3.2; 712 -2.8; 783 -2.6; 861 -2.5; 947 -2.9; 1042 -3.8; 1146 -5.0; 1261 -6.0; 1387 -6.7; 1526 -7.2; 1678 -7.7; 1846 -8.4; 2031 -9.1; 2234 -9.5; 2457 -9.8; 2703 -10.6; 2973 -11.0; 3270 -10.7; 3597 -10.6; 3957 -10.3; 4353 -10.2; 4788 -10.2; 5267 -9.8; 5793 -8.4; 6373 -5.8; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -9.7; 10263 -12.8; 11289 -13.2; 12418 -10.8; 13660 -8.3; 15026 -10.9; 16529 -15.1; 18182 -13.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung U Flex GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung U Flex ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.46 | 5.9 dB  |
| Peaking | 64 Hz    | 1.36 | 1.9 dB  |
| Peaking | 3272 Hz  | 1.49 | -4.9 dB |
| Peaking | 10912 Hz | 3.76 | -6.8 dB |
| Peaking | 17262 Hz | 1.35 | -9.6 dB |
| Peaking | 206 Hz   | 1.34 | -1.1 dB |
| Peaking | 836 Hz   | 0.9  | 4.7 dB  |
| Peaking | 1608 Hz  | 1.2  | -2.4 dB |
| Peaking | 5249 Hz  | 3.54 | -2.4 dB |
| Peaking | 6869 Hz  | 3.91 | 3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | -3.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -9.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20U%20Flex/Samsung%20U%20Flex.png)