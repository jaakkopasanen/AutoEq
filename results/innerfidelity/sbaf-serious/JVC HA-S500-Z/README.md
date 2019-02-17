# JVC HA-S500-Z
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.9; 25 -2.6; 28 -3.5; 31 -4.3; 34 -4.9; 37 -5.4; 41 -5.8; 45 -6.2; 49 -6.4; 54 -6.6; 60 -6.8; 66 -7.0; 72 -7.2; 79 -7.5; 87 -7.7; 96 -7.9; 106 -7.9; 116 -8.0; 128 -8.3; 141 -8.6; 155 -8.8; 170 -8.6; 187 -8.6; 206 -8.7; 227 -8.6; 249 -8.6; 274 -9.4; 302 -9.7; 332 -8.9; 365 -7.9; 402 -6.6; 442 -5.0; 486 -3.3; 535 -1.8; 588 -2.1; 647 -3.5; 712 -4.8; 783 -5.3; 861 -6.0; 947 -6.4; 1042 -6.5; 1146 -6.4; 1261 -6.4; 1387 -6.3; 1526 -5.9; 1678 -5.2; 1846 -4.1; 2031 -2.7; 2234 -1.2; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -5.2; 7711 -6.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-S500-Z GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-S500-Z ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.26 | 5.8 dB  |
| Peaking | 312 Hz  | 3.53 | -1.7 dB |
| Peaking | 463 Hz  | 0.22 | -3.1 dB |
| Peaking | 552 Hz  | 1.76 | 7.5 dB  |
| Peaking | 3283 Hz | 0.72 | 7.7 dB  |
| Peaking | 1574 Hz | 3.21 | -0.9 dB |
| Peaking | 2323 Hz | 3.83 | 1.6 dB  |
| Peaking | 3352 Hz | 2.08 | -1.0 dB |
| Peaking | 6254 Hz | 2.47 | 6.6 dB  |
| Peaking | 7143 Hz | 1.7  | -5.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | 4.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20HA-S500-Z/JVC%20HA-S500-Z.png)