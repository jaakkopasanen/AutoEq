# Audio Technica ATH-FC700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -1.4; 72 -2.2; 79 -2.6; 87 -3.5; 96 -4.5; 106 -5.1; 116 -5.5; 128 -6.0; 141 -6.4; 155 -6.6; 170 -6.5; 187 -6.4; 206 -6.4; 227 -6.2; 249 -6.7; 274 -6.9; 302 -6.7; 332 -7.0; 365 -7.2; 402 -6.9; 442 -6.7; 486 -6.7; 535 -6.7; 588 -6.3; 647 -6.1; 712 -6.0; 783 -5.9; 861 -6.2; 947 -6.4; 1042 -6.4; 1146 -6.6; 1261 -6.5; 1387 -6.9; 1526 -8.2; 1678 -9.1; 1846 -9.8; 2031 -9.9; 2234 -9.5; 2457 -8.1; 2703 -6.9; 2973 -5.7; 3270 -4.7; 3597 -3.3; 3957 -1.9; 4353 -2.5; 4788 -1.6; 5267 -1.2; 5793 -8.3; 6373 -9.0; 7010 -14.5; 7711 -13.4; 8482 -10.3; 9330 -7.9; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.4; 16529 -11.3; 18182 -10.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-FC700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-FC700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.66 | 6.9 dB   |
| Peaking | 2052 Hz  | 2.05 | -4.6 dB  |
| Peaking | 4708 Hz  | 1.29 | 6.8 dB   |
| Peaking | 7158 Hz  | 2.66 | -10.8 dB |
| Peaking | 17055 Hz | 1.89 | -5.6 dB  |
| Peaking | 35 Hz    | 1.26 | -4.0 dB  |
| Peaking | 63 Hz    | 0.12 | 3.4 dB   |
| Peaking | 134 Hz   | 0.87 | -3.6 dB  |
| Peaking | 345 Hz   | 1.02 | -2.3 dB  |
| Peaking | 12744 Hz | 2.19 | 1.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-FC700/Audio%20Technica%20ATH-FC700.png)