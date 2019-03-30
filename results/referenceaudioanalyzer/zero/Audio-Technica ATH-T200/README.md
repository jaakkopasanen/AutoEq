# Audio-Technica ATH-T200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.7; 34 -2.7; 37 -3.5; 41 -4.5; 45 -5.4; 49 -6.1; 54 -7.1; 60 -7.9; 66 -8.2; 72 -8.1; 79 -8.5; 87 -9.7; 96 -10.8; 106 -11.3; 116 -11.8; 128 -12.2; 141 -12.3; 155 -12.3; 170 -12.2; 187 -11.9; 206 -11.4; 227 -10.9; 249 -10.4; 274 -10.2; 302 -10.0; 332 -10.0; 365 -10.0; 402 -10.0; 442 -10.0; 486 -10.2; 535 -10.5; 588 -10.9; 647 -11.3; 712 -11.8; 783 -12.3; 861 -12.8; 947 -12.8; 1042 -11.7; 1146 -10.7; 1261 -10.9; 1387 -10.1; 1526 -7.9; 1678 -5.2; 1846 -2.7; 2031 -0.6; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -7.1; 7010 -10.0; 7711 -8.0; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-T200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-T200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 1.08 | 6.7 dB   |
| Peaking | 139 Hz   | 0.74 | -5.7 dB  |
| Peaking | 1099 Hz  | 0.67 | -12.1 dB |
| Peaking | 2362 Hz  | 0.48 | 11.5 dB  |
| Peaking | 7133 Hz  | 4.28 | -7.4 dB  |
| Peaking | 1427 Hz  | 6.77 | -1.6 dB  |
| Peaking | 1997 Hz  | 4.52 | 1.8 dB   |
| Peaking | 2924 Hz  | 2.66 | -1.1 dB  |
| Peaking | 5464 Hz  | 4.92 | 3.0 dB   |
| Peaking | 10587 Hz | 1.11 | -1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -7.7 dB |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-T200/Audio-Technica%20ATH-T200.png)