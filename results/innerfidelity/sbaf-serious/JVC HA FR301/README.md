# JVC HA FR301
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -9.2; 25 -9.6; 28 -10.0; 31 -10.4; 34 -10.8; 37 -11.1; 41 -11.4; 45 -11.7; 49 -12.0; 54 -12.3; 60 -12.6; 66 -12.9; 72 -13.2; 79 -13.4; 87 -13.7; 96 -14.0; 106 -14.1; 116 -14.0; 128 -14.1; 141 -14.1; 155 -13.9; 170 -13.7; 187 -13.4; 206 -13.0; 227 -12.4; 249 -11.9; 274 -11.2; 302 -10.5; 332 -9.7; 365 -8.8; 402 -7.9; 442 -6.8; 486 -6.1; 535 -4.9; 588 -3.6; 647 -2.6; 712 -1.8; 783 -0.8; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.8; 1678 -1.4; 1846 -1.7; 2031 -2.1; 2234 -2.6; 2457 -3.1; 2703 -4.4; 2973 -5.5; 3270 -6.3; 3597 -6.6; 3957 -7.5; 4353 -10.2; 4788 -12.0; 5267 -10.1; 5793 -6.4; 6373 -3.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA FR301 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA FR301 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 71 Hz   | 0.33 | -4.3 dB |
| Peaking | 242 Hz  | 0.36 | -5.9 dB |
| Peaking | 919 Hz  | 0.47 | 8.6 dB  |
| Peaking | 4827 Hz | 2.31 | -7.1 dB |
| Peaking | 6438 Hz | 4.03 | 4.9 dB  |
| Peaking | 1095 Hz | 5.07 | -0.5 dB |
| Peaking | 2889 Hz | 1.42 | 1.1 dB  |
| Peaking | 3045 Hz | 3.66 | -2.0 dB |
| Peaking | 8638 Hz | 3.5  | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20HA%20FR301/JVC%20HA%20FR301.png)