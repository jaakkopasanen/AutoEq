# Shure KSE1200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.5; 25 -6.7; 28 -6.9; 31 -7.0; 34 -7.1; 37 -7.2; 41 -7.4; 45 -7.5; 49 -7.6; 54 -7.7; 60 -7.9; 66 -8.1; 72 -8.3; 79 -8.5; 87 -8.7; 96 -8.9; 106 -9.1; 116 -9.2; 128 -9.3; 141 -9.4; 155 -9.3; 170 -9.2; 187 -9.1; 206 -8.9; 227 -8.6; 249 -8.3; 274 -8.0; 302 -7.7; 332 -7.5; 365 -7.2; 402 -6.9; 442 -6.7; 486 -6.4; 535 -6.2; 588 -6.1; 647 -5.9; 712 -5.7; 783 -5.6; 861 -5.6; 947 -5.8; 1042 -6.5; 1146 -7.8; 1261 -9.1; 1387 -10.2; 1526 -11.0; 1678 -11.4; 1846 -11.1; 2031 -9.9; 2234 -7.5; 2457 -4.7; 2703 -2.2; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.7; 6373 -2.6; 7010 -5.7; 7711 -10.8; 8482 -15.1; 9330 -14.3; 10263 -8.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.4; 16529 -12.5; 18182 -16.6; 20000 -17.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure KSE1200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure KSE1200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 109 Hz   | 0.7  | -2.3 dB  |
| Peaking | 203 Hz   | 1.13 | -1.4 dB  |
| Peaking | 1794 Hz  | 1.27 | -13.3 dB |
| Peaking | 3075 Hz  | 0.44 | 10.4 dB  |
| Peaking | 8707 Hz  | 2.79 | -13.5 dB |
| Peaking | 1132 Hz  | 1.31 | 1.3 dB   |
| Peaking | 1262 Hz  | 3.08 | -2.4 dB  |
| Peaking | 4044 Hz  | 4.6  | -0.8 dB  |
| Peaking | 5900 Hz  | 3.87 | 1.9 dB   |
| Peaking | 19213 Hz | 0.97 | -12.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 11.0 dB |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shure%20KSE1200/Shure%20KSE1200.png)