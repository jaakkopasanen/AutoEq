# HyperX Cloud Stinger
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -10.0; 25 -10.1; 28 -10.3; 31 -10.4; 34 -10.4; 37 -10.3; 41 -10.3; 45 -10.4; 49 -10.5; 54 -10.6; 60 -10.6; 66 -10.6; 72 -10.6; 79 -10.6; 87 -10.8; 96 -11.0; 106 -11.2; 116 -11.3; 128 -11.1; 141 -10.8; 155 -10.5; 170 -10.0; 187 -9.3; 206 -8.2; 227 -7.1; 249 -5.9; 274 -4.7; 302 -3.3; 332 -1.8; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.9; 535 -2.8; 588 -4.4; 647 -5.5; 712 -5.7; 783 -5.4; 861 -4.6; 947 -4.2; 1042 -4.3; 1146 -4.8; 1261 -5.7; 1387 -6.9; 1526 -8.2; 1678 -9.3; 1846 -10.0; 2031 -10.8; 2234 -10.3; 2457 -9.7; 2703 -9.3; 2973 -9.5; 3270 -8.7; 3597 -6.9; 3957 -4.7; 4353 -4.0; 4788 -3.4; 5267 -2.3; 5793 -5.3; 6373 -7.5; 7010 -5.3; 7711 -6.5; 8482 -9.7; 9330 -11.2; 10263 -8.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.9; 16529 -11.7; 18182 -12.7; 20000 -14.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Stinger GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Stinger ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.38 | -3.4 dB |
| Peaking | 145 Hz   | 0.7  | -4.5 dB |
| Peaking | 387 Hz   | 1.16 | 7.6 dB  |
| Peaking | 2110 Hz  | 2.34 | -4.8 dB |
| Peaking | 19228 Hz | 0.64 | -7.7 dB |
| Peaking | 1049 Hz  | 4.75 | 2.1 dB  |
| Peaking | 3075 Hz  | 4.51 | -2.7 dB |
| Peaking | 4844 Hz  | 2.49 | 4.3 dB  |
| Peaking | 9217 Hz  | 4.42 | -5.2 dB |
| Peaking | 12570 Hz | 2.05 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 5.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -4.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Stinger/HyperX%20Cloud%20Stinger.png)