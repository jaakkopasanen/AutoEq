# JVC XX Elation HA FR100X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.7; 25 -3.4; 28 -4.0; 31 -4.4; 34 -4.8; 37 -5.1; 41 -5.6; 45 -6.1; 49 -6.6; 54 -7.1; 60 -7.5; 66 -8.0; 72 -8.5; 79 -9.0; 87 -9.6; 96 -10.1; 106 -10.4; 116 -10.6; 128 -10.8; 141 -11.3; 155 -11.5; 170 -11.5; 187 -11.6; 206 -11.5; 227 -11.4; 249 -11.3; 274 -11.0; 302 -10.7; 332 -10.2; 365 -9.7; 402 -9.2; 442 -8.4; 486 -7.9; 535 -7.2; 588 -6.2; 647 -5.5; 712 -4.9; 783 -4.1; 861 -3.8; 947 -3.5; 1042 -3.1; 1146 -2.6; 1261 -2.4; 1387 -2.5; 1526 -2.5; 1678 -2.6; 1846 -2.7; 2031 -3.5; 2234 -4.3; 2457 -4.5; 2703 -4.8; 2973 -3.9; 3270 -3.0; 3597 -2.9; 3957 -4.8; 4353 -8.5; 4788 -10.8; 5267 -7.9; 5793 -2.4; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC XX Elation HA FR100X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC XX Elation HA FR100X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.46 | 5.7 dB  |
| Peaking | 251 Hz  | 0.32 | -7.1 dB |
| Peaking | 983 Hz  | 0.43 | 5.8 dB  |
| Peaking | 4813 Hz | 5.36 | -7.2 dB |
| Peaking | 6225 Hz | 5.12 | 6.3 dB  |
| Peaking | 2587 Hz | 3.02 | -1.7 dB |
| Peaking | 3532 Hz | 2.74 | 2.6 dB  |
| Peaking | 4298 Hz | 7.17 | -1.9 dB |
| Peaking | 8358 Hz | 3.3  | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20XX%20Elation%20HA%20FR100X/JVC%20XX%20Elation%20HA%20FR100X.png)