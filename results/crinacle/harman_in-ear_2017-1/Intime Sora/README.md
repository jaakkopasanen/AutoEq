# Intime Sora
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -11.6; 25 -11.4; 28 -11.2; 31 -11.0; 34 -10.8; 37 -10.6; 41 -10.3; 45 -10.0; 49 -9.8; 54 -9.6; 60 -9.3; 66 -9.1; 72 -8.9; 79 -8.9; 87 -8.7; 96 -8.7; 106 -8.7; 116 -8.6; 128 -8.6; 141 -8.5; 155 -8.4; 170 -8.2; 187 -8.1; 206 -8.0; 227 -7.8; 249 -7.7; 274 -7.5; 302 -7.3; 332 -7.1; 365 -6.9; 402 -6.8; 442 -6.7; 486 -6.6; 535 -6.5; 588 -6.4; 647 -6.3; 712 -6.2; 783 -6.0; 861 -5.9; 947 -6.1; 1042 -6.5; 1146 -7.0; 1261 -7.4; 1387 -7.2; 1526 -6.8; 1678 -6.1; 1846 -5.3; 2031 -4.4; 2234 -3.5; 2457 -2.9; 2703 -2.9; 2973 -3.2; 3270 -3.6; 3597 -3.9; 3957 -4.1; 4353 -4.5; 4788 -5.1; 5267 -4.9; 5793 -2.8; 6373 -0.5; 7010 -3.2; 7711 -5.4; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -6.0; 13660 -17.9; 15026 -26.4; 16529 -30.6; 18182 -30.6; 20000 -18.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Intime Sora GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Intime Sora ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 333 Hz   | 0.22 | -1.3 dB  |
| Peaking | 7231 Hz  | 0.43 | 14.2 dB  |
| Peaking | 12006 Hz | 2.25 | 12.1 dB  |
| Peaking | 16511 Hz | 0.33 | -31.3 dB |
| Peaking | 18 Hz    | 0.35 | -5.9 dB  |
| Peaking | 144 Hz   | 0.79 | -1.0 dB  |
| Peaking | 1406 Hz  | 1.5  | -3.9 dB  |
| Peaking | 2006 Hz  | 0.4  | 2.5 dB   |
| Peaking | 4593 Hz  | 2.57 | -3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 8.1 dB   |
| Peaking | 16000 Hz | 1.41 | -31.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Intime%20Sora/Intime%20Sora.png)