# Shure SRH440
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.7; 45 -2.8; 49 -3.7; 54 -4.7; 60 -5.8; 66 -6.7; 72 -7.2; 79 -7.4; 87 -7.0; 96 -6.2; 106 -7.5; 116 -9.0; 128 -9.4; 141 -8.8; 155 -8.3; 170 -7.1; 187 -8.0; 206 -7.7; 227 -7.4; 249 -7.4; 274 -7.3; 302 -7.3; 332 -7.3; 365 -8.4; 402 -8.4; 442 -7.9; 486 -7.8; 535 -7.6; 588 -7.2; 647 -7.0; 712 -7.0; 783 -6.8; 861 -6.8; 947 -6.7; 1042 -6.1; 1146 -5.8; 1261 -6.2; 1387 -6.9; 1526 -7.6; 1678 -8.0; 1846 -7.8; 2031 -7.5; 2234 -6.8; 2457 -6.0; 2703 -6.3; 2973 -6.0; 3270 -7.4; 3597 -7.4; 3957 -6.1; 4353 -5.8; 4788 -4.4; 5267 -3.4; 5793 -2.3; 6373 -1.0; 7010 -4.0; 7711 -7.0; 8482 -10.7; 9330 -12.5; 10263 -11.6; 11289 -7.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 1.04 | 6.9 dB  |
| Peaking | 127 Hz   | 1.59 | -2.8 dB |
| Peaking | 415 Hz   | 1.62 | -1.6 dB |
| Peaking | 6235 Hz  | 2.96 | 6.6 dB  |
| Peaking | 9303 Hz  | 2.82 | -7.3 dB |
| Peaking | 42 Hz    | 2.98 | 1.1 dB  |
| Peaking | 74 Hz    | 1.66 | -1.5 dB |
| Peaking | 97 Hz    | 5.79 | 2.1 dB  |
| Peaking | 1751 Hz  | 4.21 | -1.7 dB |
| Peaking | 11947 Hz | 5.98 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH440/Shure%20SRH440.png)