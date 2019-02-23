# VSonic GR02 Bass Edition
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.3; 23 -12.3; 25 -12.3; 28 -12.3; 31 -12.2; 34 -12.2; 37 -12.1; 41 -12.1; 45 -12.1; 49 -12.0; 54 -12.0; 60 -12.1; 66 -12.1; 72 -12.1; 79 -12.2; 87 -12.3; 96 -12.4; 106 -12.2; 116 -12.1; 128 -12.0; 141 -11.8; 155 -11.6; 170 -11.3; 187 -11.0; 206 -10.7; 227 -10.2; 249 -9.9; 274 -9.4; 302 -9.1; 332 -8.7; 365 -8.3; 402 -7.9; 442 -7.4; 486 -7.3; 535 -6.9; 588 -6.5; 647 -6.3; 712 -6.3; 783 -6.2; 861 -6.4; 947 -6.7; 1042 -7.1; 1146 -7.3; 1261 -7.6; 1387 -7.9; 1526 -8.1; 1678 -8.1; 1846 -7.4; 2031 -6.1; 2234 -4.6; 2457 -2.5; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -2.8; 4788 -3.8; 5267 -3.2; 5793 -3.9; 6373 -6.2; 7010 -6.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR02 Bass Edition GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR02 Bass Edition ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.21 | -5.5 dB |
| Peaking | 150 Hz  | 0.68 | -3.4 dB |
| Peaking | 1702 Hz | 1.83 | -3.7 dB |
| Peaking | 3157 Hz | 1.21 | 7.1 dB  |
| Peaking | 693 Hz  | 2.35 | 0.8 dB  |
| Peaking | 1173 Hz | 4.36 | -0.5 dB |
| Peaking | 5599 Hz | 5.2  | 2.4 dB  |
| Peaking | 6298 Hz | 2.26 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20GR02%20Bass%20Edition/VSonic%20GR02%20Bass%20Edition.png)