# JVC XX Elation HA FR100X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -4.3; 25 -5.0; 28 -5.5; 31 -5.9; 34 -6.3; 37 -6.7; 41 -7.1; 45 -7.6; 49 -8.1; 54 -8.6; 60 -9.0; 66 -9.6; 72 -10.0; 79 -10.6; 87 -11.2; 96 -11.7; 106 -12.0; 116 -12.2; 128 -12.3; 141 -12.9; 155 -13.1; 170 -13.1; 187 -13.2; 206 -13.1; 227 -12.9; 249 -12.8; 274 -12.5; 302 -12.2; 332 -11.7; 365 -11.2; 402 -10.7; 442 -10.0; 486 -9.5; 535 -8.7; 588 -7.7; 647 -7.0; 712 -6.4; 783 -5.7; 861 -5.3; 947 -5.0; 1042 -4.7; 1146 -4.2; 1261 -4.0; 1387 -4.0; 1526 -4.1; 1678 -4.1; 1846 -4.2; 2031 -5.1; 2234 -5.9; 2457 -6.0; 2703 -6.4; 2973 -5.4; 3270 -4.5; 3597 -4.5; 3957 -6.3; 4353 -10.1; 4788 -12.4; 5267 -9.5; 5793 -4.0; 6373 -0.5; 7010 -2.5; 7711 -4.8; 8482 -5.0; 9330 -5.0; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC XX Elation HA FR100X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC XX Elation HA FR100X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 2.22 | 3.0 dB  |
| Peaking | 129 Hz  | 0.54 | -7.1 dB |
| Peaking | 313 Hz  | 1.1  | -4.1 dB |
| Peaking | 4822 Hz | 4.6  | -8.6 dB |
| Peaking | 6411 Hz | 4.88 | 5.9 dB  |
| Peaking | 510 Hz  | 3.02 | -1.1 dB |
| Peaking | 1612 Hz | 0.83 | 2.5 dB  |
| Peaking | 2668 Hz | 1.24 | -3.3 dB |
| Peaking | 3446 Hz | 2.65 | 3.1 dB  |
| Peaking | 4270 Hz | 8.61 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.9 dB |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20XX%20Elation%20HA%20FR100X/JVC%20XX%20Elation%20HA%20FR100X.png)