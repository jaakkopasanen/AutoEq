# Sennheiser HD 820
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -1.6; 25 -1.7; 28 -1.7; 31 -1.6; 34 -1.5; 37 -1.4; 41 -1.3; 45 -1.4; 49 -1.4; 54 -1.4; 60 -1.6; 66 -1.9; 72 -2.3; 79 -2.8; 87 -3.4; 96 -4.0; 106 -4.6; 116 -5.0; 128 -5.4; 141 -5.6; 155 -5.6; 170 -5.4; 187 -4.7; 206 -3.3; 227 -1.1; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -1.7; 442 -2.7; 486 -3.5; 535 -4.0; 588 -4.5; 647 -5.3; 712 -6.0; 783 -6.5; 861 -6.7; 947 -6.7; 1042 -6.4; 1146 -6.1; 1261 -5.5; 1387 -5.0; 1526 -4.3; 1678 -3.6; 1846 -3.6; 2031 -4.3; 2234 -4.1; 2457 -3.1; 2703 -2.8; 2973 -1.4; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -1.7; 5267 -2.9; 5793 -4.3; 6373 -5.7; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 820 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 820 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.62 | 5.7 dB  |
| Peaking | 313 Hz  | 1.44 | 6.5 dB  |
| Peaking | 1714 Hz | 4.16 | 2.0 dB  |
| Peaking | 3717 Hz | 1.35 | 6.5 dB  |
| Peaking | 70 Hz   | 3.28 | 0.9 dB  |
| Peaking | 147 Hz  | 2.37 | -1.6 dB |
| Peaking | 472 Hz  | 0.28 | 0.5 dB  |
| Peaking | 877 Hz  | 2.14 | -1.6 dB |
| Peaking | 8903 Hz | 2.67 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 5.7 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20820/Sennheiser%20HD%20820.png)