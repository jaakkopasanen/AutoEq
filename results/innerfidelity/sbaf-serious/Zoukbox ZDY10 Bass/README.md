# Zoukbox ZDY10 Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.0; 25 -8.1; 28 -8.3; 31 -8.5; 34 -8.6; 37 -8.7; 41 -8.8; 45 -9.0; 49 -9.1; 54 -9.1; 60 -9.4; 66 -9.5; 72 -9.7; 79 -9.9; 87 -10.1; 96 -10.3; 106 -10.3; 116 -10.2; 128 -10.3; 141 -10.2; 155 -10.0; 170 -9.8; 187 -9.4; 206 -9.1; 227 -8.6; 249 -8.1; 274 -7.5; 302 -6.9; 332 -6.4; 365 -5.6; 402 -5.1; 442 -4.3; 486 -3.8; 535 -3.1; 588 -1.9; 647 -1.6; 712 -1.2; 783 -0.6; 861 -0.5; 947 -0.5; 1042 -0.6; 1146 -0.8; 1261 -0.9; 1387 -1.4; 1526 -1.9; 1678 -2.2; 1846 -2.3; 2031 -2.6; 2234 -2.8; 2457 -3.1; 2703 -2.8; 2973 -2.8; 3270 -2.5; 3597 -2.8; 3957 -3.8; 4353 -6.3; 4788 -7.5; 5267 -7.1; 5793 -5.2; 6373 -3.7; 7010 -2.3; 7711 -2.4; 8482 -3.3; 9330 -4.3; 10263 -5.2; 11289 -3.6; 12418 -1.0; 13660 -0.6; 15026 -0.6; 16529 -0.6; 18182 -0.6; 20000 -0.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zoukbox ZDY10 Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zoukbox ZDY10 Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.25 | -7.4 dB |
| Peaking | 144 Hz   | 0.68 | -5.3 dB |
| Peaking | 295 Hz   | 1.2  | -2.8 dB |
| Peaking | 4874 Hz  | 1.69 | -6.6 dB |
| Peaking | 10098 Hz | 3.27 | -4.5 dB |
| Peaking | 912 Hz   | 1.88 | 1.3 dB  |
| Peaking | 1995 Hz  | 1.24 | -1.2 dB |
| Peaking | 2546 Hz  | 2.12 | -0.7 dB |
| Peaking | 3619 Hz  | 3.93 | 1.6 dB  |
| Peaking | 13303 Hz | 4.25 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.6 dB |
| Peaking | 62 Hz    | 1.41 | -6.5 dB |
| Peaking | 125 Hz   | 1.41 | -8.1 dB |
| Peaking | 250 Hz   | 1.41 | -6.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | -4.1 dB |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Zoukbox%20ZDY10%20Bass/Zoukbox%20ZDY10%20Bass.png)