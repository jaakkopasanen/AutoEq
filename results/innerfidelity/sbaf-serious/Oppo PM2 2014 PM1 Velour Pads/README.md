# Oppo PM2 2014 PM1 Velour Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.2; 25 -4.4; 28 -4.6; 31 -4.7; 34 -4.8; 37 -4.9; 41 -4.9; 45 -4.8; 49 -4.8; 54 -4.8; 60 -4.8; 66 -5.1; 72 -5.8; 79 -6.4; 87 -6.7; 96 -7.1; 106 -7.3; 116 -7.5; 128 -7.8; 141 -8.0; 155 -8.1; 170 -8.2; 187 -8.4; 206 -8.9; 227 -9.2; 249 -9.2; 274 -8.8; 302 -8.0; 332 -7.3; 365 -7.4; 402 -7.4; 442 -7.5; 486 -8.3; 535 -8.7; 588 -8.6; 647 -8.5; 712 -7.8; 783 -7.2; 861 -7.8; 947 -7.1; 1042 -7.2; 1146 -7.3; 1261 -7.0; 1387 -7.4; 1526 -7.5; 1678 -7.6; 1846 -7.1; 2031 -6.5; 2234 -5.5; 2457 -4.5; 2703 -3.7; 2973 -3.2; 3270 -3.1; 3597 -3.5; 3957 -3.2; 4353 -3.8; 4788 -2.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -9.5; 9330 -10.4; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM2 2014 PM1 Velour Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM2 2014 PM1 Velour Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.58 | 3.2 dB  |
| Peaking | 214 Hz  | 0.19 | -2.1 dB |
| Peaking | 3056 Hz | 2.28 | 3.2 dB  |
| Peaking | 5788 Hz | 2.01 | 6.5 dB  |
| Peaking | 8912 Hz | 3.7  | -5.6 dB |
| Peaking | 18 Hz   | 2.09 | 0.9 dB  |
| Peaking | 241 Hz  | 1.84 | -2.0 dB |
| Peaking | 445 Hz  | 0.82 | 2.8 dB  |
| Peaking | 547 Hz  | 1.84 | -2.9 dB |
| Peaking | 1663 Hz | 3.51 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM2%202014%20PM1%20Velour%20Pads/Oppo%20PM2%202014%20PM1%20Velour%20Pads.png)