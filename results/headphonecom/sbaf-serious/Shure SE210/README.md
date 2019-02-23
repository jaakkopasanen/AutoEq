# Shure SE210
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.8; 49 -1.3; 54 -1.8; 60 -2.4; 66 -3.0; 72 -3.5; 79 -4.0; 87 -4.5; 96 -4.8; 106 -5.3; 116 -5.5; 128 -6.0; 141 -6.3; 155 -6.6; 170 -6.9; 187 -7.1; 206 -7.2; 227 -7.2; 249 -7.3; 274 -7.2; 302 -7.4; 332 -7.2; 365 -7.1; 402 -7.0; 442 -6.9; 486 -7.0; 535 -6.8; 588 -6.6; 647 -6.4; 712 -6.4; 783 -6.4; 861 -6.6; 947 -6.9; 1042 -7.3; 1146 -7.6; 1261 -8.0; 1387 -8.8; 1526 -9.9; 1678 -10.4; 1846 -10.3; 2031 -9.6; 2234 -8.6; 2457 -7.2; 2703 -5.4; 2973 -3.6; 3270 -1.8; 3597 -1.0; 3957 -2.1; 4353 -4.0; 4788 -4.3; 5267 -2.9; 5793 -2.1; 6373 -3.4; 7010 -7.2; 7711 -10.9; 8482 -11.6; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE210 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.7  | 6.7 dB  |
| Peaking | 1808 Hz | 1.67 | -4.6 dB |
| Peaking | 3465 Hz | 2.42 | 6.1 dB  |
| Peaking | 5882 Hz | 3.42 | 4.7 dB  |
| Peaking | 8021 Hz | 4.4  | -6.7 dB |
| Peaking | 19 Hz   | 0.29 | 2.1 dB  |
| Peaking | 32 Hz   | 1.5  | -2.6 dB |
| Peaking | 215 Hz  | 0.68 | -1.2 dB |
| Peaking | 747 Hz  | 2.22 | 0.7 dB  |
| Peaking | 9704 Hz | 8.96 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE210/Shure%20SE210.png)