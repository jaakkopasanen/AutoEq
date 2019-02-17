# VSonic GR02 Bass Edition
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.9; 23 -11.9; 25 -11.9; 28 -11.8; 31 -11.8; 34 -11.7; 37 -11.7; 41 -11.7; 45 -11.6; 49 -11.6; 54 -11.6; 60 -11.6; 66 -11.7; 72 -11.7; 79 -11.8; 87 -11.9; 96 -11.9; 106 -11.8; 116 -11.6; 128 -11.5; 141 -11.4; 155 -11.2; 170 -10.9; 187 -10.6; 206 -10.2; 227 -9.8; 249 -9.4; 274 -9.0; 302 -8.6; 332 -8.2; 365 -7.8; 402 -7.5; 442 -7.0; 486 -6.9; 535 -6.5; 588 -6.0; 647 -5.9; 712 -5.9; 783 -5.8; 861 -6.0; 947 -6.3; 1042 -6.7; 1146 -6.9; 1261 -7.2; 1387 -7.4; 1526 -7.7; 1678 -7.7; 1846 -7.0; 2031 -5.7; 2234 -4.2; 2457 -2.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.4; 4788 -3.3; 5267 -2.8; 5793 -3.5; 6373 -5.8; 7010 -5.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR02 Bass Edition GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR02 Bass Edition ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.37 | -4.9 dB |
| Peaking | 122 Hz  | 0.47 | -4.4 dB |
| Peaking | 657 Hz  | 1.19 | 1.3 dB  |
| Peaking | 1704 Hz | 1.45 | -3.7 dB |
| Peaking | 3112 Hz | 1.08 | 7.4 dB  |
| Peaking | 3302 Hz | 4.12 | -2.5 dB |
| Peaking | 3565 Hz | 1.64 | 3.3 dB  |
| Peaking | 4959 Hz | 0.88 | -2.2 dB |
| Peaking | 5518 Hz | 5.21 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20GR02%20Bass%20Edition/VSonic%20GR02%20Bass%20Edition.png)