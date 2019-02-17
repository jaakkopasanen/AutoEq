# SoundMAGIC E10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.5; 25 -7.8; 28 -8.3; 31 -8.6; 34 -8.9; 37 -9.2; 41 -9.5; 45 -9.7; 49 -10.0; 54 -10.3; 60 -10.7; 66 -11.0; 72 -11.2; 79 -11.6; 87 -12.0; 96 -12.3; 106 -12.6; 116 -12.8; 128 -12.9; 141 -13.0; 155 -13.0; 170 -12.9; 187 -12.7; 206 -12.4; 227 -12.1; 249 -11.7; 274 -11.3; 302 -10.8; 332 -10.4; 365 -9.9; 402 -9.4; 442 -8.7; 486 -8.0; 535 -7.5; 588 -7.2; 647 -6.8; 712 -6.3; 783 -6.2; 861 -6.2; 947 -6.2; 1042 -6.6; 1146 -6.3; 1261 -5.2; 1387 -3.3; 1526 -2.4; 1678 -2.2; 1846 -0.8; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundMAGIC E10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundMAGIC E10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 1.22 | 1.3 dB  |
| Peaking | 72 Hz   | 0.38 | -2.8 dB |
| Peaking | 177 Hz  | 0.55 | -4.8 dB |
| Peaking | 2423 Hz | 0.9  | 6.2 dB  |
| Peaking | 5174 Hz | 1.93 | 4.8 dB  |
| Peaking | 1128 Hz | 2.48 | -3.7 dB |
| Peaking | 1290 Hz | 1.03 | 2.8 dB  |
| Peaking | 3843 Hz | 1.66 | 3.9 dB  |
| Peaking | 4483 Hz | 0.64 | -3.7 dB |
| Peaking | 6246 Hz | 4.17 | 3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SoundMAGIC%20E10/SoundMAGIC%20E10.png)