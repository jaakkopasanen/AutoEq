# Sony XBA-N3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.4; 25 -10.6; 28 -10.8; 31 -10.9; 34 -10.9; 37 -10.9; 41 -11.0; 45 -11.0; 49 -10.9; 54 -10.9; 60 -10.9; 66 -10.9; 72 -10.9; 79 -10.8; 87 -10.7; 96 -10.6; 106 -10.3; 116 -10.6; 128 -11.0; 141 -11.0; 155 -10.8; 170 -10.4; 187 -10.1; 206 -9.7; 227 -9.3; 249 -8.9; 274 -8.5; 302 -8.1; 332 -7.6; 365 -7.1; 402 -6.8; 442 -6.5; 486 -6.2; 535 -6.0; 588 -5.7; 647 -5.6; 712 -5.4; 783 -5.4; 861 -5.4; 947 -5.8; 1042 -6.3; 1146 -6.8; 1261 -7.0; 1387 -6.9; 1526 -5.7; 1678 -4.9; 1846 -5.1; 2031 -4.7; 2234 -3.8; 2457 -2.7; 2703 -1.5; 2973 -0.5; 3270 -0.5; 3597 -2.2; 3957 -3.3; 4353 -2.2; 4788 -3.0; 5267 -2.6; 5793 -1.2; 6373 -1.4; 7010 -3.9; 7711 -5.8; 8482 -6.8; 9330 -8.2; 10263 -8.6; 11289 -7.9; 12418 -8.0; 13660 -14.1; 15026 -24.4; 16529 -28.6; 18182 -23.1; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-N3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-N3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.33 | -4.8 dB  |
| Peaking | 167 Hz   | 1    | -2.9 dB  |
| Peaking | 3023 Hz  | 3.07 | 3.9 dB   |
| Peaking | 9603 Hz  | 0.36 | 8.6 dB   |
| Peaking | 16448 Hz | 0.78 | -28.8 dB |
| Peaking | 1297 Hz  | 4.69 | -1.9 dB  |
| Peaking | 6149 Hz  | 4.07 | 3.4 dB   |
| Peaking | 9474 Hz  | 1.29 | -3.4 dB  |
| Peaking | 12356 Hz | 2.27 | 5.6 dB   |
| Peaking | 14816 Hz | 4.24 | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 16000 Hz | 1.41 | -25.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20XBA-N3/Sony%20XBA-N3.png)