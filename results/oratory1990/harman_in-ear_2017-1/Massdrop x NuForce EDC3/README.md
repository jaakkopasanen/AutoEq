# Massdrop x NuForce EDC3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -4.9; 25 -5.0; 28 -5.2; 31 -5.3; 34 -5.4; 37 -5.5; 41 -5.7; 45 -5.8; 49 -6.0; 54 -6.3; 60 -6.6; 66 -6.8; 72 -7.1; 79 -7.5; 87 -7.9; 96 -8.3; 106 -8.7; 116 -9.0; 128 -9.3; 141 -9.5; 155 -9.7; 170 -9.7; 187 -9.8; 206 -9.9; 227 -10.4; 249 -11.0; 274 -11.2; 302 -11.1; 332 -10.7; 365 -10.4; 402 -10.4; 442 -10.4; 486 -10.3; 535 -10.0; 588 -9.7; 647 -9.4; 712 -9.1; 783 -8.7; 861 -8.6; 947 -8.8; 1042 -9.2; 1146 -9.8; 1261 -10.3; 1387 -10.4; 1526 -9.9; 1678 -9.0; 1846 -7.8; 2031 -6.4; 2234 -4.7; 2457 -3.2; 2703 -2.1; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.0; 5793 -1.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -14.8; 16529 -19.9; 18182 -19.2; 20000 -14.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x NuForce EDC3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x NuForce EDC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 293 Hz   | 0.51 | -4.4 dB  |
| Peaking | 1463 Hz  | 1.5  | -4.4 dB  |
| Peaking | 3029 Hz  | 1.36 | 4.4 dB   |
| Peaking | 5094 Hz  | 0.96 | 4.9 dB   |
| Peaking | 17798 Hz | 0.98 | -15.1 dB |
| Peaking | 26 Hz    | 0.93 | 1.8 dB   |
| Peaking | 6427 Hz  | 5.22 | 3.4 dB   |
| Peaking | 7471 Hz  | 1.76 | -2.5 dB  |
| Peaking | 13574 Hz | 1.85 | 5.2 dB   |
| Peaking | 15605 Hz | 2.71 | -5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB   |
| Peaking | 62 Hz    | 1.41 | 0.0 dB   |
| Peaking | 125 Hz   | 1.41 | -2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -13.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Massdrop%20x%20NuForce%20EDC3/Massdrop%20x%20NuForce%20EDC3.png)