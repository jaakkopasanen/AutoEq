# Audio Technica ATH-CKX5iS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.6; 28 -8.6; 31 -8.5; 34 -8.5; 37 -8.5; 41 -8.5; 45 -8.5; 49 -8.4; 54 -8.4; 60 -8.4; 66 -8.4; 72 -8.4; 79 -8.4; 87 -8.4; 96 -8.4; 106 -8.2; 116 -8.0; 128 -7.9; 141 -7.6; 155 -7.4; 170 -7.0; 187 -6.6; 206 -6.2; 227 -5.7; 249 -5.2; 274 -4.7; 302 -4.3; 332 -3.7; 365 -3.2; 402 -2.7; 442 -2.2; 486 -1.9; 535 -1.5; 588 -0.9; 647 -0.7; 712 -0.7; 783 -0.5; 861 -0.9; 947 -1.4; 1042 -2.0; 1146 -2.5; 1261 -3.2; 1387 -4.0; 1526 -5.1; 1678 -5.8; 1846 -5.9; 2031 -5.2; 2234 -5.8; 2457 -6.3; 2703 -7.3; 2973 -7.2; 3270 -5.7; 3597 -4.1; 3957 -4.4; 4353 -6.8; 4788 -9.0; 5267 -10.2; 5793 -8.5; 6373 -5.1; 7010 -2.7; 7711 -4.4; 8482 -4.6; 9330 -4.8; 10263 -7.4; 11289 -6.6; 12418 -4.7; 13660 -6.5; 15026 -5.4; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-CKX5iS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-CKX5iS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 55 Hz    | 0.16 | -4.1 dB |
| Peaking | 756 Hz   | 0.46 | 5.8 dB  |
| Peaking | 1853 Hz  | 0.84 | -4.1 dB |
| Peaking | 5221 Hz  | 4.83 | -6.0 dB |
| Peaking | 20753 Hz | 1.73 | -0.9 dB |
| Peaking | 2167 Hz  | 3.23 | 2.0 dB  |
| Peaking | 3311 Hz  | 1.23 | -3.3 dB |
| Peaking | 3641 Hz  | 3.56 | 4.8 dB  |
| Peaking | 7006 Hz  | 5.76 | 3.1 dB  |
| Peaking | 10582 Hz | 5.34 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 3.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-CKX5iS/Audio%20Technica%20ATH-CKX5iS.png)