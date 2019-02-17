# Oppo PM2 2014 PM1 Alt Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -2.9; 25 -3.0; 28 -3.1; 31 -3.2; 34 -3.3; 37 -3.3; 41 -3.3; 45 -3.1; 49 -3.0; 54 -3.3; 60 -3.2; 66 -3.5; 72 -4.1; 79 -4.7; 87 -5.0; 96 -5.5; 106 -5.8; 116 -5.9; 128 -6.2; 141 -6.3; 155 -6.4; 170 -6.4; 187 -6.8; 206 -7.3; 227 -7.5; 249 -7.6; 274 -7.0; 302 -6.6; 332 -5.8; 365 -6.0; 402 -6.2; 442 -6.2; 486 -6.7; 535 -7.2; 588 -7.1; 647 -7.1; 712 -6.6; 783 -6.1; 861 -6.8; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.5; 1387 -7.0; 1526 -7.2; 1678 -7.2; 1846 -6.8; 2031 -6.4; 2234 -5.7; 2457 -4.7; 2703 -3.8; 2973 -2.7; 3270 -2.3; 3597 -2.3; 3957 -1.6; 4353 -1.7; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.9; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM2 2014 PM1 Alt Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM2 2014 PM1 Alt Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.69 | 3.4 dB  |
| Peaking | 57 Hz   | 1.45 | 2.4 dB  |
| Peaking | 230 Hz  | 3.33 | -1.4 dB |
| Peaking | 5279 Hz | 1    | 6.8 dB  |
| Peaking | 8630 Hz | 2.35 | -4.6 dB |
| Peaking | 346 Hz  | 5.11 | 0.9 dB  |
| Peaking | 576 Hz  | 4.07 | -0.8 dB |
| Peaking | 1737 Hz | 1.92 | -1.6 dB |
| Peaking | 3039 Hz | 2.51 | 1.5 dB  |
| Peaking | 4475 Hz | 6.08 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM2%202014%20PM1%20Alt%20Pads/Oppo%20PM2%202014%20PM1%20Alt%20Pads.png)