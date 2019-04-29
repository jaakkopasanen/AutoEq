# Lime Ears Model X Bass sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.8; 25 -6.9; 28 -7.0; 31 -7.2; 34 -7.3; 37 -7.4; 41 -7.6; 45 -7.8; 49 -7.9; 54 -8.1; 60 -8.4; 66 -8.7; 72 -9.0; 79 -9.4; 87 -9.8; 96 -10.3; 106 -10.6; 116 -10.9; 128 -11.2; 141 -11.5; 155 -11.7; 170 -11.8; 187 -11.9; 206 -11.9; 227 -11.8; 249 -11.7; 274 -11.6; 302 -11.3; 332 -10.9; 365 -10.5; 402 -10.2; 442 -9.9; 486 -9.4; 535 -8.9; 588 -8.4; 647 -7.9; 712 -7.2; 783 -6.6; 861 -6.1; 947 -5.8; 1042 -5.8; 1146 -6.1; 1261 -6.4; 1387 -6.1; 1526 -5.6; 1678 -4.9; 1846 -4.1; 2031 -3.3; 2234 -2.5; 2457 -1.8; 2703 -0.8; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -2.6; 5267 -2.8; 5793 -1.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.7; 15026 -17.3; 16529 -18.8; 18182 -14.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Model X Bass sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Model X Bass sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 116 Hz   | 0.67 | -2.4 dB  |
| Peaking | 257 Hz   | 0.6  | -4.3 dB  |
| Peaking | 3817 Hz  | 0.67 | 6.5 dB   |
| Peaking | 12961 Hz | 2.37 | 6.1 dB   |
| Peaking | 16033 Hz | 0.99 | -14.3 dB |
| Peaking | 916 Hz   | 3.25 | 1.1 dB   |
| Peaking | 1381 Hz  | 2.78 | -1.2 dB  |
| Peaking | 5090 Hz  | 3.18 | -4.5 dB  |
| Peaking | 6254 Hz  | 1.57 | 5.3 dB   |
| Peaking | 7568 Hz  | 2.98 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -13.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Lime%20Ears%20Model%20X%20Bass%20sample%201/Lime%20Ears%20Model%20X%20Bass%20sample%201.png)