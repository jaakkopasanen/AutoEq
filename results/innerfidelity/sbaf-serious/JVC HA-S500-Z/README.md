# JVC HA-S500-Z
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -4.2; 25 -5.0; 28 -5.9; 31 -6.6; 34 -7.2; 37 -7.7; 41 -8.2; 45 -8.5; 49 -8.7; 54 -9.0; 60 -9.2; 66 -9.4; 72 -9.6; 79 -9.9; 87 -10.0; 96 -10.2; 106 -10.2; 116 -10.4; 128 -10.7; 141 -10.9; 155 -11.1; 170 -10.9; 187 -10.9; 206 -11.0; 227 -10.9; 249 -10.9; 274 -11.7; 302 -12.0; 332 -11.3; 365 -10.2; 402 -9.0; 442 -7.4; 486 -5.6; 535 -4.1; 588 -4.4; 647 -5.8; 712 -7.1; 783 -7.6; 861 -8.3; 947 -8.7; 1042 -8.8; 1146 -8.7; 1261 -8.7; 1387 -8.6; 1526 -8.2; 1678 -7.5; 1846 -6.5; 2031 -5.0; 2234 -3.5; 2457 -1.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.7; 3957 -1.7; 4353 -3.2; 4788 -3.5; 5267 -1.1; 5793 -0.5; 6373 -1.0; 7010 -7.5; 7711 -8.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-S500-Z GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-S500-Z ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.44 | 3.7 dB  |
| Peaking | 125 Hz  | 0.53 | -4.3 dB |
| Peaking | 297 Hz  | 2.96 | -3.8 dB |
| Peaking | 3122 Hz | 2.09 | 6.9 dB  |
| Peaking | 5713 Hz | 4.44 | 6.1 dB  |
| Peaking | 557 Hz  | 3.44 | 4.5 dB  |
| Peaking | 1209 Hz | 0.89 | -2.7 dB |
| Peaking | 2411 Hz | 3.38 | 2.5 dB  |
| Peaking | 6434 Hz | 8.82 | 3.4 dB  |
| Peaking | 7317 Hz | 5.7  | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20HA-S500-Z/JVC%20HA-S500-Z.png)