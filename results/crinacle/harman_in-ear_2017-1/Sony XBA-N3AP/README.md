# Sony XBA-N3AP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.7; 25 -10.1; 28 -10.5; 31 -10.8; 34 -11.0; 37 -11.1; 41 -11.3; 45 -11.5; 49 -11.6; 54 -11.7; 60 -11.7; 66 -11.8; 72 -11.9; 79 -12.0; 87 -12.0; 96 -12.1; 106 -12.1; 116 -12.0; 128 -12.0; 141 -11.8; 155 -11.6; 170 -11.3; 187 -11.0; 206 -10.6; 227 -10.2; 249 -9.8; 274 -9.4; 302 -9.0; 332 -8.4; 365 -8.0; 402 -7.6; 442 -7.3; 486 -7.0; 535 -6.7; 588 -6.4; 647 -6.2; 712 -5.9; 783 -5.7; 861 -5.5; 947 -5.7; 1042 -6.2; 1146 -6.8; 1261 -7.0; 1387 -7.3; 1526 -7.2; 1678 -6.7; 1846 -6.0; 2031 -5.4; 2234 -4.5; 2457 -3.3; 2703 -1.9; 2973 -0.6; 3270 -0.5; 3597 -1.8; 3957 -2.9; 4353 -2.0; 4788 -2.8; 5267 -2.9; 5793 -1.3; 6373 -1.0; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.5; 10263 -6.8; 11289 -6.7; 12418 -8.7; 13660 -15.3; 15026 -24.4; 16529 -29.8; 18182 -26.3; 20000 -12.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-N3AP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-N3AP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 52 Hz    | 0.38 | -4.7 dB  |
| Peaking | 162 Hz   | 0.76 | -3.0 dB  |
| Peaking | 5442 Hz  | 0.61 | 8.3 dB   |
| Peaking | 11959 Hz | 1.67 | 9.7 dB   |
| Peaking | 16586 Hz | 0.62 | -26.5 dB |
| Peaking | 1548 Hz  | 2.66 | -2.1 dB  |
| Peaking | 3066 Hz  | 3.63 | 3.3 dB   |
| Peaking | 5383 Hz  | 1.5  | -2.3 dB  |
| Peaking | 6110 Hz  | 4.91 | 4.0 dB   |
| Peaking | 15202 Hz | 8.79 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -4.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 16000 Hz | 1.41 | -26.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20XBA-N3AP/Sony%20XBA-N3AP.png)