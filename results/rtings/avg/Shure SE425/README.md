# Shure SE425
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.0; 96 -2.1; 106 -2.7; 116 -3.8; 128 -4.7; 141 -5.5; 155 -6.2; 170 -6.7; 187 -7.2; 206 -7.6; 227 -7.9; 249 -8.0; 274 -8.1; 302 -8.2; 332 -8.2; 365 -8.1; 402 -7.9; 442 -7.7; 486 -7.5; 535 -7.1; 588 -6.7; 647 -6.2; 712 -6.0; 783 -5.9; 861 -6.2; 947 -7.2; 1042 -8.0; 1146 -8.6; 1261 -8.8; 1387 -8.9; 1526 -8.8; 1678 -8.6; 1846 -8.4; 2031 -8.2; 2234 -7.5; 2457 -6.8; 2703 -5.9; 2973 -5.8; 3270 -6.4; 3597 -7.4; 3957 -7.6; 4353 -6.5; 4788 -4.0; 5267 -2.1; 5793 -2.1; 6373 -4.4; 7010 -7.8; 7711 -6.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE425 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE425 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 120 Hz  | 0.14 | 9.0 dB   |
| Peaking | 256 Hz  | 0.47 | -10.3 dB |
| Peaking | 1410 Hz | 1.25 | -3.7 dB  |
| Peaking | 5588 Hz | 3.89 | 5.3 dB   |
| Peaking | 7072 Hz | 8.13 | -2.5 dB  |
| Peaking | 83 Hz   | 5.62 | 1.1 dB   |
| Peaking | 468 Hz  | 5.36 | -0.6 dB  |
| Peaking | 2853 Hz | 6.39 | 1.3 dB   |
| Peaking | 3893 Hz | 5.85 | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.8 dB  |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SE425/Shure%20SE425.png)