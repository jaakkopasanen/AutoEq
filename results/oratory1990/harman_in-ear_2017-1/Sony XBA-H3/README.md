# Sony XBA-H3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.4; 25 -6.5; 28 -6.7; 31 -6.9; 34 -7.0; 37 -7.2; 41 -7.3; 45 -7.5; 49 -7.6; 54 -7.8; 60 -8.1; 66 -8.4; 72 -8.7; 79 -9.0; 87 -9.3; 96 -9.6; 106 -9.9; 116 -10.1; 128 -10.3; 141 -10.4; 155 -10.3; 170 -10.3; 187 -10.1; 206 -9.8; 227 -9.5; 249 -9.1; 274 -8.7; 302 -8.3; 332 -7.9; 365 -7.5; 402 -7.2; 442 -6.9; 486 -6.6; 535 -6.4; 588 -6.2; 647 -6.0; 712 -5.8; 783 -5.8; 861 -6.1; 947 -6.3; 1042 -6.7; 1146 -7.1; 1261 -7.3; 1387 -7.1; 1526 -6.7; 1678 -6.3; 1846 -5.4; 2031 -3.8; 2234 -1.3; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -2.5; 3597 -3.9; 3957 -4.2; 4353 -6.3; 4788 -8.9; 5267 -7.9; 5793 -3.9; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -11.8; 10263 -13.9; 11289 -11.2; 12418 -10.5; 13660 -15.9; 15026 -22.2; 16529 -26.2; 18182 -26.0; 20000 -17.7
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
| Peaking | 140 Hz   | 0.71 | -4.0 dB  |
| Peaking | 2687 Hz  | 2.3  | 7.1 dB   |
| Peaking | 6507 Hz  | 4.94 | 6.9 dB   |
| Peaking | 16762 Hz | 0.85 | -17.1 dB |
| Peaking | 19030 Hz | 0.89 | -8.9 dB  |
| Peaking | 1443 Hz  | 1.59 | -2.3 dB  |
| Peaking | 2568 Hz  | 0.21 | 1.2 dB   |
| Peaking | 4898 Hz  | 5.49 | -4.2 dB  |
| Peaking | 9985 Hz  | 5.54 | -4.7 dB  |
| Peaking | 12201 Hz | 5.15 | 3.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB   |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 16000 Hz | 1.41 | -26.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20XBA-H3/Sony%20XBA-H3.png)