# Dolby Dimension
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.7; 25 -2.3; 28 -3.0; 31 -3.5; 34 -4.0; 37 -4.4; 41 -4.9; 45 -5.5; 49 -5.9; 54 -6.2; 60 -6.5; 66 -6.7; 72 -7.0; 79 -7.3; 87 -7.5; 96 -7.9; 106 -8.4; 116 -8.9; 128 -9.0; 141 -8.7; 155 -8.6; 170 -8.8; 187 -9.0; 206 -9.0; 227 -8.8; 249 -8.8; 274 -8.9; 302 -8.9; 332 -9.1; 365 -9.0; 402 -9.0; 442 -8.9; 486 -8.9; 535 -9.2; 588 -9.2; 647 -8.8; 712 -8.6; 783 -8.1; 861 -6.9; 947 -5.9; 1042 -5.6; 1146 -6.1; 1261 -6.0; 1387 -5.6; 1526 -6.1; 1678 -6.6; 1846 -7.2; 2031 -7.6; 2234 -7.4; 2457 -6.5; 2703 -6.0; 2973 -6.2; 3270 -7.0; 3597 -7.2; 3957 -6.3; 4353 -3.2; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -6.5; 10263 -6.5; 11289 -7.9; 12418 -9.4; 13660 -8.7; 15026 -8.1; 16529 -9.7; 18182 -10.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dolby Dimension GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dolby Dimension ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.69 | 6.1 dB  |
| Peaking | 230 Hz   | 0.37 | -2.8 dB |
| Peaking | 5515 Hz  | 2.5  | 7.1 dB  |
| Peaking | 12407 Hz | 2.64 | -2.7 dB |
| Peaking | 17572 Hz | 1.45 | -4.1 dB |
| Peaking | 625 Hz   | 1.49 | -2.6 dB |
| Peaking | 1500 Hz  | 0.37 | 2.4 dB  |
| Peaking | 2052 Hz  | 1.9  | -3.1 dB |
| Peaking | 3539 Hz  | 4.34 | -3.0 dB |
| Peaking | 7484 Hz  | 2.39 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -4.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Dolby%20Dimension/Dolby%20Dimension.png)