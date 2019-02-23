# Sennheiser Momentum In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -11.1; 25 -11.3; 28 -11.5; 31 -11.6; 34 -11.6; 37 -11.5; 41 -11.5; 45 -11.4; 49 -11.5; 54 -11.6; 60 -11.7; 66 -11.9; 72 -12.2; 79 -12.4; 87 -12.7; 96 -12.9; 106 -13.1; 116 -13.3; 128 -13.4; 141 -13.4; 155 -13.3; 170 -13.1; 187 -12.9; 206 -12.5; 227 -12.0; 249 -11.4; 274 -11.8; 302 -11.1; 332 -10.5; 365 -9.8; 402 -9.1; 442 -8.4; 486 -7.7; 535 -6.9; 588 -6.1; 647 -5.3; 712 -4.4; 783 -3.6; 861 -2.9; 947 -2.5; 1042 -2.2; 1146 -2.1; 1261 -2.1; 1387 -2.1; 1526 -1.9; 1678 -1.7; 1846 -1.5; 2031 -1.4; 2234 -1.5; 2457 -1.5; 2703 -1.3; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.8; 5267 -2.3; 5793 -5.2; 6373 -9.9; 7010 -13.1; 7711 -12.7; 8482 -9.7; 9330 -8.2; 10263 -8.7; 11289 -8.7; 12418 -9.3; 13660 -8.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.95 | -3.3 dB  |
| Peaking | 204 Hz   | 0.25 | -7.7 dB  |
| Peaking | 890 Hz   | 0.45 | 6.6 dB   |
| Peaking | 5305 Hz  | 0.76 | 16.3 dB  |
| Peaking | 6831 Hz  | 1.06 | -19.2 dB |
| Peaking | 133 Hz   | 4.28 | -0.2 dB  |
| Peaking | 7698 Hz  | 5.94 | -1.3 dB  |
| Peaking | 8932 Hz  | 3.39 | 1.9 dB   |
| Peaking | 13053 Hz | 2.23 | -2.7 dB  |
| Peaking | 14664 Hz | 1.67 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)