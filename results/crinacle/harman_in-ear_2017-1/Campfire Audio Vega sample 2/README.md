# Campfire Audio Vega sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.6; 23 -12.8; 25 -12.9; 28 -13.1; 31 -13.2; 34 -13.3; 37 -13.4; 41 -13.4; 45 -13.5; 49 -13.6; 54 -13.6; 60 -13.7; 66 -13.8; 72 -14.0; 79 -14.1; 87 -14.2; 96 -14.4; 106 -14.5; 116 -14.5; 128 -14.5; 141 -14.4; 155 -14.3; 170 -14.0; 187 -13.7; 206 -13.4; 227 -13.0; 249 -12.6; 274 -12.1; 302 -11.6; 332 -10.9; 365 -10.3; 402 -9.8; 442 -9.3; 486 -8.8; 535 -8.3; 588 -7.8; 647 -7.4; 712 -7.0; 783 -6.6; 861 -6.4; 947 -6.6; 1042 -6.8; 1146 -7.2; 1261 -8.0; 1387 -7.4; 1526 -6.0; 1678 -5.4; 1846 -4.4; 2031 -2.7; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.6; 5793 -2.8; 6373 -6.0; 7010 -7.2; 7711 -8.5; 8482 -9.2; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.7; 16529 -9.5; 18182 -9.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Vega sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Vega sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 1.52 | -5.7 dB |
| Peaking | 39 Hz    | 0.32 | -5.9 dB |
| Peaking | 174 Hz   | 0.57 | -5.5 dB |
| Peaking | 3404 Hz  | 0.82 | 9.0 dB  |
| Peaking | 7882 Hz  | 0.11 | -2.0 dB |
| Peaking | 1316 Hz  | 6.3  | -2.0 dB |
| Peaking | 2291 Hz  | 4.08 | 2.8 dB  |
| Peaking | 5264 Hz  | 2.3  | 6.0 dB  |
| Peaking | 8321 Hz  | 0.54 | -6.6 dB |
| Peaking | 11252 Hz | 0.99 | 6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Vega%20sample%202/Campfire%20Audio%20Vega%20sample%202.png)