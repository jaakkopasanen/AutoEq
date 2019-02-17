# Shure SE530
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.4; 25 -4.5; 28 -4.6; 31 -4.7; 34 -4.8; 37 -5.0; 41 -5.1; 45 -5.3; 49 -5.5; 54 -5.8; 60 -6.1; 66 -6.5; 72 -6.8; 79 -7.2; 87 -7.6; 96 -8.1; 106 -8.4; 116 -8.7; 128 -9.0; 141 -9.3; 155 -9.5; 170 -9.7; 187 -9.7; 206 -9.9; 227 -9.8; 249 -9.9; 274 -9.7; 302 -9.6; 332 -9.4; 365 -9.2; 402 -8.9; 442 -8.5; 486 -8.3; 535 -8.0; 588 -7.4; 647 -7.0; 712 -6.8; 783 -6.4; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -6.9; 1387 -7.4; 1526 -7.8; 1678 -8.2; 1846 -8.3; 2031 -8.3; 2234 -7.7; 2457 -6.1; 2703 -4.2; 2973 -2.5; 3270 -1.1; 3597 -0.6; 3957 -1.0; 4353 -2.1; 4788 -1.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE530 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.53 | 2.2 dB  |
| Peaking | 204 Hz  | 0.59 | -3.7 dB |
| Peaking | 2019 Hz | 2.1  | -3.2 dB |
| Peaking | 3480 Hz | 1.73 | 6.0 dB  |
| Peaking | 5748 Hz | 3    | 5.5 dB  |
| Peaking | 465 Hz  | 1.11 | -1.7 dB |
| Peaking | 617 Hz  | 0.65 | 1.6 dB  |
| Peaking | 1487 Hz | 2.76 | -0.8 dB |
| Peaking | 8267 Hz | 4.15 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE530/Shure%20SE530.png)