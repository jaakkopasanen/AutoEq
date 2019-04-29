# Yamha EPH-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.7; 25 -10.0; 28 -10.2; 31 -10.4; 34 -10.5; 37 -10.6; 41 -10.7; 45 -10.7; 49 -10.8; 54 -10.9; 60 -11.0; 66 -11.1; 72 -11.2; 79 -11.2; 87 -11.3; 96 -11.5; 106 -11.5; 116 -11.5; 128 -11.5; 141 -11.4; 155 -11.2; 170 -11.0; 187 -10.8; 206 -10.4; 227 -10.1; 249 -9.7; 274 -9.3; 302 -8.9; 332 -8.6; 365 -8.2; 402 -7.8; 442 -7.5; 486 -7.1; 535 -6.8; 588 -6.5; 647 -6.1; 712 -5.7; 783 -5.4; 861 -5.2; 947 -5.2; 1042 -5.7; 1146 -6.6; 1261 -7.8; 1387 -8.4; 1526 -8.5; 1678 -8.7; 1846 -9.0; 2031 -9.8; 2234 -10.4; 2457 -9.5; 2703 -7.0; 2973 -4.2; 3270 -1.8; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.2; 7010 -7.0; 7711 -8.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.4; 15026 -16.3; 16529 -18.9; 18182 -16.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamha EPH-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamha EPH-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 48 Hz    | 0.35 | -4.1 dB  |
| Peaking | 164 Hz   | 0.83 | -3.0 dB  |
| Peaking | 2269 Hz  | 1.64 | -7.9 dB  |
| Peaking | 3897 Hz  | 0.9  | 8.5 dB   |
| Peaking | 16801 Hz | 1.2  | -13.9 dB |
| Peaking | 835 Hz   | 3.07 | 1.8 dB   |
| Peaking | 6269 Hz  | 4.36 | 3.8 dB   |
| Peaking | 7351 Hz  | 4.54 | -5.7 dB  |
| Peaking | 12411 Hz | 2.51 | 3.3 dB   |
| Peaking | 14570 Hz | 3.13 | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 16000 Hz | 1.41 | -13.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Yamha%20EPH-100/Yamha%20EPH-100.png)