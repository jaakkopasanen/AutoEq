# Bloc Roc Galvanize S2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.7; 25 -3.6; 28 -4.9; 31 -6.0; 34 -7.0; 37 -7.9; 41 -8.9; 45 -9.7; 49 -10.3; 54 -10.9; 60 -11.4; 66 -11.5; 72 -11.7; 79 -11.6; 87 -11.2; 96 -11.0; 106 -11.3; 116 -11.3; 128 -11.3; 141 -11.2; 155 -11.0; 170 -10.5; 187 -10.4; 206 -10.1; 227 -9.4; 249 -8.8; 274 -8.1; 302 -8.3; 332 -8.2; 365 -7.6; 402 -7.1; 442 -6.7; 486 -6.5; 535 -5.7; 588 -4.4; 647 -3.3; 712 -2.8; 783 -2.8; 861 -3.1; 947 -3.7; 1042 -4.2; 1146 -5.0; 1261 -5.5; 1387 -6.8; 1526 -8.2; 1678 -9.0; 1846 -8.5; 2031 -8.1; 2234 -7.2; 2457 -5.7; 2703 -4.0; 2973 -2.6; 3270 -3.0; 3597 -0.8; 3957 -0.5; 4353 -1.3; 4788 -6.0; 5267 -5.9; 5793 -4.7; 6373 -4.5; 7010 -4.2; 7711 -5.4; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bloc Roc Galvanize S2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bloc Roc Galvanize S2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.16 | 5.5 dB  |
| Peaking | 64 Hz   | 0.66 | -5.9 dB |
| Peaking | 172 Hz  | 1.1  | -3.6 dB |
| Peaking | 1803 Hz | 3.58 | -4.0 dB |
| Peaking | 3732 Hz | 2.72 | 5.5 dB  |
| Peaking | 437 Hz  | 1.31 | -1.6 dB |
| Peaking | 750 Hz  | 1.34 | 4.5 dB  |
| Peaking | 1880 Hz | 0.34 | -1.0 dB |
| Peaking | 2852 Hz | 6.74 | 2.3 dB  |
| Peaking | 6846 Hz | 4.23 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -5.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bloc%20Roc%20Galvanize%20S2/Bloc%20Roc%20Galvanize%20S2.png)