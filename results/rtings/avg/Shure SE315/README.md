# Shure SE315
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.0; 106 -1.8; 116 -2.7; 128 -3.5; 141 -4.2; 155 -4.8; 170 -5.3; 187 -5.6; 206 -5.9; 227 -6.1; 249 -6.2; 274 -6.5; 302 -6.6; 332 -6.5; 365 -6.5; 402 -6.3; 442 -6.2; 486 -6.0; 535 -5.7; 588 -5.5; 647 -5.3; 712 -5.1; 783 -5.0; 861 -5.1; 947 -5.8; 1042 -7.1; 1146 -8.7; 1261 -9.8; 1387 -10.5; 1526 -10.6; 1678 -10.1; 1846 -8.8; 2031 -6.7; 2234 -3.6; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.9; 4353 -2.8; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE315 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 46 Hz    | 0.33 | 6.8 dB   |
| Peaking | 852 Hz   | 0.58 | 12.6 dB  |
| Peaking | 1545 Hz  | 0.39 | -23.6 dB |
| Peaking | 2707 Hz  | 0.68 | 19.6 dB  |
| Peaking | 5679 Hz  | 2.22 | 6.1 dB   |
| Peaking | 16 Hz    | 1    | 1.6 dB   |
| Peaking | 41 Hz    | 1.1  | -1.0 dB  |
| Peaking | 90 Hz    | 2.58 | 1.3 dB   |
| Peaking | 152 Hz   | 2.68 | -0.6 dB  |
| Peaking | 13594 Hz | 2.08 | 0.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.4 dB  |
| Peaking | 125 Hz   | 1.41 | 2.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SE315/Shure%20SE315.png)