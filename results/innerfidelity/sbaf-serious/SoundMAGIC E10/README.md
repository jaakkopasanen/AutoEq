# SoundMAGIC E10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -11.1; 25 -11.5; 28 -11.9; 31 -12.2; 34 -12.5; 37 -12.8; 41 -13.1; 45 -13.4; 49 -13.6; 54 -13.9; 60 -14.3; 66 -14.6; 72 -14.8; 79 -15.2; 87 -15.6; 96 -15.9; 106 -16.2; 116 -16.4; 128 -16.5; 141 -16.6; 155 -16.6; 170 -16.5; 187 -16.3; 206 -16.0; 227 -15.7; 249 -15.3; 274 -14.9; 302 -14.5; 332 -14.0; 365 -13.5; 402 -13.0; 442 -12.4; 486 -11.6; 535 -11.1; 588 -10.8; 647 -10.4; 712 -10.0; 783 -9.8; 861 -9.8; 947 -9.8; 1042 -10.2; 1146 -9.9; 1261 -8.8; 1387 -6.9; 1526 -6.0; 1678 -5.8; 1846 -4.4; 2031 -2.3; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -5.0; 7010 -5.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundMAGIC E10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundMAGIC E10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.28 | -4.0 dB |
| Peaking | 188 Hz  | 0.36 | -8.3 dB |
| Peaking | 1126 Hz | 1.91 | -3.5 dB |
| Peaking | 3179 Hz | 0.75 | 7.2 dB  |
| Peaking | 1794 Hz | 5.53 | -1.6 dB |
| Peaking | 2186 Hz | 3.2  | 1.8 dB  |
| Peaking | 3129 Hz | 2.83 | -1.1 dB |
| Peaking | 5656 Hz | 2.51 | 6.5 dB  |
| Peaking | 6474 Hz | 1.53 | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB |
| Peaking | 125 Hz   | 1.41 | -8.3 dB |
| Peaking | 250 Hz   | 1.41 | -7.4 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | -3.9 dB |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SoundMAGIC%20E10/SoundMAGIC%20E10.png)