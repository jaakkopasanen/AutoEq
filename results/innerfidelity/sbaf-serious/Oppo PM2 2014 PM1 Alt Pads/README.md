# Oppo PM2 2014 PM1 Alt Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.3; 25 -4.4; 28 -4.5; 31 -4.6; 34 -4.6; 37 -4.7; 41 -4.6; 45 -4.5; 49 -4.4; 54 -4.6; 60 -4.6; 66 -4.9; 72 -5.5; 79 -6.1; 87 -6.4; 96 -6.9; 106 -7.2; 116 -7.3; 128 -7.6; 141 -7.6; 155 -7.8; 170 -7.8; 187 -8.2; 206 -8.6; 227 -8.9; 249 -8.9; 274 -8.4; 302 -7.9; 332 -7.1; 365 -7.4; 402 -7.6; 442 -7.6; 486 -8.1; 535 -8.6; 588 -8.5; 647 -8.5; 712 -7.9; 783 -7.5; 861 -8.2; 947 -7.8; 1042 -7.9; 1146 -8.0; 1261 -7.8; 1387 -8.3; 1526 -8.6; 1678 -8.6; 1846 -8.2; 2031 -7.7; 2234 -7.0; 2457 -6.0; 2703 -5.2; 2973 -4.1; 3270 -3.7; 3597 -3.7; 3957 -2.9; 4353 -3.1; 4788 -1.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.3; 9330 -9.8; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM2 2014 PM1 Alt Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM2 2014 PM1 Alt Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.58 | 3.4 dB  |
| Peaking | 203 Hz  | 0.21 | -2.0 dB |
| Peaking | 1690 Hz | 1.79 | -2.3 dB |
| Peaking | 5965 Hz | 0.9  | 7.3 dB  |
| Peaking | 8641 Hz | 2.16 | -7.5 dB |
| Peaking | 247 Hz  | 2.57 | -1.4 dB |
| Peaking | 340 Hz  | 1.65 | 1.4 dB  |
| Peaking | 571 Hz  | 3.18 | -0.8 dB |
| Peaking | 3068 Hz | 6.11 | 0.9 dB  |
| Peaking | 4418 Hz | 9.61 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM2%202014%20PM1%20Alt%20Pads/Oppo%20PM2%202014%20PM1%20Alt%20Pads.png)