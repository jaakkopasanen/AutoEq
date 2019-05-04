# HyperX Cloud Stinger
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -9.8; 25 -10.0; 28 -10.1; 31 -10.2; 34 -10.2; 37 -10.1; 41 -10.1; 45 -10.2; 49 -10.3; 54 -10.4; 60 -10.4; 66 -10.4; 72 -10.4; 79 -10.4; 87 -10.5; 96 -10.8; 106 -11.0; 116 -11.0; 128 -10.9; 141 -10.6; 155 -10.3; 170 -9.8; 187 -9.1; 206 -8.1; 227 -7.0; 249 -5.8; 274 -4.7; 302 -3.2; 332 -1.7; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.9; 535 -2.8; 588 -4.5; 647 -5.6; 712 -5.9; 783 -5.6; 861 -4.7; 947 -4.4; 1042 -4.4; 1146 -5.0; 1261 -5.9; 1387 -7.1; 1526 -8.4; 1678 -9.5; 1846 -10.4; 2031 -11.2; 2234 -11.2; 2457 -10.6; 2703 -9.9; 2973 -9.6; 3270 -8.4; 3597 -6.6; 3957 -4.4; 4353 -3.6; 4788 -3.8; 5267 -2.9; 5793 -5.2; 6373 -6.5; 7010 -5.4; 7711 -7.3; 8482 -9.4; 9330 -9.5; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.7; 16529 -11.6; 18182 -12.5; 20000 -13.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Stinger GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Stinger ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.37 | -3.3 dB |
| Peaking | 147 Hz   | 0.71 | -4.2 dB |
| Peaking | 387 Hz   | 1.17 | 7.6 dB  |
| Peaking | 2271 Hz  | 1.62 | -5.4 dB |
| Peaking | 4638 Hz  | 2.74 | 4.3 dB  |
| Peaking | 686 Hz   | 2.64 | -2.9 dB |
| Peaking | 1072 Hz  | 1.03 | 3.5 dB  |
| Peaking | 1627 Hz  | 1.23 | -2.6 dB |
| Peaking | 2339 Hz  | 4.82 | 1.2 dB  |
| Peaking | 19162 Hz | 0.6  | -7.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 4.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Stinger/HyperX%20Cloud%20Stinger.png)