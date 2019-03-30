# HyperX Cloud Mix
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.2; 25 -7.5; 28 -8.0; 31 -8.4; 34 -8.6; 37 -8.7; 41 -8.8; 45 -8.8; 49 -8.9; 54 -9.0; 60 -9.2; 66 -9.4; 72 -9.6; 79 -9.9; 87 -10.1; 96 -10.2; 106 -10.3; 116 -10.4; 128 -10.5; 141 -10.5; 155 -10.5; 170 -10.4; 187 -10.4; 206 -10.4; 227 -10.3; 249 -10.2; 274 -10.1; 302 -9.7; 332 -9.1; 365 -8.3; 402 -7.5; 442 -6.7; 486 -5.7; 535 -4.8; 588 -4.4; 647 -4.5; 712 -5.2; 783 -6.0; 861 -6.6; 947 -6.8; 1042 -6.8; 1146 -6.9; 1261 -7.4; 1387 -8.1; 1526 -8.7; 1678 -8.7; 1846 -8.3; 2031 -7.4; 2234 -5.9; 2457 -4.3; 2703 -3.4; 2973 -3.3; 3270 -3.0; 3597 -1.9; 3957 -1.2; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -5.0; 7010 -6.6; 7711 -6.1; 8482 -7.7; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -9.9; 15026 -11.1; 16529 -7.6; 18182 -6.5; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Mix GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Mix ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 94 Hz    | 0.6  | -3.7 dB |
| Peaking | 235 Hz   | 1.76 | -2.7 dB |
| Peaking | 1655 Hz  | 3.07 | -3.2 dB |
| Peaking | 4364 Hz  | 1.37 | 6.6 dB  |
| Peaking | 14595 Hz | 2.19 | -5.0 dB |
| Peaking | 327 Hz   | 3.68 | -1.1 dB |
| Peaking | 586 Hz   | 2.79 | 2.9 dB  |
| Peaking | 5506 Hz  | 4.35 | 2.8 dB  |
| Peaking | 5949 Hz  | 6.99 | 3.7 dB  |
| Peaking | 6391 Hz  | 2.12 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Mix/HyperX%20Cloud%20Mix.png)