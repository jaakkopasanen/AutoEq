# Sennheiser HD 449
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.9; 25 -6.3; 28 -6.8; 31 -7.2; 34 -7.6; 37 -7.9; 41 -8.1; 45 -8.3; 49 -8.5; 54 -8.7; 60 -8.7; 66 -8.8; 72 -8.8; 79 -8.6; 87 -8.3; 96 -7.5; 106 -6.2; 116 -6.4; 128 -8.8; 141 -9.9; 155 -8.8; 170 -8.0; 187 -9.5; 206 -9.2; 227 -8.6; 249 -8.1; 274 -7.4; 302 -6.9; 332 -6.2; 365 -5.5; 402 -5.6; 442 -5.5; 486 -5.6; 535 -5.8; 588 -6.0; 647 -6.5; 712 -6.8; 783 -6.4; 861 -6.5; 947 -6.7; 1042 -6.5; 1146 -6.5; 1261 -7.3; 1387 -8.2; 1526 -8.6; 1678 -8.6; 1846 -8.1; 2031 -6.8; 2234 -5.2; 2457 -3.6; 2703 -3.4; 2973 -2.8; 3270 -2.6; 3597 -2.4; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 449 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 449 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 58 Hz   | 1.37 | -2.4 dB |
| Peaking | 182 Hz  | 1.89 | -2.7 dB |
| Peaking | 1624 Hz | 2.97 | -3.3 dB |
| Peaking | 4490 Hz | 1.12 | 6.6 dB  |
| Peaking | 111 Hz  | 7.26 | 2.1 dB  |
| Peaking | 135 Hz  | 7.93 | -2.4 dB |
| Peaking | 421 Hz  | 2.49 | 1.4 dB  |
| Peaking | 6339 Hz | 3.4  | 4.2 dB  |
| Peaking | 7402 Hz | 1.56 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20449/Sennheiser%20HD%20449.png)