# Ambient Acoustics AM7 Yellow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -0.9; 54 -1.2; 60 -1.6; 66 -2.0; 72 -2.4; 79 -2.8; 87 -3.3; 96 -3.7; 106 -4.2; 116 -4.6; 128 -4.9; 141 -5.2; 155 -5.4; 170 -5.5; 187 -5.7; 206 -5.8; 227 -5.7; 249 -5.6; 274 -5.6; 302 -5.4; 332 -5.4; 365 -5.3; 402 -5.2; 442 -5.2; 486 -5.3; 535 -5.4; 588 -5.6; 647 -5.8; 712 -6.0; 783 -6.2; 861 -6.4; 947 -6.8; 1042 -7.5; 1146 -8.7; 1261 -10.1; 1387 -11.4; 1526 -12.8; 1678 -14.5; 1846 -15.8; 2031 -15.6; 2234 -12.5; 2457 -9.3; 2703 -8.0; 2973 -9.4; 3270 -11.6; 3597 -6.7; 3957 -0.9; 4353 -0.5; 4788 -0.5; 5267 -1.8; 5793 -2.5; 6373 -4.6; 7010 -8.4; 7711 -9.5; 8482 -6.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.9; 18182 -17.1; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ambient Acoustics AM7 Yellow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ambient Acoustics AM7 Yellow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.37 | 6.2 dB   |
| Peaking | 1450 Hz  | 3.84 | -2.0 dB  |
| Peaking | 1916 Hz  | 2.13 | -9.5 dB  |
| Peaking | 4645 Hz  | 3.05 | 7.7 dB   |
| Peaking | 18829 Hz | 1.48 | -12.4 dB |
| Peaking | 2138 Hz  | 0.12 | 0.7 dB   |
| Peaking | 3253 Hz  | 8.74 | -6.2 dB  |
| Peaking | 5970 Hz  | 6.74 | 2.5 dB   |
| Peaking | 7374 Hz  | 4.18 | -4.4 dB  |
| Peaking | 15377 Hz | 3.79 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.8 dB   |
| Peaking | 125 Hz   | 1.41 | 0.7 dB   |
| Peaking | 250 Hz   | 1.41 | 0.3 dB   |
| Peaking | 500 Hz   | 1.41 | 1.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -3.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ambient%20Acoustics%20AM7%20Yellow/Ambient%20Acoustics%20AM7%20Yellow.png)