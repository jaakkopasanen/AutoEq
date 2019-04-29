# Ambient Acoustics AM16
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.8; 25 -5.2; 28 -5.6; 31 -5.9; 34 -6.1; 37 -6.3; 41 -6.5; 45 -6.7; 49 -6.8; 54 -7.0; 60 -7.2; 66 -7.4; 72 -7.6; 79 -7.9; 87 -8.1; 96 -8.4; 106 -8.6; 116 -8.8; 128 -8.9; 141 -8.9; 155 -8.9; 170 -8.9; 187 -8.9; 206 -8.8; 227 -8.7; 249 -8.4; 274 -8.2; 302 -8.1; 332 -7.9; 365 -7.7; 402 -7.5; 442 -7.3; 486 -7.1; 535 -7.0; 588 -6.8; 647 -6.6; 712 -6.4; 783 -6.1; 861 -6.0; 947 -6.1; 1042 -6.6; 1146 -7.5; 1261 -8.4; 1387 -8.9; 1526 -8.8; 1678 -8.2; 1846 -7.4; 2031 -6.9; 2234 -6.7; 2457 -1.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -2.8; 4353 -3.7; 4788 -7.4; 5267 -8.3; 5793 -4.5; 6373 -6.0; 7010 -14.4; 7711 -16.3; 8482 -8.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.9; 16529 -13.9; 18182 -9.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ambient Acoustics AM16 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ambient Acoustics AM16 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 159 Hz   | 0.7  | -2.6 dB  |
| Peaking | 1709 Hz  | 1.61 | -3.6 dB  |
| Peaking | 3022 Hz  | 1.68 | 7.7 dB   |
| Peaking | 7478 Hz  | 6    | -12.1 dB |
| Peaking | 16889 Hz | 2.73 | -8.5 dB  |
| Peaking | 20 Hz    | 1.64 | 2.2 dB   |
| Peaking | 850 Hz   | 3.78 | 1.1 dB   |
| Peaking | 5061 Hz  | 9.44 | -4.3 dB  |
| Peaking | 6029 Hz  | 9.47 | 3.6 dB   |
| Peaking | 12343 Hz | 1.51 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ambient%20Acoustics%20AM16/Ambient%20Acoustics%20AM16.png)