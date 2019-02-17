# Audio Technica ATH-CKM500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.9; 25 -4.4; 28 -5.0; 31 -5.5; 34 -6.0; 37 -6.4; 41 -7.0; 45 -7.4; 49 -7.9; 54 -8.4; 60 -8.9; 66 -9.4; 72 -9.9; 79 -10.4; 87 -10.9; 96 -11.3; 106 -11.6; 116 -11.8; 128 -12.1; 141 -12.3; 155 -12.3; 170 -12.3; 187 -12.2; 206 -12.0; 227 -11.6; 249 -11.3; 274 -10.8; 302 -10.2; 332 -9.5; 365 -8.8; 402 -8.0; 442 -7.0; 486 -6.2; 535 -5.2; 588 -3.9; 647 -2.9; 712 -2.1; 783 -1.1; 861 -0.7; 947 -0.5; 1042 -0.6; 1146 -1.0; 1261 -1.8; 1387 -2.7; 1526 -3.7; 1678 -4.4; 1846 -4.8; 2031 -5.3; 2234 -5.9; 2457 -6.0; 2703 -6.4; 2973 -6.6; 3270 -5.9; 3597 -5.3; 3957 -5.2; 4353 -7.1; 4788 -8.3; 5267 -8.8; 5793 -10.0; 6373 -8.3; 7010 -6.6; 7711 -4.9; 8482 -4.6; 9330 -6.5; 10263 -8.0; 11289 -3.4; 12418 -0.6; 13660 -0.6; 15026 -0.6; 16529 -0.6; 18182 -0.6; 20000 -0.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-CKM500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-CKM500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 97 Hz    | 0.41 | -9.7 dB |
| Peaking | 261 Hz   | 0.88 | -5.8 dB |
| Peaking | 2500 Hz  | 1.48 | -5.0 dB |
| Peaking | 5645 Hz  | 1.59 | -8.6 dB |
| Peaking | 10066 Hz | 4.5  | -6.6 dB |
| Peaking | 30 Hz    | 2.24 | -0.7 dB |
| Peaking | 471 Hz   | 2.13 | -1.5 dB |
| Peaking | 914 Hz   | 1.29 | 2.3 dB  |
| Peaking | 1598 Hz  | 2.83 | -1.7 dB |
| Peaking | 12364 Hz | 5.1  | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -6.5 dB |
| Peaking | 125 Hz   | 1.41 | -9.5 dB |
| Peaking | 250 Hz   | 1.41 | -9.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.5 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | -5.5 dB |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-CKM500/Audio%20Technica%20ATH-CKM500.png)