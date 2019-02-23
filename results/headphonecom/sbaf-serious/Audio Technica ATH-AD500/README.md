# Audio Technica ATH-AD500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -2.0; 87 -2.9; 96 -3.5; 106 -4.3; 116 -4.7; 128 -5.2; 141 -5.4; 155 -5.6; 170 -5.7; 187 -5.7; 206 -5.8; 227 -5.7; 249 -5.9; 274 -5.9; 302 -5.8; 332 -5.8; 365 -5.4; 402 -5.3; 442 -5.4; 486 -5.5; 535 -5.5; 588 -5.4; 647 -5.6; 712 -5.4; 783 -5.8; 861 -6.3; 947 -6.7; 1042 -7.3; 1146 -7.5; 1261 -7.9; 1387 -8.0; 1526 -7.7; 1678 -6.2; 1846 -5.1; 2031 -4.9; 2234 -5.2; 2457 -5.7; 2703 -5.7; 2973 -4.6; 3270 -4.3; 3597 -4.4; 3957 -10.6; 4353 -11.3; 4788 -10.0; 5267 -9.1; 5793 -0.9; 6373 -2.8; 7010 -8.1; 7711 -11.4; 8482 -14.2; 9330 -15.1; 10263 -12.8; 11289 -9.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.49 | 6.7 dB   |
| Peaking | 3499 Hz  | 2.08 | 8.3 dB   |
| Peaking | 4196 Hz  | 2.13 | -10.4 dB |
| Peaking | 6061 Hz  | 5.45 | 9.6 dB   |
| Peaking | 9031 Hz  | 2.39 | -9.3 dB  |
| Peaking | 142 Hz   | 2.12 | -0.8 dB  |
| Peaking | 658 Hz   | 0.82 | 1.5 dB   |
| Peaking | 1464 Hz  | 1.12 | -3.0 dB  |
| Peaking | 1891 Hz  | 2.81 | 3.5 dB   |
| Peaking | 12573 Hz | 4.58 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-AD500/Audio%20Technica%20ATH-AD500.png)