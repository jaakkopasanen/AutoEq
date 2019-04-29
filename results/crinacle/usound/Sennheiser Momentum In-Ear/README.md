# Sennheiser Momentum In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.9; 25 -9.2; 28 -9.5; 31 -9.8; 34 -10.1; 37 -10.3; 41 -10.5; 45 -10.6; 49 -10.8; 54 -11.0; 60 -11.2; 66 -11.4; 72 -11.7; 79 -11.9; 87 -12.1; 96 -12.3; 106 -12.5; 116 -12.6; 128 -12.6; 141 -12.6; 155 -12.5; 170 -12.2; 187 -12.0; 206 -11.7; 227 -11.3; 249 -10.8; 274 -10.4; 302 -9.8; 332 -9.3; 365 -8.8; 402 -8.2; 442 -7.7; 486 -7.1; 535 -6.6; 588 -6.0; 647 -5.4; 712 -4.8; 783 -4.1; 861 -3.6; 947 -3.3; 1042 -3.4; 1146 -4.0; 1261 -4.4; 1387 -4.8; 1526 -4.7; 1678 -4.1; 1846 -3.4; 2031 -2.8; 2234 -2.3; 2457 -1.9; 2703 -1.5; 2973 -1.0; 3270 -0.7; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -1.7; 5793 -4.2; 6373 -9.1; 7010 -14.3; 7711 -14.4; 8482 -9.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.0; 13660 -10.5; 15026 -8.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.42 | -2.8 dB  |
| Peaking | 156 Hz   | 0.53 | -5.1 dB  |
| Peaking | 864 Hz   | 1.36 | 3.1 dB   |
| Peaking | 4087 Hz  | 0.78 | 7.4 dB   |
| Peaking | 7271 Hz  | 3.14 | -12.8 dB |
| Peaking | 2427 Hz  | 1.75 | 1.4 dB   |
| Peaking | 3993 Hz  | 0.57 | -1.3 dB  |
| Peaking | 5207 Hz  | 3.32 | 2.1 dB   |
| Peaking | 9256 Hz  | 4.13 | 1.8 dB   |
| Peaking | 13896 Hz | 3.2  | -4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)