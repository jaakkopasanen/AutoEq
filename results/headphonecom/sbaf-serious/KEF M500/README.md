# KEF M500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.5; 25 -10.5; 28 -10.5; 31 -10.5; 34 -10.5; 37 -10.4; 41 -10.3; 45 -10.4; 49 -10.5; 54 -10.5; 60 -10.5; 66 -10.7; 72 -10.9; 79 -11.1; 87 -11.0; 96 -10.9; 106 -11.3; 116 -11.3; 128 -12.0; 141 -12.6; 155 -12.8; 170 -12.7; 187 -12.6; 206 -12.5; 227 -12.7; 249 -12.4; 274 -11.6; 302 -10.5; 332 -8.9; 365 -7.9; 402 -7.7; 442 -7.8; 486 -8.2; 535 -8.7; 588 -8.8; 647 -8.7; 712 -8.1; 783 -7.4; 861 -6.7; 947 -6.0; 1042 -5.3; 1146 -4.5; 1261 -4.3; 1387 -4.5; 1526 -4.4; 1678 -4.4; 1846 -4.2; 2031 -4.2; 2234 -4.2; 2457 -4.3; 2703 -4.7; 2973 -4.9; 3270 -5.3; 3597 -4.8; 3957 -3.8; 4353 -1.7; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KEF M500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KEF M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.19 | -3.9 dB |
| Peaking | 197 Hz  | 1.03 | -4.9 dB |
| Peaking | 665 Hz  | 2.21 | -2.7 dB |
| Peaking | 1433 Hz | 0.68 | 2.5 dB  |
| Peaking | 5350 Hz | 2.16 | 6.5 dB  |
| Peaking | 273 Hz  | 4.9  | -1.0 dB |
| Peaking | 368 Hz  | 4.43 | 1.2 dB  |
| Peaking | 3350 Hz | 8.46 | -0.8 dB |
| Peaking | 6447 Hz | 6.44 | 2.5 dB  |
| Peaking | 7767 Hz | 2.19 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/KEF%20M500/KEF%20M500.png)