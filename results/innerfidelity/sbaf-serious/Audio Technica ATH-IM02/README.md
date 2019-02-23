# Audio Technica ATH-IM02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.4; 25 -4.5; 28 -4.7; 31 -4.8; 34 -5.0; 37 -5.1; 41 -5.3; 45 -5.5; 49 -5.7; 54 -6.0; 60 -6.2; 66 -6.6; 72 -7.0; 79 -7.3; 87 -7.8; 96 -8.2; 106 -8.5; 116 -8.7; 128 -9.0; 141 -9.3; 155 -9.6; 170 -9.6; 187 -9.7; 206 -9.7; 227 -9.7; 249 -9.7; 274 -9.5; 302 -9.4; 332 -9.1; 365 -8.8; 402 -8.6; 442 -8.1; 486 -7.9; 535 -7.5; 588 -6.8; 647 -6.6; 712 -6.3; 783 -6.0; 861 -6.0; 947 -6.1; 1042 -6.4; 1146 -6.5; 1261 -6.8; 1387 -7.3; 1526 -8.0; 1678 -8.5; 1846 -8.7; 2031 -8.9; 2234 -8.6; 2457 -7.0; 2703 -3.7; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.4; 4788 -4.0; 5267 -6.2; 5793 -5.7; 6373 -3.5; 7010 -4.6; 7711 -7.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -6.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-IM02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-IM02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.56 | 2.3 dB  |
| Peaking | 191 Hz  | 0.65 | -3.5 dB |
| Peaking | 2241 Hz | 1.78 | -6.7 dB |
| Peaking | 3037 Hz | 1.54 | 8.6 dB  |
| Peaking | 3995 Hz | 5.18 | 2.4 dB  |
| Peaking | 829 Hz  | 2.42 | 1.1 dB  |
| Peaking | 1595 Hz | 5.55 | -0.8 dB |
| Peaking | 5533 Hz | 6.28 | -2.5 dB |
| Peaking | 6680 Hz | 3.45 | 3.6 dB  |
| Peaking | 7578 Hz | 3.56 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-IM02/Audio%20Technica%20ATH-IM02.png)