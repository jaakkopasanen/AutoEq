# Audio Technica ATH-ANC9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -11.1; 25 -11.4; 28 -11.8; 31 -11.9; 34 -11.7; 37 -11.3; 41 -10.3; 45 -9.3; 49 -8.4; 54 -7.6; 60 -6.9; 66 -6.7; 72 -6.7; 79 -7.0; 87 -7.4; 96 -8.0; 106 -8.3; 116 -8.4; 128 -8.4; 141 -8.1; 155 -7.7; 170 -7.1; 187 -6.4; 206 -5.7; 227 -5.0; 249 -4.5; 274 -3.9; 302 -3.4; 332 -2.9; 365 -2.5; 402 -2.7; 442 -2.2; 486 -2.3; 535 -2.0; 588 -1.2; 647 -0.6; 712 -0.5; 783 -0.5; 861 -0.8; 947 -2.9; 1042 -6.1; 1146 -9.4; 1261 -12.5; 1387 -13.9; 1526 -14.2; 1678 -12.4; 1846 -11.1; 2031 -9.7; 2234 -10.0; 2457 -9.4; 2703 -9.8; 2973 -10.7; 3270 -11.1; 3597 -11.2; 3957 -11.4; 4353 -11.2; 4788 -10.0; 5267 -8.8; 5793 -8.4; 6373 -4.5; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ANC9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 1.32 | -5.9 dB  |
| Peaking | 130 Hz  | 1.73 | -2.8 dB  |
| Peaking | 917 Hz  | 0.61 | 14.8 dB  |
| Peaking | 1355 Hz | 1.06 | -18.9 dB |
| Peaking | 3795 Hz | 2.01 | -4.8 dB  |
| Peaking | 42 Hz   | 3.27 | -0.9 dB  |
| Peaking | 62 Hz   | 3.24 | 1.0 dB   |
| Peaking | 525 Hz  | 6.44 | -0.8 dB  |
| Peaking | 5713 Hz | 3.11 | -2.2 dB  |
| Peaking | 6594 Hz | 4.17 | 4.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 6.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | -3.8 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ANC9/Audio%20Technica%20ATH-ANC9.png)