# Audio Technica ATH-M10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -1.0; 54 -1.7; 60 -1.8; 66 -2.1; 72 -2.4; 79 -2.8; 87 -4.4; 96 -5.2; 106 -6.5; 116 -7.3; 128 -8.0; 141 -8.5; 155 -8.7; 170 -8.6; 187 -9.4; 206 -9.5; 227 -9.8; 249 -10.1; 274 -10.3; 302 -10.5; 332 -10.6; 365 -10.6; 402 -10.6; 442 -10.4; 486 -10.6; 535 -10.7; 588 -10.5; 647 -10.6; 712 -11.0; 783 -11.3; 861 -12.0; 947 -12.2; 1042 -9.4; 1146 -8.7; 1261 -10.8; 1387 -10.8; 1526 -9.9; 1678 -8.3; 1846 -7.1; 2031 -6.6; 2234 -5.0; 2457 -2.6; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -7.0; 7010 -7.4; 7711 -9.0; 8482 -10.1; 9330 -9.5; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.39 | 7.9 dB  |
| Peaking | 222 Hz  | 0.28 | -5.2 dB |
| Peaking | 864 Hz  | 3    | -3.2 dB |
| Peaking | 1449 Hz | 2.76 | -3.8 dB |
| Peaking | 3548 Hz | 1.22 | 7.5 dB  |
| Peaking | 2144 Hz | 4.72 | -1.8 dB |
| Peaking | 2630 Hz | 2.88 | 2.2 dB  |
| Peaking | 3466 Hz | 3.84 | -1.7 dB |
| Peaking | 5545 Hz | 3.67 | 5.0 dB  |
| Peaking | 7916 Hz | 1.82 | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -3.1 dB |
| Peaking | 1000 Hz  | 1.41 | -4.8 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 9.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-M10/Audio%20Technica%20ATH-M10.png)