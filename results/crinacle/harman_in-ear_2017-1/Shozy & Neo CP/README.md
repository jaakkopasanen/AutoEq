# Shozy & Neo CP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.4; 25 -5.8; 28 -6.2; 31 -6.6; 34 -6.8; 37 -7.0; 41 -7.2; 45 -7.5; 49 -7.8; 54 -8.0; 60 -8.3; 66 -8.6; 72 -8.9; 79 -9.3; 87 -9.7; 96 -10.1; 106 -10.5; 116 -10.9; 128 -11.2; 141 -11.4; 155 -11.5; 170 -11.6; 187 -11.8; 206 -11.9; 227 -11.9; 249 -11.7; 274 -11.6; 302 -11.4; 332 -11.0; 365 -10.7; 402 -10.4; 442 -10.1; 486 -9.7; 535 -9.2; 588 -8.8; 647 -8.3; 712 -7.8; 783 -7.2; 861 -6.8; 947 -6.6; 1042 -6.8; 1146 -7.2; 1261 -7.6; 1387 -7.6; 1526 -7.1; 1678 -6.5; 1846 -5.7; 2031 -4.7; 2234 -3.3; 2457 -1.8; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.1; 5793 -3.1; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.1; 15026 -17.4; 16529 -19.0; 18182 -14.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shozy & Neo CP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shozy & Neo CP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 1.18 | 2.3 dB   |
| Peaking | 136 Hz   | 0.79 | -0.4 dB  |
| Peaking | 214 Hz   | 0.41 | -5.1 dB  |
| Peaking | 3958 Hz  | 0.86 | 6.9 dB   |
| Peaking | 16448 Hz | 1.42 | -14.2 dB |
| Peaking | 1513 Hz  | 2.96 | -1.9 dB  |
| Peaking | 2634 Hz  | 5.17 | 1.8 dB   |
| Peaking | 8075 Hz  | 6    | -1.6 dB  |
| Peaking | 12558 Hz | 2.72 | 3.2 dB   |
| Peaking | 14676 Hz | 3.93 | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB   |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -13.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shozy%20&%20Neo%20CP/Shozy%20&%20Neo%20CP.png)