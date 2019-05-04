# SMS Audio STREET by 50 Active Noise Cancelling
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -1.2; 31 -3.6; 34 -6.9; 37 -9.9; 41 -13.1; 45 -15.1; 49 -15.8; 54 -15.5; 60 -14.4; 66 -13.3; 72 -12.4; 79 -11.6; 87 -10.9; 96 -10.5; 106 -10.3; 116 -10.0; 128 -9.6; 141 -9.0; 155 -8.5; 170 -8.0; 187 -7.5; 206 -7.0; 227 -6.5; 249 -6.2; 274 -6.0; 302 -5.8; 332 -5.6; 365 -4.9; 402 -4.5; 442 -4.2; 486 -3.9; 535 -3.9; 588 -4.1; 647 -4.5; 712 -5.3; 783 -6.4; 861 -7.7; 947 -9.0; 1042 -9.3; 1146 -9.5; 1261 -10.6; 1387 -10.0; 1526 -9.7; 1678 -9.4; 1846 -7.9; 2031 -6.5; 2234 -6.2; 2457 -6.3; 2703 -6.7; 2973 -5.6; 3270 -3.9; 3597 -3.4; 3957 -2.8; 4353 -0.5; 4788 -0.5; 5267 -3.2; 5793 -8.1; 6373 -8.2; 7010 -8.7; 7711 -8.9; 8482 -8.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -12.3; 13660 -15.9; 15026 -14.9; 16529 -12.8; 18182 -8.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SMS Audio STREET by 50 Active Noise Cancelling GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SMS Audio STREET by 50 Active Noise Cancelling ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 1.11 | 12.0 dB  |
| Peaking | 48 Hz    | 0.96 | -13.4 dB |
| Peaking | 1322 Hz  | 2.53 | -4.4 dB  |
| Peaking | 4413 Hz  | 3.3  | 7.0 dB   |
| Peaking | 14755 Hz | 1.37 | -9.8 dB  |
| Peaking | 521 Hz   | 1.22 | 3.2 dB   |
| Peaking | 953 Hz   | 3.66 | -2.4 dB  |
| Peaking | 5008 Hz  | 9.88 | 3.7 dB   |
| Peaking | 6564 Hz  | 1.9  | -2.8 dB  |
| Peaking | 10719 Hz | 3.76 | 3.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | -9.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -9.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SMS%20Audio%20STREET%20by%2050%20Active%20Noise%20Cancelling/SMS%20Audio%20STREET%20by%2050%20Active%20Noise%20Cancelling.png)