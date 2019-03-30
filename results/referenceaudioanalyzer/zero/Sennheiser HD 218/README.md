# Sennheiser HD 218
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.2; 41 -1.9; 45 -2.4; 49 -2.9; 54 -3.4; 60 -4.0; 66 -4.6; 72 -4.9; 79 -5.1; 87 -5.2; 96 -5.3; 106 -5.7; 116 -6.3; 128 -7.0; 141 -7.4; 155 -7.8; 170 -7.8; 187 -7.6; 206 -7.7; 227 -8.1; 249 -8.7; 274 -8.9; 302 -8.5; 332 -7.9; 365 -7.5; 402 -7.1; 442 -6.6; 486 -6.2; 535 -6.1; 588 -5.9; 647 -5.8; 712 -5.5; 783 -5.4; 861 -5.2; 947 -5.2; 1042 -5.1; 1146 -4.8; 1261 -4.6; 1387 -4.2; 1526 -3.9; 1678 -3.5; 1846 -3.1; 2031 -2.6; 2234 -2.4; 2457 -2.7; 2703 -2.9; 2973 -2.5; 3270 -1.4; 3597 -1.1; 3957 -3.5; 4353 -7.1; 4788 -9.2; 5267 -10.6; 5793 -11.3; 6373 -11.3; 7010 -12.0; 7711 -13.1; 8482 -12.6; 9330 -10.2; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 218 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 218 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.65 | 6.3 dB  |
| Peaking | 242 Hz   | 1.16 | -2.4 dB |
| Peaking | 2197 Hz  | 0.73 | 4.1 dB  |
| Peaking | 3543 Hz  | 3.97 | 5.1 dB  |
| Peaking | 6677 Hz  | 1.15 | -7.1 dB |
| Peaking | 94 Hz    | 6.54 | 0.3 dB  |
| Peaking | 4997 Hz  | 4.7  | -1.2 dB |
| Peaking | 6672 Hz  | 4.16 | 1.8 dB  |
| Peaking | 8593 Hz  | 2.38 | -4.2 dB |
| Peaking | 10090 Hz | 1.35 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.2 dB |
| Peaking | 16000 Hz | 1.41 | 1.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20218/Sennheiser%20HD%20218.png)