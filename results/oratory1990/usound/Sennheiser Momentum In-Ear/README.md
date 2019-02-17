# Sennheiser Momentum In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.6; 25 -11.8; 28 -12.0; 31 -12.1; 34 -12.1; 37 -12.0; 41 -12.0; 45 -12.0; 49 -12.0; 54 -12.1; 60 -12.3; 66 -12.5; 72 -12.7; 79 -12.9; 87 -13.2; 96 -13.5; 106 -13.7; 116 -13.8; 128 -13.9; 141 -13.9; 155 -13.8; 170 -13.7; 187 -13.4; 206 -13.0; 227 -12.5; 249 -11.9; 274 -12.4; 302 -11.6; 332 -11.0; 365 -10.3; 402 -9.6; 442 -8.9; 486 -8.2; 535 -7.4; 588 -6.6; 647 -5.8; 712 -5.0; 783 -4.1; 861 -3.4; 947 -3.0; 1042 -2.7; 1146 -2.7; 1261 -2.6; 1387 -2.6; 1526 -2.5; 1678 -2.2; 1846 -2.0; 2031 -2.0; 2234 -2.0; 2457 -2.0; 2703 -1.8; 2973 -1.4; 3270 -1.0; 3597 -0.6; 3957 -0.5; 4353 -0.6; 4788 -1.3; 5267 -2.9; 5793 -5.7; 6373 -10.4; 7010 -13.6; 7711 -13.3; 8482 -10.2; 9330 -8.8; 10263 -9.2; 11289 -9.2; 12418 -9.9; 13660 -9.1; 15026 -6.4; 16529 -5.2; 18182 -3.3; 20000 -2.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.15 | -8.7 dB  |
| Peaking | 225 Hz   | 0.55 | -5.4 dB  |
| Peaking | 5280 Hz  | 0.7  | 6.5 dB   |
| Peaking | 7080 Hz  | 1.83 | -15.1 dB |
| Peaking | 12577 Hz | 1.07 | -6.6 dB  |
| Peaking | 229 Hz   | 2.49 | 1.3 dB   |
| Peaking | 459 Hz   | 0.5  | -1.0 dB  |
| Peaking | 938 Hz   | 1.24 | 1.8 dB   |
| Peaking | 2686 Hz  | 3.09 | -0.7 dB  |
| Peaking | 4861 Hz  | 4.93 | 0.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.1 dB  |
| Peaking | 62 Hz    | 1.41 | -6.5 dB  |
| Peaking | 125 Hz   | 1.41 | -9.1 dB  |
| Peaking | 250 Hz   | 1.41 | -7.9 dB  |
| Peaking | 500 Hz   | 1.41 | -3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -11.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)