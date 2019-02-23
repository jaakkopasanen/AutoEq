# Audio Technica ATH-Pro700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.4; 66 -2.3; 72 -2.9; 79 -3.4; 87 -3.4; 96 -2.9; 106 -2.7; 116 -2.5; 128 -2.4; 141 -2.2; 155 -1.9; 170 -1.6; 187 -1.0; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -1.8; 332 -5.2; 365 -8.5; 402 -11.2; 442 -13.1; 486 -14.0; 535 -14.2; 588 -14.2; 647 -14.2; 712 -14.1; 783 -14.3; 861 -14.6; 947 -14.6; 1042 -14.4; 1146 -13.7; 1261 -13.5; 1387 -12.6; 1526 -11.7; 1678 -10.5; 1846 -9.0; 2031 -7.5; 2234 -6.2; 2457 -4.9; 2703 -4.8; 2973 -5.0; 3270 -4.1; 3597 -2.3; 3957 -5.1; 4353 -7.5; 4788 -3.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -10.6; 10263 -8.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-Pro700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-Pro700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 115 Hz   | 0.1  | 14.5 dB  |
| Peaking | 277 Hz   | 0.68 | 20.5 dB  |
| Peaking | 422 Hz   | 0.22 | -32.4 dB |
| Peaking | 2748 Hz  | 0.88 | 11.5 dB  |
| Peaking | 5814 Hz  | 2.39 | 9.4 dB   |
| Peaking | 81 Hz    | 5.65 | -1.1 dB  |
| Peaking | 3698 Hz  | 8.76 | 3.5 dB   |
| Peaking | 4217 Hz  | 9.69 | -4.0 dB  |
| Peaking | 9622 Hz  | 4.92 | -5.9 dB  |
| Peaking | 10301 Hz | 1.33 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | 2.2 dB  |
| Peaking | 250 Hz   | 1.41 | 8.2 dB  |
| Peaking | 500 Hz   | 1.41 | -8.4 dB |
| Peaking | 1000 Hz  | 1.41 | -7.8 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-Pro700/Audio%20Technica%20ATH-Pro700.png)