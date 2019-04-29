# Custom Art Pro330v2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.4; 25 -4.7; 28 -5.1; 31 -5.5; 34 -5.7; 37 -6.0; 41 -6.3; 45 -6.5; 49 -6.7; 54 -6.9; 60 -7.3; 66 -7.6; 72 -8.0; 79 -8.4; 87 -8.9; 96 -9.4; 106 -9.9; 116 -10.3; 128 -10.6; 141 -11.0; 155 -11.3; 170 -11.6; 187 -11.8; 206 -11.9; 227 -12.0; 249 -12.1; 274 -12.1; 302 -12.0; 332 -11.9; 365 -11.6; 402 -11.5; 442 -11.2; 486 -10.9; 535 -10.4; 588 -9.8; 647 -9.2; 712 -8.3; 783 -7.3; 861 -6.4; 947 -5.6; 1042 -5.1; 1146 -4.8; 1261 -4.5; 1387 -4.2; 1526 -4.9; 1678 -6.7; 1846 -6.1; 2031 -3.3; 2234 -1.1; 2457 -0.5; 2703 -0.5; 2973 -0.8; 3270 -2.3; 3597 -3.3; 3957 -2.3; 4353 -2.3; 4788 -2.8; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.2; 15026 -18.7; 16529 -19.6; 18182 -12.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Custom Art Pro330v2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Custom Art Pro330v2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.74 | 3.0 dB   |
| Peaking | 240 Hz   | 0.5  | -6.0 dB  |
| Peaking | 2702 Hz  | 1.06 | 5.6 dB   |
| Peaking | 5867 Hz  | 2.74 | 5.5 dB   |
| Peaking | 16229 Hz | 1.92 | -15.6 dB |
| Peaking | 1156 Hz  | 2.2  | 2.1 dB   |
| Peaking | 1757 Hz  | 5.11 | -3.6 dB  |
| Peaking | 2291 Hz  | 5.8  | 1.3 dB   |
| Peaking | 13239 Hz | 2.9  | 4.4 dB   |
| Peaking | 14816 Hz | 4.5  | -5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB   |
| Peaking | 62 Hz    | 1.41 | -0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -13.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Custom%20Art%20Pro330v2/Custom%20Art%20Pro330v2.png)