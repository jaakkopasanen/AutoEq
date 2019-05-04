# AfterShokz Trekz Air
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -1.9; 141 -6.1; 155 -8.2; 170 -8.7; 187 -8.8; 206 -9.4; 227 -10.3; 249 -10.8; 274 -11.0; 302 -11.1; 332 -11.0; 365 -10.3; 402 -9.9; 442 -9.2; 486 -6.3; 535 -5.4; 588 -6.1; 647 -5.3; 712 -4.2; 783 -5.0; 861 -5.5; 947 -6.6; 1042 -5.5; 1146 -3.8; 1261 -3.8; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -3.5; 2234 -7.7; 2457 -8.5; 2703 -8.2; 2973 -7.7; 3270 -7.5; 3597 -9.7; 3957 -13.3; 4353 -17.3; 4788 -19.7; 5267 -14.0; 5793 -9.1; 6373 -8.3; 7010 -6.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -15.4; 12418 -22.0; 13660 -15.9; 15026 -7.3; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AfterShokz Trekz Air GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AfterShokz Trekz Air ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 117 Hz   | 0.18 | 9.3 dB   |
| Peaking | 256 Hz   | 0.7  | -13.6 dB |
| Peaking | 1594 Hz  | 2.82 | 6.7 dB   |
| Peaking | 4610 Hz  | 3.66 | -14.1 dB |
| Peaking | 12519 Hz | 4.06 | -17.4 dB |
| Peaking | 22 Hz    | 2.44 | 1.2 dB   |
| Peaking | 121 Hz   | 3.88 | 3.3 dB   |
| Peaking | 151 Hz   | 4.31 | -3.4 dB  |
| Peaking | 2407 Hz  | 6.38 | -3.1 dB  |
| Peaking | 8615 Hz  | 2.19 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.5 dB  |
| Peaking | 125 Hz   | 1.41 | 4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -6.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -9.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -5.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AfterShokz%20Trekz%20Air/AfterShokz%20Trekz%20Air.png)