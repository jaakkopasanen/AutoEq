# Advanced S2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -12.9; 25 -13.0; 28 -13.1; 31 -13.1; 34 -13.1; 37 -13.1; 41 -13.1; 45 -13.0; 49 -13.0; 54 -12.9; 60 -12.8; 66 -12.8; 72 -12.8; 79 -12.8; 87 -12.8; 96 -12.8; 106 -12.7; 116 -12.6; 128 -12.4; 141 -12.2; 155 -12.0; 170 -11.7; 187 -11.3; 206 -10.9; 227 -10.5; 249 -10.0; 274 -9.6; 302 -9.0; 332 -8.4; 365 -7.8; 402 -7.3; 442 -6.9; 486 -6.4; 535 -6.0; 588 -5.5; 647 -5.2; 712 -4.8; 783 -4.6; 861 -4.0; 947 -3.3; 1042 -4.3; 1146 -5.3; 1261 -6.3; 1387 -7.0; 1526 -7.3; 1678 -7.7; 1846 -8.3; 2031 -9.1; 2234 -9.8; 2457 -9.5; 2703 -7.6; 2973 -5.4; 3270 -4.2; 3597 -4.5; 3957 -6.5; 4353 -9.3; 4788 -6.8; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.2; 15026 -22.6; 16529 -27.5; 18182 -26.9; 20000 -16.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced S2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced S2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 47 Hz    | 0.16 | -6.7 dB  |
| Peaking | 771 Hz   | 0.85 | 3.2 dB   |
| Peaking | 2119 Hz  | 1.68 | -4.8 dB  |
| Peaking | 10701 Hz | 0.37 | 15.2 dB  |
| Peaking | 16810 Hz | 0.48 | -31.7 dB |
| Peaking | 3342 Hz  | 3.57 | 3.0 dB   |
| Peaking | 4470 Hz  | 4.6  | -6.4 dB  |
| Peaking | 5728 Hz  | 2.32 | 7.8 dB   |
| Peaking | 9679 Hz  | 0.44 | -4.0 dB  |
| Peaking | 12352 Hz | 2.7  | 7.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.8 dB  |
| Peaking | 62 Hz    | 1.41 | -4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 16000 Hz | 1.41 | -24.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Advanced%20S2000/Advanced%20S2000.png)