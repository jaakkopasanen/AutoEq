# Grado PS1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.4; 37 -2.3; 41 -3.7; 45 -4.8; 49 -5.8; 54 -7.1; 60 -8.4; 66 -9.5; 72 -10.4; 79 -11.1; 87 -11.6; 96 -11.8; 106 -11.8; 116 -11.6; 128 -11.2; 141 -10.7; 155 -10.3; 170 -9.8; 187 -9.2; 206 -8.8; 227 -8.3; 249 -8.1; 274 -7.8; 302 -7.3; 332 -6.7; 365 -6.1; 402 -6.5; 442 -6.5; 486 -6.4; 535 -6.2; 588 -6.0; 647 -6.0; 712 -5.9; 783 -6.0; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.9; 1526 -8.9; 1678 -8.7; 1846 -7.8; 2031 -7.6; 2234 -7.5; 2457 -7.5; 2703 -7.6; 2973 -7.7; 3270 -7.2; 3597 -7.5; 3957 -14.7; 4353 -13.7; 4788 -13.0; 5267 -14.1; 5793 -14.8; 6373 -18.6; 7010 -17.3; 7711 -15.9; 8482 -15.2; 9330 -14.3; 10263 -11.3; 11289 -7.1; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado PS1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 27 Hz   | 0.83 | 7.3 dB   |
| Peaking | 95 Hz   | 0.82 | -6.5 dB  |
| Peaking | 1578 Hz | 5.45 | -2.4 dB  |
| Peaking | 4105 Hz | 7.35 | -5.6 dB  |
| Peaking | 6926 Hz | 1.43 | -11.9 dB |
| Peaking | 618 Hz  | 1.23 | 0.9 dB   |
| Peaking | 3451 Hz | 7.9  | 3.4 dB   |
| Peaking | 5190 Hz | 1.05 | -1.7 dB  |
| Peaking | 9547 Hz | 2.74 | -7.0 dB  |
| Peaking | 9570 Hz | 0.95 | 4.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB   |
| Peaking | 62 Hz    | 1.41 | -3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 4000 Hz  | 1.41 | -3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -10.5 dB |
| Peaking | 16000 Hz | 1.41 | 1.7 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20PS1000/Grado%20PS1000.png)