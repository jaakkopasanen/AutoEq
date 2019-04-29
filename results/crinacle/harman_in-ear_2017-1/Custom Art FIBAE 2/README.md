# Custom Art FIBAE 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.4; 25 -6.5; 28 -6.8; 31 -7.0; 34 -7.2; 37 -7.4; 41 -7.6; 45 -7.8; 49 -7.9; 54 -8.2; 60 -8.4; 66 -8.7; 72 -9.1; 79 -9.4; 87 -9.8; 96 -10.3; 106 -10.6; 116 -10.9; 128 -11.2; 141 -11.4; 155 -11.7; 170 -11.7; 187 -11.8; 206 -11.7; 227 -11.6; 249 -11.5; 274 -11.3; 302 -11.0; 332 -10.6; 365 -10.1; 402 -9.7; 442 -9.3; 486 -8.9; 535 -8.4; 588 -7.9; 647 -7.4; 712 -6.9; 783 -6.4; 861 -6.1; 947 -6.1; 1042 -6.5; 1146 -7.4; 1261 -8.3; 1387 -9.1; 1526 -9.9; 1678 -10.8; 1846 -11.6; 2031 -9.8; 2234 -5.8; 2457 -3.0; 2703 -0.7; 2973 -0.5; 3270 -0.6; 3597 -3.0; 3957 -0.9; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.7; 10263 -8.6; 11289 -6.5; 12418 -6.5; 13660 -11.3; 15026 -17.5; 16529 -13.9; 18182 -8.8; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Custom Art FIBAE 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Custom Art FIBAE 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 181 Hz   | 0.53 | -5.5 dB  |
| Peaking | 1867 Hz  | 2    | -10.7 dB |
| Peaking | 2617 Hz  | 1.03 | 8.5 dB   |
| Peaking | 5481 Hz  | 2.25 | 5.1 dB   |
| Peaking | 15436 Hz | 1.99 | -11.7 dB |
| Peaking | 15 Hz    | 1.52 | 0.5 dB   |
| Peaking | 881 Hz   | 2.82 | 1.4 dB   |
| Peaking | 1329 Hz  | 4.65 | -1.1 dB  |
| Peaking | 9548 Hz  | 5.48 | -3.2 dB  |
| Peaking | 12298 Hz | 4.46 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -10.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Custom%20Art%20FIBAE%202/Custom%20Art%20FIBAE%202.png)