# Beyerdynamic T70 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -1.8; 25 -2.0; 28 -2.3; 31 -2.5; 34 -2.7; 37 -2.9; 41 -3.1; 45 -3.2; 49 -3.3; 54 -3.4; 60 -3.5; 66 -3.7; 72 -3.9; 79 -4.4; 87 -4.9; 96 -5.5; 106 -5.9; 116 -6.3; 128 -7.0; 141 -7.5; 155 -7.3; 170 -6.8; 187 -7.3; 206 -7.2; 227 -6.8; 249 -6.7; 274 -6.7; 302 -6.8; 332 -7.1; 365 -7.3; 402 -7.6; 442 -7.3; 486 -6.9; 535 -6.2; 588 -6.1; 647 -6.3; 712 -6.5; 783 -6.4; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.5; 1261 -6.5; 1387 -6.8; 1526 -7.0; 1678 -7.0; 1846 -6.3; 2031 -5.3; 2234 -3.2; 2457 -2.3; 2703 -2.9; 2973 -3.3; 3270 -3.5; 3597 -3.6; 3957 -0.5; 4353 -2.4; 4788 -3.0; 5267 -0.6; 5793 -0.5; 6373 -1.9; 7010 -7.2; 7711 -12.0; 8482 -14.9; 9330 -14.8; 10263 -11.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.61 | 4.6 dB   |
| Peaking | 2524 Hz  | 3.49 | 4.2 dB   |
| Peaking | 3979 Hz  | 4.43 | 4.8 dB   |
| Peaking | 5860 Hz  | 2.69 | 7.9 dB   |
| Peaking | 8625 Hz  | 2.57 | -10.8 dB |
| Peaking | 71 Hz    | 1.43 | 1.9 dB   |
| Peaking | 108 Hz   | 0.32 | -1.0 dB  |
| Peaking | 139 Hz   | 4.36 | -0.9 dB  |
| Peaking | 1623 Hz  | 4.85 | -1.1 dB  |
| Peaking | 11595 Hz | 5.83 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T70%20250%20Ohm/Beyerdynamic%20T70%20250%20Ohm.png)