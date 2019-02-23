# Westone W10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.6; 25 -2.9; 28 -3.4; 31 -3.8; 34 -4.2; 37 -4.5; 41 -4.9; 45 -5.3; 49 -5.6; 54 -5.9; 60 -6.4; 66 -6.8; 72 -7.2; 79 -7.7; 87 -8.1; 96 -8.7; 106 -9.0; 116 -9.3; 128 -9.7; 141 -10.0; 155 -10.3; 170 -10.4; 187 -10.5; 206 -10.7; 227 -10.6; 249 -10.7; 274 -10.6; 302 -10.5; 332 -10.4; 365 -10.3; 402 -10.3; 442 -10.0; 486 -9.8; 535 -9.6; 588 -9.0; 647 -8.7; 712 -8.8; 783 -8.4; 861 -8.5; 947 -8.5; 1042 -8.6; 1146 -8.6; 1261 -8.5; 1387 -8.6; 1526 -8.6; 1678 -8.2; 1846 -7.4; 2031 -6.3; 2234 -5.2; 2457 -3.9; 2703 -3.1; 2973 -2.2; 3270 -1.5; 3597 -1.3; 3957 -0.8; 4353 -0.7; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.3  | 4.9 dB  |
| Peaking | 232 Hz  | 0.36 | -4.4 dB |
| Peaking | 1496 Hz | 1.76 | -2.5 dB |
| Peaking | 4237 Hz | 0.99 | 6.7 dB  |
| Peaking | 2796 Hz | 3.3  | 0.8 dB  |
| Peaking | 4128 Hz | 3.76 | -0.9 dB |
| Peaking | 6305 Hz | 2.74 | 4.6 dB  |
| Peaking | 7392 Hz | 1.53 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W10/Westone%20W10.png)