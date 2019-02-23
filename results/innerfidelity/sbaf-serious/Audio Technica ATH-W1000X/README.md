# Audio Technica ATH-W1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -1.1; 41 -2.4; 45 -3.6; 49 -4.5; 54 -5.5; 60 -6.9; 66 -7.8; 72 -8.4; 79 -9.4; 87 -10.1; 96 -10.5; 106 -10.8; 116 -10.7; 128 -10.8; 141 -10.7; 155 -10.7; 170 -10.3; 187 -10.2; 206 -10.1; 227 -9.7; 249 -9.4; 274 -8.9; 302 -8.5; 332 -8.0; 365 -7.4; 402 -6.4; 442 -5.3; 486 -5.8; 535 -7.0; 588 -7.8; 647 -8.0; 712 -8.2; 783 -7.3; 861 -7.7; 947 -8.4; 1042 -8.4; 1146 -8.3; 1261 -8.7; 1387 -9.1; 1526 -9.9; 1678 -9.7; 1846 -9.2; 2031 -9.3; 2234 -8.9; 2457 -7.4; 2703 -4.8; 2973 -3.4; 3270 -2.6; 3597 -2.7; 3957 -2.3; 4353 -5.0; 4788 -1.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -7.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.1; 18182 -10.8; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-W1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-W1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.73 | 7.4 dB  |
| Peaking | 111 Hz   | 0.63 | -5.5 dB |
| Peaking | 2134 Hz  | 0.8  | -4.9 dB |
| Peaking | 3182 Hz  | 1.71 | 6.9 dB  |
| Peaking | 5661 Hz  | 2.75 | 6.7 dB  |
| Peaking | 13 Hz    | 1.55 | 1.2 dB  |
| Peaking | 432 Hz   | 0.99 | -1.4 dB |
| Peaking | 447 Hz   | 3.06 | 3.7 dB  |
| Peaking | 9528 Hz  | 4.15 | -1.1 dB |
| Peaking | 18919 Hz | 1.17 | -5.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-W1000X/Audio%20Technica%20ATH-W1000X.png)