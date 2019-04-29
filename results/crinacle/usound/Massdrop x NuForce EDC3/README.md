# Massdrop x NuForce EDC3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.6; 25 -2.9; 28 -3.4; 31 -3.7; 34 -3.9; 37 -4.1; 41 -4.4; 45 -4.6; 49 -4.8; 54 -5.0; 60 -5.3; 66 -5.7; 72 -6.0; 79 -6.4; 87 -6.8; 96 -7.3; 106 -7.7; 116 -8.1; 128 -8.4; 141 -8.7; 155 -9.0; 170 -9.2; 187 -9.3; 206 -9.4; 227 -9.6; 249 -9.6; 274 -9.6; 302 -9.6; 332 -9.5; 365 -9.4; 402 -9.2; 442 -9.1; 486 -8.9; 535 -8.7; 588 -8.5; 647 -8.3; 712 -7.9; 783 -7.6; 861 -7.3; 947 -7.3; 1042 -7.7; 1146 -8.5; 1261 -9.3; 1387 -9.7; 1526 -9.3; 1678 -8.7; 1846 -7.5; 2031 -6.2; 2234 -5.0; 2457 -4.1; 2703 -3.6; 2973 -2.8; 3270 -1.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.9; 5793 -2.9; 6373 -1.4; 7010 -4.0; 7711 -6.5; 8482 -8.7; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x NuForce EDC3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x NuForce EDC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 11 Hz    |  0.23 | 4.3 dB  |
| Peaking | 242 Hz   |  0.46 | -3.4 dB |
| Peaking | 1495 Hz  |  1.99 | -4.0 dB |
| Peaking | 4246 Hz  |  0.85 | 6.5 dB  |
| Peaking | 8468 Hz  |  3.97 | -4.3 dB |
| Peaking | 907 Hz   |  5.76 | 0.6 dB  |
| Peaking | 6522 Hz  | 11.57 | 2.3 dB  |
| Peaking | 15467 Hz |  0.22 | -0.4 dB |
| Peaking | 17997 Hz |  0.97 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Massdrop%20x%20NuForce%20EDC3/Massdrop%20x%20NuForce%20EDC3.png)