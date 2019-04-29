# Massdrop x NuForce EDC3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.8; 25 -4.1; 28 -4.5; 31 -4.8; 34 -5.1; 37 -5.3; 41 -5.5; 45 -5.7; 49 -5.9; 54 -6.2; 60 -6.5; 66 -6.8; 72 -7.1; 79 -7.5; 87 -7.9; 96 -8.4; 106 -8.8; 116 -9.2; 128 -9.5; 141 -9.9; 155 -10.2; 170 -10.3; 187 -10.4; 206 -10.5; 227 -10.7; 249 -10.7; 274 -10.7; 302 -10.7; 332 -10.5; 365 -10.2; 402 -10.1; 442 -9.9; 486 -9.7; 535 -9.4; 588 -9.2; 647 -8.9; 712 -8.6; 783 -8.2; 861 -8.0; 947 -8.1; 1042 -8.5; 1146 -9.2; 1261 -9.8; 1387 -9.8; 1526 -9.2; 1678 -8.5; 1846 -7.3; 2031 -5.6; 2234 -3.8; 2457 -2.4; 2703 -1.5; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.1; 5793 -1.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.6; 16529 -16.0; 18182 -19.4; 20000 -18.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x NuForce EDC3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x NuForce EDC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 10 Hz    | 0.26 | 3.4 dB   |
| Peaking | 243 Hz   | 0.42 | -4.4 dB  |
| Peaking | 1503 Hz  | 1.47 | -5.3 dB  |
| Peaking | 3585 Hz  | 0.65 | 7.3 dB   |
| Peaking | 18858 Hz | 0.8  | -14.8 dB |
| Peaking | 3752 Hz  | 5.72 | -0.5 dB  |
| Peaking | 6393 Hz  | 5.13 | 2.7 dB   |
| Peaking | 8099 Hz  | 2.62 | -2.5 dB  |
| Peaking | 13487 Hz | 3.36 | 3.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -9.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Massdrop%20x%20NuForce%20EDC3/Massdrop%20x%20NuForce%20EDC3.png)