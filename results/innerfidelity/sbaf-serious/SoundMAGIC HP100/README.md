# SoundMAGIC HP100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.7; 25 -7.4; 28 -8.1; 31 -8.7; 34 -9.0; 37 -9.2; 41 -9.4; 45 -9.5; 49 -9.5; 54 -9.4; 60 -9.2; 66 -8.6; 72 -8.0; 79 -7.9; 87 -6.4; 96 -4.8; 106 -4.1; 116 -4.4; 128 -5.4; 141 -6.3; 155 -4.3; 170 -1.5; 187 -4.8; 206 -6.4; 227 -7.5; 249 -7.9; 274 -8.0; 302 -7.8; 332 -7.7; 365 -7.7; 402 -7.6; 442 -7.4; 486 -7.6; 535 -7.5; 588 -7.2; 647 -7.1; 712 -7.1; 783 -6.8; 861 -6.8; 947 -6.3; 1042 -6.7; 1146 -6.8; 1261 -6.9; 1387 -7.2; 1526 -7.7; 1678 -7.9; 1846 -7.8; 2031 -8.1; 2234 -8.3; 2457 -8.0; 2703 -7.6; 2973 -6.4; 3270 -5.6; 3597 -6.1; 3957 -7.4; 4353 -7.9; 4788 -3.8; 5267 -2.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -7.5; 8482 -12.2; 9330 -12.9; 10263 -9.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundMAGIC HP100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundMAGIC HP100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 95 Hz   | 0.33 | -3.9 dB |
| Peaking | 105 Hz  | 2.08 | 6.0 dB  |
| Peaking | 170 Hz  | 4.28 | 7.0 dB  |
| Peaking | 6061 Hz | 3.18 | 7.4 dB  |
| Peaking | 8936 Hz | 3.58 | -8.1 dB |
| Peaking | 19 Hz   | 2.96 | 1.8 dB  |
| Peaking | 2233 Hz | 1.56 | -2.0 dB |
| Peaking | 3283 Hz | 4.6  | 1.9 dB  |
| Peaking | 4378 Hz | 4.27 | -3.5 dB |
| Peaking | 4931 Hz | 5.84 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | 3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SoundMAGIC%20HP100/SoundMAGIC%20HP100.png)