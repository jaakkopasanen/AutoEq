# Sennheiser Momentum In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.1; 25 -10.2; 28 -10.3; 31 -10.5; 34 -10.6; 37 -10.7; 41 -10.8; 45 -10.9; 49 -11.0; 54 -11.1; 60 -11.3; 66 -11.6; 72 -11.8; 79 -12.0; 87 -12.2; 96 -12.4; 106 -12.6; 116 -12.7; 128 -12.8; 141 -12.7; 155 -12.5; 170 -12.3; 187 -12.0; 206 -11.6; 227 -11.2; 249 -11.0; 274 -10.8; 302 -10.3; 332 -9.7; 365 -9.0; 402 -8.3; 442 -7.6; 486 -6.9; 535 -5.9; 588 -5.0; 647 -4.1; 712 -3.2; 783 -2.7; 861 -2.7; 947 -3.1; 1042 -3.7; 1146 -4.2; 1261 -4.4; 1387 -4.5; 1526 -4.5; 1678 -4.5; 1846 -4.4; 2031 -4.1; 2234 -3.2; 2457 -1.8; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -1.4; 4353 -2.1; 4788 -3.1; 5267 -3.6; 5793 -4.7; 6373 -7.8; 7010 -10.6; 7711 -9.0; 8482 -7.4; 9330 -9.8; 10263 -13.9; 11289 -13.9; 12418 -11.8; 13660 -9.4; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.49 | -2.7 dB |
| Peaking | 140 Hz   | 0.39 | -6.0 dB |
| Peaking | 775 Hz   | 1.25 | 4.7 dB  |
| Peaking | 3286 Hz  | 1.26 | 6.6 dB  |
| Peaking | 10938 Hz | 1.7  | -8.1 dB |
| Peaking | 5714 Hz  | 2.22 | 2.5 dB  |
| Peaking | 6902 Hz  | 4.02 | -4.7 dB |
| Peaking | 8423 Hz  | 0.66 | -1.0 dB |
| Peaking | 8622 Hz  | 4.12 | 3.4 dB  |
| Peaking | 15125 Hz | 2.54 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)