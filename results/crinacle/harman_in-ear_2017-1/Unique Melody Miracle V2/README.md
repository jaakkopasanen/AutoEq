# Unique Melody Miracle V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.1; 25 -8.2; 28 -8.3; 31 -8.4; 34 -8.4; 37 -8.4; 41 -8.5; 45 -8.5; 49 -8.6; 54 -8.7; 60 -8.7; 66 -8.9; 72 -9.1; 79 -9.3; 87 -9.6; 96 -9.9; 106 -10.1; 116 -10.3; 128 -10.4; 141 -10.6; 155 -10.7; 170 -10.6; 187 -10.6; 206 -10.5; 227 -10.4; 249 -10.3; 274 -10.1; 302 -9.9; 332 -9.6; 365 -9.2; 402 -9.1; 442 -8.9; 486 -8.6; 535 -8.4; 588 -8.1; 647 -7.9; 712 -7.7; 783 -7.4; 861 -7.3; 947 -7.4; 1042 -7.9; 1146 -8.6; 1261 -9.2; 1387 -9.3; 1526 -8.9; 1678 -7.9; 1846 -6.5; 2031 -4.5; 2234 -2.4; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.4; 5267 -6.3; 5793 -5.7; 6373 -1.5; 7010 -5.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.5; 15026 -21.9; 16529 -26.3; 18182 -24.5; 20000 -21.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody Miracle V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody Miracle V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 273 Hz   | 0.2  | -4.6 dB  |
| Peaking | 1523 Hz  | 1.08 | -10.2 dB |
| Peaking | 2709 Hz  | 0.36 | 15.0 dB  |
| Peaking | 12622 Hz | 0.8  | 20.5 dB  |
| Peaking | 15911 Hz | 0.33 | -31.6 dB |
| Peaking | 28 Hz    | 0.27 | -1.1 dB  |
| Peaking | 65 Hz    | 0.99 | 1.2 dB   |
| Peaking | 4492 Hz  | 5.53 | 2.1 dB   |
| Peaking | 5512 Hz  | 5.07 | -5.3 dB  |
| Peaking | 6185 Hz  | 8.8  | 5.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 16000 Hz | 1.41 | -21.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Unique%20Melody%20Miracle%20V2/Unique%20Melody%20Miracle%20V2.png)