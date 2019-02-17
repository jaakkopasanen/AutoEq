# Shure SE210
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.2; 60 -1.8; 66 -2.3; 72 -2.8; 79 -3.3; 87 -3.8; 96 -4.2; 106 -4.6; 116 -4.8; 128 -5.4; 141 -5.7; 155 -5.9; 170 -6.2; 187 -6.5; 206 -6.5; 227 -6.6; 249 -6.6; 274 -6.6; 302 -6.7; 332 -6.6; 365 -6.4; 402 -6.3; 442 -6.3; 486 -6.4; 535 -6.2; 588 -6.0; 647 -5.7; 712 -5.8; 783 -5.8; 861 -6.0; 947 -6.3; 1042 -6.6; 1146 -7.0; 1261 -7.3; 1387 -8.1; 1526 -9.2; 1678 -9.8; 1846 -9.6; 2031 -9.0; 2234 -8.0; 2457 -6.5; 2703 -4.7; 2973 -2.9; 3270 -1.1; 3597 -0.5; 3957 -1.5; 4353 -3.4; 4788 -3.7; 5267 -2.2; 5793 -1.4; 6373 -2.8; 7010 -6.5; 7711 -10.3; 8482 -10.9; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE210 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.56 | 6.6 dB  |
| Peaking | 1818 Hz | 2.17 | -4.1 dB |
| Peaking | 3479 Hz | 2.39 | 6.3 dB  |
| Peaking | 5889 Hz | 3.07 | 5.2 dB  |
| Peaking | 8008 Hz | 4.34 | -6.2 dB |
| Peaking | 20 Hz   | 0.4  | 1.6 dB  |
| Peaking | 32 Hz   | 1.57 | -2.0 dB |
| Peaking | 196 Hz  | 1.05 | -0.7 dB |
| Peaking | 724 Hz  | 2.09 | 1.0 dB  |
| Peaking | 9569 Hz | 9.64 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE210/Shure%20SE210.png)