# Massdrop x NuForce Stride
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.7; 25 -7.1; 28 -7.6; 31 -8.0; 34 -8.3; 37 -8.6; 41 -8.9; 45 -9.2; 49 -9.4; 54 -9.7; 60 -10.0; 66 -10.2; 72 -10.5; 79 -10.8; 87 -11.1; 96 -11.3; 106 -11.5; 116 -11.6; 128 -11.6; 141 -11.5; 155 -11.1; 170 -10.5; 187 -10.6; 206 -11.4; 227 -11.2; 249 -10.7; 274 -10.1; 302 -9.5; 332 -8.8; 365 -8.1; 402 -7.5; 442 -6.9; 486 -6.3; 535 -5.6; 588 -5.0; 647 -4.4; 712 -3.7; 783 -3.1; 861 -2.7; 947 -2.6; 1042 -2.8; 1146 -3.0; 1261 -3.0; 1387 -2.7; 1526 -2.3; 1678 -1.8; 1846 -1.4; 2031 -0.9; 2234 -0.5; 2457 -0.5; 2703 -1.4; 2973 -2.7; 3270 -4.3; 3597 -5.1; 3957 -5.4; 4353 -5.6; 4788 -6.4; 5267 -8.2; 5793 -10.0; 6373 -7.9; 7010 -4.1; 7711 -5.7; 8482 -5.9; 9330 -6.8; 10263 -9.3; 11289 -8.3; 12418 -10.3; 13660 -18.9; 15026 -25.7; 16529 -24.5; 18182 -19.5; 20000 -14.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x NuForce Stride GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x NuForce Stride ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 50 Hz    | 0.84 | -2.2 dB  |
| Peaking | 113 Hz   | 0.87 | -4.5 dB  |
| Peaking | 250 Hz   | 1.26 | -3.7 dB  |
| Peaking | 1707 Hz  | 0.57 | 4.8 dB   |
| Peaking | 16337 Hz | 1.09 | -21.4 dB |
| Peaking | 2454 Hz  | 2.93 | 3.0 dB   |
| Peaking | 5834 Hz  | 4.4  | -5.4 dB  |
| Peaking | 7655 Hz  | 1.26 | 6.0 dB   |
| Peaking | 11873 Hz | 4.42 | 5.9 dB   |
| Peaking | 18730 Hz | 0.04 | -2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 16000 Hz | 1.41 | -24.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Massdrop%20x%20NuForce%20Stride/Massdrop%20x%20NuForce%20Stride.png)