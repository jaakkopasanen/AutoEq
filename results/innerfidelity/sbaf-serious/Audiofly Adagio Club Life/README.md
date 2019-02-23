# Audiofly Adagio Club Life
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.2; 31 -1.7; 34 -2.1; 37 -2.5; 41 -3.0; 45 -3.4; 49 -3.8; 54 -4.2; 60 -4.6; 66 -5.1; 72 -5.5; 79 -6.0; 87 -6.4; 96 -6.8; 106 -7.1; 116 -7.4; 128 -7.7; 141 -8.0; 155 -8.2; 170 -8.5; 187 -8.5; 206 -8.6; 227 -8.4; 249 -8.4; 274 -8.3; 302 -8.1; 332 -7.9; 365 -7.7; 402 -7.4; 442 -6.9; 486 -6.8; 535 -6.5; 588 -6.1; 647 -5.8; 712 -6.1; 783 -5.9; 861 -6.3; 947 -6.8; 1042 -7.6; 1146 -8.4; 1261 -9.1; 1387 -9.7; 1526 -9.7; 1678 -9.2; 1846 -8.1; 2031 -6.8; 2234 -5.9; 2457 -5.2; 2703 -5.2; 2973 -5.9; 3270 -5.4; 3597 -3.1; 3957 -0.8; 4353 -1.5; 4788 -2.1; 5267 -2.3; 5793 -4.0; 6373 -5.7; 7010 -8.0; 7711 -8.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audiofly Adagio Club Life GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audiofly Adagio Club Life ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.89 | 5.9 dB  |
| Peaking | 47 Hz   | 1.38 | 1.3 dB  |
| Peaking | 189 Hz  | 0.93 | -2.3 dB |
| Peaking | 1458 Hz | 2.76 | -3.8 dB |
| Peaking | 4291 Hz | 2.3  | 5.8 dB  |
| Peaking | 697 Hz  | 1.7  | 1.6 dB  |
| Peaking | 1297 Hz | 0.25 | -0.6 dB |
| Peaking | 2402 Hz | 4.29 | 1.6 dB  |
| Peaking | 5465 Hz | 5.59 | 2.0 dB  |
| Peaking | 7326 Hz | 5.25 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audiofly%20Adagio%20Club%20Life/Audiofly%20Adagio%20Club%20Life.png)