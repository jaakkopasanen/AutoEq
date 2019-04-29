# Fake Shure SE846
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.4; 25 -1.9; 28 -2.6; 31 -3.2; 34 -3.6; 37 -4.0; 41 -4.4; 45 -4.8; 49 -5.1; 54 -5.4; 60 -5.8; 66 -6.2; 72 -6.7; 79 -7.1; 87 -7.5; 96 -8.0; 106 -8.4; 116 -8.8; 128 -9.1; 141 -9.4; 155 -9.6; 170 -9.7; 187 -9.8; 206 -9.8; 227 -9.7; 249 -9.6; 274 -9.3; 302 -9.1; 332 -8.8; 365 -8.4; 402 -8.1; 442 -7.7; 486 -7.2; 535 -6.8; 588 -6.3; 647 -5.8; 712 -5.2; 783 -4.7; 861 -4.4; 947 -4.4; 1042 -4.9; 1146 -6.0; 1261 -7.4; 1387 -8.9; 1526 -10.6; 1678 -12.7; 1846 -12.1; 2031 -12.3; 2234 -16.0; 2457 -15.4; 2703 -14.0; 2973 -11.7; 3270 -9.2; 3597 -3.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -3.3; 5793 -3.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fake Shure SE846 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fake Shure SE846 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.67 | 6.3 dB   |
| Peaking | 175 Hz   | 0.87 | -3.8 dB  |
| Peaking | 2437 Hz  | 1.76 | -10.8 dB |
| Peaking | 4204 Hz  | 2.39 | 9.1 dB   |
| Peaking | 6369 Hz  | 6.72 | 4.9 dB   |
| Peaking | 344 Hz   | 2.11 | -0.9 dB  |
| Peaking | 719 Hz   | 2.43 | 1.0 dB   |
| Peaking | 947 Hz   | 2.18 | 2.9 dB   |
| Peaking | 1639 Hz  | 5.25 | -3.0 dB  |
| Peaking | 22050 Hz | 1.69 | 0.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB   |
| Peaking | 62 Hz    | 1.41 | 0.2 dB   |
| Peaking | 125 Hz   | 1.41 | -2.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Fake%20Shure%20SE846/Fake%20Shure%20SE846.png)