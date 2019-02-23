# Shure SE315
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.1; 72 -1.6; 79 -2.3; 87 -3.1; 96 -3.9; 106 -4.7; 116 -5.6; 128 -6.4; 141 -7.1; 155 -7.7; 170 -8.1; 187 -8.5; 206 -8.8; 227 -9.0; 249 -9.1; 274 -9.4; 302 -9.5; 332 -9.4; 365 -9.4; 402 -9.2; 442 -9.1; 486 -8.9; 535 -8.6; 588 -8.4; 647 -8.2; 712 -8.0; 783 -7.9; 861 -8.0; 947 -8.7; 1042 -10.0; 1146 -11.6; 1261 -12.7; 1387 -13.4; 1526 -13.5; 1678 -13.0; 1846 -11.7; 2031 -9.6; 2234 -6.5; 2457 -3.3; 2703 -1.2; 2973 -0.6; 3270 -1.2; 3597 -2.8; 3957 -4.8; 4353 -5.7; 4788 -3.4; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE315 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.31 | 7.3 dB  |
| Peaking | 195 Hz  | 0.52 | -5.3 dB |
| Peaking | 1555 Hz | 1.5  | -8.2 dB |
| Peaking | 2850 Hz | 2.29 | 8.0 dB  |
| Peaking | 5786 Hz | 3.25 | 6.6 dB  |
| Peaking | 836 Hz  | 2.08 | 2.4 dB  |
| Peaking | 854 Hz  | 1.1  | -1.6 dB |
| Peaking | 4281 Hz | 5.33 | -3.5 dB |
| Peaking | 4397 Hz | 1.92 | 1.8 dB  |
| Peaking | 8160 Hz | 3.51 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -3.7 dB |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SE315/Shure%20SE315.png)