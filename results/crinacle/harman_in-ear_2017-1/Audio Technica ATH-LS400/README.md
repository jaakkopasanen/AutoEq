# Audio Technica ATH-LS400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.9; 25 -8.1; 28 -8.4; 31 -8.5; 34 -8.7; 37 -8.8; 41 -8.9; 45 -9.1; 49 -9.2; 54 -9.4; 60 -9.6; 66 -9.9; 72 -10.3; 79 -10.6; 87 -11.0; 96 -11.3; 106 -11.7; 116 -12.0; 128 -12.3; 141 -12.5; 155 -12.8; 170 -12.8; 187 -12.8; 206 -12.8; 227 -12.7; 249 -12.5; 274 -12.3; 302 -12.0; 332 -11.6; 365 -11.1; 402 -10.8; 442 -10.3; 486 -9.8; 535 -9.2; 588 -8.6; 647 -8.0; 712 -7.4; 783 -6.7; 861 -6.1; 947 -5.8; 1042 -5.9; 1146 -6.1; 1261 -6.1; 1387 -5.7; 1526 -4.8; 1678 -4.0; 1846 -3.8; 2031 -4.3; 2234 -5.0; 2457 -4.4; 2703 -2.7; 2973 -0.9; 3270 -0.5; 3597 -2.7; 3957 -3.6; 4353 -2.2; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.3; 15026 -25.7; 16529 -31.1; 18182 -19.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-LS400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-LS400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 80 Hz    | 0.23 | -1.8 dB  |
| Peaking | 211 Hz   | 0.48 | -5.1 dB  |
| Peaking | 5427 Hz  | 3.57 | 3.1 dB   |
| Peaking | 6435 Hz  | 0.23 | 4.7 dB   |
| Peaking | 16332 Hz | 1.84 | -30.3 dB |
| Peaking | 2317 Hz  | 6    | -1.8 dB  |
| Peaking | 3093 Hz  | 6.66 | 2.7 dB   |
| Peaking | 7837 Hz  | 5.94 | -4.2 dB  |
| Peaking | 13438 Hz | 2.71 | 9.0 dB   |
| Peaking | 15000 Hz | 3.1  | -9.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 16000 Hz | 1.41 | -22.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Audio%20Technica%20ATH-LS400/Audio%20Technica%20ATH-LS400.png)