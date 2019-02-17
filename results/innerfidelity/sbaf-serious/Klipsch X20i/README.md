# Klipsch X20i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.0; 25 -7.1; 28 -7.3; 31 -7.4; 34 -7.6; 37 -7.6; 41 -7.8; 45 -7.9; 49 -8.0; 54 -8.3; 60 -8.5; 66 -8.8; 72 -9.2; 79 -9.5; 87 -9.8; 96 -10.2; 106 -10.4; 116 -10.6; 128 -10.8; 141 -10.9; 155 -11.0; 170 -11.0; 187 -11.0; 206 -11.0; 227 -10.8; 249 -10.6; 274 -10.4; 302 -10.1; 332 -9.8; 365 -9.4; 402 -9.1; 442 -8.7; 486 -8.4; 535 -7.9; 588 -7.3; 647 -6.9; 712 -6.6; 783 -6.2; 861 -6.2; 947 -6.3; 1042 -6.5; 1146 -6.6; 1261 -6.8; 1387 -7.3; 1526 -7.7; 1678 -7.9; 1846 -7.9; 2031 -7.8; 2234 -8.0; 2457 -7.7; 2703 -7.3; 2973 -5.1; 3270 -1.4; 3597 -0.5; 3957 -0.5; 4353 -1.4; 4788 -2.7; 5267 -2.7; 5793 -2.1; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch X20i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X20i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 131 Hz  | 0.59 | -4.0 dB |
| Peaking | 285 Hz  | 1.19 | -2.0 dB |
| Peaking | 2561 Hz | 1.44 | -4.2 dB |
| Peaking | 3649 Hz | 1.78 | 8.3 dB  |
| Peaking | 6216 Hz | 4.67 | 4.6 dB  |
| Peaking | 491 Hz  | 1.8  | -1.0 dB |
| Peaking | 731 Hz  | 0.91 | 1.1 dB  |
| Peaking | 1565 Hz | 3.57 | -0.9 dB |
| Peaking | 8238 Hz | 4.09 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X20i/Klipsch%20X20i.png)