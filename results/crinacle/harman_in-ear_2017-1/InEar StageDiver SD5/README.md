# InEar StageDiver SD5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.3; 25 -7.4; 28 -7.6; 31 -7.7; 34 -7.8; 37 -7.9; 41 -8.0; 45 -8.1; 49 -8.2; 54 -8.4; 60 -8.7; 66 -8.9; 72 -9.2; 79 -9.5; 87 -9.8; 96 -10.2; 106 -10.5; 116 -10.7; 128 -10.9; 141 -11.1; 155 -11.2; 170 -11.2; 187 -11.1; 206 -10.8; 227 -10.6; 249 -10.4; 274 -10.1; 302 -9.6; 332 -9.1; 365 -8.5; 402 -8.0; 442 -7.6; 486 -7.0; 535 -6.5; 588 -6.1; 647 -5.6; 712 -5.2; 783 -4.8; 861 -4.7; 947 -4.9; 1042 -5.6; 1146 -6.6; 1261 -7.7; 1387 -8.3; 1526 -8.5; 1678 -8.2; 1846 -7.5; 2031 -6.3; 2234 -4.9; 2457 -3.4; 2703 -2.1; 2973 -1.3; 3270 -1.0; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.6; 6373 -4.6; 7010 -7.1; 7711 -9.0; 8482 -8.8; 9330 -8.4; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -9.9; 15026 -20.9; 16529 -24.7; 18182 -22.3; 20000 -16.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar StageDiver SD5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar StageDiver SD5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 119 Hz   | 0.62 | -3.8 dB  |
| Peaking | 234 Hz   | 1.31 | -2.2 dB  |
| Peaking | 8094 Hz  | 2.06 | -11.6 dB |
| Peaking | 9032 Hz  | 0.43 | 14.4 dB  |
| Peaking | 16786 Hz | 0.65 | -24.9 dB |
| Peaking | 908 Hz   | 1.1  | 5.9 dB   |
| Peaking | 1525 Hz  | 0.62 | -7.5 dB  |
| Peaking | 2935 Hz  | 1.01 | 5.1 dB   |
| Peaking | 13264 Hz | 3.41 | 9.0 dB   |
| Peaking | 13724 Hz | 1.44 | -5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 16000 Hz | 1.41 | -19.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/InEar%20StageDiver%20SD5/InEar%20StageDiver%20SD5.png)