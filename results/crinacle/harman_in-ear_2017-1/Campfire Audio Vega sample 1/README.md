# Campfire Audio Vega sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -13.6; 25 -13.6; 28 -13.6; 31 -13.6; 34 -13.6; 37 -13.6; 41 -13.6; 45 -13.6; 49 -13.6; 54 -13.6; 60 -13.7; 66 -13.8; 72 -13.9; 79 -14.0; 87 -14.1; 96 -14.2; 106 -14.3; 116 -14.3; 128 -14.3; 141 -14.2; 155 -14.1; 170 -13.8; 187 -13.6; 206 -13.2; 227 -12.8; 249 -12.4; 274 -11.9; 302 -11.4; 332 -10.7; 365 -10.1; 402 -9.7; 442 -9.2; 486 -8.6; 535 -8.2; 588 -7.7; 647 -7.3; 712 -6.9; 783 -6.5; 861 -6.3; 947 -6.4; 1042 -6.7; 1146 -7.0; 1261 -7.8; 1387 -7.1; 1526 -6.4; 1678 -5.9; 1846 -4.8; 2031 -2.8; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.5; 5793 -2.6; 6373 -4.2; 7010 -4.6; 7711 -6.5; 8482 -9.4; 9330 -9.9; 10263 -7.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.6; 16529 -15.8; 18182 -15.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Vega sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Vega sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.27 | -6.5 dB  |
| Peaking | 157 Hz   | 0.48 | -6.4 dB  |
| Peaking | 3685 Hz  | 0.81 | 6.9 dB   |
| Peaking | 8857 Hz  | 3.98 | -5.1 dB  |
| Peaking | 17487 Hz | 1.47 | -11.3 dB |
| Peaking | 1431 Hz  | 2.63 | -2.2 dB  |
| Peaking | 2305 Hz  | 4.37 | 2.5 dB   |
| Peaking | 3596 Hz  | 5.08 | -1.0 dB  |
| Peaking | 13900 Hz | 2.47 | 2.5 dB   |
| Peaking | 15830 Hz | 3.6  | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -8.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Vega%20sample%201/Campfire%20Audio%20Vega%20sample%201.png)