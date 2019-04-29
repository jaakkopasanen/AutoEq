# Lime Ears Model X Bass sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.0; 25 -6.2; 28 -6.5; 31 -6.7; 34 -6.9; 37 -7.1; 41 -7.3; 45 -7.5; 49 -7.7; 54 -8.0; 60 -8.2; 66 -8.4; 72 -8.8; 79 -9.1; 87 -9.5; 96 -9.9; 106 -10.3; 116 -10.7; 128 -11.0; 141 -11.2; 155 -11.4; 170 -11.5; 187 -11.7; 206 -11.8; 227 -11.7; 249 -11.6; 274 -11.4; 302 -11.2; 332 -10.8; 365 -10.4; 402 -10.1; 442 -9.7; 486 -9.2; 535 -8.7; 588 -8.1; 647 -7.4; 712 -6.7; 783 -5.9; 861 -5.2; 947 -4.7; 1042 -4.7; 1146 -4.9; 1261 -5.1; 1387 -4.9; 1526 -4.5; 1678 -4.1; 1846 -3.8; 2031 -3.7; 2234 -3.0; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.6; 3957 -1.8; 4353 -3.0; 4788 -6.0; 5267 -4.9; 5793 -1.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.3; 9330 -10.8; 10263 -7.7; 11289 -6.5; 12418 -6.5; 13660 -10.6; 15026 -16.4; 16529 -20.0; 18182 -21.8; 20000 -19.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Model X Bass sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Model X Bass sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 196 Hz   | 0.54 | -5.5 dB  |
| Peaking | 2873 Hz  | 0.84 | 5.8 dB   |
| Peaking | 6302 Hz  | 5.19 | 5.4 dB   |
| Peaking | 8975 Hz  | 7.01 | -3.8 dB  |
| Peaking | 18415 Hz | 0.76 | -17.2 dB |
| Peaking | 19 Hz    | 1.73 | 1.0 dB   |
| Peaking | 927 Hz   | 3.54 | 1.8 dB   |
| Peaking | 4893 Hz  | 9.76 | -3.1 dB  |
| Peaking | 12442 Hz | 2.65 | 5.2 dB   |
| Peaking | 15348 Hz | 1.98 | -4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB   |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 16000 Hz | 1.41 | -15.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Lime%20Ears%20Model%20X%20Bass%20sample%202/Lime%20Ears%20Model%20X%20Bass%20sample%202.png)