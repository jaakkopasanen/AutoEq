# InEar PhoPhile-8 Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.1; 25 -1.4; 28 -1.7; 31 -2.0; 34 -2.3; 37 -2.5; 41 -2.8; 45 -3.0; 49 -3.2; 54 -3.4; 60 -3.7; 66 -4.0; 72 -4.4; 79 -4.7; 87 -5.1; 96 -5.5; 106 -5.9; 116 -6.1; 128 -6.4; 141 -6.7; 155 -6.9; 170 -7.0; 187 -7.1; 206 -7.1; 227 -7.2; 249 -7.2; 274 -7.2; 302 -7.1; 332 -6.9; 365 -6.8; 402 -6.7; 442 -6.6; 486 -6.5; 535 -6.3; 588 -6.2; 647 -6.0; 712 -5.7; 783 -5.5; 861 -5.3; 947 -5.4; 1042 -5.8; 1146 -6.5; 1261 -7.0; 1387 -7.1; 1526 -6.7; 1678 -6.1; 1846 -5.2; 2031 -4.2; 2234 -2.8; 2457 -1.5; 2703 -0.6; 2973 -0.5; 3270 -1.0; 3597 -1.1; 3957 -1.0; 4353 -0.9; 4788 -1.5; 5267 -3.4; 5793 -4.6; 6373 -3.2; 7010 -3.5; 7711 -5.2; 8482 -5.3; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -9.0; 15026 -18.3; 16529 -25.3; 18182 -29.0; 20000 -27.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar PhoPhile-8 Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar PhoPhile-8 Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.39 | 4.3 dB   |
| Peaking | 416 Hz   | 0.12 | -2.0 dB  |
| Peaking | 3880 Hz  | 0.66 | 9.6 dB   |
| Peaking | 12141 Hz | 0.74 | 18.5 dB  |
| Peaking | 17834 Hz | 0.24 | -30.1 dB |
| Peaking | 861 Hz   | 1.1  | 3.9 dB   |
| Peaking | 1275 Hz  | 0.6  | -3.5 dB  |
| Peaking | 2515 Hz  | 2.28 | 3.0 dB   |
| Peaking | 5726 Hz  | 6.24 | -1.7 dB  |
| Peaking | 6666 Hz  | 4.94 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB   |
| Peaking | 62 Hz    | 1.41 | 0.9 dB   |
| Peaking | 125 Hz   | 1.41 | -1.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 16000 Hz | 1.41 | -23.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/InEar%20PhoPhile-8%20Treble/InEar%20PhoPhile-8%20Treble.png)