# Audeze iSine 20 Cipher
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -7.5; 25 -8.3; 28 -9.2; 31 -9.7; 34 -9.8; 37 -9.6; 41 -9.3; 45 -9.2; 49 -9.3; 54 -9.6; 60 -9.9; 66 -9.8; 72 -9.6; 79 -9.3; 87 -8.9; 96 -8.6; 106 -8.4; 116 -8.7; 128 -9.2; 141 -9.0; 155 -8.4; 170 -7.7; 187 -7.3; 206 -7.2; 227 -7.5; 249 -7.7; 274 -7.7; 302 -7.2; 332 -6.7; 365 -6.2; 402 -6.1; 442 -6.3; 486 -6.6; 535 -6.7; 588 -6.8; 647 -6.8; 712 -6.9; 783 -7.0; 861 -7.3; 947 -7.8; 1042 -7.7; 1146 -7.8; 1261 -8.2; 1387 -9.0; 1526 -10.2; 1678 -10.0; 1846 -9.4; 2031 -8.3; 2234 -7.7; 2457 -7.9; 2703 -7.2; 2973 -5.7; 3270 -6.0; 3597 -5.9; 3957 -3.3; 4353 -3.7; 4788 -5.0; 5267 -2.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.2; 13660 -15.6; 15026 -26.2; 16529 -28.5; 18182 -20.8; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze iSine 20 Cipher GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine 20 Cipher ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 52 Hz    | 0.53 | -3.3 dB  |
| Peaking | 137 Hz   | 3.82 | -1.4 dB  |
| Peaking | 1750 Hz  | 1.14 | -4.3 dB  |
| Peaking | 9953 Hz  | 0.38 | 10.7 dB  |
| Peaking | 16042 Hz | 0.9  | -30.8 dB |
| Peaking | 261 Hz   | 6.6  | -0.9 dB  |
| Peaking | 6175 Hz  | 3.2  | 6.2 dB   |
| Peaking | 7405 Hz  | 1.28 | -4.3 dB  |
| Peaking | 12278 Hz | 2.71 | 5.1 dB   |
| Peaking | 14532 Hz | 4.33 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 16000 Hz | 1.41 | -24.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Audeze%20iSine%2020%20Cipher/Audeze%20iSine%2020%20Cipher.png)