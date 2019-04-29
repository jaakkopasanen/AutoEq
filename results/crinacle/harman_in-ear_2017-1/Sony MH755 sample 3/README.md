# Sony MH755 sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.2; 23 -12.8; 25 -12.5; 28 -12.1; 31 -11.7; 34 -11.4; 37 -11.0; 41 -10.5; 45 -10.1; 49 -9.7; 54 -9.4; 60 -9.0; 66 -8.6; 72 -8.4; 79 -8.2; 87 -8.0; 96 -7.8; 106 -7.7; 116 -7.5; 128 -7.4; 141 -7.2; 155 -7.0; 170 -6.8; 187 -6.6; 206 -6.3; 227 -6.0; 249 -5.8; 274 -5.6; 302 -5.2; 332 -4.9; 365 -4.5; 402 -4.3; 442 -4.1; 486 -3.9; 535 -3.6; 588 -3.4; 647 -3.1; 712 -2.9; 783 -2.6; 861 -2.5; 947 -2.6; 1042 -3.0; 1146 -3.8; 1261 -4.4; 1387 -4.6; 1526 -4.5; 1678 -4.2; 1846 -3.9; 2031 -3.5; 2234 -3.1; 2457 -3.1; 2703 -4.0; 2973 -4.6; 3270 -4.6; 3597 -4.2; 3957 -3.6; 4353 -3.0; 4788 -2.4; 5267 -1.8; 5793 -0.9; 6373 -0.5; 7010 -1.6; 7711 -3.7; 8482 -4.0; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.6; 13660 -14.9; 15026 -22.8; 16529 -23.4; 18182 -21.4; 20000 -16.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH755 sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH755 sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.26 | -9.6 dB  |
| Peaking | 150 Hz   | 0.75 | -2.0 dB  |
| Peaking | 763 Hz   | 1.95 | 1.7 dB   |
| Peaking | 10792 Hz | 0.36 | 21.2 dB  |
| Peaking | 15866 Hz | 0.37 | -34.8 dB |
| Peaking | 950 Hz   | 6.58 | 0.5 dB   |
| Peaking | 3224 Hz  | 5.95 | -1.0 dB  |
| Peaking | 6067 Hz  | 2.21 | 4.0 dB   |
| Peaking | 10747 Hz | 0.65 | -3.2 dB  |
| Peaking | 12218 Hz | 3.51 | 6.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 16000 Hz | 1.41 | -24.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20MH755%20sample%203/Sony%20MH755%20sample%203.png)