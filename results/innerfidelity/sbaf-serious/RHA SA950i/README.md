# RHA SA950i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.0; 23 -12.4; 25 -12.7; 28 -13.1; 31 -13.3; 34 -13.4; 37 -13.4; 41 -13.5; 45 -13.4; 49 -13.4; 54 -13.3; 60 -13.3; 66 -13.3; 72 -13.3; 79 -13.4; 87 -13.4; 96 -13.2; 106 -13.5; 116 -13.4; 128 -13.5; 141 -13.9; 155 -14.2; 170 -13.9; 187 -14.2; 206 -14.1; 227 -13.8; 249 -13.7; 274 -13.7; 302 -13.8; 332 -14.1; 365 -14.3; 402 -14.3; 442 -14.1; 486 -14.1; 535 -13.7; 588 -12.8; 647 -12.0; 712 -10.6; 783 -9.0; 861 -7.7; 947 -7.1; 1042 -6.6; 1146 -7.6; 1261 -9.7; 1387 -11.6; 1526 -12.4; 1678 -12.1; 1846 -10.6; 2031 -8.5; 2234 -7.0; 2457 -5.4; 2703 -4.2; 2973 -3.3; 3270 -1.9; 3597 -2.2; 3957 -0.7; 4353 -0.5; 4788 -4.1; 5267 -8.6; 5793 -5.0; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA SA950i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA SA950i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.25 | -6.5 dB |
| Peaking | 228 Hz  | 0.72 | -4.5 dB |
| Peaking | 484 Hz  | 1.57 | -5.4 dB |
| Peaking | 1616 Hz | 2.88 | -6.7 dB |
| Peaking | 3737 Hz | 1.54 | 5.7 dB  |
| Peaking | 656 Hz  | 5.92 | -1.2 dB |
| Peaking | 994 Hz  | 4.72 | 2.2 dB  |
| Peaking | 4520 Hz | 4.89 | 6.3 dB  |
| Peaking | 5238 Hz | 2.68 | -8.1 dB |
| Peaking | 6283 Hz | 4.86 | 7.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.6 dB |
| Peaking | 500 Hz   | 1.41 | -6.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20SA950i/RHA%20SA950i.png)