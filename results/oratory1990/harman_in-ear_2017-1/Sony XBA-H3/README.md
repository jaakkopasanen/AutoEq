# Sony XBA-H3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.5; 25 -6.6; 28 -6.8; 31 -7.0; 34 -7.1; 37 -7.3; 41 -7.4; 45 -7.6; 49 -7.8; 54 -8.0; 60 -8.2; 66 -8.5; 72 -8.8; 79 -9.1; 87 -9.4; 96 -9.7; 106 -10.0; 116 -10.2; 128 -10.4; 141 -10.5; 155 -10.5; 170 -10.4; 187 -10.2; 206 -9.9; 227 -9.6; 249 -9.2; 274 -8.8; 302 -8.4; 332 -8.0; 365 -7.6; 402 -7.3; 442 -7.0; 486 -6.7; 535 -6.5; 588 -6.3; 647 -6.1; 712 -5.9; 783 -5.9; 861 -6.2; 947 -6.4; 1042 -6.8; 1146 -7.2; 1261 -7.4; 1387 -7.2; 1526 -6.8; 1678 -6.4; 1846 -5.5; 2031 -3.9; 2234 -1.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -2.6; 3597 -4.0; 3957 -4.3; 4353 -6.5; 4788 -9.0; 5267 -8.0; 5793 -4.1; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -11.9; 10263 -14.0; 11289 -11.3; 12418 -10.6; 13660 -16.1; 15026 -22.4; 16529 -26.3; 18182 -26.1; 20000 -17.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-H3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-H3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 139 Hz   | 0.68 | -4.1 dB  |
| Peaking | 2687 Hz  | 2.38 | 7.2 dB   |
| Peaking | 6545 Hz  | 4.87 | 6.9 dB   |
| Peaking | 16790 Hz | 0.83 | -17.4 dB |
| Peaking | 19140 Hz | 0.9  | -8.6 dB  |
| Peaking | 1430 Hz  | 1.59 | -2.4 dB  |
| Peaking | 2486 Hz  | 0.22 | 1.1 dB   |
| Peaking | 4902 Hz  | 5.62 | -4.2 dB  |
| Peaking | 10029 Hz | 5.58 | -4.7 dB  |
| Peaking | 12249 Hz | 5.28 | 3.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 16000 Hz | 1.41 | -26.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20XBA-H3/Sony%20XBA-H3.png)