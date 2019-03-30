# Sennheiser ie4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.8; 25 -13.2; 28 -13.7; 31 -13.9; 34 -14.1; 37 -14.3; 41 -14.4; 45 -14.5; 49 -14.6; 54 -14.7; 60 -14.8; 66 -14.7; 72 -14.5; 79 -14.5; 87 -14.5; 96 -14.3; 106 -14.1; 116 -14.0; 128 -13.8; 141 -13.5; 155 -13.3; 170 -13.0; 187 -12.7; 206 -12.3; 227 -11.9; 249 -11.5; 274 -11.1; 302 -10.6; 332 -10.0; 365 -9.5; 402 -8.9; 442 -8.3; 486 -7.6; 535 -6.9; 588 -6.6; 647 -6.3; 712 -5.7; 783 -5.1; 861 -4.3; 947 -3.7; 1042 -3.1; 1146 -2.4; 1261 -1.8; 1387 -1.3; 1526 -0.9; 1678 -0.7; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.7; 2703 -1.4; 2973 -2.0; 3270 -2.5; 3597 -3.0; 3957 -3.1; 4353 -3.1; 4788 -3.1; 5267 -3.1; 5793 -4.2; 6373 -8.4; 7010 -11.2; 7711 -9.6; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser ie4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser ie4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.49 | -4.3 dB |
| Peaking | 111 Hz  | 0.31 | -7.0 dB |
| Peaking | 1841 Hz | 0.59 | 6.1 dB  |
| Peaking | 5442 Hz | 2.93 | 2.6 dB  |
| Peaking | 6994 Hz | 3.9  | -7.2 dB |
| Peaking | 1958 Hz | 2.84 | -0.2 dB |
| Peaking | 2394 Hz | 3.7  | 0.4 dB  |
| Peaking | 3572 Hz | 2.04 | -0.4 dB |
| Peaking | 4240 Hz | 3.76 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20ie4/Sennheiser%20ie4.png)