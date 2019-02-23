# Enigmacoustics Dharma Production 2015
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.4; 28 -2.3; 31 -3.0; 34 -3.7; 37 -4.2; 41 -4.7; 45 -5.2; 49 -5.6; 54 -6.1; 60 -6.6; 66 -7.1; 72 -7.4; 79 -7.7; 87 -8.0; 96 -8.4; 106 -8.7; 116 -8.8; 128 -8.9; 141 -8.8; 155 -8.5; 170 -7.9; 187 -7.5; 206 -7.0; 227 -6.9; 249 -7.0; 274 -6.8; 302 -6.3; 332 -5.7; 365 -5.1; 402 -4.9; 442 -4.7; 486 -4.7; 535 -4.8; 588 -4.7; 647 -5.1; 712 -5.4; 783 -5.6; 861 -6.2; 947 -6.7; 1042 -6.4; 1146 -7.0; 1261 -7.1; 1387 -7.7; 1526 -7.9; 1678 -8.8; 1846 -9.2; 2031 -8.2; 2234 -7.0; 2457 -6.2; 2703 -5.1; 2973 -3.2; 3270 -1.8; 3597 -1.5; 3957 -1.9; 4353 -4.7; 4788 -7.8; 5267 -9.8; 5793 -13.4; 6373 -9.4; 7010 -6.0; 7711 -6.1; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.5; 13660 -10.2; 15026 -10.0; 16529 -9.2; 18182 -8.5; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Enigmacoustics Dharma Production 2015 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Enigmacoustics Dharma Production 2015 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 2.06 | 6.2 dB  |
| Peaking | 1817 Hz  | 2.65 | -3.3 dB |
| Peaking | 3537 Hz  | 2.43 | 5.9 dB  |
| Peaking | 5734 Hz  | 4.99 | -7.9 dB |
| Peaking | 15414 Hz | 1.5  | -4.1 dB |
| Peaking | 38 Hz    | 1.86 | 1.3 dB  |
| Peaking | 121 Hz   | 0.97 | -2.7 dB |
| Peaking | 479 Hz   | 1.43 | 2.0 dB  |
| Peaking | 5163 Hz  | 3.68 | -0.8 dB |
| Peaking | 7381 Hz  | 4.84 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Enigmacoustics%20Dharma%20Production%202015/Enigmacoustics%20Dharma%20Production%202015.png)