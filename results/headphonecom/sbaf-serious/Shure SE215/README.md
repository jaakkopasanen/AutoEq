# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.9; 25 -9.9; 28 -9.9; 31 -9.9; 34 -10.0; 37 -10.1; 41 -10.2; 45 -10.3; 49 -10.4; 54 -10.7; 60 -10.9; 66 -11.0; 72 -11.3; 79 -11.4; 87 -11.6; 96 -11.8; 106 -11.8; 116 -11.8; 128 -11.9; 141 -11.9; 155 -11.8; 170 -11.6; 187 -11.4; 206 -11.1; 227 -10.7; 249 -10.3; 274 -9.8; 302 -9.3; 332 -8.7; 365 -8.0; 402 -7.4; 442 -6.9; 486 -6.3; 535 -5.7; 588 -5.1; 647 -4.6; 712 -4.2; 783 -3.9; 861 -3.9; 947 -4.1; 1042 -4.6; 1146 -4.8; 1261 -5.3; 1387 -6.8; 1526 -7.9; 1678 -8.7; 1846 -9.4; 2031 -9.9; 2234 -10.0; 2457 -8.7; 2703 -6.2; 2973 -3.3; 3270 -0.9; 3597 -0.5; 3957 -2.1; 4353 -7.1; 4788 -11.8; 5267 -6.6; 5793 -0.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 54 Hz   | 0.43 | -4.2 dB  |
| Peaking | 167 Hz  | 1.11 | -3.8 dB  |
| Peaking | 3665 Hz | 2.69 | 12.9 dB  |
| Peaking | 4955 Hz | 1.37 | -19.9 dB |
| Peaking | 5786 Hz | 1.91 | 19.1 dB  |
| Peaking | 20 Hz   | 2.22 | -1.1 dB  |
| Peaking | 304 Hz  | 1.72 | -1.4 dB  |
| Peaking | 898 Hz  | 0.86 | 3.7 dB   |
| Peaking | 2034 Hz | 1.45 | -4.0 dB  |
| Peaking | 3009 Hz | 4.88 | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE215/Shure%20SE215.png)