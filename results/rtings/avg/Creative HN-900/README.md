# Creative HN-900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.9; 49 -3.5; 54 -5.3; 60 -6.1; 66 -5.2; 72 -7.0; 79 -10.0; 87 -12.0; 96 -13.1; 106 -13.8; 116 -14.2; 128 -14.3; 141 -14.1; 155 -14.1; 170 -13.9; 187 -13.3; 206 -12.7; 227 -12.2; 249 -11.6; 274 -11.1; 302 -10.6; 332 -10.2; 365 -9.9; 402 -9.8; 442 -9.9; 486 -10.2; 535 -10.9; 588 -11.8; 647 -12.7; 712 -12.4; 783 -10.9; 861 -8.4; 947 -6.1; 1042 -5.8; 1146 -7.3; 1261 -5.3; 1387 -3.3; 1526 -2.4; 1678 -1.4; 1846 -0.5; 2031 -0.5; 2234 -1.8; 2457 -3.5; 2703 -1.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.4; 5267 -6.4; 5793 -5.0; 6373 -6.3; 7010 -5.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.8; 13660 -13.0; 15026 -12.6; 16529 -10.3; 18182 -9.8; 20000 -12.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative HN-900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative HN-900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.39 | 10.4 dB  |
| Peaking | 112 Hz   | 0.54 | -13.3 dB |
| Peaking | 675 Hz   | 2.07 | -6.4 dB  |
| Peaking | 2640 Hz  | 0.56 | 6.1 dB   |
| Peaking | 15520 Hz | 0.81 | -6.0 dB  |
| Peaking | 1177 Hz  | 7.84 | -3.4 dB  |
| Peaking | 2507 Hz  | 3.52 | -5.2 dB  |
| Peaking | 2852 Hz  | 0.66 | 2.7 dB   |
| Peaking | 5732 Hz  | 2.6  | -3.1 dB  |
| Peaking | 11512 Hz | 6.33 | 2.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -9.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -4.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -7.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20HN-900/Creative%20HN-900.png)