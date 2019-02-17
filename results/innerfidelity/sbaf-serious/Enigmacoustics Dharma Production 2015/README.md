# Enigmacoustics Dharma Production 2015
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.2; 28 -2.1; 31 -2.8; 34 -3.5; 37 -4.0; 41 -4.5; 45 -5.0; 49 -5.4; 54 -5.9; 60 -6.4; 66 -6.9; 72 -7.2; 79 -7.4; 87 -7.8; 96 -8.2; 106 -8.5; 116 -8.6; 128 -8.7; 141 -8.6; 155 -8.3; 170 -7.7; 187 -7.3; 206 -6.8; 227 -6.7; 249 -6.8; 274 -6.6; 302 -6.1; 332 -5.5; 365 -4.9; 402 -4.7; 442 -4.5; 486 -4.5; 535 -4.6; 588 -4.5; 647 -4.9; 712 -5.2; 783 -5.3; 861 -6.0; 947 -6.5; 1042 -6.1; 1146 -6.8; 1261 -6.9; 1387 -7.4; 1526 -7.7; 1678 -8.5; 1846 -9.0; 2031 -8.0; 2234 -6.8; 2457 -6.0; 2703 -4.9; 2973 -3.0; 3270 -1.6; 3597 -1.3; 3957 -1.6; 4353 -4.5; 4788 -7.6; 5267 -9.6; 5793 -13.2; 6373 -9.1; 7010 -5.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.0; 15026 -9.7; 16529 -9.0; 18182 -8.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Enigmacoustics Dharma Production 2015 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Enigmacoustics Dharma Production 2015 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.73 | 6.2 dB  |
| Peaking | 1829 Hz  | 3.2  | -3.1 dB |
| Peaking | 3540 Hz  | 2.33 | 6.1 dB  |
| Peaking | 5737 Hz  | 5.12 | -7.7 dB |
| Peaking | 15248 Hz | 1.63 | -3.7 dB |
| Peaking | 43 Hz    | 2.51 | 0.9 dB  |
| Peaking | 121 Hz   | 1.1  | -2.4 dB |
| Peaking | 483 Hz   | 1.3  | 2.3 dB  |
| Peaking | 7195 Hz  | 7.09 | 1.8 dB  |
| Peaking | 18159 Hz | 3.25 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Enigmacoustics%20Dharma%20Production%202015/Enigmacoustics%20Dharma%20Production%202015.png)