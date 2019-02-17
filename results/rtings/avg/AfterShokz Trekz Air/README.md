# AfterShokz Trekz Air
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -1.9; 141 -6.2; 155 -8.3; 170 -8.8; 187 -9.0; 206 -9.6; 227 -10.3; 249 -10.8; 274 -11.0; 302 -11.1; 332 -11.0; 365 -10.4; 402 -9.9; 442 -9.2; 486 -6.2; 535 -5.3; 588 -6.1; 647 -5.2; 712 -4.0; 783 -4.8; 861 -5.4; 947 -6.5; 1042 -5.4; 1146 -3.5; 1261 -3.6; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -3.0; 2234 -6.8; 2457 -7.5; 2703 -7.6; 2973 -7.6; 3270 -7.5; 3597 -10.0; 3957 -13.7; 4353 -17.6; 4788 -19.8; 5267 -12.9; 5793 -8.7; 6373 -9.6; 7010 -6.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -14.3; 12418 -21.6; 13660 -16.5; 15026 -7.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AfterShokz Trekz Air GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AfterShokz Trekz Air ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 124 Hz   | 0.17 | 9.7 dB   |
| Peaking | 256 Hz   | 0.68 | -14.1 dB |
| Peaking | 1609 Hz  | 2.57 | 6.5 dB   |
| Peaking | 4580 Hz  | 3.53 | -13.9 dB |
| Peaking | 12635 Hz | 3.94 | -16.9 dB |
| Peaking | 21 Hz    | 2.69 | 1.2 dB   |
| Peaking | 120 Hz   | 3.83 | 3.4 dB   |
| Peaking | 152 Hz   | 4.19 | -3.5 dB  |
| Peaking | 2436 Hz  | 5.71 | -2.0 dB  |
| Peaking | 8779 Hz  | 2.33 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB   |
| Peaking | 62 Hz    | 1.41 | 5.6 dB   |
| Peaking | 125 Hz   | 1.41 | 4.0 dB   |
| Peaking | 250 Hz   | 1.41 | -6.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -10.0 dB |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 16000 Hz | 1.41 | -5.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AfterShokz%20Trekz%20Air/AfterShokz%20Trekz%20Air.png)