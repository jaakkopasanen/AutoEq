# Empire Ears Bravado
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.0; 23 -15.9; 25 -15.7; 28 -15.5; 31 -15.2; 34 -15.0; 37 -14.7; 41 -14.3; 45 -14.0; 49 -13.7; 54 -13.4; 60 -13.0; 66 -12.7; 72 -12.5; 79 -12.3; 87 -12.1; 96 -11.9; 106 -11.7; 116 -11.4; 128 -11.1; 141 -10.8; 155 -10.4; 170 -10.0; 187 -9.6; 206 -9.0; 227 -8.5; 249 -8.0; 274 -7.4; 302 -6.9; 332 -6.3; 365 -5.7; 402 -5.3; 442 -4.7; 486 -4.1; 535 -3.7; 588 -3.4; 647 -2.6; 712 -2.0; 783 -1.7; 861 -1.5; 947 -1.7; 1042 -2.2; 1146 -3.0; 1261 -4.0; 1387 -4.8; 1526 -5.1; 1678 -5.2; 1846 -5.3; 2031 -5.7; 2234 -6.1; 2457 -5.7; 2703 -4.0; 2973 -1.8; 3270 -0.5; 3597 -0.5; 3957 -1.4; 4353 -3.5; 4788 -6.1; 5267 -6.6; 5793 -3.2; 6373 -1.1; 7010 -3.5; 7711 -5.3; 8482 -4.9; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -6.5; 15026 -7.3; 16529 -5.7; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Bravado GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Bravado ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.26 | -10.8 dB |
| Peaking | 144 Hz   | 0.73 | -3.3 dB  |
| Peaking | 790 Hz   | 1.62 | 3.9 dB   |
| Peaking | 3478 Hz  | 3.98 | 5.1 dB   |
| Peaking | 22050 Hz | 2.35 | 0.9 dB   |
| Peaking | 1033 Hz  | 6.7  | 0.9 dB   |
| Peaking | 2119 Hz  | 3.1  | -1.8 dB  |
| Peaking | 5109 Hz  | 7.66 | -3.3 dB  |
| Peaking | 6360 Hz  | 6.03 | 4.2 dB   |
| Peaking | 14979 Hz | 2.75 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.4 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Empire%20Ears%20Bravado/Empire%20Ears%20Bravado.png)