# SoundMAGIC HP100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.6; 25 -7.3; 28 -8.1; 31 -8.6; 34 -8.9; 37 -9.1; 41 -9.3; 45 -9.4; 49 -9.4; 54 -9.3; 60 -9.1; 66 -8.5; 72 -7.9; 79 -7.8; 87 -6.3; 96 -4.7; 106 -4.0; 116 -4.4; 128 -5.3; 141 -6.2; 155 -4.2; 170 -1.4; 187 -4.7; 206 -6.3; 227 -7.4; 249 -7.8; 274 -7.9; 302 -7.8; 332 -7.7; 365 -7.6; 402 -7.5; 442 -7.3; 486 -7.5; 535 -7.5; 588 -7.1; 647 -7.0; 712 -7.0; 783 -6.7; 861 -6.7; 947 -6.3; 1042 -6.7; 1146 -6.7; 1261 -6.8; 1387 -7.1; 1526 -7.6; 1678 -7.8; 1846 -7.7; 2031 -8.0; 2234 -8.2; 2457 -7.9; 2703 -7.5; 2973 -6.4; 3270 -5.5; 3597 -6.0; 3957 -7.3; 4353 -7.8; 4788 -3.7; 5267 -2.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -7.5; 8482 -12.2; 9330 -12.8; 10263 -9.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 94 Hz   | 0.36 | -4.0 dB |
| Peaking | 105 Hz  | 2.01 | 6.2 dB  |
| Peaking | 171 Hz  | 4.36 | 7.0 dB  |
| Peaking | 6051 Hz | 3.12 | 7.4 dB  |
| Peaking | 8936 Hz | 3.59 | -8.0 dB |
| Peaking | 18 Hz   | 2.97 | 1.9 dB  |
| Peaking | 2238 Hz | 1.61 | -1.9 dB |
| Peaking | 3303 Hz | 4.57 | 1.9 dB  |
| Peaking | 4392 Hz | 4.27 | -3.4 dB |
| Peaking | 4912 Hz | 6.01 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | 3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SoundMAGIC%20HP100/SoundMAGIC%20HP100.png)