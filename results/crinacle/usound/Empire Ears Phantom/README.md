# Empire Ears Phantom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.8; 25 -7.0; 28 -7.3; 31 -7.5; 34 -7.6; 37 -7.8; 41 -8.0; 45 -8.2; 49 -8.3; 54 -8.5; 60 -8.8; 66 -9.1; 72 -9.4; 79 -9.8; 87 -10.1; 96 -10.6; 106 -11.0; 116 -11.3; 128 -11.6; 141 -11.7; 155 -12.0; 170 -12.1; 187 -12.1; 206 -12.0; 227 -11.9; 249 -11.7; 274 -11.5; 302 -11.2; 332 -10.9; 365 -10.5; 402 -10.2; 442 -9.8; 486 -9.3; 535 -8.8; 588 -8.3; 647 -7.7; 712 -7.1; 783 -6.4; 861 -5.8; 947 -5.4; 1042 -5.4; 1146 -5.8; 1261 -6.1; 1387 -6.0; 1526 -5.3; 1678 -4.2; 1846 -2.9; 2031 -1.9; 2234 -1.4; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.4; 5267 -1.7; 5793 -3.5; 6373 -5.7; 7010 -5.2; 7711 -7.6; 8482 -8.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Phantom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Phantom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 150 Hz  | 0.54 | -5.0 dB |
| Peaking | 336 Hz  | 1.08 | -2.1 dB |
| Peaking | 2654 Hz | 1.1  | 5.3 dB  |
| Peaking | 4491 Hz | 1.71 | 3.9 dB  |
| Peaking | 8148 Hz | 4.7  | -3.1 dB |
| Peaking | 552 Hz  | 2.63 | -0.5 dB |
| Peaking | 971 Hz  | 1.86 | 1.6 dB  |
| Peaking | 1347 Hz | 1.95 | -1.6 dB |
| Peaking | 1913 Hz | 4.37 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Empire%20Ears%20Phantom/Empire%20Ears%20Phantom.png)