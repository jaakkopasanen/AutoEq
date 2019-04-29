# InEar StageDiver SD2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.0; 25 -5.2; 28 -5.4; 31 -5.5; 34 -5.7; 37 -5.8; 41 -6.0; 45 -6.2; 49 -6.3; 54 -6.5; 60 -6.8; 66 -7.1; 72 -7.5; 79 -8.0; 87 -8.4; 96 -8.8; 106 -9.2; 116 -9.5; 128 -9.9; 141 -10.2; 155 -10.5; 170 -10.7; 187 -10.8; 206 -10.9; 227 -10.9; 249 -10.9; 274 -10.8; 302 -10.7; 332 -10.5; 365 -10.3; 402 -10.1; 442 -9.8; 486 -9.5; 535 -9.1; 588 -8.7; 647 -8.3; 712 -7.8; 783 -7.3; 861 -6.9; 947 -6.8; 1042 -7.1; 1146 -7.7; 1261 -8.3; 1387 -8.5; 1526 -8.3; 1678 -8.2; 1846 -8.2; 2031 -7.9; 2234 -6.7; 2457 -4.2; 2703 -1.4; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -3.3; 5793 -2.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -18.2; 15026 -29.2; 16529 -31.0; 18182 -27.6; 20000 -22.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar StageDiver SD2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar StageDiver SD2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 378 Hz   | 0.35 | -6.6 dB  |
| Peaking | 1767 Hz  | 0.96 | -10.2 dB |
| Peaking | 3944 Hz  | 0.25 | 20.2 dB  |
| Peaking | 12168 Hz | 1.35 | 16.8 dB  |
| Peaking | 15448 Hz | 0.35 | -37.3 dB |
| Peaking | 22 Hz    | 1.27 | 1.8 dB   |
| Peaking | 48 Hz    | 2.13 | 0.7 dB   |
| Peaking | 2834 Hz  | 9.62 | 1.6 dB   |
| Peaking | 5496 Hz  | 8.71 | -3.0 dB  |
| Peaking | 6287 Hz  | 7.42 | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB   |
| Peaking | 62 Hz    | 1.41 | -0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 16000 Hz | 1.41 | -30.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/InEar%20StageDiver%20SD2/InEar%20StageDiver%20SD2.png)