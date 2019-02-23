# HiFiMAN Edition X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.1; 28 -2.9; 31 -3.5; 34 -3.9; 37 -4.2; 41 -4.5; 45 -4.6; 49 -4.7; 54 -4.9; 60 -5.0; 66 -5.1; 72 -5.2; 79 -5.6; 87 -6.2; 96 -6.6; 106 -6.7; 116 -6.8; 128 -7.0; 141 -7.1; 155 -7.2; 170 -7.3; 187 -7.4; 206 -7.4; 227 -7.6; 249 -7.8; 274 -7.7; 302 -8.0; 332 -7.7; 365 -7.0; 402 -6.8; 442 -7.2; 486 -7.9; 535 -8.4; 588 -8.1; 647 -8.3; 712 -7.7; 783 -5.7; 861 -6.9; 947 -8.0; 1042 -6.8; 1146 -5.2; 1261 -5.0; 1387 -6.0; 1526 -5.7; 1678 -6.4; 1846 -6.5; 2031 -6.1; 2234 -6.6; 2457 -6.3; 2703 -6.6; 2973 -6.9; 3270 -6.4; 3597 -5.8; 3957 -6.4; 4353 -8.3; 4788 -7.5; 5267 -4.7; 5793 -4.2; 6373 -6.5; 7010 -5.2; 7711 -6.4; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.9; 20000 -13.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN Edition X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN Edition X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.83 | 7.6 dB  |
| Peaking | 63 Hz   | 1.62 | 1.2 dB  |
| Peaking | 327 Hz  | 0.39 | -1.1 dB |
| Peaking | 1214 Hz | 5.88 | 2.8 dB  |
| Peaking | 5642 Hz | 7.23 | 3.1 dB  |
| Peaking | 314 Hz  | 2.54 | -1.2 dB |
| Peaking | 388 Hz  | 1.55 | 1.7 dB  |
| Peaking | 533 Hz  | 2.83 | -1.6 dB |
| Peaking | 4263 Hz | 1.72 | 1.5 dB  |
| Peaking | 4464 Hz | 5.39 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20Edition%20X/HiFiMAN%20Edition%20X.png)