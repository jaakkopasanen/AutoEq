# Audio Technica ATH-CKX5iS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.6; 28 -8.6; 31 -8.5; 34 -8.5; 37 -8.5; 41 -8.5; 45 -8.5; 49 -8.4; 54 -8.4; 60 -8.4; 66 -8.4; 72 -8.4; 79 -8.4; 87 -8.4; 96 -8.4; 106 -8.2; 116 -8.0; 128 -7.9; 141 -7.6; 155 -7.4; 170 -7.0; 187 -6.6; 206 -6.2; 227 -5.7; 249 -5.2; 274 -4.7; 302 -4.3; 332 -3.7; 365 -3.2; 402 -2.7; 442 -2.2; 486 -1.9; 535 -1.5; 588 -0.9; 647 -0.7; 712 -0.7; 783 -0.5; 861 -0.9; 947 -1.4; 1042 -2.0; 1146 -2.5; 1261 -3.2; 1387 -4.0; 1526 -5.1; 1678 -5.8; 1846 -5.9; 2031 -5.2; 2234 -5.8; 2457 -6.3; 2703 -7.3; 2973 -7.2; 3270 -5.7; 3597 -4.1; 3957 -4.4; 4353 -6.8; 4788 -9.0; 5267 -10.2; 5793 -8.5; 6373 -5.1; 7010 -2.4; 7711 -1.5; 8482 -1.8; 9330 -4.2; 10263 -7.4; 11289 -6.6; 12418 -4.6; 13660 -6.5; 15026 -5.2; 16529 -1.7; 18182 -1.7; 20000 -1.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-CKX5iS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-CKX5iS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.25 | -7.3 dB |
| Peaking | 1715 Hz  | 3.22 | -3.6 dB |
| Peaking | 2750 Hz  | 2.6  | -5.1 dB |
| Peaking | 5190 Hz  | 3.45 | -8.5 dB |
| Peaking | 12430 Hz | 1.27 | -4.7 dB |
| Peaking | 21 Hz    | 2.45 | -0.9 dB |
| Peaking | 181 Hz   | 1.54 | -0.9 dB |
| Peaking | 664 Hz   | 1.66 | 2.1 dB  |
| Peaking | 7954 Hz  | 3.92 | 2.6 dB  |
| Peaking | 10323 Hz | 6.56 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | -4.7 dB |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-CKX5iS/Audio%20Technica%20ATH-CKX5iS.png)