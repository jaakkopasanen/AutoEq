# InEar StageDiver SD3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -8.9; 25 -9.0; 28 -9.2; 31 -9.3; 34 -9.4; 37 -9.6; 41 -9.8; 45 -9.9; 49 -10.0; 54 -10.2; 60 -10.5; 66 -10.8; 72 -11.2; 79 -11.6; 87 -12.0; 96 -12.5; 106 -12.8; 116 -13.2; 128 -13.5; 141 -13.8; 155 -14.1; 170 -14.1; 187 -14.2; 206 -14.1; 227 -14.0; 249 -13.8; 274 -13.5; 302 -13.0; 332 -12.5; 365 -11.8; 402 -11.3; 442 -10.7; 486 -10.0; 535 -9.3; 588 -8.7; 647 -8.1; 712 -7.4; 783 -6.8; 861 -6.3; 947 -6.1; 1042 -6.3; 1146 -6.9; 1261 -7.4; 1387 -7.7; 1526 -7.8; 1678 -7.9; 1846 -8.3; 2031 -8.4; 2234 -7.4; 2457 -4.6; 2703 -1.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.2; 15026 -27.1; 16529 -30.2; 18182 -26.3; 20000 -16.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar StageDiver SD3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar StageDiver SD3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.51 | -2.0 dB  |
| Peaking | 99 Hz    | 0.76 | -1.4 dB  |
| Peaking | 210 Hz   | 0.5  | -7.0 dB  |
| Peaking | 8672 Hz  | 0.36 | 12.0 dB  |
| Peaking | 16562 Hz | 0.7  | -31.3 dB |
| Peaking | 1994 Hz  | 1.39 | -11.3 dB |
| Peaking | 2396 Hz  | 0.73 | 7.6 dB   |
| Peaking | 7560 Hz  | 5.25 | -3.5 dB  |
| Peaking | 8661 Hz  | 3.89 | -2.7 dB  |
| Peaking | 12494 Hz | 5.78 | 6.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB  |
| Peaking | 250 Hz   | 1.41 | -6.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 16000 Hz | 1.41 | -27.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/InEar%20StageDiver%20SD3/InEar%20StageDiver%20SD3.png)