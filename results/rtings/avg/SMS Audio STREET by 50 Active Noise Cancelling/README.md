# SMS Audio STREET by 50 Active Noise Cancelling
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -1.2; 31 -3.8; 34 -7.0; 37 -10.0; 41 -13.4; 45 -15.4; 49 -16.0; 54 -15.6; 60 -14.6; 66 -13.5; 72 -12.6; 79 -11.8; 87 -11.1; 96 -10.8; 106 -10.5; 116 -10.2; 128 -9.8; 141 -9.3; 155 -8.7; 170 -8.2; 187 -7.7; 206 -7.2; 227 -6.6; 249 -6.3; 274 -6.0; 302 -5.9; 332 -5.6; 365 -4.9; 402 -4.6; 442 -4.2; 486 -3.9; 535 -3.9; 588 -4.0; 647 -4.4; 712 -5.2; 783 -6.3; 861 -7.6; 947 -8.8; 1042 -9.3; 1146 -9.3; 1261 -10.5; 1387 -9.8; 1526 -9.4; 1678 -9.2; 1846 -7.6; 2031 -5.9; 2234 -5.2; 2457 -5.4; 2703 -5.9; 2973 -5.5; 3270 -4.1; 3597 -3.5; 3957 -3.4; 4353 -0.5; 4788 -0.5; 5267 -3.3; 5793 -8.2; 6373 -9.0; 7010 -8.6; 7711 -8.1; 8482 -9.3; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -12.2; 13660 -16.7; 15026 -15.3; 16529 -12.9; 18182 -8.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SMS Audio STREET by 50 Active Noise Cancelling GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SMS Audio STREET by 50 Active Noise Cancelling ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 1.12 | 12.4 dB  |
| Peaking | 47 Hz    | 0.93 | -13.7 dB |
| Peaking | 1301 Hz  | 2.86 | -4.3 dB  |
| Peaking | 4433 Hz  | 3.43 | 7.0 dB   |
| Peaking | 14657 Hz | 1.49 | -10.5 dB |
| Peaking | 525 Hz   | 1.28 | 3.2 dB   |
| Peaking | 954 Hz   | 3.17 | -2.3 dB  |
| Peaking | 3878 Hz  | 0.92 | 0.9 dB   |
| Peaking | 6407 Hz  | 2.97 | -3.6 dB  |
| Peaking | 11028 Hz | 4.91 | 3.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -9.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -9.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SMS%20Audio%20STREET%20by%2050%20Active%20Noise%20Cancelling/SMS%20Audio%20STREET%20by%2050%20Active%20Noise%20Cancelling.png)