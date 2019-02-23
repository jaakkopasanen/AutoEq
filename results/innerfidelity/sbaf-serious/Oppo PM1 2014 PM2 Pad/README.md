# Oppo PM1 2014 PM2 Pad
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.2; 25 -4.4; 28 -4.6; 31 -4.7; 34 -4.8; 37 -4.9; 41 -5.0; 45 -5.0; 49 -4.9; 54 -4.7; 60 -4.7; 66 -5.2; 72 -5.9; 79 -6.4; 87 -7.0; 96 -7.4; 106 -7.7; 116 -7.9; 128 -8.2; 141 -8.5; 155 -8.6; 170 -8.6; 187 -8.8; 206 -8.8; 227 -8.6; 249 -8.9; 274 -9.3; 302 -9.6; 332 -9.4; 365 -7.6; 402 -6.1; 442 -6.6; 486 -7.5; 535 -7.9; 588 -7.7; 647 -8.0; 712 -8.4; 783 -8.3; 861 -8.5; 947 -6.7; 1042 -6.3; 1146 -6.9; 1261 -7.2; 1387 -7.8; 1526 -8.3; 1678 -8.6; 1846 -8.5; 2031 -8.1; 2234 -7.7; 2457 -6.8; 2703 -5.7; 2973 -4.5; 3270 -4.1; 3597 -4.3; 3957 -3.8; 4353 -3.6; 4788 -2.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -7.0; 9330 -8.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM1 2014 PM2 Pad GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 2014 PM2 Pad ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.21 | 2.4 dB  |
| Peaking | 105 Hz  | 1.66 | -1.1 dB |
| Peaking | 202 Hz  | 0.54 | -3.6 dB |
| Peaking | 1738 Hz | 2.58 | -2.4 dB |
| Peaking | 5442 Hz | 2.06 | 6.4 dB  |
| Peaking | 325 Hz  | 4.3  | -1.5 dB |
| Peaking | 404 Hz  | 4.81 | 2.5 dB  |
| Peaking | 757 Hz  | 3.76 | -1.5 dB |
| Peaking | 3189 Hz | 4.58 | 1.8 dB  |
| Peaking | 9004 Hz | 4.53 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM1%202014%20PM2%20Pad/Oppo%20PM1%202014%20PM2%20Pad.png)