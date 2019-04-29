# AZLA Horizon
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.4; 25 -8.4; 28 -8.4; 31 -8.4; 34 -8.4; 37 -8.3; 41 -8.2; 45 -8.1; 49 -8.0; 54 -7.9; 60 -7.8; 66 -7.8; 72 -7.8; 79 -7.8; 87 -7.8; 96 -7.8; 106 -7.8; 116 -7.7; 128 -7.7; 141 -7.6; 155 -7.4; 170 -7.1; 187 -6.8; 206 -6.5; 227 -6.2; 249 -5.8; 274 -5.3; 302 -4.9; 332 -4.5; 365 -4.1; 402 -3.6; 442 -3.2; 486 -2.8; 535 -2.4; 588 -2.0; 647 -1.6; 712 -1.2; 783 -0.8; 861 -0.5; 947 -0.5; 1042 -0.8; 1146 -1.5; 1261 -2.3; 1387 -2.9; 1526 -3.1; 1678 -3.1; 1846 -3.1; 2031 -3.4; 2234 -3.8; 2457 -4.4; 2703 -4.6; 2973 -4.0; 3270 -3.0; 3597 -2.3; 3957 -2.2; 4353 -2.8; 4788 -4.2; 5267 -6.4; 5793 -7.4; 6373 -6.2; 7010 -6.4; 7711 -7.5; 8482 -4.8; 9330 -4.1; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -5.8; 16529 -7.2; 18182 -7.8; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AZLA Horizon GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AZLA Horizon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.27 | -4.2 dB |
| Peaking | 146 Hz   | 0.73 | -2.6 dB |
| Peaking | 829 Hz   | 0.98 | 3.7 dB  |
| Peaking | 6549 Hz  | 2.43 | -3.0 dB |
| Peaking | 18448 Hz | 0.95 | -4.3 dB |
| Peaking | 2674 Hz  | 3.33 | -1.4 dB |
| Peaking | 3890 Hz  | 2.17 | 2.5 dB  |
| Peaking | 5159 Hz  | 6.01 | -1.4 dB |
| Peaking | 5545 Hz  | 8.66 | -1.4 dB |
| Peaking | 12231 Hz | 2.27 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/AZLA%20Horizon/AZLA%20Horizon.png)