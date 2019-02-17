# Grado SR60i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.5; 37 -2.3; 41 -3.3; 45 -4.1; 49 -4.9; 54 -5.7; 60 -6.4; 66 -6.9; 72 -7.4; 79 -7.7; 87 -8.2; 96 -8.6; 106 -8.6; 116 -8.7; 128 -8.8; 141 -8.8; 155 -8.8; 170 -8.6; 187 -8.4; 206 -8.3; 227 -7.8; 249 -7.6; 274 -7.5; 302 -7.3; 332 -7.3; 365 -7.1; 402 -6.9; 442 -6.7; 486 -6.7; 535 -6.6; 588 -6.2; 647 -6.1; 712 -6.3; 783 -6.1; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -7.2; 1387 -8.0; 1526 -9.1; 1678 -9.9; 1846 -12.7; 2031 -16.3; 2234 -14.6; 2457 -11.6; 2703 -9.4; 2973 -7.7; 3270 -8.0; 3597 -7.6; 3957 -5.2; 4353 -5.0; 4788 -4.4; 5267 -6.0; 5793 -5.1; 6373 -4.1; 7010 -7.8; 7711 -8.0; 8482 -8.2; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 27 Hz   | 0.74 | 8.1 dB   |
| Peaking | 120 Hz  | 0.23 | -3.7 dB  |
| Peaking | 1311 Hz | 0.12 | 2.2 dB   |
| Peaking | 2082 Hz | 2.18 | -11.4 dB |
| Peaking | 8880 Hz | 2.78 | -3.2 dB  |
| Peaking | 3493 Hz | 5.38 | -2.6 dB  |
| Peaking | 4367 Hz | 1.51 | 3.1 dB   |
| Peaking | 6212 Hz | 6.87 | 4.6 dB   |
| Peaking | 6584 Hz | 1.12 | -4.1 dB  |
| Peaking | 9250 Hz | 2.26 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR60i/Grado%20SR60i.png)