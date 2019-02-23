# Audio Technica ATH-FC700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.2; 72 -1.9; 79 -2.4; 87 -3.3; 96 -4.2; 106 -4.8; 116 -5.2; 128 -5.8; 141 -6.1; 155 -6.3; 170 -6.3; 187 -6.2; 206 -6.1; 227 -6.0; 249 -6.5; 274 -6.7; 302 -6.5; 332 -6.7; 365 -6.9; 402 -6.7; 442 -6.4; 486 -6.5; 535 -6.5; 588 -6.1; 647 -5.8; 712 -5.7; 783 -5.6; 861 -6.0; 947 -6.1; 1042 -6.2; 1146 -6.4; 1261 -6.3; 1387 -6.7; 1526 -8.0; 1678 -8.9; 1846 -9.5; 2031 -9.6; 2234 -9.3; 2457 -7.9; 2703 -6.7; 2973 -5.5; 3270 -4.4; 3597 -3.1; 3957 -1.7; 4353 -2.2; 4788 -1.4; 5267 -1.1; 5793 -8.1; 6373 -8.8; 7010 -14.3; 7711 -13.1; 8482 -10.1; 9330 -7.7; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.2; 16529 -11.0; 18182 -10.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-FC700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-FC700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.61 | 6.9 dB   |
| Peaking | 2069 Hz  | 2.16 | -4.5 dB  |
| Peaking | 4709 Hz  | 1.2  | 6.9 dB   |
| Peaking | 7137 Hz  | 2.67 | -10.9 dB |
| Peaking | 17221 Hz | 1.92 | -5.3 dB  |
| Peaking | 36 Hz    | 1.18 | -4.7 dB  |
| Peaking | 43 Hz    | 0.42 | 4.1 dB   |
| Peaking | 119 Hz   | 0.73 | -2.2 dB  |
| Peaking | 781 Hz   | 2.22 | 0.9 dB   |
| Peaking | 12340 Hz | 2.17 | 0.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-FC700/Audio%20Technica%20ATH-FC700.png)