# Massdrop x NuForce Stride
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.6; 25 -5.0; 28 -5.5; 31 -5.9; 34 -6.2; 37 -6.5; 41 -6.8; 45 -7.1; 49 -7.3; 54 -7.6; 60 -7.9; 66 -8.1; 72 -8.4; 79 -8.7; 87 -9.0; 96 -9.2; 106 -9.4; 116 -9.5; 128 -9.5; 141 -9.4; 155 -9.0; 170 -8.4; 187 -8.5; 206 -9.3; 227 -9.1; 249 -8.6; 274 -8.0; 302 -7.4; 332 -6.9; 365 -6.3; 402 -5.7; 442 -5.1; 486 -4.6; 535 -4.0; 588 -3.4; 647 -2.7; 712 -2.1; 783 -1.5; 861 -1.0; 947 -0.8; 1042 -1.0; 1146 -1.3; 1261 -1.5; 1387 -1.6; 1526 -1.4; 1678 -1.0; 1846 -0.7; 2031 -0.5; 2234 -0.7; 2457 -1.3; 2703 -2.5; 2973 -4.1; 3270 -5.6; 3597 -6.2; 3957 -6.0; 4353 -5.8; 4788 -6.3; 5267 -8.1; 5793 -10.1; 6373 -8.5; 7010 -4.9; 7711 -4.7; 8482 -5.0; 9330 -5.1; 10263 -6.0; 11289 -5.9; 12418 -6.8; 13660 -9.0; 15026 -8.4; 16529 -5.2; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x NuForce Stride GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x NuForce Stride ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 105 Hz   | 0.62 | -4.2 dB |
| Peaking | 249 Hz   | 1.37 | -2.3 dB |
| Peaking | 931 Hz   | 1.03 | 4.2 dB  |
| Peaking | 2057 Hz  | 2.26 | 4.0 dB  |
| Peaking | 5747 Hz  | 3.61 | -5.4 dB |
| Peaking | 18 Hz    | 2.2  | 1.3 dB  |
| Peaking | 2602 Hz  | 5.69 | 1.1 dB  |
| Peaking | 3498 Hz  | 3.94 | -1.8 dB |
| Peaking | 7308 Hz  | 5.8  | 1.9 dB  |
| Peaking | 14120 Hz | 2.43 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Massdrop%20x%20NuForce%20Stride/Massdrop%20x%20NuForce%20Stride.png)