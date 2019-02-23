# Audio Technica ATH-WS55
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -6.0; 25 -6.7; 28 -7.5; 31 -8.1; 34 -8.7; 37 -9.1; 41 -9.4; 45 -9.8; 49 -10.3; 54 -10.6; 60 -10.9; 66 -11.2; 72 -11.2; 79 -11.4; 87 -11.5; 96 -11.6; 106 -12.0; 116 -12.3; 128 -12.7; 141 -12.9; 155 -13.0; 170 -12.7; 187 -12.7; 206 -12.4; 227 -11.4; 249 -10.4; 274 -9.8; 302 -9.4; 332 -8.9; 365 -8.8; 402 -8.3; 442 -7.4; 486 -7.2; 535 -7.2; 588 -7.3; 647 -7.6; 712 -8.1; 783 -8.4; 861 -8.9; 947 -9.3; 1042 -9.5; 1146 -7.8; 1261 -9.0; 1387 -9.6; 1526 -9.6; 1678 -8.6; 1846 -7.5; 2031 -5.7; 2234 -3.8; 2457 -1.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.5; 6373 -5.1; 7010 -7.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-WS55 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-WS55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.9  | -3.4 dB |
| Peaking | 164 Hz  | 0.87 | -5.9 dB |
| Peaking | 934 Hz  | 2.61 | -2.6 dB |
| Peaking | 1558 Hz | 2.1  | -4.7 dB |
| Peaking | 3409 Hz | 0.96 | 7.3 dB  |
| Peaking | 1980 Hz | 5.09 | -0.5 dB |
| Peaking | 2597 Hz | 4.66 | 1.5 dB  |
| Peaking | 3433 Hz | 3.12 | -1.2 dB |
| Peaking | 5611 Hz | 2.88 | 5.4 dB  |
| Peaking | 6448 Hz | 1.98 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-WS55/Audio%20Technica%20ATH-WS55.png)