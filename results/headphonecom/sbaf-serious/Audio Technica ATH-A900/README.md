# Audio Technica ATH-A900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.6; 41 -2.9; 45 -3.9; 49 -4.7; 54 -5.5; 60 -5.7; 66 -5.1; 72 -4.4; 79 -5.6; 87 -6.5; 96 -6.4; 106 -5.8; 116 -6.0; 128 -6.0; 141 -5.9; 155 -5.6; 170 -4.8; 187 -4.7; 206 -4.3; 227 -4.1; 249 -4.4; 274 -5.7; 302 -7.6; 332 -9.4; 365 -10.9; 402 -11.4; 442 -11.1; 486 -10.7; 535 -10.3; 588 -9.8; 647 -9.4; 712 -9.5; 783 -8.9; 861 -8.2; 947 -9.0; 1042 -9.2; 1146 -9.6; 1261 -10.1; 1387 -10.9; 1526 -10.0; 1678 -9.8; 1846 -9.9; 2031 -9.6; 2234 -8.6; 2457 -7.2; 2703 -6.5; 2973 -6.4; 3270 -5.5; 3597 -4.5; 3957 -4.8; 4353 -5.7; 4788 -3.8; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.7; 16529 -10.6; 18182 -8.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.79 | 6.4 dB  |
| Peaking | 444 Hz   | 2.24 | -5.0 dB |
| Peaking | 1408 Hz  | 1.17 | -4.0 dB |
| Peaking | 5718 Hz  | 2.53 | 6.7 dB  |
| Peaking | 16982 Hz | 2.49 | -4.7 dB |
| Peaking | 234 Hz   | 0.4  | -2.3 dB |
| Peaking | 248 Hz   | 0.9  | 5.5 dB  |
| Peaking | 336 Hz   | 3.23 | -3.4 dB |
| Peaking | 3434 Hz  | 4.86 | 1.7 dB  |
| Peaking | 8044 Hz  | 4.98 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -5.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-A900/Audio%20Technica%20ATH-A900.png)