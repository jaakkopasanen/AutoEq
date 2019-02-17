# Oppo PM1 2014 Alt Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.0; 25 -4.2; 28 -4.4; 31 -4.6; 34 -4.7; 37 -4.8; 41 -4.8; 45 -4.8; 49 -4.8; 54 -4.7; 60 -4.4; 66 -4.7; 72 -5.8; 79 -6.4; 87 -6.7; 96 -7.4; 106 -7.6; 116 -7.8; 128 -8.1; 141 -8.4; 155 -8.5; 170 -8.5; 187 -8.7; 206 -8.7; 227 -8.6; 249 -8.9; 274 -9.3; 302 -9.6; 332 -9.5; 365 -8.0; 402 -6.6; 442 -7.0; 486 -7.7; 535 -8.0; 588 -7.7; 647 -8.1; 712 -8.6; 783 -8.7; 861 -9.0; 947 -7.1; 1042 -6.5; 1146 -6.8; 1261 -6.8; 1387 -7.3; 1526 -7.6; 1678 -7.6; 1846 -7.0; 2031 -6.5; 2234 -6.0; 2457 -5.0; 2703 -4.2; 2973 -3.0; 3270 -2.6; 3597 -2.7; 3957 -1.9; 4353 -1.6; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.3; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM1 2014 Alt Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 2014 Alt Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 53 Hz   | 0.18 | 2.6 dB  |
| Peaking | 147 Hz  | 0.72 | -4.1 dB |
| Peaking | 301 Hz  | 3.1  | -2.7 dB |
| Peaking | 762 Hz  | 1.72 | -2.3 dB |
| Peaking | 4811 Hz | 1.41 | 6.4 dB  |
| Peaking | 1685 Hz | 3.53 | -1.6 dB |
| Peaking | 3074 Hz | 3.4  | 1.7 dB  |
| Peaking | 4490 Hz | 4.28 | -1.2 dB |
| Peaking | 6255 Hz | 4.82 | 2.6 dB  |
| Peaking | 8841 Hz | 2.84 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM1%202014%20Alt%20Pads/Oppo%20PM1%202014%20Alt%20Pads.png)