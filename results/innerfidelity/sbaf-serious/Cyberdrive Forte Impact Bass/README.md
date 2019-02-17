# Cyberdrive Forte Impact Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.6; 23 -15.6; 25 -15.7; 28 -15.7; 31 -15.6; 34 -15.6; 37 -15.6; 41 -15.6; 45 -15.6; 49 -15.5; 54 -15.5; 60 -15.5; 66 -15.5; 72 -15.6; 79 -15.6; 87 -15.7; 96 -15.7; 106 -15.5; 116 -15.3; 128 -15.1; 141 -14.9; 155 -14.7; 170 -14.3; 187 -13.9; 206 -13.5; 227 -13.0; 249 -12.5; 274 -12.0; 302 -11.5; 332 -11.0; 365 -10.4; 402 -9.9; 442 -9.2; 486 -8.8; 535 -8.2; 588 -7.5; 647 -7.1; 712 -6.7; 783 -6.1; 861 -5.9; 947 -6.0; 1042 -5.5; 1146 -5.2; 1261 -5.4; 1387 -5.5; 1526 -5.6; 1678 -5.4; 1846 -4.8; 2031 -3.9; 2234 -3.1; 2457 -1.7; 2703 -1.1; 2973 -0.5; 3270 -0.6; 3597 -1.9; 3957 -4.4; 4353 -7.7; 4788 -9.3; 5267 -9.9; 5793 -12.6; 6373 -17.0; 7010 -13.7; 7711 -9.7; 8482 -7.5; 9330 -8.4; 10263 -10.2; 11289 -7.3; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -6.6; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cyberdrive Forte Impact Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cyberdrive Forte Impact Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 53 Hz    | 0.17 | -10.3 dB |
| Peaking | 2955 Hz  | 1.65 | 6.4 dB   |
| Peaking | 6315 Hz  | 2.54 | -11.2 dB |
| Peaking | 10068 Hz | 8.68 | -2.4 dB  |
| Peaking | 10675 Hz | 6.41 | -2.0 dB  |
| Peaking | 12 Hz    | 1.96 | -1.2 dB  |
| Peaking | 860 Hz   | 1.76 | 1.2 dB   |
| Peaking | 3659 Hz  | 5.45 | 1.6 dB   |
| Peaking | 4520 Hz  | 3.57 | -2.3 dB  |
| Peaking | 5576 Hz  | 6.62 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.0 dB |
| Peaking | 62 Hz    | 1.41 | -6.9 dB  |
| Peaking | 125 Hz   | 1.41 | -7.6 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -7.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.6 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cyberdrive%20Forte%20Impact%20Bass/Cyberdrive%20Forte%20Impact%20Bass.png)