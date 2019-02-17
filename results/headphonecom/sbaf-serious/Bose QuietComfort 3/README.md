# Bose QuietComfort 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.9; 25 -11.1; 28 -11.2; 31 -11.2; 34 -11.2; 37 -11.1; 41 -10.9; 45 -10.8; 49 -10.7; 54 -10.6; 60 -10.5; 66 -10.7; 72 -10.7; 79 -10.9; 87 -11.1; 96 -11.3; 106 -11.3; 116 -11.4; 128 -11.5; 141 -11.5; 155 -11.5; 170 -11.2; 187 -11.0; 206 -10.6; 227 -10.1; 249 -9.6; 274 -9.1; 302 -8.7; 332 -8.2; 365 -7.8; 402 -7.4; 442 -7.2; 486 -7.1; 535 -6.9; 588 -6.7; 647 -6.9; 712 -7.0; 783 -7.0; 861 -6.6; 947 -6.4; 1042 -6.7; 1146 -7.0; 1261 -7.2; 1387 -7.0; 1526 -5.6; 1678 -5.1; 1846 -3.3; 2031 -1.7; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -0.6; 3270 -1.0; 3597 -2.4; 3957 -4.0; 4353 -5.1; 4788 -2.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.4  | -4.3 dB |
| Peaking | 148 Hz  | 0.7  | -4.4 dB |
| Peaking | 2605 Hz | 1.74 | 6.6 dB  |
| Peaking | 5880 Hz | 2.39 | 6.6 dB  |
| Peaking | 7919 Hz | 2.11 | -1.7 dB |
| Peaking | 1309 Hz | 3.3  | -1.6 dB |
| Peaking | 2016 Hz | 6.81 | 1.3 dB  |
| Peaking | 4096 Hz | 7.26 | -2.7 dB |
| Peaking | 4196 Hz | 2.79 | 2.4 dB  |
| Peaking | 4398 Hz | 9.3  | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Bose%20QuietComfort%203/Bose%20QuietComfort%203.png)