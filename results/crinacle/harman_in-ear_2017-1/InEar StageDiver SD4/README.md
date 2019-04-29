# InEar StageDiver SD4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.4; 25 -7.5; 28 -7.6; 31 -7.7; 34 -7.8; 37 -7.9; 41 -8.0; 45 -8.2; 49 -8.4; 54 -8.5; 60 -8.8; 66 -9.1; 72 -9.4; 79 -9.8; 87 -10.2; 96 -10.7; 106 -11.1; 116 -11.4; 128 -11.8; 141 -12.1; 155 -12.3; 170 -12.4; 187 -12.5; 206 -12.6; 227 -12.5; 249 -12.5; 274 -12.3; 302 -12.1; 332 -11.8; 365 -11.4; 402 -11.1; 442 -10.7; 486 -10.2; 535 -9.7; 588 -9.2; 647 -8.6; 712 -7.9; 783 -7.1; 861 -6.4; 947 -5.9; 1042 -5.7; 1146 -5.8; 1261 -5.7; 1387 -5.1; 1526 -4.2; 1678 -3.1; 1846 -2.1; 2031 -0.9; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.1; 5267 -4.9; 5793 -5.8; 6373 -5.3; 7010 -5.2; 7711 -8.4; 8482 -10.2; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.8; 15026 -21.2; 16529 -28.0; 18182 -26.8; 20000 -14.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar StageDiver SD4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar StageDiver SD4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 199 Hz   | 0.64 | -1.7 dB  |
| Peaking | 264 Hz   | 0.27 | -4.8 dB  |
| Peaking | 8246 Hz  | 1.32 | -13.9 dB |
| Peaking | 9664 Hz  | 0.3  | 26.5 dB  |
| Peaking | 16869 Hz | 0.46 | -37.8 dB |
| Peaking | 1367 Hz  | 2.61 | -2.3 dB  |
| Peaking | 2473 Hz  | 0.44 | 1.1 dB   |
| Peaking | 5509 Hz  | 5.41 | -3.6 dB  |
| Peaking | 13089 Hz | 5.41 | 4.2 dB   |
| Peaking | 15173 Hz | 3.71 | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 16000 Hz | 1.41 | -22.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/InEar%20StageDiver%20SD4/InEar%20StageDiver%20SD4.png)