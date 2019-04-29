# Unique Melody Mason V3 Ported
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.3; 34 -2.0; 37 -2.6; 41 -3.3; 45 -3.9; 49 -4.4; 54 -5.0; 60 -5.6; 66 -6.1; 72 -6.7; 79 -7.2; 87 -7.7; 96 -8.2; 106 -8.7; 116 -8.9; 128 -9.2; 141 -9.4; 155 -9.5; 170 -9.5; 187 -9.5; 206 -9.3; 227 -9.1; 249 -8.9; 274 -8.7; 302 -8.3; 332 -8.1; 365 -7.7; 402 -7.5; 442 -7.3; 486 -7.1; 535 -7.0; 588 -6.8; 647 -6.7; 712 -6.6; 783 -6.6; 861 -6.6; 947 -6.9; 1042 -7.4; 1146 -8.2; 1261 -8.7; 1387 -8.8; 1526 -8.5; 1678 -7.8; 1846 -7.1; 2031 -6.2; 2234 -5.0; 2457 -3.6; 2703 -1.9; 2973 -0.6; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -3.7; 5267 -8.6; 5793 -10.3; 6373 -6.5; 7010 -6.0; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.6; 15026 -22.4; 16529 -26.9; 18182 -26.0; 20000 -23.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody Mason V3 Ported GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody Mason V3 Ported ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.67 | 7.7 dB   |
| Peaking | 155 Hz   | 0    | -2.6 dB  |
| Peaking | 5709 Hz  | 4.22 | -9.4 dB  |
| Peaking | 7922 Hz  | 0.28 | 10.5 dB  |
| Peaking | 17373 Hz | 0.48 | -25.5 dB |
| Peaking | 20 Hz    | 1.45 | 1.6 dB   |
| Peaking | 1573 Hz  | 2.66 | -2.8 dB  |
| Peaking | 2943 Hz  | 4.17 | 2.3 dB   |
| Peaking | 4060 Hz  | 1.78 | 3.6 dB   |
| Peaking | 12453 Hz | 3.23 | 7.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB   |
| Peaking | 62 Hz    | 1.41 | -0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -22.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Unique%20Melody%20Mason%20V3%20Ported/Unique%20Melody%20Mason%20V3%20Ported.png)