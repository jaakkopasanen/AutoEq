# NuForce Stride
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.6; 25 -5.0; 28 -5.5; 31 -5.9; 34 -6.2; 37 -6.5; 41 -6.8; 45 -7.1; 49 -7.3; 54 -7.6; 60 -7.9; 66 -8.2; 72 -8.4; 79 -8.7; 87 -9.0; 96 -9.2; 106 -9.4; 116 -9.5; 128 -9.5; 141 -9.4; 155 -9.1; 170 -8.4; 187 -8.5; 206 -9.3; 227 -9.1; 249 -8.6; 274 -8.0; 302 -7.5; 332 -6.9; 365 -6.3; 402 -5.7; 442 -5.1; 486 -4.6; 535 -4.0; 588 -3.4; 647 -2.7; 712 -2.1; 783 -1.5; 861 -1.0; 947 -0.8; 1042 -1.0; 1146 -1.3; 1261 -1.5; 1387 -1.6; 1526 -1.4; 1678 -1.0; 1846 -0.7; 2031 -0.5; 2234 -0.7; 2457 -1.3; 2703 -2.5; 2973 -4.1; 3270 -5.6; 3597 -6.2; 3957 -6.0; 4353 -5.8; 4788 -6.3; 5267 -8.0; 5793 -10.2; 6373 -8.5; 7010 -4.9; 7711 -2.8; 8482 -3.0; 9330 -4.7; 10263 -6.0; 11289 -6.0; 12418 -6.8; 13660 -9.0; 15026 -8.4; 16529 -4.6; 18182 -2.1; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce Stride GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce Stride ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.52 | -4.1 dB |
| Peaking | 115 Hz   | 0.66 | -6.0 dB |
| Peaking | 277 Hz   | 0.93 | -4.9 dB |
| Peaking | 5323 Hz  | 1.36 | -7.4 dB |
| Peaking | 14112 Hz | 1.27 | -8.2 dB |
| Peaking | 2366 Hz  | 1.35 | 2.1 dB  |
| Peaking | 3287 Hz  | 2.57 | -2.8 dB |
| Peaking | 4856 Hz  | 2.84 | 5.3 dB  |
| Peaking | 6206 Hz  | 1.14 | -5.8 dB |
| Peaking | 7536 Hz  | 2.7  | 6.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -6.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.2 dB |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -7.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/NuForce%20Stride/NuForce%20Stride.png)