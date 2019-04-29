# Kumitate KL-Sirius custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.6; 31 -2.1; 34 -2.5; 37 -2.9; 41 -3.2; 45 -3.5; 49 -3.7; 54 -4.0; 60 -4.3; 66 -4.6; 72 -4.9; 79 -5.2; 87 -5.6; 96 -6.0; 106 -6.4; 116 -6.6; 128 -6.9; 141 -7.2; 155 -7.4; 170 -7.6; 187 -7.7; 206 -7.8; 227 -7.9; 249 -7.9; 274 -7.9; 302 -7.9; 332 -7.9; 365 -7.8; 402 -7.8; 442 -7.7; 486 -7.6; 535 -7.6; 588 -7.5; 647 -7.4; 712 -7.3; 783 -7.1; 861 -7.1; 947 -7.4; 1042 -8.1; 1146 -9.2; 1261 -10.2; 1387 -10.7; 1526 -10.2; 1678 -9.1; 1846 -7.6; 2031 -6.3; 2234 -5.4; 2457 -5.0; 2703 -4.9; 2973 -5.0; 3270 -5.1; 3597 -4.6; 3957 -4.1; 4353 -4.0; 4788 -3.1; 5267 -1.2; 5793 -0.5; 6373 -1.9; 7010 -4.0; 7711 -6.2; 8482 -6.4; 9330 -6.8; 10263 -8.2; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Sirius custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Sirius custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.22 | 5.9 dB  |
| Peaking | 51 Hz    | 1.97 | 1.8 dB  |
| Peaking | 1577 Hz  | 1.04 | -7.7 dB |
| Peaking | 2158 Hz  | 1.02 | 6.0 dB  |
| Peaking | 5642 Hz  | 2.95 | 6.2 dB  |
| Peaking | 12 Hz    | 0.38 | 0.3 dB  |
| Peaking | 82 Hz    | 1.67 | 0.9 dB  |
| Peaking | 232 Hz   | 0.52 | -1.5 dB |
| Peaking | 889 Hz   | 2.56 | 1.5 dB  |
| Peaking | 10103 Hz | 4.35 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-Sirius%20custom/Kumitate%20KL-Sirius%20custom.png)