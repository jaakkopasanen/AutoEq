# Skullcandy Roc Nation Aviator
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.2; 31 -2.2; 34 -3.3; 37 -4.3; 41 -5.4; 45 -6.4; 49 -7.2; 54 -8.0; 60 -8.9; 66 -9.6; 72 -10.2; 79 -10.8; 87 -11.4; 96 -12.0; 106 -12.2; 116 -12.3; 128 -12.6; 141 -12.7; 155 -12.8; 170 -12.7; 187 -12.6; 206 -12.6; 227 -12.2; 249 -12.1; 274 -11.8; 302 -11.5; 332 -11.2; 365 -10.9; 402 -10.7; 442 -10.3; 486 -10.1; 535 -9.5; 588 -8.8; 647 -8.7; 712 -7.9; 783 -6.2; 861 -5.9; 947 -5.7; 1042 -6.4; 1146 -6.6; 1261 -7.2; 1387 -9.1; 1526 -10.2; 1678 -10.6; 1846 -10.6; 2031 -10.1; 2234 -9.4; 2457 -8.5; 2703 -8.5; 2973 -9.4; 3270 -10.2; 3597 -9.8; 3957 -11.1; 4353 -14.8; 4788 -14.3; 5267 -10.2; 5793 -6.6; 6373 -5.8; 7010 -5.7; 7711 -6.5; 8482 -10.6; 9330 -13.0; 10263 -11.9; 11289 -9.2; 12418 -6.7; 13660 -7.2; 15026 -7.4; 16529 -6.5; 18182 -6.5; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Roc Nation Aviator GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Roc Nation Aviator ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.98 | 7.1 dB  |
| Peaking | 151 Hz  | 0.41 | -6.7 dB |
| Peaking | 1853 Hz | 2.34 | -4.1 dB |
| Peaking | 4458 Hz | 3.9  | -8.9 dB |
| Peaking | 9661 Hz | 3.75 | -7.0 dB |
| Peaking | 562 Hz  | 0.99 | -3.4 dB |
| Peaking | 872 Hz  | 0.63 | 4.1 dB  |
| Peaking | 1456 Hz | 3.74 | -2.6 dB |
| Peaking | 4394 Hz | 0.38 | -1.6 dB |
| Peaking | 6544 Hz | 2.33 | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | -4.4 dB |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Roc%20Nation%20Aviator/Skullcandy%20Roc%20Nation%20Aviator.png)