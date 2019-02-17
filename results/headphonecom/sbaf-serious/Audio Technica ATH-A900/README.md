# Audio Technica ATH-A900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.4; 49 -2.1; 54 -2.9; 60 -3.2; 66 -2.5; 72 -1.9; 79 -3.1; 87 -4.0; 96 -3.9; 106 -3.3; 116 -3.5; 128 -3.5; 141 -3.4; 155 -3.1; 170 -2.3; 187 -2.2; 206 -1.8; 227 -1.6; 249 -1.9; 274 -3.2; 302 -5.1; 332 -6.9; 365 -8.4; 402 -8.9; 442 -8.6; 486 -8.2; 535 -7.7; 588 -7.3; 647 -6.9; 712 -7.0; 783 -6.3; 861 -5.7; 947 -6.5; 1042 -6.7; 1146 -7.1; 1261 -7.6; 1387 -8.4; 1526 -7.5; 1678 -7.3; 1846 -7.3; 2031 -7.1; 2234 -6.1; 2457 -4.7; 2703 -4.0; 2973 -3.9; 3270 -3.0; 3597 -2.0; 3957 -2.3; 4353 -3.2; 4788 -1.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.1; 18182 -6.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.37 | 6.1 dB  |
| Peaking | 173 Hz   | 2.46 | 3.1 dB  |
| Peaking | 237 Hz   | 4.62 | 4.0 dB  |
| Peaking | 3571 Hz  | 2.51 | 3.8 dB  |
| Peaking | 5634 Hz  | 2.7  | 6.3 dB  |
| Peaking | 419 Hz   | 2.95 | -3.1 dB |
| Peaking | 1372 Hz  | 5.08 | -1.9 dB |
| Peaking | 1951 Hz  | 2.89 | -1.3 dB |
| Peaking | 2570 Hz  | 4.74 | 1.5 dB  |
| Peaking | 16848 Hz | 3.38 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | 2.3 dB  |
| Peaking | 250 Hz   | 1.41 | 4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -3.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-A900/Audio%20Technica%20ATH-A900.png)