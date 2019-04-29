# NuForce Primo8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.2; 25 -2.5; 28 -2.8; 31 -3.1; 34 -3.3; 37 -3.4; 41 -3.6; 45 -3.8; 49 -4.0; 54 -4.3; 60 -4.6; 66 -4.9; 72 -5.2; 79 -5.6; 87 -6.0; 96 -6.4; 106 -6.8; 116 -7.2; 128 -7.5; 141 -7.8; 155 -8.0; 170 -8.2; 187 -8.4; 206 -8.7; 227 -8.8; 249 -8.7; 274 -8.9; 302 -8.9; 332 -8.9; 365 -8.8; 402 -8.7; 442 -8.7; 486 -8.6; 535 -8.4; 588 -8.3; 647 -8.1; 712 -7.8; 783 -7.6; 861 -7.3; 947 -7.4; 1042 -7.8; 1146 -8.7; 1261 -9.7; 1387 -10.4; 1526 -10.7; 1678 -10.7; 1846 -10.6; 2031 -10.4; 2234 -9.2; 2457 -6.7; 2703 -4.7; 2973 -3.8; 3270 -4.4; 3597 -5.5; 3957 -4.5; 4353 -1.1; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -3.2; 7010 -6.7; 7711 -7.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce Primo8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce Primo8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.24 | 4.6 dB  |
| Peaking | 251 Hz  | 0.53 | -2.6 dB |
| Peaking | 1801 Hz | 1.32 | -4.9 dB |
| Peaking | 2831 Hz | 3.43 | 4.0 dB  |
| Peaking | 5078 Hz | 2.54 | 7.3 dB  |
| Peaking | 925 Hz  | 2.47 | 2.3 dB  |
| Peaking | 945 Hz  | 1.38 | -1.4 dB |
| Peaking | 6063 Hz | 8.43 | 3.4 dB  |
| Peaking | 7172 Hz | 3.19 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/NuForce%20Primo8/NuForce%20Primo8.png)