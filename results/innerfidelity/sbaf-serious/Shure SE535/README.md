# Shure SE535
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.7; 25 -3.8; 28 -3.9; 31 -4.1; 34 -4.2; 37 -4.3; 41 -4.5; 45 -4.7; 49 -4.9; 54 -5.2; 60 -5.5; 66 -5.9; 72 -6.3; 79 -6.6; 87 -7.1; 96 -7.5; 106 -7.8; 116 -8.0; 128 -8.4; 141 -8.7; 155 -9.0; 170 -9.2; 187 -9.3; 206 -9.5; 227 -9.5; 249 -9.6; 274 -9.5; 302 -9.4; 332 -9.4; 365 -9.3; 402 -9.1; 442 -8.9; 486 -8.8; 535 -8.6; 588 -8.2; 647 -8.1; 712 -8.0; 783 -7.7; 861 -7.9; 947 -8.0; 1042 -8.2; 1146 -8.4; 1261 -8.5; 1387 -8.8; 1526 -9.0; 1678 -9.1; 1846 -8.9; 2031 -8.6; 2234 -7.9; 2457 -6.1; 2703 -4.5; 2973 -2.6; 3270 -1.2; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -1.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE535 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.3  | 3.0 dB  |
| Peaking | 219 Hz  | 0.44 | -3.3 dB |
| Peaking | 1884 Hz | 1.09 | -3.7 dB |
| Peaking | 3554 Hz | 1.51 | 7.0 dB  |
| Peaking | 5787 Hz | 3.14 | 5.0 dB  |
| Peaking | 4946 Hz | 3.9  | 1.1 dB  |
| Peaking | 6579 Hz | 5.88 | 3.2 dB  |
| Peaking | 6932 Hz | 1.66 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE535/Shure%20SE535.png)