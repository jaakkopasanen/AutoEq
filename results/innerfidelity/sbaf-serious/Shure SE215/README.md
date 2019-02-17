# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -9.8; 28 -9.9; 31 -10.0; 34 -10.0; 37 -10.1; 41 -10.2; 45 -10.3; 49 -10.5; 54 -10.7; 60 -10.9; 66 -11.2; 72 -11.3; 79 -11.7; 87 -11.9; 96 -12.2; 106 -12.3; 116 -12.4; 128 -12.5; 141 -12.5; 155 -12.5; 170 -12.3; 187 -12.1; 206 -11.8; 227 -11.4; 249 -11.1; 274 -10.6; 302 -10.2; 332 -9.7; 365 -9.1; 402 -8.6; 442 -7.9; 486 -7.5; 535 -6.9; 588 -6.1; 647 -5.7; 712 -5.5; 783 -5.0; 861 -5.1; 947 -5.4; 1042 -5.7; 1146 -5.9; 1261 -6.5; 1387 -7.6; 1526 -8.6; 1678 -9.4; 1846 -10.0; 2031 -10.5; 2234 -10.5; 2457 -9.1; 2703 -7.0; 2973 -3.9; 3270 -1.8; 3597 -1.5; 3957 -3.7; 4353 -9.0; 4788 -13.5; 5267 -8.4; 5793 -2.8; 6373 -0.5; 7010 -3.1; 7711 -5.4; 8482 -5.6; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 48 Hz   | 0.27 | -4.4 dB  |
| Peaking | 178 Hz  | 0.69 | -4.5 dB  |
| Peaking | 2200 Hz | 1.51 | -10.7 dB |
| Peaking | 3505 Hz | 0.76 | 9.0 dB   |
| Peaking | 4732 Hz | 4.83 | -14.4 dB |
| Peaking | 805 Hz  | 2.22 | 1.5 dB   |
| Peaking | 1554 Hz | 5.3  | -1.2 dB  |
| Peaking | 5216 Hz | 8.87 | -2.0 dB  |
| Peaking | 6383 Hz | 3.34 | 5.7 dB   |
| Peaking | 7514 Hz | 1.45 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE215/Shure%20SE215.png)