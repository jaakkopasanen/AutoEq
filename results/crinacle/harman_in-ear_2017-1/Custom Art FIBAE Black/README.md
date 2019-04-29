# Custom Art FIBAE Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.5; 25 -6.9; 28 -7.3; 31 -7.6; 34 -7.8; 37 -8.0; 41 -8.3; 45 -8.5; 49 -8.8; 54 -9.0; 60 -9.3; 66 -9.6; 72 -9.9; 79 -10.2; 87 -10.7; 96 -11.0; 106 -11.4; 116 -11.8; 128 -12.0; 141 -12.3; 155 -12.4; 170 -12.6; 187 -12.7; 206 -12.8; 227 -12.8; 249 -12.7; 274 -12.6; 302 -12.4; 332 -12.0; 365 -11.6; 402 -11.3; 442 -10.9; 486 -10.3; 535 -9.7; 588 -9.0; 647 -8.2; 712 -7.3; 783 -6.4; 861 -5.7; 947 -5.5; 1042 -5.9; 1146 -6.8; 1261 -7.5; 1387 -7.8; 1526 -7.4; 1678 -6.8; 1846 -6.0; 2031 -5.0; 2234 -3.9; 2457 -3.2; 2703 -2.9; 2973 -3.0; 3270 -1.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -8.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -14.5; 16529 -19.1; 18182 -15.4; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Custom Art FIBAE Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Custom Art FIBAE Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 144 Hz   | 0.53 | -5.4 dB  |
| Peaking | 335 Hz   | 1.12 | -3.2 dB  |
| Peaking | 1479 Hz  | 4.18 | -2.1 dB  |
| Peaking | 4394 Hz  | 0.89 | 6.7 dB   |
| Peaking | 16976 Hz | 1.35 | -13.7 dB |
| Peaking | 895 Hz   | 4.46 | 1.8 dB   |
| Peaking | 6253 Hz  | 3.26 | 3.9 dB   |
| Peaking | 7431 Hz  | 1.3  | -2.8 dB  |
| Peaking | 13183 Hz | 3.82 | 3.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -5.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -11.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Custom%20Art%20FIBAE%20Black/Custom%20Art%20FIBAE%20Black.png)