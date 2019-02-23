# Audio Technica ATH-AD500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.6; 66 -2.6; 72 -3.3; 79 -3.8; 87 -4.6; 96 -5.8; 106 -6.4; 116 -6.6; 128 -7.1; 141 -7.4; 155 -7.5; 170 -7.6; 187 -7.7; 206 -7.7; 227 -7.5; 249 -7.6; 274 -7.6; 302 -7.5; 332 -7.5; 365 -7.4; 402 -7.3; 442 -7.2; 486 -7.4; 535 -7.4; 588 -7.3; 647 -7.4; 712 -7.5; 783 -7.4; 861 -7.9; 947 -8.4; 1042 -8.7; 1146 -9.1; 1261 -9.5; 1387 -9.8; 1526 -9.6; 1678 -9.0; 1846 -8.6; 2031 -7.5; 2234 -6.9; 2457 -5.1; 2703 -4.1; 2973 -1.4; 3270 -1.0; 3597 -1.0; 3957 -5.6; 4353 -7.2; 4788 -6.3; 5267 -2.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.4; 9330 -11.5; 10263 -9.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.59 | 7.5 dB  |
| Peaking | 622 Hz  | 0.07 | -1.9 dB |
| Peaking | 3196 Hz | 3.2  | 7.8 dB  |
| Peaking | 6075 Hz | 3.34 | 7.7 dB  |
| Peaking | 9255 Hz | 4.69 | -5.5 dB |
| Peaking | 35 Hz   | 3.73 | -0.5 dB |
| Peaking | 599 Hz  | 1.02 | 1.1 dB  |
| Peaking | 1443 Hz | 1.42 | -2.8 dB |
| Peaking | 2398 Hz | 0.55 | 1.2 dB  |
| Peaking | 4335 Hz | 6.31 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-AD500/Audio%20Technica%20ATH-AD500.png)