# HiFiMAN HE-500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.6; 31 -1.8; 34 -1.8; 37 -1.9; 41 -1.9; 45 -1.9; 49 -1.9; 54 -2.0; 60 -2.2; 66 -2.5; 72 -2.6; 79 -2.8; 87 -3.1; 96 -3.3; 106 -3.5; 116 -3.6; 128 -4.0; 141 -4.1; 155 -4.3; 170 -4.2; 187 -4.2; 206 -4.4; 227 -4.4; 249 -4.4; 274 -4.6; 302 -4.6; 332 -4.4; 365 -4.6; 402 -4.9; 442 -4.5; 486 -4.6; 535 -4.4; 588 -4.3; 647 -4.2; 712 -4.3; 783 -3.3; 861 -4.0; 947 -4.3; 1042 -4.4; 1146 -4.0; 1261 -4.0; 1387 -3.1; 1526 -3.2; 1678 -2.5; 1846 -1.4; 2031 -2.0; 2234 -2.1; 2457 -1.6; 2703 -2.0; 2973 -2.0; 3270 -2.8; 3597 -3.1; 3957 -2.9; 4353 -4.7; 4788 -3.8; 5267 -1.5; 5793 -1.7; 6373 -3.4; 7010 -3.1; 7711 -4.3; 8482 -8.2; 9330 -9.7; 10263 -4.8; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -3.9; 18182 -5.5; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.04 | 3.3 dB  |
| Peaking | 54 Hz   | 1.65 | 1.5 dB  |
| Peaking | 2306 Hz | 1.68 | 2.4 dB  |
| Peaking | 5579 Hz | 6.48 | 3.0 dB  |
| Peaking | 9077 Hz | 5.36 | -6.9 dB |
| Peaking | 354 Hz  | 0.68 | -0.8 dB |
| Peaking | 4197 Hz | 2.64 | 1.1 dB  |
| Peaking | 4405 Hz | 6.42 | -2.6 dB |
| Peaking | 7327 Hz | 5.82 | 1.2 dB  |
| Peaking | 8314 Hz | 9.6  | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-500/HiFiMAN%20HE-500.png)