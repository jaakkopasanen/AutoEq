# qdc Anole V3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.3; 25 -10.4; 28 -10.6; 31 -10.8; 34 -10.9; 37 -11.1; 41 -11.2; 45 -11.3; 49 -11.4; 54 -11.6; 60 -11.8; 66 -12.1; 72 -12.3; 79 -12.5; 87 -12.7; 96 -13.1; 106 -13.3; 116 -13.5; 128 -13.6; 141 -13.8; 155 -13.8; 170 -13.8; 187 -13.7; 206 -13.5; 227 -13.3; 249 -13.0; 274 -12.7; 302 -12.3; 332 -11.8; 365 -11.4; 402 -10.9; 442 -10.3; 486 -9.7; 535 -9.0; 588 -8.3; 647 -7.5; 712 -6.7; 783 -5.8; 861 -5.0; 947 -4.5; 1042 -4.3; 1146 -4.3; 1261 -4.4; 1387 -4.0; 1526 -3.3; 1678 -2.5; 1846 -1.7; 2031 -1.0; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.2; 6373 -4.2; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.5; 15026 -22.2; 16529 -21.6; 18182 -17.9; 20000 -21.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 46 Hz    | 0.2  | -3.9 dB  |
| Peaking | 184 Hz   | 0.52 | -4.5 dB  |
| Peaking | 416 Hz   | 0.89 | -1.8 dB  |
| Peaking | 10212 Hz | 0.17 | 17.3 dB  |
| Peaking | 16208 Hz | 0.34 | -30.3 dB |
| Peaking | 1389 Hz  | 2.9  | -1.7 dB  |
| Peaking | 6145 Hz  | 0.17 | 1.1 dB   |
| Peaking | 7839 Hz  | 1.83 | -3.7 dB  |
| Peaking | 12627 Hz | 2.86 | 5.2 dB   |
| Peaking | 14768 Hz | 3.51 | -5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.9 dB  |
| Peaking | 250 Hz   | 1.41 | -5.7 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -18.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Anole%20V3/qdc%20Anole%20V3.png)