# SMS Audio STREET by 50 Active Noise Cancelling
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.7; 34 -4.2; 37 -7.3; 41 -10.6; 45 -12.7; 49 -13.2; 54 -12.8; 60 -11.8; 66 -10.7; 72 -9.9; 79 -9.0; 87 -8.3; 96 -8.0; 106 -7.7; 116 -7.5; 128 -7.0; 141 -6.5; 155 -6.0; 170 -5.4; 187 -4.9; 206 -4.4; 227 -3.9; 249 -3.5; 274 -3.3; 302 -3.1; 332 -2.9; 365 -2.1; 402 -1.8; 442 -1.4; 486 -1.1; 535 -1.1; 588 -1.2; 647 -1.6; 712 -2.4; 783 -3.6; 861 -4.8; 947 -6.0; 1042 -6.5; 1146 -6.6; 1261 -7.7; 1387 -7.1; 1526 -6.6; 1678 -6.4; 1846 -4.8; 2031 -3.1; 2234 -2.5; 2457 -2.6; 2703 -3.2; 2973 -2.8; 3270 -1.3; 3597 -0.7; 3957 -0.8; 4353 -0.5; 4788 -0.5; 5267 -1.3; 5793 -5.5; 6373 -6.2; 7010 -5.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.5; 13660 -13.9; 15026 -12.5; 16529 -10.1; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SMS Audio STREET by 50 Active Noise Cancelling GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SMS Audio STREET by 50 Active Noise Cancelling ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.98 | 10.4 dB  |
| Peaking | 47 Hz    | 1.22 | -11.6 dB |
| Peaking | 439 Hz   | 0.94 | 5.6 dB   |
| Peaking | 3911 Hz  | 1.33 | 6.4 dB   |
| Peaking | 14371 Hz | 1.93 | -7.9 dB  |
| Peaking | 671 Hz   | 2.54 | 2.4 dB   |
| Peaking | 1544 Hz  | 0.73 | -3.0 dB  |
| Peaking | 2165 Hz  | 2.28 | 4.4 dB   |
| Peaking | 5045 Hz  | 5.45 | 3.2 dB   |
| Peaking | 5878 Hz  | 4.22 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -7.0 dB |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 6.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -6.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SMS%20Audio%20STREET%20by%2050%20Active%20Noise%20Cancelling/SMS%20Audio%20STREET%20by%2050%20Active%20Noise%20Cancelling.png)