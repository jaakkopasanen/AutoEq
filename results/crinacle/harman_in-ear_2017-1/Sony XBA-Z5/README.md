# Sony XBA-Z5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.0; 25 -7.4; 28 -7.8; 31 -8.1; 34 -8.3; 37 -8.6; 41 -8.9; 45 -9.2; 49 -9.4; 54 -9.6; 60 -10.0; 66 -10.4; 72 -10.6; 79 -10.9; 87 -11.3; 96 -11.6; 106 -12.1; 116 -12.2; 128 -12.4; 141 -12.5; 155 -12.4; 170 -12.4; 187 -12.2; 206 -12.0; 227 -11.5; 249 -11.2; 274 -10.8; 302 -10.3; 332 -9.7; 365 -9.2; 402 -9.2; 442 -9.0; 486 -8.3; 535 -7.9; 588 -7.6; 647 -7.2; 712 -6.9; 783 -6.5; 861 -6.0; 947 -5.7; 1042 -6.1; 1146 -6.7; 1261 -7.2; 1387 -7.1; 1526 -6.5; 1678 -5.7; 1846 -4.6; 2031 -3.1; 2234 -1.8; 2457 -0.8; 2703 -0.5; 2973 -0.8; 3270 -1.3; 3597 -0.9; 3957 -1.8; 4353 -4.5; 4788 -6.2; 5267 -5.9; 5793 -2.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -14.9; 15026 -25.3; 16529 -27.3; 18182 -20.4; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-Z5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-Z5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 71 Hz    | 0.52 | -1.8 dB  |
| Peaking | 169 Hz   | 0.56 | -5.1 dB  |
| Peaking | 2936 Hz  | 1.35 | 6.4 dB   |
| Peaking | 11300 Hz | 0.68 | 10.6 dB  |
| Peaking | 15938 Hz | 0.93 | -28.1 dB |
| Peaking | 1410 Hz  | 4.73 | -1.7 dB  |
| Peaking | 5063 Hz  | 4.58 | -3.6 dB  |
| Peaking | 6276 Hz  | 3.31 | 5.6 dB   |
| Peaking | 7788 Hz  | 3.72 | -2.1 dB  |
| Peaking | 9186 Hz  | 3.75 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 16000 Hz | 1.41 | -22.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20XBA-Z5/Sony%20XBA-Z5.png)