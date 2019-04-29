# JVC HA-FW03
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -2.0; 31 -2.4; 34 -2.8; 37 -3.1; 41 -3.4; 45 -3.8; 49 -4.0; 54 -4.4; 60 -4.8; 66 -5.2; 72 -5.6; 79 -6.0; 87 -6.4; 96 -6.9; 106 -7.3; 116 -7.7; 128 -8.0; 141 -8.3; 155 -8.6; 170 -8.7; 187 -8.7; 206 -8.7; 227 -8.6; 249 -8.5; 274 -8.4; 302 -8.1; 332 -8.0; 365 -7.7; 402 -7.4; 442 -7.1; 486 -6.9; 535 -6.5; 588 -6.1; 647 -5.6; 712 -5.3; 783 -4.8; 861 -4.3; 947 -4.3; 1042 -4.5; 1146 -5.2; 1261 -5.9; 1387 -6.5; 1526 -6.6; 1678 -6.5; 1846 -6.2; 2031 -6.3; 2234 -6.7; 2457 -7.4; 2703 -8.2; 2973 -8.6; 3270 -8.2; 3597 -7.2; 3957 -6.4; 4353 -5.9; 4788 -5.9; 5267 -5.9; 5793 -5.3; 6373 -4.3; 7010 -4.9; 7711 -6.9; 8482 -6.7; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.9; 16529 -9.1; 18182 -9.9; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-FW03 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-FW03 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.27 | 6.6 dB  |
| Peaking | 183 Hz   | 0.66 | -2.5 dB |
| Peaking | 883 Hz   | 1.7  | 2.7 dB  |
| Peaking | 2944 Hz  | 4.05 | -2.4 dB |
| Peaking | 6358 Hz  | 3.94 | 2.5 dB  |
| Peaking | 1420 Hz  | 7.57 | -0.6 dB |
| Peaking | 4402 Hz  | 5.34 | 0.8 dB  |
| Peaking | 19209 Hz | 0.79 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JVC%20HA-FW03/JVC%20HA-FW03.png)