# RHA MA750
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -5.9; 25 -6.1; 28 -6.4; 31 -6.5; 34 -6.6; 37 -6.6; 41 -6.6; 45 -6.6; 49 -6.8; 54 -6.9; 60 -7.2; 66 -7.4; 72 -7.5; 79 -7.8; 87 -7.7; 96 -7.6; 106 -7.9; 116 -7.8; 128 -8.1; 141 -7.9; 155 -8.0; 170 -8.1; 187 -8.2; 206 -8.2; 227 -8.2; 249 -8.2; 274 -8.1; 302 -8.0; 332 -7.9; 365 -7.7; 402 -7.6; 442 -7.4; 486 -7.1; 535 -6.8; 588 -6.5; 647 -6.0; 712 -5.5; 783 -4.9; 861 -4.3; 947 -3.9; 1042 -3.7; 1146 -3.8; 1261 -3.9; 1387 -3.8; 1526 -3.3; 1678 -2.4; 1846 -1.4; 2031 -0.8; 2234 -0.5; 2457 -0.8; 2703 -1.7; 2973 -3.2; 3270 -4.8; 3597 -5.7; 3957 -6.0; 4353 -6.3; 4788 -7.6; 5267 -8.2; 5793 -5.1; 6373 -1.8; 7010 -2.9; 7711 -5.6; 8482 -6.0; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -8.5; 15026 -13.3; 16529 -14.6; 18182 -15.7; 20000 -15.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA MA750 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA MA750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 178 Hz   | 0.31 | -2.9 dB  |
| Peaking | 2486 Hz  | 0.73 | 5.8 dB   |
| Peaking | 4099 Hz  | 1.39 | -5.4 dB  |
| Peaking | 11666 Hz | 0.54 | 7.6 dB   |
| Peaking | 17454 Hz | 0.33 | -13.6 dB |
| Peaking | 906 Hz   | 5    | 1.0 dB   |
| Peaking | 5302 Hz  | 6.67 | -3.4 dB  |
| Peaking | 6646 Hz  | 3.16 | 5.1 dB   |
| Peaking | 7852 Hz  | 2.98 | -3.3 dB  |
| Peaking | 12768 Hz | 7.12 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -11.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/RHA%20MA750/RHA%20MA750.png)