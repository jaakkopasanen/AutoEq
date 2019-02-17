# Sennheiser Momentum In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.3; 23 -13.4; 25 -13.4; 28 -13.5; 31 -13.6; 34 -13.7; 37 -13.7; 41 -13.8; 45 -13.9; 49 -13.9; 54 -14.0; 60 -14.2; 66 -14.3; 72 -14.5; 79 -14.6; 87 -14.8; 96 -15.0; 106 -14.9; 116 -14.8; 128 -14.8; 141 -14.6; 155 -14.5; 170 -14.2; 187 -13.8; 206 -13.5; 227 -12.9; 249 -12.5; 274 -12.0; 302 -11.4; 332 -10.8; 365 -10.2; 402 -9.7; 442 -8.9; 486 -8.5; 535 -8.0; 588 -7.2; 647 -6.7; 712 -6.5; 783 -6.1; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -7.2; 1387 -7.7; 1526 -8.2; 1678 -8.4; 1846 -8.1; 2031 -7.5; 2234 -6.8; 2457 -5.4; 2703 -4.1; 2973 -2.1; 3270 -0.7; 3597 -0.5; 3957 -1.2; 4353 -3.8; 4788 -5.2; 5267 -5.8; 5793 -8.1; 6373 -11.8; 7010 -10.5; 7711 -8.0; 8482 -6.5; 9330 -6.5; 10263 -7.0; 11289 -9.1; 12418 -9.9; 13660 -9.7; 15026 -6.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 1.3  | -6.5 dB |
| Peaking | 52 Hz    | 0.33 | -6.5 dB |
| Peaking | 178 Hz   | 0.65 | -4.5 dB |
| Peaking | 3554 Hz  | 2.69 | 7.0 dB  |
| Peaking | 6579 Hz  | 4.15 | -6.1 dB |
| Peaking | 797 Hz   | 2.07 | 1.4 dB  |
| Peaking | 1740 Hz  | 1.94 | -2.2 dB |
| Peaking | 2886 Hz  | 4.84 | 1.4 dB  |
| Peaking | 9190 Hz  | 2.37 | 1.2 dB  |
| Peaking | 12516 Hz | 2.19 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)