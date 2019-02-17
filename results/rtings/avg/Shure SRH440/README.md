# Shure SRH440
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.2; 31 -1.8; 34 -2.3; 37 -2.7; 41 -3.1; 45 -3.5; 49 -3.8; 54 -4.1; 60 -4.5; 66 -5.0; 72 -5.6; 79 -6.5; 87 -7.4; 96 -7.9; 106 -8.1; 116 -7.7; 128 -7.0; 141 -6.7; 155 -6.3; 170 -5.6; 187 -5.1; 206 -4.9; 227 -5.2; 249 -5.6; 274 -6.2; 302 -6.8; 332 -7.5; 365 -8.2; 402 -8.2; 442 -8.0; 486 -7.9; 535 -7.6; 588 -7.5; 647 -7.3; 712 -7.0; 783 -6.8; 861 -6.6; 947 -6.6; 1042 -6.4; 1146 -7.3; 1261 -7.9; 1387 -8.2; 1526 -8.4; 1678 -8.9; 1846 -9.5; 2031 -9.3; 2234 -8.1; 2457 -6.4; 2703 -6.2; 2973 -6.3; 3270 -7.3; 3597 -7.6; 3957 -7.4; 4353 -7.2; 4788 -6.9; 5267 -7.0; 5793 -6.3; 6373 -6.1; 7010 -7.4; 7711 -9.3; 8482 -11.1; 9330 -12.5; 10263 -11.3; 11289 -7.7; 12418 -6.6; 13660 -8.2; 15026 -8.3; 16529 -6.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.4  | 6.1 dB  |
| Peaking | 45 Hz    | 2.27 | 2.1 dB  |
| Peaking | 431 Hz   | 2.51 | -1.9 dB |
| Peaking | 1788 Hz  | 2.43 | -3.0 dB |
| Peaking | 9343 Hz  | 2.8  | -6.4 dB |
| Peaking | 103 Hz   | 3.11 | -2.2 dB |
| Peaking | 206 Hz   | 2.9  | 1.9 dB  |
| Peaking | 1306 Hz  | 5.01 | -0.5 dB |
| Peaking | 12113 Hz | 5.24 | 1.7 dB  |
| Peaking | 14515 Hz | 2.71 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SRH440/Shure%20SRH440.png)